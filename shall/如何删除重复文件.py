import os
import filecmp

#所要删除重复文件的路径
path = 'C:/Users/yyk/Desktop/fileautosort/repeatedfile'
#已知路径下存在两个文件夹pic1和pic2
dirs = ['file1','file2']

#将指定目录下的所有文件的路径存储到allfiles变量中
def get_all_files(path,dirs):
    all_files = []
    for d in dirs:
        cur_path = os.path.join(path,d)
        files = os.listdir(cur_path)
        for f in files:
            all_files.append(os.path.join(cur_path,f))
    return all_files

#比较两个文件的内容是否一致
def cmp_files(x,y):
    if filecmp.cmp(x,y):
        #如果一致，则删除第二个，保留第一个,并输出信息
        os.remove(y)
        print(f"路径{y}下的文件与路径{x}下的文件一致，已删除")
        
#调用函数，获取文件列表
all_files = get_all_files(path,dirs)
print(all_files)
#用双重for循环来比较文件是否重复
for x  in all_files:
    for y in all_files:
        #如果x和y不是相同的文件，而且都存在，则执行后续操作
        if x != y and os.path.exists(x) and os.path.exists(y):
           #比较文件内容是否一致
            cmp_files(x,y)