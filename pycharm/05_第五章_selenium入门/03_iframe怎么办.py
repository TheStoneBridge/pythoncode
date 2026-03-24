from selenium import webdriver #提供 Selenium 操作各类浏览器的核心 API，是实现浏览器自动化的基础。
from selenium.webdriver.chrome.service import Service#用于管理 Chrome 浏览器驱动（ChromeDriver）的服务进程
from webdriver_manager.chrome import ChromeDriverManager # 自动管理 ChromeDriver 的版本和下载，解决 “浏览器版本与驱动版本不匹配” 的痛点。
from selenium.webdriver.common.by import By#提供了定位元素的方式常量（如 ID、CLASS_NAME、XPATH、CSS_SELECTOR 等） 例如可以用By.XPATH来指定使用 XPath 语法定位元素
from selenium.webdriver.support.wait import WebDriverWait # 显式等待：等待元素加载/可交互（避免硬等）
from selenium.webdriver.support import expected_conditions as EC  # 等待条件：预定义元素状态（可点击/可见等）

#1.浏览器配置:伪装正常用户，关闭自动化提示
chrome_options = webdriver.ChromeOptions()
#2.移除"Chrome正受到自动测试软件控制"的提示
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option("useAutomationExtension", False)
#禁用Blink运行时的功能，降低被识别概率
chrome_options.add_argument("--disable-blink-features=AutomationControlled")

driver= webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=chrome_options)

driver.get("https://www.yinghuadongman.com.cn/v/46941-1-1/")
#切换到iframe里面
iframe = driver.find_element(By.XPATH, '//*[@id="playleft"]/iframe')#先定位到frame
driver.switch_to.frame(iframe)#切换到frame

input = driver.find_element(By.XPATH, '//*[@id="player"]/div[2]/video')  #这个元素在iframe的网页里面 初始get不是在iframe的网页里面，不切换到iframe里面是定位不到的
src = input.get_attribute("src")
print(src)


#跳出iframe
driver.switch_to.parent_frame()
content = driver.find_element(By.XPATH,'/html/body/section/div/div/div[2]/h4/span')
print(content.text)