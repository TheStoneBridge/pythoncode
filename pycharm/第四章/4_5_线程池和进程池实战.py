# 1. 如何提取单个页面的数据
# 2. 上线程池，多个页面同时抓取

import requests
from lxml import etree
# 导入格式化打印模块，让字典输出更清晰
from pprint import pprint
import csv
from concurrent.futures import ThreadPoolExecutor
import threading
import time


# 初始化锁
write_lock = threading.Lock()
f = open("xinfadi.csv","w",encoding="utf-8")
csvwriter = csv.writer(f)
# 写入表头
header = ["品名", "最低价", "平均价", "最高价", "产地", "计量单位", "发布日期"]
csvwriter.writerow(header)
def download_one_page(url,current):
    # 每次请求前等待1-3秒（随机延迟更难被反爬识别）
    time.sleep(random.uniform(1, 3))
    headers ={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36 Edg/144.0.0.0",
        "Referer": "http://www.xinfadi.com.cn/priceDetail.html"
    }
    params = {
    "current": current,
    "limit": 20,
    "pubDateStartTime": "2024/01/01",
    "pubDateEndTime": "",
    "prodPcatid": "",  
    "prodCatid": "",     # 二级分类留空=全部子类
    "prodName": ""
    }
    try:
         # 发送请求（改用session保持连接，降低反爬）
        session = requests.Session()
        response = session.post(url, data=params, headers=headers,timeout=10)
        response.raise_for_status()
        list = response.json().get("list")
        # print("序号\t品名\t最低价\t平均价\t最高价\t产地\t计量单位\t发布日期")
        
         # 检查是否有数据
        if not list:
            print(f"第{current}页无数据（可能被反爬/页面不存在）")
            return
        # 加锁写入CSV（关键：避免多线程同时写）
        with write_lock:  # 上锁
            for idx,data in enumerate(list, 1):  # idx为序号（从1开始）
                prodName = data.get("prodName")  # 品名
                lowPrice = data.get("lowPrice")  # 最低价
                highPrice = data.get("highPrice")# 最高价
                avgPrice = data.get("avgPrice")  # 平均价
                place = data.get("place")        # 产地
                unitInfo = data.get("unitInfo")# 计量单位
                pubDate = data.get("pubDate")    # 发布日期
                row_date=[prodName,lowPrice,avgPrice,highPrice,place,unitInfo,pubDate]
                csvwriter.writerow(row_date)
            print(f"第{current}页爬取数据成功")
    except Exception as e:
        print(f"第{current}页爬取失败：{str(e)}")        
if __name__ == '__main__':
    with ThreadPoolExecutor(10) as t:
        for i in range(1,200):
          t.submit(download_one_page, url="http://www.xinfadi.com.cn/getPriceData.html", current=i)   
    f.close()      
    print("所有任务执行完毕，文件已保存")