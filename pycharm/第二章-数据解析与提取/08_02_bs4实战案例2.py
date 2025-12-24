import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service #在 Selenium 中，from selenium.webdriver.chrome.service import Service 的作用是导入用于管理 Chrome 驱动服务的 Service 类。  其主要功能是：负责启动和控制 Chrome 浏览器驱动程序（chromedriver）的进程  可以配置驱动程序的路径、日志级别等参数  在代码中通常与 ChromeDriverManager 配合使用，用于初始化 Chrome 浏览器实例
from webdriver_manager.chrome import ChromeDriverManager  #ChromeDriverManager 的主要功能是自动管理 Chrome 浏览器驱动（chromedriver） 它可以：自动检测当前系统中安装的 Chrome 浏览器版本  自动下载与当前 Chrome 版本匹配的 chromedriver 自动处理驱动的路径配置，无需手动下载和设置驱动路径  在代码中，它被用于初始化 Chrome 浏览器驱动
import time
from bs4 import BeautifulSoup
import os


save_dir = r"d:\pythoncode\pycharm\第二章-数据解析与提取\08_02_bs图片"
if not os.path.exists(save_dir):
    os.makedirs(save_dir)
n = 1  #图片的名字

'''
这个网站是动态加载  即普通requests请求无法获取全部数据  只能获得动态加载前的数据  所以 通过模拟浏览器获取数据  引用到了selenium模块
'''
#初始化浏览器
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# 访问网页
url = "https://www.bizhihui.com/"
driver.get(url)
'''
注意
子页面的url如果开头是/,直接在前面拼接上域名即可
子页面的url不是/开头,此时需要找到主页面的url,去掉最后一个/后面的所有内容,和当前获取到的url进行拼接
'''

# 等待动态内容加载（可以根据实际情况调整等待时间或使用显式等待）
time.sleep(3)  # 简单的隐式等待，实际项目中推荐显式等待

# 获取加载完成后的页面源码
page_source = driver.page_source

# 保存内容
with open("bizhihui_dynamic.txt", "w", encoding="utf-8") as f:
    f.write(page_source)
    print("动态内容保存成功")
main_page = BeautifulSoup(page_source, 'html.parser')
a_list  = main_page.find_all("a", attrs={"class":"item-img"})

for item in a_list:
    href = item.get("href")   #获得子页面的href
    print(href)
    driver.get(href)
    page_source = driver.page_source
    child_page = BeautifulSoup(page_source, 'html.parser')
    div = child_page.find("div", attrs={"class":"article-content"})
    img_src = div.find("img").get("src")
    href1 = img_src.split("-")[0]
    print(href1)
    
    # 下载图片
    img_resp = requests.get(href1)
    # 使用os.path.join拼接路径，避免跨平台路径问题
    img_path = os.path.join(save_dir, f"{n}.jpg")
    with open(img_path, "wb") as f:
        f.write(img_resp.content)
    print(f"图片已保存到: {img_path}")
    n += 1  # 递增图片编号（如果需要下载多张）
    
    # print(item.get("href"))
# print(len(a_list))

# 关闭浏览器
driver.quit()

# headers = {
#    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36 Edg/143.0.0.0",
#    "referer":"https://www.bizhihui.com/"
#    }
# resp = requests.get(url)
# resp.encoding="utf-8"
# with open("bizhihui.txt","w",encoding="utf-8") as f:
#     f.write(resp.text)
#     f.close()
#     print("保存成功")