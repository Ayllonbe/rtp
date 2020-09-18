#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 2020

@author: Aaron Ayllon Benitez
@description: Task 2 to relation extraction project: preprocessing the data
"""


import pandas as pd
print("reading file")
# Reading the preprocess link data.
dfTypeR = pd.read_csv("../data/3702.protein.actions.v11.0-pre.txt",sep="\t",keep_default_na=False)
# Reading the Seidr file converted in tsv.
dfSf    = pd.read_csv("../data/arabidopsisNetwork.tsv",sep='[;\t]', engine='python', keep_default_na=False, na_values='nan')
print("preprocessing")
# Transform NAs into 0. (Step to discuss)
dfSf = dfSf.fillna(0)
selected_col = []
# Automatic selection of the colons from Seidr.
for c in dfSf.columns:
    #if "Source" in c or "Target" in c or "Type" in c or "score" in c or ("D" in c and "SDev" not in c):
    if "Source" in c or "Target" in c or "Type" in c or "rank" in c or ("D" in c and "SDev" not in c):
        selected_col.append(c)
dfSf = dfSf[selected_col]
# Combine the pandas obj by the columns Source, Target and Type.
result = pd.merge( dfTypeR,dfSf,
                  on=["Source","Target","Type"],
                  how="inner")
# Remove the row duplicates.
result = result.drop_duplicates()
print("exporting")
# export result.
result.to_csv("../data/nnDataInputRank.csv", sep=',',index=False)
print("Done.")