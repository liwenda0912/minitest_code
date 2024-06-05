import csv
import time
import unittest
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By


class Login:
    def open1(self, driver):
        self.driver = driver
        self.driver.get('http://localhost:8000/verydows-master/index.php?c=user&a=login')
        self.driver.implicitly_wait(2)
        self.login()

    def login(self):
        self.driver.implicitly_wait(2)
        # 输入账号
        self.driver.find_element(By.XPATH, '//*[@id="username"]').send_keys('liwenda')
        # 输入密码
        self.driver.find_element(By.XPATH, '//*[@id="password"]').send_keys('123456')
        # num = input("请输入验证码：")
        # self.driver.find_element(By.XPATH, '//*[@id="captcha"]').send_keys(num)
        # 点击登录
        self.driver.find_element(By.XPATH, '//*[@id="login-form"]/div/a').click()
        self.off()
        time.sleep(6)

    def off(self):
        self.driver.implicitly_wait(2)


class unLogin(unittest.TestCase):
    filename = r'D:\PycharmProjects\软件测试脚本\自动化项目\test_data\data.csv'

    def setUp(self) -> None:
        pass

    def test_unLogin(self):
        with open(self.filename, 'r', encoding='utf-8')as f:
            data1 = csv.reader(f)
            for i in data1:
                self.driver = webdriver.Chrome()
                self.driver.get('http://localhost:8000/verydows-master/index.php?c=user&a=login')
                self.driver.implicitly_wait(2)
                self.driver.implicitly_wait(2)
                # 输入账号
                self.driver.find_element(By.XPATH, '//*[@id="username"]').send_keys(i[0])
                # 输入密码
                self.driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(i[1])
                # 点击登录
                self.driver.find_element(By.XPATH, '//*[@id="login-form"]/div/a').click()
                time.sleep(4)
                if i[0] != '':
                    if i[1] != '':
                        self.assertEqual(self.driver.find_element(By.XPATH,
                                                                  '/html/body/div/div[2]/h3').text,
                                         '用户名或密码错误', '反向测试不通过')
                    else:
                        self.assertEqual(self.driver.find_element(By.XPATH,
                                                                  '//*[@id="login-form"]/div/dl[2]/dd/span/font').text,
                                         '请输入密码', '反向测试不通过')
                else:
                    self.assertEqual(self.driver.find_element(By.XPATH,
                                                              '//*[@id="login-form"]/div/dl[1]/dd/span/font').text,
                                     '请输入用户名', '反向测试不通过')

                self.driver.quit()

    def tearDown(self) -> None:
        pass


# 接口测试
# header = {
#             'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,'
#                       'image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9 ',
#             'Cookie': 'VDSSKEY=u0c6kc08h4cbbfutmemba39aia; UVID=2c20ec487f0ee8085e6dbd55d915c62d; LOGINED_USER=liwenda',
#             'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
#                           'Chrome/104.0.5112.102 Safari/537.36'
#         }
# url = self.driver.current_url
# response = requests.get(url=url, headers=header)
# print(response.status_code)
# print(response.headers)


if __name__ == '__main__':
    driver = webdriver.Chrome()
    Login().open1(driver)
    unittest.main()
