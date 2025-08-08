import pandas as pd

df = pd.read_excel(r'd:\pythoncode\shall\数据结构上手项目.xls', sheet_name='Sheet1')

# 输出每一行的数据
for index, row in df.iterrows():
    print(list(row))
    print(list(row)[0])  # 输出每一行的第一列数据
    print(list(row)[1])  # 输出每一行的第二列数据   
    print(list(row)[2])  # 输出每一行的第三列数据