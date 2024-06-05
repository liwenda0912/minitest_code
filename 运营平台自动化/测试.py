from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pytesseract
from selenium.webdriver.common.action_chains import ActionChains
from PIL import Image
import json

# driver = webdriver.Chrome()
# driver.get('https://www.baidu.com')
# driver.maximize_window()
# time.sleep(5)
# action = ActionChains(driver)
#
# # 点击登录按钮
# driver.find_element(By.XPATH, '//*[@id="u1"]/a').click()
# # print(driver.find_element(By.XPATH, '//*[@id="u1"]/a').is_displayed())
# time.sleep(5)
# ac = driver.find_element(By.XPATH, '//*[@id="s-top-loginbtn"]')
#
# # 模拟js点击按钮
# # ad = driver.find_element(By.XPATH, '//*[@id="s-usersetting-top"]')
# # driver.execute_script('arguments[0].click();', ad)
#
# # 点击账号输入框并输入登录账号
# action.move_to_element(driver.find_element(By.XPATH, '//*[@id="TANGRAM__PSP_11__userName"]')).perform()
# action.click(driver.find_element(By.XPATH, '//*[@id="TANGRAM__PSP_11__userName"]')).send_keys(
#     '15767112315').perform()
#
# # 点击密码输入框并输入密码
# action.move_to_element(driver.find_element(By.XPATH, '//*[@id="TANGRAM__PSP_11__password"]')).perform()
# action.click(driver.find_element(By.XPATH, '//*[@id="TANGRAM__PSP_11__password"]')).send_keys(
#     'da.09123').perform()
# # 点击登录按钮
# driver.find_element(By.XPATH, '//*[@id="TANGRAM__PSP_11__submit"]').click()
# time.sleep(5)
# # 获取登录的账户名称
# name = driver.find_element(By.XPATH, '//*[@id="s-top-username"]/span[2]').get_attribute('innerText')
#
# # 校验账户
# if name == 'LeeboringLee':
#     # 获取登录账号的cookie信息
#     d = driver.get_cookies()
with open('1.txt', 'r') as f:
    d = f.read()
    d = json.loads(d)
    driver = webdriver.Chrome()
    driver.get('https://www.baidu.com')
    time.sleep(5)
    # 将获取到的cookie一个一个提取出来
    for cookie in d:
        name = driver.find_element(By.XPATH, '//*[@id="u1"]/a').get_attribute('innerText')
        print(cookie)
        # cookie_dict = {
        #     'domain': cookie.get('domain'),
        #     'name': cookie.get('name'),
        #     'value': cookie.get('value'),
        #     "expires": cookie.get('expiry'),
        #     'path': '/',
        #     'httpOnly': False,
        #     'secure': False
        # }
        # 网页加载cookie
        if name != 'LeeboringLee':
            driver.add_cookie(cookie)
            driver.get('https://www.baidu.com')
            driver.refresh()
            time.sleep(5)
        time.sleep(10)
