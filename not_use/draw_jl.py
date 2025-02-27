import matplotlib.pyplot as plt
import numpy as np
# Open file   
import math 
import os

# coding=utf-8
 
 
if __name__ == '__main__':
    pro_path = "C:\\Users\\pc\\Desktop\\zjh\\jl_change"
    files = os.listdir(pro_path)
    lie = len(files)
    num= math.ceil(lie/3)
    js=1
    for file in files:
        pl=[]
        real=[]
        img=[]
        file_path = pro_path+"\\"+file
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
            real.append(b)
            a=line.strip().split()[2:3]
            b=float(' '.join(a))
            img.append(b)
        plt.subplot(1,1,js)
        plt.plot(pl, real, 'r-',pl, img, 'r--', alpha=0.5, linewidth=1)
        plt.grid()
        plt.title(file)
        plt.xlabel('pl') #x_label
        plt.ylabel('Epsilon')#y_label
        # plt.ylim(-1,1)#仅设置y轴坐标范围
        js=js+1
    plt.show()