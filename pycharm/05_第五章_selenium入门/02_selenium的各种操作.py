#爬取拉勾网
from selenium.webdriver.chrome.service import Service #用于管理 Chrome 浏览器驱动（ChromeDriver）的服务进程
from webdriver_manager.chrome import ChromeDriverManager # 自动管理 ChromeDriver 的版本和下载，解决 “浏览器版本与驱动版本不匹配” 的痛点。
from selenium import webdriver #提供 Selenium 操作各类浏览器的核心 API，是实现浏览器自动化的基础。
from selenium.webdriver.common.by import By #提供了定位元素的方式常量（如 ID、CLASS_NAME、XPATH、CSS_SELECTOR 等） 例如可以用By.XPATH来指定使用 XPath 语法定位元素
from selenium.webdriver.common.action_chains import ActionChains # 模拟鼠标/键盘的链式操作（拖动、点击等）
from selenium.webdriver.support.wait import WebDriverWait # 显式等待：等待元素加载/可交互（避免硬等）
from selenium.webdriver.support import expected_conditions as EC # 等待条件：预定义元素状态（可点击/可见等）
from selenium.webdriver.common.keys import Keys  # Selenium 中用于模拟键盘按键操作的核心工具类，它封装了键盘上所有常用按键（包括普通字符键、功能键、组合键等）的常量，让我们可以通过代码模拟用户按下 / 释放键盘按键的行为。
from selenium.common.exceptions import TimeoutException  # 关键：导入TimeoutException
from selenium.common.exceptions import StaleElementReferenceException #专门捕获 StaleElementReferenceException
import random
import time

def random_sleep(min_time=0.5, max_time=2): #增加随机等待（替代固定time.sleep），模拟人类操作
    time.sleep(random.uniform(min_time, max_time))

# 新增：带重试的元素定位函数
def find_element_with_retry(driver, wait, by, value, retry=2):
    """
    带重试机制的元素定位，专门处理StaleElementReferenceException
    :param driver: 浏览器驱动对象
    :param wait: WebDriverWait对象
    :param by: 定位方式（By.XXX）
    :param value: 定位表达式
    :param retry: 重试次数
    :return: 定位到的元素
    :raise: TimeoutException 重试后仍失败则抛出
    """
    for _ in range(retry):
        try:
            return wait.until(EC.element_to_be_clickable((by, value)))
        except StaleElementReferenceException:
            print(f"元素 {value} 出现StaleElement异常，正在重试...")
            random_sleep(1, 2)
            continue
    raise TimeoutException(f"元素 {value} 定位失败（重试{retry}次）")

# 🔥 关键：自动尝试2个XPath获取薪资
def get_salary_with_two_xpath(driver, wait):
    # 第一个 XPath
    xpath1 = "//*[@id='__next']/div[1]/div[1]/div/div[1]/div[1]/span[2]"
    # 第二个 XPath（你新发现的）
    xpath2 = "//*[@id='__next']/div[1]/div[1]/div/div[1]/div[1]/h1/span/span/span[2]"

    try:
        return find_element_with_retry(driver, wait, By.XPATH, xpath1)
    except TimeoutException:
        print("薪资 XPath1 失败，尝试 XPath2...")
        return find_element_with_retry(driver, wait, By.XPATH, xpath2)

#1.浏览器配置:伪装正常用户，关闭自动化提示
chrome_options = webdriver.ChromeOptions()
#2.移除"Chrome正受到自动测试软件控制"的提示
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option("useAutomationExtension", False)
# 禁用Blink运行时的功能，降低被识别概率
chrome_options.add_argument("--disable-blink-features=AutomationControlled")

