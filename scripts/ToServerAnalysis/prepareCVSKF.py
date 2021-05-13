#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 08:08:40 2021

@author: aaron
"""

import pandas as pd
import numpy as np
import sys, getopt
import pickle

from sklearn.impute import KNNImputer
from sklearn.preprocessing import MinMaxScaler


from sklearn.model_selection import StratifiedKFold
from imblearn.combine import SMOTETomek 

from tpot import TPOTClassifier

def save_object(obj, filename):
    with open(filename, 'wb') as output:  # Overwrites any existing file.
        pickle.dump(obj, output, pickle.HIGHEST_PROTOCOL)
def transformBinaryLinkTable(tolabelize, df_back,col_pos='Link'):
    print("Binarizing")
    df = df_back.copy()
    dic = {}
    for x in df[col_pos].value_counts().index.values:
        if x != tolabelize:
            dic[x] = 0
        else:
            dic[x] = 1
    df[col_pos] = df[col_pos].map(dic)
    print("Done")
    return(df)

def run():
   files=["athal","scere","dmel","eugra","potra"]
   links=["reaction","binding","regulation","catalysis"]
   for org in files:
      file="results/"+org+".processed_data.tsv"
      print(org)
      print("Reading file")
      df = pd.read_csv(file,
                           sep="\t",
                           keep_default_na=True)
      print(df.shape)
      for linktype in links:
         print(linktype)
         binaryLinkTable = transformBinaryLinkTable(linktype,df)
         print(binaryLinkTable.shape)
         X =  np.asarray(binaryLinkTable.iloc[:,1:])
         y =  np.asarray(binaryLinkTable["Link"])
         print("Starting Cross-Validation with TPOT")
         skf = StratifiedKFold(n_splits=10)
         #resDic = {}
         i = 1
         for train_index, test_index in skf.split(X, y): 
            X_trainDev, X_test = X[train_index], X[test_index]
            y_trainDev, y_test = y[train_index], y[test_index]
            smt = SMOTETomek(random_state=i, n_jobs=-1)
            X_train, y_train = smt.fit_resample(X_trainDev, y_trainDev)
            dataToAnalise = [ X_train, y_train, X_test, y_test]
            save_object(dataToAnalise, org+'_'+linktype+'_to_SK'+str(i)+'.pkl')
            i+=1
    
if __name__ == "__main__":
   run()  
    
    
    
