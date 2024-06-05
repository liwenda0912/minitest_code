import time
import unittest
from selenium import webdriver
from 运营平台自动化.pom.public.public import Public
from 运营平台自动化.pom.public.logincode import Login2
from 运营平台自动化.pom.public.Assert import Assert
from selenium.webdriver.common.by import By


class Grant_coupon(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        Login2().test_login2(self.driver)
        self.url = ''
        self.PUBLIC = Public(self.driver, self.url)

    def test_grant_coupon(self):
        # 测试代码
        # self.PUBLIC.Open_url()
        # self.a = (By.XPATH, '//*[@id="kw"]')
        # print(self.a)
        # self.PUBLIC.WaitElement(self.a, 'test')
        # self.PUBLIC.Send_key(self.a, '百度')
        # time.sleep(20)
        # self.PUBLIC.Click(By.XPATH, '//*[@id="hotsearch-content-wrapper"]/li[6]/a/span[2]')

        # 发放优惠券
        self.PUBLIC.Action_WaitElements((By.XPATH, '//*[@id="wrapper"]/div[2]/nav/ul[1]/li[2]/a/span'), '无法点击资源中心')
        self.PUBLIC.WaitElement((By.XPATH, '//*[@id="wrapper"]/div[2]/nav/ul[1]/li[2]/ul/li[2]/ul/li[3]'), '无法访问优惠券管理')
        self.PUBLIC.Frame_switch_window((By.XPATH, '//*[@id="page-content"]/iframe[2]'), '找不到iframe的id为"page-content"里的iframe[2]的元素')
        self.PUBLIC.WaitElement((By.XPATH, '//*[@id="0"]/td[13]/div/button[5]/i'), '找不到发放按钮')
        # 填写发放用户信息
        self.PUBLIC.Switch_Window()
        self.PUBLIC.WaitElement((By.XPATH, '//*[@id="layui-layer1"]'), '无法找到发放优惠券弹窗')
        self.PUBLIC.Frame_switch_window((By.XPATH, '//*[@id="layui-layer-iframe1"]'), '找不到iframe的id为layui-layer-iframe1的元素')
        self.PUBLIC.Send_key((By.XPATH, '//*[@id="assign"]/div[1]/div[5]/div/div/input'), '15767112316')
        self.PUBLIC.Click(By.XPATH, '//*[@id="assign"]/div[1]/div[5]/div/span/button')
        self.PUBLIC.WaitElement((By.XPATH, '//*[@id="assign"]/div[1]/div[6]/div/div/div[3]/table/tbody/tr/td[1]/div/label/span/span'), '该元素不存在')
        self.PUBLIC.Click(By.XPATH, '//*[@id="actions"]/button')
        # 二次确认发放
        self.PUBLIC.Click(By.XPATH, '//*[@id="layui-layer3"]/div[3]/a[1]')
        Assert().assertTest_Send(self.driver)

    def tearDown(self) -> None:
        time.sleep(2)
        self.driver.quit()
