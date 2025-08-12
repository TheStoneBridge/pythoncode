import os
import shutil

path = "C:/Users/yyk/Desktop/fileautosort"
files = os.listdir(path)
print(files)
for f in files:
    folder_name = path + '/' + f.split('.')[-1]
    if not os.path.exists(folder_name):
        os.mkdir(folder_name) #创建文件夹
        shutil.move(path+'/'+f,folder_name)  #移动文件
    else:
        shutil.move(path+'/'+f,folder_name)    
        
print("完成")
        
        
        
        
        
        
        
    