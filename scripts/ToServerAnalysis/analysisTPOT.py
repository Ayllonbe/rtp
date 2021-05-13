#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 08:08:40 2021

@author: aaron
"""

import pandas as pd
import numpy as np
import sys, getopt

from sklearn.impute import KNNImputer
from sklearn.preprocessing import MinMaxScaler

from sklearn.model_selection import StratifiedKFold
from imblearn.combine import SMOTETomek 

from tpot import TPOTClassifier

def run(file):
    print("TPOT")
   tpot = TPOTClassifier(generations=100, population_size=100, 
                        scoring='f1', verbosity=2, random_state=42, n_jobs=-1)
   
   with open(file, 'rb') as input:
       X_train, y_train, X_test, y_test = = pickle.load(input)
      tpot.fit(X_train, y_train) 
      scores = tpot.score(X_test, y_test)
      print("F1 "+scores)
    
def main(argv):
   f = ''
   try:
     # opts, args = getopt.getopt(argv,"hx:j:",["xmlfile=","jsonfile="])
     opts, args = getopt.getopt(argv,"hf:",["file="])
   except getopt.GetoptError:
      print('[error] analysisTPOT.py -f <file>')
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print('analysisTPOT.py -f <file>')
         print("-" * 25)
         print('-f --file:\tpickle file to run')
         
         
         sys.exit()
      elif opt in ("-f", "--file"):
         f = arg
   
   run(f)

if __name__ == "__main__":
   main(sys.argv[1:])  
    
    
    
