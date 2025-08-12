import os
import shutil


path = 'C:/Users/yyk/Desktop/fileautosort/zip'
def scan_file(path):  #扫描文件
    files = os.listdir(path)
    for f in files:
        if f.endswith('.zip'):
            return f

def unzip_file(f):  #解压文件
    folder_name = f.split('.')[0]
    target_path = path + '/' + folder_name
    os.mkdir(target_path)
    shutil.unpack_archive(path +'/'+f,target_path)

def delete(f):  #删除文件
    os.remove(path +'/'+f)

while True:
    zip_file = scan_file(path) 
    if zip_file:
        unzip_file(zip_file)
        delete(zip_file)
        print(1)