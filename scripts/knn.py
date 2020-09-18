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
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
import optunity
import optunity.metrics


def main(file):
    np.random.seed(1234)
    inputT = pd.read_csv(file,sep=",",keep_default_na=False)
    inputT["Type"] = inputT["Type"].map({"Directed":1,"Undirected":0})
    #inputT["Link"] = inputT["Link"].map({"catalysis":False,"binding":True,"reaction":False,"regulation":False})
    inputT["Link"] = inputT["Link"].map({"catalysis":1,"binding":0,"reaction":1,"regulation":0})
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

    #clf = make_pipeline(StandardScaler(), SVC(gamma='auto'))
    #print("Training model 1.")
    #train model
    #clf.fit(train, train_labels)
    #predicted_labels = clf.predict(deep)
    #print( "FINISHED classifying. accuracy score : ")
    #print(accuracy_score(deep_labels, predicted_labels)   )
    data=feature_matrix.to_numpy()
    labels = labels.to_numpy()

# compute area under ROC curve of default parameters
    @optunity.cross_validated(x=data, y=labels, num_folds=5)
    def knn_rbf_tuned_auroc(x_train, y_train, x_test, y_test):
        model =  KNeighborsClassifier(n_neighbors=9).fit(x_train, y_train)
        prediction = model.predict(x_test)
        #print("here")
        #decision_values = model.decision_function(x_test)
       
        #auc = optunity.metrics.roc_auc(y_test, decision_values)
        auc = optunity.metrics.roc_auc(y_test, prediction)
       # acc = optunity.metrics.accuracy(y_test, prediction)
        #print("Acc " + str(acc))
      #  print("AUC " + str(auc))
        return auc
    @optunity.cross_validated(x=data, y=labels, num_folds=5)
    def knn_accuracy(x_train, y_train, x_test, y_test):
        model = KNeighborsClassifier(n_neighbors=3).fit(x_train, y_train)
        prediction = model.predict(x_test)
        acc = optunity.metrics.accuracy(y_test, prediction)
        return acc
    
    print(knn_rbf_tuned_auroc())
  #  print("----")
    print(knn_accuracy())
    
    
if __name__ == "__main__":
   main("../data/preprocessed_nnDataInput.csv")