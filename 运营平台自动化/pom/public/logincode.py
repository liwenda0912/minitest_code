import time
import unittest
from selenium.common import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from 运营平台自动化.pom.public.HandlePicture import Handle_Img
from 运营平台自动化.pom.public.HandlePicture import Get_CheckCode
from 运营平台自动化.pom.public.public import Public
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class Login2(unittest.TestCase):
    def setUp(self, ) -> None:
        pass

    # def test_login1(self):
    #     self.driver = webdriver.Chrome()
    def test_login2(self, driver):
        self.driver = driver
        self.driver.maximize_window()
        self.url = 'http://172.16.0.17:8303/user/evking_login'
        self.PUBLIC = Public(self.driver, self.url)
        self.PUBLIC.Open_url()
        # self.driver.get(self.url)
        # 填写登录账号
        # self.driver.find_element(By.XPATH, '//*[@id="username"]').click()
        # self.driver.find_element(By.XPATH, '//*[@id="username"]').send_keys('15767112315')
        self.PUBLIC.Click(By.XPATH, '//*[@id="username"]')
        self.PUBLIC.Send_key((By.XPATH, '//*[@id="username"]'), '15767112315')
        # 填写登录密码
        # self.driver.find_element(By.XPATH, '//*[@id="pwd"]').click()
        # self.driver.find_element(By.XPATH, '//*[@id="pwd"]').send_keys('da091234')
        self.PUBLIC.Click(By.XPATH, '//*[@id="pwd"]')
        self.PUBLIC.Send_key((By.XPATH, '//*[@id="pwd"]'), 'da091234')
        # 处理验证码图片
        while True:
            # 获取验证码
            # self.driver.find_element(By.XPATH, '//*[@id="refreshCheckcode"]/span/i').click()
            self.PUBLIC.Click(By.XPATH, '//*[@id="refreshCheckcode"]/span/i')
            time.sleep(3)
            # self.driver.find_element(By.XPATH, '//*[@id="imgcheckcode"]').screenshot('imgcheckcode_picture/imgcheckcode.png')
            self.PUBLIC.ScreenShot((By.XPATH, '//*[@id="imgcheckcode"]'), '../picture/checkcode.png')
            Handle_Img()
            checkcode = Get_CheckCode()
            # 填写验证码
            # self.driver.find_element(By.XPATH, '//*[@id="checkcode"]').click
            self.PUBLIC.Click(By.XPATH, '//*[@id="checkcode"]')
            # self.driver.find_element(By.XPATH, '//*[@id="checkcode"]').clear()
            self.PUBLIC.ClearKey(By.XPATH, '//*[@id="checkcode"]')
            # self.driver.find_element(By.XPATH, '//*[@id="checkcode"]').send_keys(checkcode)
            self.PUBLIC.Send_key((By.XPATH, '//*[@id="checkcode"]'), checkcode)
            try:
                self.PUBLIC.Click(By.XPATH, '//*[@id="login"]')
                time.sleep(2)
                if self.PUBLIC.Find_element_Text(By.XPATH, '//*[@class="layui-layer layui-layer-tips"]') == '请输入验证码':
                    self.PUBLIC.Click(By.XPATH, '//*[@id="refreshCheckcode"]/span/i')
                    self.PUBLIC.ScreenShot((By.XPATH, '//*[@id="imgcheckcode"]'), '../picture/checkcode.png')
                    Handle_Img()
                    checkcode = Get_CheckCode()
                    self.PUBLIC.Click(By.XPATH, '//*[@id="checkcode"]')
                    self.PUBLIC.ClearKey(By.XPATH, '//*[@id="checkcode"]')
                    self.PUBLIC.Send_key((By.XPATH, '//*[@id="checkcode"]'), checkcode)
                    self.PUBLIC.Click(By.XPATH, '//*[@id="login"]')
            except NoSuchElementException:
                element = WebDriverWait(self.driver, timeout=50, poll_frequency=0.5, ignored_exceptions=None).until(
                    EC.presence_of_element_located((By.XPATH, '//*[@class="layui-layer layui-layer-dialog '
                                                              'layui-layer-border layui-layer-msg '
                                                              'layui-layer-hui"]')), "找不到该元素")
                if element:
                    if self.PUBLIC.Find_element_Text(By.XPATH, '//*[@class="layui-layer layui-layer-dialog '
                                                               'layui-layer-border layui-layer-msg '
                                                               'layui-layer-hui"]') == '登录成功':
                        break
                else:
                    print(element)
            finally:
                element = WebDriverWait(self.driver, timeout=50, poll_frequency=0.5, ignored_exceptions=None).until(
                    EC.presence_of_element_located((By.XPATH, '//*[@class="layui-layer layui-layer-dialog '
                                                              'layui-layer-border layui-layer-msg '
                                                              'layui-layer-hui"]')), "找不到该元素")
                if element:
                    if self.PUBLIC.Find_element_Text(By.XPATH, '//*[@class="layui-layer layui-layer-dialog '
                                                               'layui-layer-border layui-layer-msg '
                                                               'layui-layer-hui"]') == '登录成功':
                        break
                else:
                    print(element)

    def tearDown(self) -> None:
        time.sleep(10)


if __name__ == '__main__':
    unittest.main()
