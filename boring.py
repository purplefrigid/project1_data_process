import math 
import os
import numpy as np
import matplotlib.pyplot as plt
str2="THETA    PHI      magn.    phase     magn.    phase        in m*m                     axial r. angle   direction" 
str3="Excitation index:              1"
pro_path = "D:\\keti\\zjh\\"
feko_path = pro_path+"feko_data"
luo_path = pro_path+"luo_data"
dataresult_path = pro_path+"result"
change_path=pro_path+"result_change"
feko_files = os.listdir(feko_path)
luo_files = os.listdir(luo_path)
def bubble_sort(array):
    for i in range(1, len(array)):
        for j in range(0, len(array)-i):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array
if __name__ == '__main__':

    # feko数据
    for file in feko_files:
        file_path = feko_path+"\\"+file
        fileHandler  =  open  (file_path,  "r")	
        list1= []
        list2=[]
        file_name = file.split('.')[0]
        txt = pro_path+"result\\"+file_name+'.txt'
        # Get list of all lines in file
        listOfLines  =  fileHandler.readlines()
        # Close file
        fileHandler.close()
        # Iterate over the lines
        for  num ,line in  enumerate(listOfLines):
            str1 = line.strip()
            #print(line.strip())
            if str1==str2:
                list1.append(num)
            if str1 == str3:
                list2.append(num)
        #print(list1)
        #print(list2)

        #write 到data.txt文件中

        for num,data in enumerate(list1):
            a=listOfLines[data+1].strip().split()
            b=a[6:7]
            c=' '.join(b)
            d=float(c)
            e=round(10*math.log(d,10),4)

            g=listOfLines[list2[num]+1].strip().split()
            h=g[5:6]
            I=','.join(h)[:5]
            if num ==0:
                with open(txt,"w") as f:
                    f.write(I+' '+str(d)+'\n')           
            else:
                with open(txt,"a") as f:
                    f.write(I+' '+str(d)+'\n')

    # 罗老师算的数据
    for file in luo_files:
        file_path = luo_path+"\\"+file
        fileHandler  =  open  (file_path,  "r")	
        file_name = file.split('.')[0]+"."+file.split('.')[1]
        bianhao = file_name.split('_')[1]
        pinlv =file_name.split('_')[2].strip("Ghz")
        result_path = pro_path+"result\\zjh_"+bianhao+'.txt'
        listOfLines  =  fileHandler.readlines()
        # Close file
        fileHandler.close()
        # Iterate over the lines
        try:
            a=listOfLines[0].strip().split()
            b=a[3:4]
            c=float(' '.join(b))
            d=str(math.pow(10,c/10))
            with open(result_path,"a") as f:
                f.write(pinlv+' '+d+'\n')
        except:
            print(file)

    # 排序
    result_files = os.listdir(dataresult_path)
    for file in result_files:
        pl=[]
        file_path = dataresult_path+"\\"+file
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
        fl = bubble_sort(pl)
        # fl = np.arange(1.025,18,0.175)
        # for i in range(len(fl)):
        #     fl[i]=round(fl[i],3)
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
                    # break


    # 画图
    draw_file=os.listdir(change_path)
    lie = len(draw_file)
    
    js=1
    b1= 0
    draw=list(range(1000, 1201,1))
    num= math.ceil(len(draw)/5)
    for file in draw_file:
        pl=[]
        rcs=[]
        xl=int(file.split('.')[0].split('_')[1])
        if xl in draw:
            file_path = change_path+"\\"+file
            result_path  = pro_path+"kuandu_data\\"+file
            fileHandler  =  open  (file_path,  "r")	
            listOfLines  =  fileHandler.readlines()
            # Close file
            fileHandler.close()
            for  line in  listOfLines:
                a=line.strip().split()[0:1]
                b=float(' '.join(a))
                if b==b1:
                    c=line.strip().split()[1:2]
                    d=float(' '.join(c))*15/b1
                    rcs[-1]= (rcs[-1]+d)/2             
                    b1= b
                else :    
                    b1= b     
                    pl.append(b)
                    c=line.strip().split()[1:2]
                    d=float(' '.join(c))*15/b1
                    rcs.append(d)
            for n,i in enumerate(rcs):
                # rcs[n]=round(rcs[n],2)
                rcs[n]=round(10*math.log(rcs[n],10),4)
                if n == 0:
                    with open(result_path,"w") as f:
                        f.write(str(pl[n])+' '+str(rcs[n])+"\n")                        
                else:
                    with open(result_path,"a") as f:
                        f.write(str(pl[n])+' '+str(rcs[n])+"\n")     
    #         plt.subplot(5,num,js)
    #         # plt.subplot(1,1,js)
    #         plt.plot(pl, rcs, 'b*--', alpha=0.5, linewidth=1)
    #         plt.title(file)
    #         #plt.legend()  #显示上面的label
    #         plt.xlabel('pl') #x_label
    #         plt.ylabel('Scattering Width')#y_label
    #         # plt.ylim(-1,1)#仅设置y轴坐标范围
    #         js=js+1
    # plt.show()
