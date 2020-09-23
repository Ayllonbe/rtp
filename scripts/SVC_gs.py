#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 11:24:52 2020

@author: aaron
"""

import argparse
import logging
import os
import sys
from sklearn.externals.joblib import parallel_backend
from sklearn.externals.joblib import register_parallel_backend
from sklearn.externals.joblib import cpu_count
from ipyparallel import Client
from ipyparallel.joblib import IPythonParallelBackend

import pandas as pd
from sklearn.model_selection import train_test_split

from sklearn.metrics import plot_roc_curve
import matplotlib.pyplot as plt

from sklearn.metrics import make_scorer
from sklearn.metrics import accuracy_score
from sklearn.metrics import auc
from sklearn.metrics import roc_curve
from sklearn.svm import SVC
from sklearn.model_selection import GridSearchCV

FILE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(FILE_DIR)

#prepare the logger
parser = argparse.ArgumentParser()
parser.add_argument("-i", "--input", help="Input file path")
parser.add_argument("-p", "--profile", default="ipy_profile",
                 help="Name of IPython profile to use")
args = parser.parse_args()

profile = args.profile
logging.basicConfig(filename=os.path.join(FILE_DIR,profile+'.log'),
                    filemode='w',
                    level=logging.DEBUG)
logging.info("number of CPUs found: {0}".format(cpu_count()))
logging.info("args.profile: {0}".format(profile))

#prepare the engines
c = Client(profile=profile)
#The following command will make sure that each engine is running in
# the right working directory to access the custom function(s).
c[:].map(os.chdir, [FILE_DIR]*len(c))
logging.info("c.ids :{0}".format(str(c.ids)))
bview = c.load_balanced_view()
register_parallel_backend('ipyparallel',
                          lambda : IPythonParallelBackend(view=bview))

#Get data
inputT = pd.read_csv(args.input,sep=",",keep_default_na=False)

#Parameters to test in parallel
param_grid = [
  {'C': [1, 10, 100, 1000,10000,100000], 
   'kernel': ['linear','sigmoid','poly'],
   'class_weight':['balanced',None]},
  {'C': [1, 10, 100, 1000,10000,100000], 
   'gamma': [0.1, 0.01,0.001,0.0001,0.00001,0.000001,0.0000001],
   'kernel': ['rbf'],
   'shrinking':[True,False],
   'class_weight':['balanced',None]},
 ]

# The scorers can be either be one of the predefined metric strings or a scorer
# callable, like the one returned by make_scorer
scoring = {'AUC': 'roc_auc', 'Accuracy': make_scorer(accuracy_score)}
# Setting refit='AUC', refits an estimator on the whole dataset with the
# parameter setting that has the best cross-validated AUC score.
# That estimator is made available at ``gs.best_estimator_`` along with
# parameters like ``gs.best_score_``, ``gs.best_params_`` and
# ``gs.best_index_``
gs = GridSearchCV(SVC(random_state=42),
                  param_grid=param_grid,
                  scoring=scoring, refit='AUC', 
                  return_train_score=True,
                  cv=10,
                   n_jobs=len(c))
X = inputT.loc[:,"ARACNE_score":"irp_score"]
y = inputT["Link"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Run grid search
with parallel_backend('ipyparallel'):
    gs.fit(X_train, y_train)
# extract results
results = gs.cv_results_
results = pd.DataFrame(results)
results.to_csv(os.path.join(FILE_DIR,'scores_rbf_digits.csv'))

info = "Best estimator: " + str(gs.best_estimator_) + "\navg. AUC score using Cross Validation (10): " + str(gs.best_score_)

y_predict = gs.best_estimator_.predict(X_test)
fpr, tpr, thresholds = roc_curve(y_test, y_predict)
info = "\n AUC with the test data: "+ str(auc(fpr, tpr))


