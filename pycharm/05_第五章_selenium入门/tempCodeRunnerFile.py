from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import io
import time
import sys
import os

# ========== 核心修复：绝对路径导入，绕开所有相对导入问题 ==========
# 1. 获取ddddocr的安装根目录（替换成你实际的路径）
ddddocr_root = r'D:\Python\Lib\site-packages\ddddocr'
# 2. 把core和utils目录加入Python路径（让代码能找到BaseEngine/OCREngine等）
sys.path.append(os.path.join(ddddocr_root, 'core'))
sys.path.append(os.path.join(ddddocr_root, 'utils'))

# 3. 直接导入真实的类（匹配你core/__init__.py里的OCREngine）
from ocr_engine import OCREngine  # 注意：你文件里是OCREngine（大写E），不是OcrEngine
# 4. 导入utils里的依赖（避免识别时缺依赖）
from utils import (
    ALLOWED_IMAGE_FORMATS,
    MAX_IMAGE_BYTES,
    MAX_IMAGE_SIDE,
    base64_to_image
)

# ========== 初始化OCR识别器（用真实的OCREngine类） ==========
# 新版OCREngine初始化时show_ad参数可能不需要，去掉即可
ocr = OCREngine()

# ========== 浏览器操作逻辑（完全保留你的原有逻辑） ==========
# 初始化浏览器
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
wait = WebDriverWait(driver, 10)
driver.get("https://www.chaojiying.com/user/login/")
driver.maximize_window()
time.sleep(1)  # 等待页面完全加载

# 输入超级鹰账号密码
account_input = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div/div[3]/div[1]/form/p[1]/input')))
account_input.clear()
account_input.send_keys("18614075987")

password_input = wait.until(EC.presence_of_element_located((By.XPATH,'/html/body/div[3]/div/div[3]/div[1]/form/p[2]/input')))
password_input.clear()
password_input.send_keys("q6035945")

# 获取验证码图片（双重等待，确保截图完整）
yzm_img = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div/div[3]/div[1]/form/div/img')))
time.sleep(0.8)  # 等待图片渲染完成，避免截图空白/模糊
png_data = yzm_img.screenshot_as_png  # 获取二进制截图

# ========== 验证码识别（适配OCREngine的方法） ==========
# 先尝试classification方法（通用），失败则试predict方法
try:
    yzm_result = ocr.classification(png_data)
except AttributeError:
    yzm_result = ocr.predict(png_data)

# 清洗识别结果：去除空格/换行等无效字符
yzm_result = yzm_result.strip().replace(' ', '').replace('\n', '').replace('\t', '')
print("✅ 验证码识别结果：", yzm_result if yzm_result else "识别失败，可刷新图片重试")

# 输入验证码到输入框
yzm_input = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div/div[3]/div[1]/form/p[3]/input')))
yzm_input.clear()
yzm_input.send_keys(yzm_result)

# 停留10秒查看结果
time.sleep(10)

# 关闭浏览器（如需保留，注释此行）
driver.quit()