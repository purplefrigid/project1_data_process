import pandas as pd  
import os
import numpy as np  
# 读取 Excel 文件  
df = pd.read_excel('data11.xlsx', header=None)  

# pro_path = "C:\\Users\\zgnhz\\Desktop\\新建文件夹 (3)\\zjh\\"
# data_path=pro_path+"kuandu_data"
data_path="./kuandu_data"
files = os.listdir(data_path)
for file in files:
# 遍历每一行
    bh= file.split(".")[0].split("_")[1]   
    file_path = data_path+"\\"+file
    fileHandler  =  open  (file_path,  "r")	
    listOfLines  =  fileHandler.readlines()
    for index, row in df.iterrows():  
        # b=18
        if row[0] ==int(bh):
            for  num ,line in  enumerate(listOfLines):
                a=line.strip().split()[1]
                pl=line.strip().split()[0]
                for ls, line in df.items():  
                    if line[0] ==float(pl):
                        break
                df.at[index, ls] = float(a)
                # b=b+1
# 保存修改后的 DataFrame 到新的 Excel 文件  
df.to_excel('modified_file.xlsx', index=False, header=False)


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
                if abs(b-(row[ls-1]+row[ls-2])/2)>15:
                    row[ls]=2*row[ls-1]-row[ls-2]
                    df.at[index, ls] = row[ls]
            except:
                break
        
df.to_excel('modified_file1.xlsx', index=False, header=False)