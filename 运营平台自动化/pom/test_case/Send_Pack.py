import unittest
from selenium.webdriver.common.by import By
from 运营平台自动化.pom.public.public import Public


class Send_Pack(unittest.TestCase):
    def setUp(self) -> None:
        self.url = ''

    def test_Send_Card(self, driver):
        self.driver = driver
        self.PUBLIC = Public(self.driver, self.url)
        self.PUBLIC.WaitElement((By.XPATH, '//*[@id="0"]/td[11]/div/button[4]'), '找不到发放按钮')
        self.PUBLIC.Switch_Window()
        self.PUBLIC.WaitElement((By.XPATH, '//*[@id="layui-layer3"]/div[1]'), '无法找到发放优惠券弹窗')
        self.PUBLIC.Frame_switch_window((By.XPATH, '//*[@id="layui-layer-iframe3"]'),
                                        '找不到iframe的id为layui-layer-iframe3的元素')
        # 填写发放用户信息
        self.PUBLIC.ClearKey(By.XPATH, '//*[@id="assignCard"]/div[1]/div[3]/div/div/div/input')
        self.PUBLIC.Send_key((By.XPATH, '//*[@id="assignCard"]/div[1]/div[3]/div/div/div/input'), '10')
        self.PUBLIC.ClearKey(By.XPATH, '//*[@id="assignCard"]/div[1]/div[4]/div/div[1]/div/input')
        self.PUBLIC.Send_key((By.XPATH, '//*[@id="assignCard"]/div[1]/div[4]/div/div[1]/div/input'), '10')
        self.PUBLIC.Send_key((By.XPATH, '//*[@id="assignCard"]/div[1]/div[7]/div/div/input'), '15767112316')
        self.PUBLIC.Click(By.XPATH, '//*[@id="assignCard"]/div[1]/div[7]/div/span/button')
        self.PUBLIC.WaitElement(
            (By.XPATH, '//*[@id="assignCard"]/div[1]/div[8]/div/div/div[3]/table/tbody/tr/td[1]/div/label/span/span'),
            '该元素不存在')
        self.PUBLIC.Click(By.XPATH, '//*[@id="actions"]/button')
        # 二次确认发放
        self.PUBLIC.WaitElement((By.XPATH, '//*[@id="layui-layer3"]/div[3]/a[1]'), '没有二次确认弹窗')
        # Assert().assertTest_Send(self.driver)

    def tearDown(self) -> None:
        pass
