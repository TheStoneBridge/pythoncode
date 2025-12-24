"""
1. 拿到页面源代码
2. 从页面源代码中提取你需要的数据.价格,名称,公司名称
"""
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options #用于配置 Chrome 浏览器的启动选项（如无头模式、窗口大小、代理设置等），可以对浏览器行为进行自定义配置
# from selenium.webdriver.common.by import By   #提供了定位元素的方式常量（如 ID、CLASS_NAME、XPATH、CSS_SELECTOR 等） 例如可以用By.XPATH来指定使用 XPath 语法定位元素
from selenium.webdriver.support.ui import WebDriverWait #用于实现显式等待功能，等待某个条件满足后再继续执行后续代码 可以避免因页面加载延迟导致的元素定位失败问题
from selenium.webdriver.support import expected_conditions as EC #提供了一系列预定义的条件判断方法（如元素是否可见、是否存在、是否可点击等） 通常与WebDriverWait配合使用，实现等待条件的判断
from lxml import etree


# 设置Chrome 浏览器的选项
chrome_options = Options()
chrome_options.add_argument('--headless')  # 启动无头模式
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36 Edg/143.0.0.0")

#初始化浏览器驱动
driver = webdriver.Chrome(options=chrome_options)   

try:
    url ="https://www.zbj.com/fw/?k=saas"
    
    driver.get(url)
    
    # 显示等待：等待目标元素加载完成（以“服务名称”为例，XPath需根据实际页面调整）
    # 最多等待10秒，每0.5秒检查一次元素是否存在
    
    wait = WebDriverWait(driver, 10, 0.5)
    
    
    page_source = driver.page_source
    
    et = etree.HTML(page_source)
    div_list = et.xpath('//div[@class="search-result-list-service"]/div')
    for div in div_list:
        price=div.xpath('.//div[@class="price"]/span/text()')[0]
        bussiness_name=div.xpath('.//div[@class="shop-info text-overflow-line"]/text()')[0]
        
        product_name_list = div.xpath('.//div[@class="serve-name text-overflow-line-two oneline"]/span//text()')  #获取span标签下的所有文本
        valid_texts = [text.strip() for text in product_name_list if text.strip()] #去掉空文本
        product_name = ''.join(valid_texts) #将文本列表合并为一个字符串
        
        print(f"产品名称：{product_name}，价格：{price}，公司名称：{bussiness_name}")
        
    # with open("zbj.txt", "w", encoding="utf-8") as f:
    #     f.write(page_source)
    #     print("保存成功")
        
  
    
finally:
    driver.quit()