import requests
from bs4 import BeautifulSoup
import os
import math
import time 
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

# 配置请求重试（全局生效）
session = requests.Session()
retry = Retry(
    total=5,  # 最多重试3次
    backoff_factor=2,  # 重试间隔：1秒、2秒、4秒...
    status_forcelist=[503]  # 只对503错误重试
)
session.mount('http://', HTTPAdapter(max_retries=retry))

url = "http://www.xinfadi.com.cn/getPriceData.html"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36 Edg/143.0.0.0',
    'Referer' : 'http://www.xinfadi.com.cn/priceDetail.html',
    'Content-Type':'application/x-www-form-urlencoded'
    }
params = {
    "current": 1,
    "limit": 20,
    "pubDateStartTime": "2025-12-09",
    "pubDateEndTime": "2025-12-10",
    "prodPcatid": 1189,  # 必须写1189（肉禽蛋一级分类）
    "prodCatid": "",     # 二级分类留空=全部子类
    "prodName": ""
}
try:
    response = session.post(url,headers=headers,data=params)
    data = response.json()

    print("接口返回状态码：", response.status_code)  # 正常应为200
    print("接口返回前100字符：", response.text[:100])  # 正常应是JSON格式

    with open("data.json","w",encoding="utf-8") as f:
        f.write(response.text)
        print("保存成功")
        
    total_count = data.get("count",0)
    page_size = params["limit"]
    total_pages = math.ceil(total_count / page_size) if total_count > 0 else 0  # math.ceil()向上取整

    print(f"接口请求成功!共{total_count}条数据,共{total_pages}页,每页显示{page_size}条数据")
    
    with open("data.json","w",encoding="utf-8") as f:
        f.write(response.text)
        print("保存成功")
except Exception as e:
    print(f"请求第一页失败:",{str(e)})
    print("接口请求失败")        

if total_pages == 0:
    print("没有数据可爬取")

else:
    print("\n开始爬取商品价格数据")
    print("一级分类\t二级分类\t品名\t最低价\t平均价\t最高价\t规格\t产地\t单位\t发布日期")
    
for current_page in range(1,total_pages+1):
    params["current"] = current_page
    try:
        response = session.post(url,headers=headers,data=params)
        response.raise_for_status()
        page_data = response.json()
        
        #提取当前页的商品列表
        if page_data.get("list"):
            for item in page_data["list"]:
                    一级分类 = item.get("prodCat", "")
                    二级分类 = item.get("prodPcat", "")
                    品名 = item.get("prodName", "")
                    最低价 = item.get("lowPrice", "")
                    平均价 = item.get("avgPrice", "")
                    最高价 = item.get("highPrice", "")
                    规格 = item.get("specInfo", "")
                    产地 = item.get("place", "")
                    单位 = item.get("unitInfo", "")
                    发布日期 = item.get("pubDate", "")[:10]
                    # 修正打印格式（之前多了两个\t，导致列对齐错乱）
                    print(f"{一级分类}\t\t\t{二级分类}\t{品名}\t{最低价}\t{平均价}\t{最高价}\t{规格}\t{产地}\t{单位}\t{发布日期}")
            
            print(f"✅ 第{current_page}/{total_pages}页爬取完成")
        
    except Exception as e:
        print(f"❌ 第{current_page}页爬取失败：{str(e)}")
        continue  # 某页失败不影响其他页，继续爬下一页
# data = response.json()

# if data.get("list"):
#     for item in data["list"]:
#         # 对应表格的每一列，直接从JSON里取字段
#         一级分类 = item.get("prodCat", "")  # 一级分类
#         二级分类 = item.get("prodPcat", "")  # 二级分类
#         品名 = item.get("prodName", "")      # 品名
#         最低价 = item.get("lowPrice", "")    # 最低价
#         平均价 = item.get("avgPrice", "")    # 平均价
#         最高价 = item.get("highPrice", "")   # 最高价
#         规格 = item.get("specInfo", "")      # 规格
#         产地 = item.get("place", "")         # 产地
#         单位 = item.get("unitInfo", "")      # 单位
#         发布日期 = item.get("pubDate", "")[:10]  # 发布日期（截取前10位）
        
#         # 打印或保存数据
#         print(f"{一级分类}\t{二级分类}\t{品名}\t{最低价}\t{平均价}\t{最高价}\t{规格}\t{产地}\t{单位}\t{发布日期}")
# else:
#     print("未获取到数据，可能参数错误或接口限制")

# 将response.text内容写入文件
# with open("xinfadi.html.txt","w",encoding="utf-8") as f:
#     f.write(response.text)
# print("保存成功")

# 初始化BS4对象
# print(response.text)
# page = BeautifulSoup(response.text,'html.parser')
# table = page.find("table",attrs={"border":"0"})
# print(table)
# trs = table.find_all("tr")[1:]
# print(trs)
# for tr in trs:
#     tds = tr.find_all("td")
#     onetype = tds[0].text
#     name = tds[2].text
#     lprice = tds[3].text
#     pprice = tds[4].text
#     hprice = tds[5].text
#     kind = tds[6].text
#     place = tds[7].text
#     unit = tds[8].text
#     date = tds[9].text
#     print(onetype,name,lprice,pprice,hprice,kind,place,unit,date)