import matplotlib.pyplot as plt
import numpy as np
# Open file   
import math 
import os

# coding=utf-8
def bubble_sort(array):
    for i in range(1, len(array)):
        for j in range(0, len(array)-i):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array
 
 
if __name__ == '__main__':
    pro_path = "C:\\Users\\pc\\Desktop\\zjh\\"
    data_path = pro_path+"result_change"
    files = os.listdir(data_path)
    pl=[]
    rcs=[]
    lie = len(files)
    num= math.ceil(lie/3)
    js=1
    for file in files:
        pl=[]
        rcs=[]
        file_path = data_path+"\\"+file
        fileHandler  =  open  (file_path,  "r")	
        listOfLines  =  fileHandler.readlines()
        # Close file
        fileHandler.close()
        for  line in  listOfLines:
            a=line.strip().split()[0:1]
            b=float(' '.join(a))
            pl.append(b)
            a=line.strip().split()[1:2]
            b=float(' '.join(a))
            rcs.append(b)

        plt.subplot(3,num,js)
        plt.plot(pl, rcs, 'b*--', alpha=0.5, linewidth=1)
        plt.title(file)
        plt.legend()  #显示上面的label
        plt.xlabel('pl') #x_label
        plt.ylabel('rcs')#y_label
        # plt.ylim(-1,1)#仅设置y轴坐标范围
        js=js+1
    plt.show()