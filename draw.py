 
import math 
import os
import numpy as np
import matplotlib.pyplot as plt

path=".\\kuandu_data\\"
draw_file=os.listdir(path)
lie = len(draw_file)

js=1
b1= 0
draw=list(range(721, 751,1))
num= math.ceil(len(draw)/5)
for file in draw_file:
    pl=[]
    rcs=[]
    xl=int(file.split('.')[0].split('_')[1])
    if xl in draw:
        fileHandler  =  open  (path+file,  "r")	
        listOfLines  =  fileHandler.readlines()
        # Close file
        fileHandler.close()
        for  line in  listOfLines:
            a=line.strip().split()[0:1]
            b=float(' '.join(a))  
            pl.append(b)
            c=line.strip().split()[1:2]
            d=float(' '.join(c))
            rcs.append(d)
        plt.subplot(5,num,js)
        # plt.subplot(1,1,js)
        plt.plot(pl, rcs, 'b*--', alpha=0.5, linewidth=1)
        plt.title(file)
        #plt.legend()  #显示上面的label
        plt.xlabel('pl') #x_label
        plt.ylabel('Scattering Width')#y_label
        # plt.ylim(-1,1)#仅设置y轴坐标范围
        js=js+1
plt.show()