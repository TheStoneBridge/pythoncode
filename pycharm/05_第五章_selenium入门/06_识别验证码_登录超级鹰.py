from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.chaojiying.com/user/login/") #打开登录页面

png = driver.find_element(By.XPATH, '/html/body/div[3]/div/div[3]/div[1]/form/div/img') #定位验证码图片

