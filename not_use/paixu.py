import os
import numpy as np
# coding=utf-8
def bubble_sort(array):
    for i in range(1, len(array)):
        for j in range(0, len(array)-i):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array
if __name__ == '__main__':
    pro_path = "C:\\Users\\pc\\Desktop\\zjh\\"
    data_path = pro_path+"result"
    change_path=pro_path+"result_change"
    files = os.listdir(data_path)
    pl=[]
    for file in files:
        file_path = data_path+"\\"+file
        result_path = change_path+"\\"+file
        fileHandler  =  open  (file_path,  "r")	
        listOfLines  =  fileHandler.readlines()
        # Close file
        fileHandler.close()
        for  num ,line in  enumerate(listOfLines):
            a=line.strip().split()[0:1]
            b=float(' '.join(a))
            pl=np.append(pl,b)
        pl=np.unique(pl)
        #sx_rg = bubble_sort(pl)
        fl = np.arange(1.025,18,0.175)
        for i in range(len(fl)):
            fl[i]=round(fl[i],3)
        for num,i in enumerate(fl):
            for  line in  listOfLines:
                a=line.strip().split()[0:1]
                b=float(' '.join(a))
                if b ==i:
                    if num == 0:
                        with open(result_path,"w") as f:
                            f.write(line)                        
                    else:
                        with open(result_path,"a") as f:
                            f.write(line)
                    break
                
