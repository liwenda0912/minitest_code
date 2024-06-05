# 1.perform（） 运行存储在actionchains里面的动作
# 2.double_click() 双击
# 3.context_click（）右击
# 4.move_to_element() 鼠标悬浮
# 5.drag_and_drop（）拖拽
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://www.baidu.com')
action = ActionChains(driver)
# 鼠标悬停
# move = driver.find_element(By.XPATH, '//*[@id="form"]/span[1]/span[1]')
# action.move_to_element(move).perform()
# time.sleep(2)

# 鼠标右击
# move = driver.find_element(By.XPATH, '//*[@id="form"]/span[1]/span[1]')
# action.context_click(move).perform()
# time.sleep(2)

# 鼠标双击
move = driver.find_element(By.XPATH, '//*[@id="form"]/span[1]/span[1]')
action.double_click(move).perform()
time.sleep(2)

driver.quit()
