# https://dushu.baidu.com/api/pc/getCatalog?data={%22book_id%22:%224306063500%22}  %22等价于" 效果如下
# https://dushu.baidu.com/api/pc/getCatalog?data={"book_id":"4306063500"}   => 所有章节的内容（名称,cid）

#https://dushu.baidu.com/api/pc/getChapterContent?data={"book_id":"4306063500","cid":"4306063500|1569782244","need_bookinfo":1}


import requests
import asyncio
import aiohttp
import aiofiles
import json
import os

"""
1. 同步操作，访问getCatalog  拿到所有章节的cid和名称
2. 异步操作，访问getChapterContent  拿到所有章节的内容
"""
#定义文件夹名称
save_dir =r'd:\pythoncode\pycharm\第四章\西游记'
#如果文件夹不存在则创建
if not os.path.exists(save_dir):
    os.mkdir(save_dir)  
async def  aiodownload(cid,title):
    #定义文件夹名称
    save_dir ='d:\pythoncode\pycharm\第四章\西游记'
    #如果文件夹不存在则创建
    if not os.path.exists(save_dir):
        os.mkdir(save_dir)   
    
    file_path = os.path.join(save_dir, f"{title}.txt")  # 拼接文件路径
    
    data ={
        "book_id":"4306063500",
        "cid":f"4306063500|{cid}",
        "need_bookinfo":1
    }
    data = json.dumps(data)  # 将字典转换为JSON字符串
    url = f'https://dushu.baidu.com/api/pc/getChapterContent?data={data}'
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            dic = await response.json()  # 解析JSON响应
            async with aiofiles.open(file_path,mode='w',encoding='utf-8') as f:
                await f.write(dic['data']['novel']['content'])  # 将章节内容写入文件    
async def getCatalog(url):
    response = requests.get(url)
    dic = response.json()
    tasks = []
    for item in dic['data']['novel']['items']:
        title = item['title']
        cid = item['cid']
        # 准备异步任务
        task = asyncio.create_task(aiodownload(cid,title))
        tasks.append(task)
    await asyncio.wait(tasks)

if __name__=='__main__':
    url = 'https://dushu.baidu.com/api/pc/getCatalog?data={"book_id":"4306063500"}'
    asyncio.run(getCatalog(url))
    