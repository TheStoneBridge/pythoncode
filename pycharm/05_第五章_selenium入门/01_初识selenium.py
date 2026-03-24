# selenium 可以自动打开一个浏览器.
# 输入网址
# 能从页面里提取东西
# 先确定打开的是哪个浏览器   -》Chrome

from selenium.webdriver.chrome.service import Service #用于管理 Chrome 浏览器驱动（ChromeDriver）的服务进程
from webdriver_manager.chrome import ChromeDriverManager # 自动管理 ChromeDriver 的版本和下载，解决 “浏览器版本与驱动版本不匹配” 的痛点。
from selenium import webdriver #提供 Selenium 操作各类浏览器的核心 API，是实现浏览器自动化的基础。
import time

# 创建浏览器对象
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

url ='https://www.baidu.com'
driver.get(url)
print(driver.title) # 打印页面标题

time.sleep(5)

driver.quit()