#2.初始化浏览器
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=chrome_options)
driver.maximize_window() #必须最大化窗口,否则滑块位置会偏移
try:
    driver.get("https://www.lagou.com/")
    wait = WebDriverWait(driver, 20)
    print("正在等待滑块出现...")
    #等待滑块出现并定位
    # 3. 核心优化: 先判断是否存在滑块验证（容错+跳过逻辑）
    
    slider = None
    try:
        slider = wait.until(
            EC.element_to_be_clickable((By.CLASS_NAME, "nc_iconfont.btn_slide"))
        )
        print("滑块已找到")
    except Exception as e:
        print(f"滑块未找到: {e}")

#4. 仅当存在滑块时才执行滑动逻辑
    if slider:
        action = ActionChains(driver)
        action.click_and_hold(slider) #按住滑块
        
        #动态获取轨道宽度(增加异常捕获:防止轨道元素定位失败)
        try:
            track = driver.find_element(By.ID,"nc_1_wrapper")
            track_width = track.size['width']
        except:
            #备用方案:使用固定宽度（根据实际情况调整）
            track_width = 300
            print("未找到滑块轨道元素，使用固定宽度")
        
        #分段滑动：模拟人类操作
        steps =15
        strp_x = track_width / steps    
        for  _ in range(steps):
            action.move_by_offset(xoffset=strp_x, yoffset=0)
            time.sleep(0.1)
        
        action.release().perform()  #释放并执行
        print("滑块已滑动完成")
        random_sleep(2, 3)
    
    search_input = wait.until(
        EC.presence_of_element_located((By.XPATH,"//*[@id='search_input']"))
    )
    search_input.clear()
    search_input.send_keys("python",Keys.ENTER)
    
    random_sleep(2, 3)
    
    # ===== 新增：切换到新打开的标签页 =====
# 1. 获取当前所有窗口的句柄（列表形式，新窗口通常是最后一个）
    windows = driver.window_handles
    driver.switch_to.window(windows[-1])
    # print(f"已切换到新标签页，当前窗口句柄：{driver.current_window_handle}")
    
    try:
    # 优化1：用presence_of_element_located验证「至少一个元素存在」，且增加可见性验证
    # 优化2：改用更稳定的搜索结果容器定位（示例，需根据实际页面调整）
        #数据提取
        
        #selenuium可以动态执行js
        driver.execute_script(   #这里是删除一个广告
            """
            var a = document.getElementsByClassName("content-right__3l85R")[0];
            a.parentNode.removeChild(a)
            """
        )
        
        
        job_count = len(wait.until(
        EC.presence_of_all_elements_located((By.XPATH, "//*[@id='openWinPostion']"))
        ))
        # 能走到这一步，说明元素存在且可见，直接判定搜索成功
        for i  in range(job_count):
            try:
                
                li = find_element_with_retry(driver, wait, By.XPATH, f"(//*[@id='openWinPostion'])[{i+1}]")
                print(li.text)
                li.click()
                
                windows = driver.window_handles
                driver.switch_to.window(windows[-1])
                
                #//*[@id="__next"]/div[1]/div[1]/div/div[1]/div[1]/h1/span/span/span[2]
                #//*[@id="__next"]/div[1]/div[1]/div/div[1]/div[1]/h1/span/span/span[2]
                salary = get_salary_with_two_xpath(driver, wait)
                print(salary.text)
                #//*[@id="job_detail"]/dd[2]/div
                job_detail = find_element_with_retry(driver, wait, By.XPATH, "//*[@id='job_detail']/dd[2]/div")
                print(job_detail.text)
                
                random_sleep(2, 3)
                #关闭窗口
                driver.close()
                random_sleep(2, 3)
                
                #切换窗口
                windows = driver.window_handles
                driver.switch_to.window(windows[-1])
            
        
         
            except TimeoutException:
                # 超时说明元素未出现，判定搜索失败
                print("搜索失败：未找到搜索结果元素")
                driver.close()
                driver.switch_to.window(driver.window_handles[-1])
                random_sleep(2, 3)
                continue
                
    except Exception as e:
        print(f"搜索结果验证异常：{e}")
    
       
    
    
except Exception as e:
    print(f"发生错误: {e}")

finally:    
    driver.quit()