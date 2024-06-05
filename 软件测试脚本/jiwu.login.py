import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="chromedriver")
driver.get('http://cd.jiwu.com/fangjia/')

# 浏览器页面大小
driver.set_window_size(1080,500)
time.sleep(2)

# 最大化窗口
driver.maximize_window()
time.sleep(2)

# 最小化窗口
driver.minimize_window()

# 窗口刷新
driver.refresh()
if driver.find_element(By.XPATH, '//*[@id="login_header"]').is_enabled():
    # 判断是否被选择.is_selected()    是否显示.is_enabled()    是否隐藏.is_displayed():
    print('yes')
else:
    print("no")

# 获取文本信息（警告，提示框）的文本
print(driver.find_element(By.XPATH, "/html/body/div[5]/div[1]/div[5]/div[1]").text)
driver.find_element(By.XPATH, '//*[@id="login_header"]').click()

# 窗口截图截图
# driver.save_screenshot('1.png')
driver.get_screenshot_as_file("{}.{}".format('p/liwenda','png'))

driver.find_element(By.XPATH, '//*[@id="phone"]').send_keys('1576711231')
driver.find_element(By.XPATH, '//*[@id="send-verify-code"]').click()
time.sleep(2)
print(driver.find_element(By.XPATH, '//*[@id="merr1"]').text)
time.sleep(2)

# 清理输入框里的数据或字符串
driver.find_element(By.XPATH, '//*[@id="phone"]').clear()
driver.find_element(By.XPATH, '//*[@id="phone"]').send_keys('15767112315')
driver.find_element(By.XPATH, '//*[@id="send-verify-code"]').click()
time.sleep(2)

# 获取文本信息（警告，提示框）的文本
print(driver.find_element(By.XPATH, '//*[@id="merr1"]').text)
time.sleep(2)

# 收取属性的值
value = driver.find_element(By.XPATH, '//*[@id="merr1"]').get_attribute('id')
print(value)

driver.find_element(By.XPATH,'//*[@id="quick-login"]/div/i').click()

# 窗口后退
driver.back()
time.sleep(2)
# 窗口退出(只退出driver绑定的句柄）
driver.close()
