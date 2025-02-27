# Open file   
import math 
import os


pro_path = "C:\\Users\\pc\\Desktop\\zjh\\"
data_path = pro_path+"luo_data"
files = os.listdir(data_path)

for file in files:
    file_path = data_path+"\\"+file
    fileHandler  =  open  (file_path,  "r")	
    file_name = file.split('.')[0]+"."+file.split('.')[1]
    bianhao = file_name.split('_')[1]
    pinlv =file_name.split('_')[2].strip("Ghz")
    result_path = pro_path+"result\\zjh_"+bianhao+'.txt'
    listOfLines  =  fileHandler.readlines()
    # Close file
    fileHandler.close()
    # Iterate over the lines
    a=listOfLines[0].strip().split()
    b=a[3:4]
    c=' '.join(b)
    with open(result_path,"a") as f:
        f.write(pinlv+' '+c+'\n')

	

