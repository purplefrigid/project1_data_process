import pandas as pd
import numpy as np  
import matplotlib.pyplot as plt
import numpy as np
# Open file   
import math 
import os
# 读取 Excel 文件 
draw=list(range(800, 831,1))
# draw = [156,491,487,318,317,293]
num= math.ceil(len(draw)/5) 
js = 1
df = pd.read_excel('modified_file1.xlsx', header=None)  

LS = np.arange(17,114,1)
for index, row in df.iterrows():  
    if index in draw:
        pl=np.arange(1.025,17.825,0.175)
        rcs=[]
        for ls in LS: 
            rcs.append(row[ls])
        try:
            plt.subplot(5,num,js)
            # plt.subplot(1,1,js)
            plt.plot(pl, rcs, 'b*--', alpha=0.5, linewidth=1)
            plt.title(row[0])
            #plt.legend()  #显示上面的label
            plt.xlabel('pl') #x_label
            plt.ylabel('Scattering Width')#y_label
            # plt.ylim(-1,1)#仅设置y轴坐标范围
            js=js+1
        except:
            break
plt.show()

