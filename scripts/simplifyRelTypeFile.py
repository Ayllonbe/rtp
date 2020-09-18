#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 2020

@author: Aaron Ayllon Benitez
@description: Task 1 to relation extraction project: simplify the STRING file.
"""

import pandas as pd
import numpy as np
print("reading file")
# Read STRING file downloaded from the website.
df = pd.read_csv("../data/3702.protein.actions.v11.0.txt",sep="\t",keep_default_na=False)
print("preprocessing")
# init diccionary <dic>.
dic = {}
# for loop to go through the rows in the pandas table.
# It is a preprocessing step.
for row in df.values:
    newRow = []
    # fromp and top are the source and target protein respectively.
    fromp = row[0].split(".")[1]
    top = row[1].split(".")[1]
    # concatenate them into a variable inter.
    inter = fromp+"-"+top
    # same thing for the type of link and their action (if no action the value is "").
    typeR = row[2]+"-"+row[3]
    # initialization of keys in <dic>.
    if(inter not in dic):
        dic[inter] = {}
    if(typeR not in dic[inter]):
        dic[inter][typeR] = []
    newRow = []
    # the columns 4 and 5 determine if the relation is directed or not, 
    # in that case, we change the value instead.
    if(row[4] == 'f'):
        newRow.append("Undirected")
        newRow.append(row[6])
        newRow.append(0)
    else:
        if(row[5] =='t'):
            newRow.append("Directed")
            newRow.append(row[6])
            newRow.append(0)
        else:
            newRow.append("Directed")
            newRow.append(row[6])
            newRow.append(1)
    dic[inter][typeR].append(newRow)

newAr = []
# We run the dic in a for loop to apply some criterias:
# 1. if we have directed in both side, we add a new undirected link.
# 2. the links with actions (except activation or inhibition) we kept.
# 3. creation of an array to create the new table.
for k1 in dic:
    vecType = []
    arrP = k1.split("-")
    for k2 in dic[k1]:
        vecType.append(k2)
        countD = 0
        score =0
        for x in dic[k1][k2]:
            if x[0] == "Directed":
                countD=countD+1
            score = score + x[1]    
        if countD ==2:
            newRows = [["Undirected", int(score/len(dic[k1][k2])),0],
                        ["Directed", int(score/len(dic[k1][k2])),0],
                        ["Directed", int(score/len(dic[k1][k2])),1]]
            dic[k1][k2] = newRows 
        ele = k2
        arrT = k2.split("-")
        if arrT[1] =="" or arrT[0] == "activation" or arrT[0] == "inhibition":
            ele=arrT[0]
            
            
        for r in dic[k1][k2]:
                if(r[2]==1):
                   newAr.append([arrP[1],arrP[0],ele,
                         r[0],r[1]])
                else:
                    newAr.append([arrP[0],arrP[1],ele,
                         r[0],r[1]])
                    newAr.append([arrP[1],arrP[0],ele,
                         r[0],r[1]])
print("exporting")
# transform the array in pandas obj.
df2 = pd.DataFrame(np.array(newAr), columns=["Source","Target","Link","Type","Score"])
# Print
df2.iloc[:,0:4].to_csv("../data/3702.protein.actions.v11.0-pre.txt", sep='\t',index=False)
print("Done.")