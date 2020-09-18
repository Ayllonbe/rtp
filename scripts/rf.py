#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 2020

@author: Aaron Ayllon Benitez
@description: Task 3 to relation extraction project: calsification
"""

import pandas as pd
import numpy as np
from collections import Counter
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import roc_curve
from sklearn.metrics import auc
from sklearn.model_selection import train_test_split
from sklearn.metrics import plot_roc_curve
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.neural_network import MLPClassifier

def main(file):
    np.random.seed(1234)
    inputT = pd.read_csv(file,sep=",",keep_default_na=False)
    inputT["Type"] = inputT["Type"].map({"Directed":1,"Undirected":0})
    inputT["Link"] = inputT["Link"].map({"catalysis":0,"binding":1,"reaction":0,"regulation":0})
    inputT = inputT.drop_duplicates()
    inputT['iteraction'] = inputT['Source'].str.cat(inputT['Target'],sep="-")
    arr = []
    zero = inputT.loc[inputT['Link'] == 0]
    ones = inputT.loc[inputT['Link'] == 1]
    print(zero)
    print(ones)
    inter0 = zero['iteraction']
    index0 = inter0.index
    inter1 = ones['iteraction'].to_numpy()
    for idx, interaction in np.ndenumerate(inter0):
        if(interaction in inter1):
            arr.append(index0[idx[0]])
           
    inputT = inputT.drop(arr)
    
    X = inputT.loc[:,"ARACNE_score":"irp_score"]
    y         = inputT["Link"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)
    model = RandomForestClassifier(n_estimators=1000)
    knn = KNeighborsClassifier(n_neighbors=9)
    svc = SVC()
    nn = MLPClassifier(max_iter=500)
    

    print("Training model 1.")
    #train model
    model.fit(X_train, y_train)
    print("Training model 2.")
    knn.fit(X_train, y_train)
    print("training model 3.")
    svc.fit(X_train, y_train)
    print("training model 4.")
    nn.fit(X_train, y_train)
    
    knn_disp = plot_roc_curve(knn, X_test, y_test)
    svc_disp = plot_roc_curve(svc, X_test, y_test, ax=knn_disp.ax_)
    nn_disp = plot_roc_curve(nn, X_test, y_test, ax=svc_disp.ax_)
    rfc_disp = plot_roc_curve(model, X_test, y_test, ax=nn_disp.ax_)
    rfc_disp.figure_.suptitle("Binding link - ROC curve comparison")
    plt.show()
if __name__ == "__main__":
   main("../data/preprocessed_nnDataInput.csv")
   
   
   
   
   