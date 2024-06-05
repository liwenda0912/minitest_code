import time
import unittest
from selenium.webdriver.common.by import By
from 运营平台自动化.pom.public.logincode import Login2
from 运营平台自动化.pom.public.public import Public
from selenium import webdriver


class StopChargeService(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.url = ''
        Login2().test_login2(self.driver)
        self.PUBLIC = Public(self.driver, self.url)

    def test_Charge_Service_Option(self):
        self.PUBLIC.Action_WaitElements((By.XPATH, '//*[@id="wrapper"]/div[2]/nav/ul[1]/li[1]/a/span'), '无法点击资源中心')
        # 访问卡包管理界面
        self.PUBLIC.WaitElement((By.XPATH, '//*[@id="wrapper"]/div[2]/nav/ul[1]/li[1]/ul/li[2]/ul/li[2]'),
                                '无法访问充电服务监控')
        self.PUBLIC.Frame_switch_window((By.XPATH, '//*[@id="page-content"]/iframe[2]'), '无法访问卡包界面的element')
        # 点击创建储值卡按钮
        self.PUBLIC.WaitElement((By.XPATH, '//*[@id="btn-search"]'),
                                '找不到搜索按钮')
        time.sleep(2)
        self.PUBLIC.Send_key((By.XPATH, '//*[@id="serviceNo"]'), 'S23092647240381064')
        self.PUBLIC.Click(By.XPATH, '//*[@id="search-form"]/div[1]/div/div[24]/div/input[1]')
        time.sleep(2)
        self.PUBLIC.ClearKey(By.XPATH, '/html/body/div[8]/div[1]/div/div[1]/span[1]/span[1]/div/input')
        self.PUBLIC.Send_key((By.XPATH, '/html/body/div[8]/div[1]/div/div[1]/span[1]/span[1]/div/input'), '2023-09-01')
        self.PUBLIC.Click(By.XPATH, '/html/body/div[8]/div[2]/button[2]')
        self.PUBLIC.Click(By.XPATH, '//*[@id="search_submit"]')
        self.PUBLIC.Click(By.XPATH, '//*[@id="btn-search"]')
        time.sleep(2)
        if self.PUBLIC.Find_element_Text(By.XPATH, '//*[@id="0"]/td[8]/div/span') == '废弃':
            print('订单已废弃，无法操作订单')
            self.driver.quit()
        elif self.PUBLIC.Find_element_Text(By.XPATH, '//*[@id="0"]/td[8]/div/span') == '充电中':
            self.Stop_Charge_Service()
        elif self.PUBLIC.Find_element_Text(By.XPATH, '//*[@id="0"]/td[8]/div/span') == '充电异常':
            self.Interrupt_Charge_Service()
        elif self.PUBLIC.Find_element_Text(By.XPATH, '//*[@id="0"]/td[8]/div/span') == '已完成':
            self.After_Sales_Charge_Service()
        elif self.PUBLIC.Find_element_Text(By.XPATH, '//*[@id="0"]/td[8]/div/span') == '异常中':
            self.Exception_Handling_charge_Service()
        else:
            print('订单已废弃，无法操作订单')
            self.driver.quit()

    def Stop_Charge_Service(self):
        time.sleep(2)
        self.PUBLIC.Click(By.XPATH, '//*[@id="0"]/td[13]/div/button[1]')
        self.PUBLIC.Switch_Window()
        self.PUBLIC.Frame_switch_window((By.XPATH, '//*[@id="layui-layer-iframe1"]'), ' 找不到该iframe元素')
        self.PUBLIC.Click(By.XPATH, '//*[@id="panel-tab"]/ul/li[3]')
        time.sleep(2)
        if self.PUBLIC.Find_element_Text(By.XPATH, '//*[@id="vertical-timeline"]/div[1]/div[2]/p/span') == '充电策略:直到充满':
            self.PUBLIC.Click(By.XPATH, '//*[@id="vertical-timeline"]/div[1]/div[2]/input')

    def Interrupt_Charge_Service(self):
        time.sleep(2)
        if self.PUBLIC.Find_element_Text(By.XPATH, '//*[@id="0"]/td[13]/div/button[2]') == '挂起':
            self.PUBLIC.Click(By.XPATH, '//*[@id="0"]/td[13]/div/button[2]')
            self.PUBLIC.WaitElement((By.XPATH, '//*[@id="layui-layer1"]/div[3]/a[1]'), '找不到确认按钮')

    def Exception_Handling_charge_Service(self):
        time.sleep(2)
        if self.PUBLIC.Find_element_Text(By.XPATH, '//*[@id="0"]/td[13]/div/button[2]') == ' 人工处理':
            self.PUBLIC.Click(By.XPATH, '//*[@id="0"]/td[13]/div/button[2]')
            self.PUBLIC.Switch_Window()
            self.PUBLIC.Frame_switch_window((By.XPATH, '//*[@id="layui-layer-iframe1"]'), '找不到iframe的element元素')
            self.PUBLIC.Click(By.XPATH, '//*[@id="panel"]/form/div[3]/div/select')
            self.PUBLIC.Click(By.XPATH, '//*[@id="panel"]/form/div[3]/div/select/option[3]')
            if self.PUBLIC.Find_element_Text(By.XPATH, '//*[@id="panel"]/form/div[8]/label') == '充电量':
                self.PUBLIC.Click(By.XPATH, '//*[@id="actions"]/button')
            elif self.PUBLIC.Find_element_Text(By.XPATH, '//*[@id="panel"]/form/div[8]/label') == '充电电量':
                self.PUBLIC.Send_key((By.XPATH, '/html/body/div[2]/div/form/div[13]/div/div/input'), '20')
                self.PUBLIC.Send_key((By.XPATH, '//*[@id="panel"]/form/div[14]/div/div/input'), '20')
                self.PUBLIC.Click(By.XPATH, '//*[@id="actions"]/button')

    def After_Sales_Charge_Service(self):
        pass

    def tearDown(self) -> None:
        time.sleep(10)
