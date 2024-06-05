import csv
import random
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest


class Register(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(executable_path="chromedriver")
        self.driver.get('http://localhost:8000/verydows-master/index.php?c=user&a=register')

    def test_register(self):
        a = str(random.randrange(1, 20, 1))
        self.driver.implicitly_wait(4)
        self.driver.find_element(By.XPATH, '//*[@id="username"]').send_keys('wenda' + a)
        self.driver.find_element(By.XPATH, '//*[@id="email"]').send_keys('8798'+a+'@qq.com')
        self.driver.find_element(By.XPATH, '//*[@id="password"]').send_keys('123456')
        self.driver.find_element(By.XPATH, '//*[@id="repassword"]').send_keys('123456')
        # captcha = str(input("请输入验证码："))
        # self.driver.find_element(By.XPATH, '//*[@id="captcha"]').send_keys(captcha)
        self.driver.find_element(By.XPATH, '//*[@id="register-form"]/div/div[2]/a').click()
        time.sleep(5)
        self.assertEqual(self.driver.find_element(By.XPATH, '//*[@id="top-userbar"]/a').text, 'wenda'+a,
                         "用户格式注册测试失败！")

    '''
        不正确的用户名注册
        '''

    def test_unregister(self):
        # 隐形等待
        filename = r'D:\PycharmProjects\软件测试脚本\自动化项目\test_data\data1.csv'
        with open(filename, 'r', encoding='utf-8')as f:
            self.data = csv.reader(f)
            for i in self.data:
                print(i)
                # 输入用户名
                self.driver.find_element(By.XPATH, '//*[@id="username"]').clear()
                self.driver.find_element(By.XPATH, '//*[@id="username"]').send_keys(i[0])
                # 输入注册的邮箱号
                self.driver.find_element(By.XPATH, '//*[@id="email"]').clear()
                self.driver.find_element(By.XPATH, '//*[@id="email"]').send_keys(i[1])
                # 输入要设置的密码
                self.driver.find_element(By.XPATH, '//*[@id="password"]').clear()
                self.driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(i[2])
                # 输入确认密码
                self.driver.find_element(By.XPATH, '//*[@id="repassword"]').clear()
                self.driver.find_element(By.XPATH, '//*[@id="repassword"]').send_keys(i[2])
                # # 输入验证码
                # self.driver.find_element(By.XPATH, '//*[@id="captcha"]').clear()
                # self.driver.find_element(By.XPATH, '//*[@id="captcha"]').send_keys(i[3])
                # 点击登录按钮
                self.driver.find_element(By.XPATH, '//*[@id="register-form"]/div/div[2]/a').click()
                # 判断测试结果

                self.assertEqual(self.driver.find_element(By.XPATH,
                                                          '//*[@id="register-form"]/div/dl[1]/dd/span/font').text,
                                 '用户名不符合格式要求', '反向测试不通过')

    def tearDown(self) -> None:
        self.driver.implicitly_wait(5)
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
