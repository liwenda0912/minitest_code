import time

from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver import ActionChains

from appnium.mini_Selenium_Program.Public.Utils.SeleniumUtils import Driver, Waiting
from appnium.mini_Selenium_Program.Public.Utils.distUtils import dict_


class AddCarPage(object):
    def __init__(self, appium):
        self.appnium = appium
        self.driver = Driver(appium)
        self.wait = Waiting(self.appnium)
        self.action = ActionChains(self.appnium)

    def addCarMessage(self, **kwargs):
        # 添加车辆操作
        self.driver.Switch_Win(text_="车牌号码")
        el = self.driver.Find_element(AppiumBy.XPATH, "//*[starts-with(@class, 'car plate--car')]")
        self.action.click(el).perform()
        self.carKeyBoardSelect(carName=kwargs.get("carNum"))
        # 关闭键盘

        self.action.click(el).perform()
        # 点击默认设置
        self.driver.Find_element(AppiumBy.XPATH, '//*[starts-with(@class, "switch switch")]').click()
        # 点击保存
        self.action.click(
            self.driver.Find_element(AppiumBy.XPATH, "//*[starts-with(@class, 'btn btn')]")).perform()

    def carKeyBoardSelect(self, carName):
        keyboard_list = []
        for k, v in dict_(carName).items():
            if k == 0:
                keyboard_list = self.driver.Find_elements(AppiumBy.XPATH,
                                                          '//*[starts-with(@class, "u-keyboard-grids-btn")]')
            elif k == 1:
                keyboard_list = self.driver.Find_elements(AppiumBy.XPATH,
                                                          '//*[starts-with(@class, "u-keyboard-grids-btn")]')
            # 判断获取的车辆号码是否超过8位
            elif k == 8:
                break
            else:
                keyboard_list = keyboard_list
            for i in keyboard_list:
                # lower忽略大小写
                if i.text.lower() == v.lower():
                    time.sleep(1)
                    self.action.click(i).perform()
                    break
                else:
                    continue
