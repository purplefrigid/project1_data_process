# Open file   
import math 
import os
str2="THETA    PHI      magn.    phase     magn.    phase        in m*m                     axial r. angle   direction" 
str3="Excitation index:              1"
pro_path = "C:\\Users\\pc\\Desktop\\zjh\\"
data_path = pro_path+"feko_data"
files = os.listdir(data_path)

for file in files:
    file_path = data_path+"\\"+file
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
                f.write(I+' '+str(e)+'\n')           
        else:
            with open(txt,"a") as f:
                f.write(I+' '+str(e)+'\n')

	

