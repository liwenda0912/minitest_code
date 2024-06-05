
import time
from selenium.webdriver import ChromeOptions
from selenium.webdriver import ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By


# 获取某一页的html(想获取那一页就放在跳转之后的代码下面
# win = c.window_handles
# time.sleep(2)
# c.switch_to.window(win[0])
# print(c.page_source)


def login():
    # 模拟人为在浏览器登录，防止淘宝识别是selenium访问
    option = ChromeOptions()
    option.add_argument('--disable-blink-features=AutomationControlled')  # 设置当前爬虫行为不是selenium自动框架
    c = webdriver.Chrome(executable_path="chromedriver", options=option)  # options=option是应用防识别selenium
    c.get("https://www.taobao.com")
    c.find_element(By.XPATH, '//*[@id="J_SiteNavLogin"]/div[1]/div[1]/a[1]').click()
    loginButtom(c)


def loginButtom(c):
    username = '15767112315'
    ps = 'da.09123'
    c.find_element(By.XPATH, '//*[@id="fm-login-id"]').send_keys(username)
    c.find_element(By.XPATH, '//*[@id="fm-login-password"]').send_keys(ps)
    c.find_element(By.XPATH, '//*[@id="login-form"]/div[4]/button').click()
    win = c.window_handles
    time.sleep(1)
    c.switch_to.window(win[0])
    if c.find_element(By.XPATH, '//*[@id="J_SiteNavLogin"]/div[1]/div/a').text == 't_1501927449804_0190':
        uesrMessage(c)

    else:
        messageCheck(c)


def messageCheck(c):
    iframe = c.find_element(By.XPATH, '//*[@id="content"]/div/div[1]/iframe')
    c.switch_to.frame(iframe)
    c.find_element(By.XPATH, '//*[@id="otherValidator"]').click()
    c.find_element(By.XPATH, '//*[@id="content"]/div/ol/li[1]/a').click()
    c.find_element(By.XPATH, '//*[@id="J_GetCode"]').click()
    number = input("请输入短信验证码:")
    c.find_element(By.XPATH, '//*[@id="J_Phone_Checkcode"]').send_keys(number)
    c.find_element(By.XPATH, '//*[@id="submitBtn"]').click()
    uesrMessage(c)


def uesrMessage(c):
    c.find_element(By.XPATH,'/html/body/div[3]/div[2]/div[1]/div/ul[1]/li[3]/a').click()
    win = c.window_handles
    time.sleep(1)
    c.switch_to.window(win[0])
    print(win)
    da = c.find_element(By.XPATH, '/html/body/div[3]/div[2]/div[2]/div[2]/div[5]/div/div[1]/a')
    time.sleep(10)
    page(c,win)

def page(c, win):
    c.switch_to.window(win[1])
    print(c.page_source)


if __name__ == '__main__':
    login()
