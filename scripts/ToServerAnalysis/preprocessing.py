import time
from itertools import cycle
# dataframes
import pandas as pd
import numpy as np

print("reading file")
org = "dmel"
# Reading the preprocess link data.
dfTypeR = pd.read_csv("../../data/rtp_project_data/"+org+".protein.actions.v11.0.txt.gz",
                      sep="\t",
                     # engine='python',
                      compression="gzip",
                      keep_default_na=False)
# Reading the Seidr file converted in tsv.
dfSf    = pd.read_csv("../../data/rtp_project_data/"+org+"-network.txt",
                      sep='[;\t]',
                      engine='python',
                      keep_default_na=False,
                      na_values='nan')


print("-----------string-action file-----------")
print(dfTypeR.head())
print("-----------seidr file-----------")
print(dfSf.head())
# Automatic selection of the colons from Seidr.
selected_col = []
for c in dfSf.columns:
    if "Source" in c or "Target" in c  or "Type" in c or "score" in c  or ("D" in c and "SDev" not in c):
        selected_col.append(c)
dfSf = dfSf[selected_col]

print("preprocessing")
dic = {}
# for loop to go through the rows in the pandas table.
# It is a preprocessing step.
for row in dfTypeR.values:
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
dfTypeR_pre = pd.DataFrame(np.array(newAr), 
                           columns=["Source","Target","Link","Type","Score"])
print("Done.")

to_despreciate = ("ptmod","expression")
dfTypeR_pre = dfTypeR_pre[~dfTypeR_pre['Link'].isin(to_despreciate)]
dfTypeR_pre['Link'] = dfTypeR_pre['Link'].replace(['activation',
                                                   "inhibition",
                                                   "expression-inhibition"],
                                                   'regulation').replace(['binding-activation',
                                                                          'binding-inhibition'],
                                                                          'binding')

# Combine the pandas obj by the columns Source, Target and Type.
result = pd.merge( dfTypeR_pre,dfSf,
                  on=["Source","Target","Type"],
                  how="inner")
# Remove the row duplicates.
result['Type'] = result["Type"].map({"Directed":1,"Undirected":0})
result = result.drop_duplicates()
print("Done.")
result.to_csv(org+".processed_data.tsv", sep='\t',index=False)
