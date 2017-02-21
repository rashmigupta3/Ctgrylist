#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import json
import pandas as pd
import numpy as np

OrgCatList = pd.read_csv('/Users/rashmi/Desktop/catlist.txt', header= None)
OrgCatarr = np.array(OrgCatList)
 
jfile = open('/Users/rashmi/Desktop/Day1.json').read()
df = json.loads(jfile)
dictfile = dict(df)

for keys,values in dictfile.items():
    key = keys
    val = values

im = values[1200].values()
im
imdict = im[0][0].items()
imdict
mscv = imdict[2]
mscv[1]

for m in range(len(val)):
    for n in range(8):
        if mscv[1].items()[n] == 'categories':
            ctgry = mscv[1].items()[n]
ctgry

catvals = ctgry[1]

catvalsarr = np.array(catvals)
catvalsdf = pd.DataFrame(catvals)
catvalsdf

CatAtrbs = []
for n in range(len(val)):
    ins = []
    im = values[n].values()
    
    while(imdict==0):
        try:
             imdict = im[0][0].items()
             continue
        except ValueError:
             print " "
    mscv = imdict[2]
    for m in range(len(val)):
            for n in range(8):
                if list(mscv[1].items())[n][0] == 'categories':
                    ctgry = list(mscv[1].items())[n]
    
           
    iden = imdict[1][1]
    path = imdict[0][1]
    ins.append(path)
    ins.append(iden)
    ins.append(ctgry)
    CatAtrbs.append(ins)
print CatAtrbs
