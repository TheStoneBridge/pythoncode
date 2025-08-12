import os
path = 'C:/Users/yyk/Desktop'
files = os.listdir(path)
# print(files)
for f in files:
    if 'bizhi' in f and f.endswith('.jpg'):
        print('找到啦！'+f)