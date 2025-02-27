import pandas as pd
import numpy as np  
import os
# 读取 Excel 文件  
df = pd.read_excel('modified_file.xlsx', header=None)  

LS = np.arange(17,114,1)
for index, row in df.iterrows():  
    for ls in LS: 
        b=row[ls]
        c = np.isnan(b)  
        if ls==17 and c == True:
            break
        if ls< 113 and c == True:
            try:
                a=0
                e= np.isnan(row[ls+a])
                while np.isnan(row[ls+a]) == True:
                    a=a+1
                    d= row[ls+a]
                    e= np.isnan(row[ls+a])
                a=a+1
                for i in range(0,a-1):
                    row[ls+i]=(i+1)*(-row[ls-1]+row[ls+a-1])/a+row[ls-1]
                    df.at[index, ls+i] = row[ls+i]
            except:
                break
        if ls == 113 and c == True:
            row[ls]=row[ls-1]
            df.at[index, ls] = row[ls]

LS1 = np.arange(19,113,1)
for index, row in df.iterrows():  
    if index >0:
        for ls in LS1: 
            b=row[ls]
            try:
                if abs(b-(row[ls-1]+row[ls-2])/2)>10:
                    row[ls]=2*row[ls-1]-row[ls-2]
                    df.at[index, ls] = row[ls]
            except:
                break
        
df.to_excel('modified_file1.xlsx', index=False, header=False)
