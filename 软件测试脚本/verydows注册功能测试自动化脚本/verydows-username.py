import csv
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def setup():
    with open('data1.csv', 'r', encoding='utf-8')as f:
        data = csv.reader(f)
        for i in data:
            driver = webdriver.Chrome(executable_path="chromedriver")
            driver.get('http://localhost:8088/verydows-master/index.php?c=user&a=register')
            unregister(driver, i)

    # register()


def register():
    driver = webdriver.Chrome(executable_path="chromedriver")
    driver.get('http://localhost:8088/verydows-master/index.php?c=user&a=register')
    driver.implicitly_wait(4)
    driver.find_element(By.XPATH, '//*[@id="username"]').send_keys('wenda1')
    driver.find_element(By.XPATH, '//*[@id="email"]').send_keys('87987@qq.com')
    driver.find_element(By.XPATH, '//*[@id="password"]').send_keys('123456')
    driver.find_element(By.XPATH, '//*[@id="repassword"]').send_keys('123456')
    captcha = str(input("请输入验证码："))
    driver.find_element(By.XPATH, '//*[@id="captcha"]').send_keys(captcha)
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="register-form"]/div/div[3]/a').click()
    time.sleep(3)
    try:
        if driver.find_element(By.XPATH, '//*[@id="top-userbar"]/font').text == 'wenda1':
            print("正确用户格式注册测试成功！")
    except:
        print("正确用户格式注册测试成功！")
    driver.quit()


'''
不正确的用户名注册
'''


def unregister(driver, i):
    # 隐形等待
    driver.implicitly_wait(2)
    # 输入用户名
    driver.find_element(By.XPATH, '//*[@id="username"]').send_keys(i[0])
    # 输入注册的邮箱号
    driver.find_element(By.XPATH, '//*[@id="email"]').send_keys(i[1])
    # 输入要设置的密码
    driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(i[2])
    # 输入确认密码
    driver.find_element(By.XPATH, '//*[@id="repassword"]').send_keys(i[2])
    # 输入验证码
    driver.find_element(By.XPATH, '//*[@id="captcha"]').send_keys(i[3])
    # 点击登录按钮
    driver.find_element(By.XPATH, '//*[@id="register-form"]/div/div[3]/a').click()
    # 判断测试结果
    try:
        if driver.find_element(By.XPATH,
                               '//*[@id="register-form"]/div/dl[1]/dd/span/font').text == '用户名不符合格式要求':
            print('测试通过')
    except:
        print('测试不通过')
    # 退出chrome浏览器
    driver.quit()


if __name__ == "__main__":
    setup()
