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
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import roc_curve
from sklearn.metrics import auc

def main(file):
    np.random.seed(1234)
    inputT = pd.read_csv(file,sep=",",keep_default_na=False)
    inputT["Type"] = inputT["Type"].map({"Directed":1,"Undirected":0})
    inputT["Link"] = inputT["Link"].map({"catalysis":0,"binding":0,"reaction":0,"regulation":1})
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
    
    feature_matrix = inputT.loc[:,"Type":"irp_score"]
    labels         = inputT["Link"]
    print(inputT.columns)
    print(feature_matrix)
    print(Counter(labels))
    msk = np.random.rand(len(inputT)) < 0.6
    train = feature_matrix[msk]
    train_labels= labels[msk]
    td = feature_matrix[~msk]
    td_labels = labels[~msk]
    msk =  np.random.rand(len(td)) < 0.5
    test = td[msk]
    test_labels = td_labels[msk]
    deep = td[~msk]
    deep_labels = td_labels[~msk]

    model = MLPClassifier(random_state=1, max_iter=500)
    print("Training model 1.")
    #train model
    model.fit(train, train_labels)
    predicted_labels = model.predict(deep)
    print( "FINISHED classifying. accuracy score : ")
    print(accuracy_score(deep_labels, predicted_labels)   )
    
    fpr, tpr, thresholds = roc_curve(deep_labels, predicted_labels, pos_label=1)
    print(auc(fpr, tpr))

  
    
if __name__ == "__main__":
   main("../data/preprocessed_nnDataInput.csv")