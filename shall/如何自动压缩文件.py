import os
import time 
import shutil
from shutil import make_archive
#指定需要检测的文件夹
path = r'C:\Users\yyk\Desktop\fileautosort\autozip'
#记录已压缩的文件夹,避免重复压缩
compressed_folders = set()
#记录有新文件加入的文件夹
folders_with_new_files = set()
#自动归类
def autosort():
    global folders_with_new_files
    folders_with_new_files.clear() #每次归类前清空，重新记录本次新增文件的文件夹
    files =  os.listdir(path)
    for f in [file  for file in files if not file.endswith('.zip')]:
        #用os.path.join()拼接路径,避免兼容性问题
        file_path = os.path.join(path,f)
        #跳过目录(只处理文件，避免将文件夹移入其他文件夹)
        if os.path.isdir(file_path):
            continue
        #获取文件后缀作为文件名(无后缀则归为'other')
        suffix = f.split('.')[-1] if '.' in f else 'other'
        folder_name = os.path.join(path,suffix)
        #创建文件夹并移动文件
        if not os.path.exists(folder_name):
            os.mkdir(folder_name)
            folders_with_new_files.add(folder_name)
        else :
            #只有当文件移动到已存在的文件夹时，才标记为有新文件
            folders_with_new_files.add(folder_name)
        shutil.move(file_path,folder_name)


while True:
    #先执行归类   会更新folders_with_new_files
    autosort()
    #筛选出所有归类文件夹(排除.zip文件和非目录)
    current_folder = [
        f for f in os.listdir(path)
        if os.path.isdir(os.path.join(path,f)) and not f.endswith('.zip')
        ]
    #只处理本次有新文件加入的文件夹
    for folder in folders_with_new_files:
        folder_name = os.path.basename(folder)
        #确保文件夹仍然存在
        if folder_name in current_folder:
            zip_name  =  os.path.join(path,folder_name)
            #压缩文件夹
            shutil.make_archive(zip_name,'zip',folder)
            compressed_folders.add(folder)
    #休眠1秒,每1秒检测一次        
    time.sleep(1)