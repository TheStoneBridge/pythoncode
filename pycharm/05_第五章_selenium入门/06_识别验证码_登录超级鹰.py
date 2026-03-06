from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from cnocr import CnOcr
import io
import time
from PIL import Image
import numpy as np

# ========== 初始化OCR识别器（专门适配字母数字验证码，零参数坑） ==========
# rec_model_name='en_number_mobile_v2.0' 英文+数字专属模型，验证码识别率拉满
# det_model_name='naive_det' 轻量检测模型，适配小尺寸验证码，无需大模型
ocr = CnOcr(
    rec_model_name='en_number_mobile_v2.0',
    det_model_name='naive_det',
    context='cpu'  # 强制用CPU，避免显卡驱动问题，零报错
)

# ========== 浏览器操作逻辑（完全保留你的原有逻辑，无缝兼容） ==========
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

# 获取验证码图片（双重等待，确保截图完整清晰）
yzm_img = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div/div[3]/div[1]/form/div/img')))
time.sleep(0.8)  # 等待图片渲染完成，避免截图空白/模糊
png_data = yzm_img.screenshot_as_png  # 二进制截图，无需存本地

# 图片格式转换（cnocr需要numpy数组格式）
img = Image.open(io.BytesIO(png_data))
img_np = np.array(img)

# ========== 验证码识别+结果清洗 ==========
result = ocr.ocr(img_np)
# 拼接识别内容，去除无效字符，统一转大写（适配超级鹰验证码）
yzm_result = "".join([item['text'] for item in result]).strip().replace(' ', '').replace('\n', '').upper()
print("✅ 验证码识别结果：", yzm_result if yzm_result else "识别失败，可刷新图片重试")

# 输入验证码到输入框
yzm_input = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div/div[3]/div[1]/form/p[3]/input')))
yzm_input.clear()
yzm_input.send_keys(yzm_result)

# 如需自动登录，取消下面注释
# login_btn = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div/div[3]/div[1]/form/p[4]/input')))
# login_btn.click()

time.sleep(10)
driver.quit()