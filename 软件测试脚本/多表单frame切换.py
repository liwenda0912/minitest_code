import time

from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="chromedriver")
driver.get('https://www.qq.com/')
driver.find_element(By.XPATH, '//*[@id="top-login"]/div[2]/a').click()
# 页面切换
# 1.获取handle句柄的所有值
handle = driver.window_handles
print(handle)
# 切换到要跳转的页面
driver.switch_to.window(handle[1])
# 内嵌frame标签的切换
# 1.获取frame标签的属性
frame = driver.find_element(By.ID, 'login_frame')
# 2.跳转到frame里面的html页面
driver.switch_to.frame(frame)
time.sleep(2)
# 进行密码登录
driver.find_element(By.XPATH, '//*[@id="u"]').send_keys('username')
driver.find_element(By.XPATH, '//*[@id="p"]').send_keys('password')
driver.find_element(By.XPATH, '//*[@id="login_button"]').click()
time.sleep(10)
# close()是关闭当前页面，quit（）是关闭浏览器
driver.quit()
