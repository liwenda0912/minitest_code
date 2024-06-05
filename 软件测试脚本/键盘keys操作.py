# 使用send_keys(参数)
# 参数：1.keys.space 空格
# keys.tab
# keys.control,"a" 全选
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get('https://www.baidu.com')

driver.find_element(By.XPATH, '//*[@id="kw"]').send_keys('seleniumm')
time.sleep(1)
# 删除一个m
driver.find_element(By.XPATH, '//*[@id="kw"]').send_keys(Keys.BACK_SPACE)
time.sleep(1)
# 拼接
driver.find_element(By.XPATH, '//*[@id="kw"]').send_keys('教程')
time.sleep(1)
# 全选输入框的文本
driver.find_element(By.XPATH, '//*[@id="kw"]').send_keys(Keys.CONTROL, 'a')
time.sleep(1)
# 剪切文本框的文字
driver.find_element(By.XPATH, '//*[@id="kw"]').send_keys(Keys.CONTROL, 'x')
time.sleep(1)
# 粘贴文本
driver.find_element(By.XPATH, '//*[@id="kw"]').send_keys(Keys.CONTROL, 'v')
time.sleep(1)
# 回车
driver.find_element(By.XPATH, '//*[@id="kw"]').send_keys(Keys.ENTER)
time.sleep(1)

driver.close()
