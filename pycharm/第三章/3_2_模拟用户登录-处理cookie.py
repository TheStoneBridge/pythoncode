#登录 ->得到cookie
#带着cookie 去请求到书架url->书架上的内容
#必须得把上面的两个操作连起来
#我们可以使用session进行请求 -> session你可以认为是一连串的请求。在这个过程中的cookie不会丢失
from PIL import Image
# 给高版本的 LANCZOS 起别名 ANTIALIAS，兼容旧依赖
Image.ANTIALIAS = Image.LANCZOS

import requests
import ddddocr
import time
import io
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By  # 补充导入By（原代码遗漏）
from pyquery import PyQuery   #用puquery来查找页面元素

import io

# 初始化OCR识别器
ocr = ddddocr.DdddOcr()

# 会话
session = requests.session()
data={
    "username": "zxcasdqwe",
    "password": "zxcqwe123"
}



#1. 登录
url = 'https://www.171k.com/login'
#初始化浏览器
# 初始化浏览器（带防反爬配置）
options = webdriver.ChromeOptions()
options.add_argument("--disable-blink-features=AutomationControlled")  # 禁用自动化检测
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)

try:
    # 打开登录页
    driver.get("https://www.171k.com/login")
    driver.maximize_window()  # 最大化窗口，模拟真人操作
    
    # ---------------------- 定位并输入用户名 ----------------------
    username_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "uname"))
    )
    username_input.send_keys("zxcasdqwe")  # 你的用户名

    # ---------------------- 定位并输入密码 ----------------------
    password_input = driver.find_element(By.NAME, "password")
    password_input.send_keys("zxcqwe123")  # 你的密码

    # ---------------------- 识别并输入验证码 ----------------------
    # 1. 定位验证码图片元素（需根据实际页面调整定位方式）
    # 常见定位方式：By.ID / By.CLASS_NAME / By.XPATH / By.CSS_SELECTOR
    captcha_img = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//img[contains(@src, 'captcha')]"))  # 需替换为实际验证码图片的XPATH
    )
    # 截取验证码图片（通过字节流方式，避免保存本地）
    captcha_screenshot = captcha_img.screenshot_as_png
    
    # OCR识别验证码
    captcha_code = ocr.classification(captcha_screenshot)
    print(f"识别到的验证码：{captcha_code}")
    
    # 定位验证码输入框（请根据实际页面调整定位方式，示例用NAME）
    captcha_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "captcha"))  # 替换为实际验证码输入框的NAME/ID/XPATH
    )
    
    captcha_input.clear()
    captcha_input.send_keys(captcha_code)
    
    # ---------------------- 5. 提交登录表单 ----------------------
    # 定位登录按钮（请根据实际页面调整定位方式）
    login_btn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@type='submit' and @class='btn btn-primary']"))  # 替换为实际登录按钮的定位
    )
    login_btn.click()
    
    # 等待登录跳转（确保登录成功）
    time.sleep(2)
    # 验证是否登录成功（可根据跳转后的URL/页面元素判断）
    if "login" not in driver.current_url:
        print("登录成功！")
    else:
        raise Exception("登录失败，可能是验证码错误/账号密码错误")
    
    # ---------------------- 6. 提取浏览器cookie并同步到requests会话 ----------------------
    # 获取浏览器的所有cookie
    browser_cookies = driver.get_cookies()
    # 将cookie添加到requests会话中
    for cookie in browser_cookies:
        session.cookies.set(cookie['name'], cookie['value'])
    
        # ---------------------- 7. 携带cookie请求书架内容 ----------------------
    # 替换为实际的书架URL
    bookshelf_url = "https://www.171k.com/user/412/bookcase"
    # 发送请求（模拟登录后的访问）
    response = session.get(bookshelf_url, headers={
        "User-Agent": driver.execute_script("return navigator.userAgent;")  # 复用浏览器的UA，防反爬
    })

    # 验证书架请求结果
    if response.status_code == 200:
        print("书架请求成功！")
        # print("书架页面内容", response.text)
        # print("书架页面的cookie", response.cookies)
        doc = PyQuery(response.text)   
        # 定位table下所有tr（跳过表头）
        tr_list = doc("table.table tr").items()  # 改用items()遍历，更稳定
        next(tr_list)  # 跳过第一个表头行
        
        for tr in tr_list:
            #书名
            book_name = tr.find("td.even a").text()
            #最新章节
            latest_chapter = tr.find("td.odd a").text()
            #更新时间
            update_time = tr.find("td.hidden-xs").text()
            print(f"书名：{book_name}，最新章节：{latest_chapter}，更新时间：{update_time}\n")
    else:
        print(f"书架请求失败，状态码：{response.status_code}")
    
except Exception as e:
    # 原代码只打印 str(e)，改为打印完整报错信息
    import traceback  # 导入打印堆栈的模块
    print(f"执行过程出错：{str(e)}")
    print("完整报错堆栈：")
    print(traceback.format_exc())  # 打印详细的错误位置和原因

finally:
    # 关闭浏览器和会话
    driver.quit()
    session.close()
    print("浏览器已关闭，会话已结束")