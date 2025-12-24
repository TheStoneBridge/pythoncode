"""
1, 提取页面源代码
2, 解析页面源代码，提取数据
"""
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service  #在 Selenium 中，from selenium.webdriver.chrome.service import Service 的作用是导入用于管理 Chrome 驱动服务的 Service 类。  其主要功能是：负责启动和控制 Chrome 浏览器驱动程序（chromedriver）的进程  可以配置驱动程序的路径、日志级别等参数  在代码中通常与 ChromeDriverManager 配合使用，用于初始化 Chrome 浏览器实例
from webdriver_manager.chrome import ChromeDriverManager#ChromeDriverManager 的主要功能是自动管理 Chrome 浏览器驱动（chromedriver） 它可以：自动检测当前系统中安装的 Chrome 浏览器版本  自动下载与当前 Chrome 版本匹配的 chromedriver 自动处理驱动的路径配置，无需手动下载和设置驱动路径  在代码中，它被用于初始化 Chrome 浏览器驱动
from selenium.webdriver.support.ui import WebDriverWait
from pyquery import PyQuery
import os

# 获取当前脚本所在目录的绝对路径
current_dir = os.path.dirname(os.path.abspath(__file__))
# 拼接CSV文件的完整路径（当前目录下的carhome.csv）
carhome = os.path.join(current_dir, "carhome.csv")
def get_page_source(url):
    
    #初始化浏览器
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get(url)
    
    # 显示等待：等待目标元素加载完成（以“服务名称”为例，XPath需根据实际页面调整）
    # 最多等待10秒，每0.5秒检查一次元素是否存在
    wait = WebDriverWait(driver, 10, 0.5)

    
    page_source = driver.page_source  

    driver.quit()
    return page_source
def parse_page_source(html):
    doc = PyQuery(html)
    mt_list = doc("li.clearfix").items()
    # print(mt_list)
    for mt in mt_list:
         # 提取车型系列（小米SU7）
        car_name = mt(".list_series__rwJ7c").text()
        # 提取具体车型（2024款 后驱长续航智驾版）
        car_type = mt(".list_spec__Cwpy6").text()
        car = car_name + " " + car_type
        place =  mt(".list_car_info__2l0lA.clearfix > li:nth-child(6) > .list_key__caXoL").text()#页面里的class="list_car_info__2l0lA clearfix"是一个元素同时有两个 class（list_car_info__2l0lA和clearfix），而 CSS 选择器中，多个 class 之间不能用空格（空格表示 “后代元素”），正确的写法是把两个 class 连起来（中间无空格），即.list_car_info__2l0lA.clearfix。
        time = mt(".list_timeline__1N6pP").text().split()[0]
        
        #判断是否有购车经销商
        if not mt(".list_car__aTF06 a:last:contains('购车经销商')"):
            #向没有购车经销商的信息中添加 购车经销商：未知
            mt(".list_car__aTF06 div").after(PyQuery("""
                                                 <a target="_blank" href="" rel="noreferrer"><span class="list_dealer_name__MweuO">购车经销商：<span class="list_dealer__NRalr">未知</span></span></a>                  
                                             """))
        Car_dealership = mt(".list_dealer__NRalr").text() #购车经销商
        price = mt(".list_car_info__2l0lA.clearfix > li:nth-child(4) >div:nth-child(1)").text()  #价格
        xiaohao = mt(".list_car_info__2l0lA.clearfix >li:nth-child(2) > div:nth-child(1)").text()  #耗电量
        gonglishu = mt(".list_car_info__2l0lA.clearfix > li:nth-child(1) > div:nth-child(1)").text()  #公里数
        sorce_items = mt(".list_dimension_score__Il_UW.clearfix li")  #获取所有评分
        pingfen = {} #定义一个空字典存放评分
        for item in sorce_items.items():
            d_name = item(".d_name").text().strip()  #评分项名称
            d_score = item(".score").text().strip() #评分项分数
            if d_name and d_score:
                pingfen[d_name] = int(d_score)
        print(f"'车型',{car},'时间',{time},'购车经销商',{Car_dealership},'价格',{price},'耗电量',{xiaohao},'公里数',{gonglishu},'评分',{pingfen}\n")
        with open("carhome.csv","a",encoding="utf-8") as f: #保存评分
            f.write(f"'车型',{car},'时间',{time},'购车经销商',{Car_dealership},'价格',{price},'耗电量',{xiaohao},'公里数',{gonglishu},'评分',{pingfen}\n")

    
    print("数据保存完成") 
        

def main():
    url ="https://k.autohome.com.cn/6962#pvareaid=3454440"
    # 获取页面源代码
    html = get_page_source(url)
    # 解析页面源代码
    result = parse_page_source(html)




if __name__ =='__main__':
    main()