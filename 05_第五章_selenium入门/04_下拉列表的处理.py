from selenium import webdriver#引入 Selenium 的浏览器驱动核心模块，是 Selenium 自动化的基础。
from selenium.webdriver.chrome.service import Service#专门管理Chrome 浏览器驱动（chromedriver）的服务进程，是 Selenium 4.x 版本的新特性（替代了旧版本的直接传驱动路径）。
from webdriver_manager.chrome import ChromeDriverManager#自动管理 chromedriver 驱动文件，是第三方实用库（需提前pip install webdriver-manager）。自动检测你本地安装的 Chrome 浏览器版本，自动下载对应版本的 chromedriver，无需手动去官网下载、配置路径。
from selenium.webdriver.chrome.options import Options#创建并配置Chrome 浏览器的启动选项，实现浏览器的个性化启动（无界面、禁用弹窗、设置分辨率等）。
from selenium.webdriver.support.select import Select #下拉列表<select>
from selenium.webdriver.common.by import By #By类，提供多种元素定位方式，如id、name、class、xpath等。



driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install())
)#创建 Chrome 浏览器对象，并传入浏览器驱动的服务进程对象。
driver.get() #打开网页
sel = driver.find_element_by_id("select") #通过id定位下拉列表
sel_new =Select(sel) #创建Select对象

print(sel_new.options) #打印所有选项
for i in range(len(sel_new.options)):
    sel_new.select_by_index(i) #通过索引选择选项
    time.sleep(2) #切换完之后再加载
    #切换完之后。
    trs = web.find_element_by_xpath("tr") #通过xpath定位表格行
    for i in trs:
        print(i.text)

#selenium 可以获取页面代码（不是页面源代码，而是F12的elements的内容）