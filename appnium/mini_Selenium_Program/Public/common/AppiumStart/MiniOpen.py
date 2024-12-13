import logging
import sys
import time
from appnium.mini_Selenium_Program.Public.Utils.SeleniumUtils import Driver, Waiting
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common import NoSuchElementException
from appnium.mini_Selenium_Program.Public.Utils.SeleniumUtils import utils_Option
from appnium.mini_Selenium_Program.Public.common.Logger.Logger import Logger
from appnium.mini_Selenium_Program.Public.common.page.WeChatLoginIndex import WeChatLoginIndex


class openMini(object):
    def __init__(self, appnium):
        self.appnium = appnium
        self.driver = Driver(self.appnium)
        self.wait = Waiting(self.appnium)
        self.utils = utils_Option
        self.logging = Logger(stream=sys.stdout)

    def test_startMiniApp(self, **kwargs):
        WeChatLoginIndex(self.appnium).LoginIndex()
        el_login = self.appnium.find_elements(AppiumBy.XPATH, '//*[@text="密码"]')
        try:
            if el_login is not None and len(el_login) != 0:
                while True:
                    # 1是传参，2是点击事件，3是获取text元素
                    self.wait.WaitElement(1, (AppiumBy.XPATH, '//*[@text="请填写微信号/QQ号/邮箱"]'), "无法找到该元素", 18027190670)
                    self.wait.WaitElement(1, (AppiumBy.XPATH, '//*[@text="请填写密码"]'), "无法找到该元素", 'wj123456')
                    # self.driver.Appnium_SendKey((AppiumBy.XPATH, '//*[@text="请填写密码"]'), "无法找到该元素", 'wj123456')
                    self.wait.WaitElement(2, (AppiumBy.XPATH, '//*[@text="同意并登录"]'), "元素找不到")
                    el_login_msg = self.appnium.find_elements(AppiumBy.XPATH, '//*[@text="确定"]')
                    # 判断页面是否存在确认按钮
                    if el_login_msg is not None and len(el_login_msg) != 0:
                        self.wait.WaitElement(2, (AppiumBy.XPATH, '//*[@text="同意并登录"]'), "元素找不到")
                        self.driver.Appnium_Clear(AppiumBy.XPATH, '//*[@class="android.widget.EditText"]')
                    else:
                        break
                self.logging.info('----------------------------登录成功！-------------------------------')
                self.driver.Appnium_swipe(500)
                self.driver.Appnium_click(AppiumBy.XPATH, '//*[@text="驾驶乐"]')
            else:
                self.logging.info('----------------------------已经登录了！-------------------------------')
                toast_lists = self.driver.Find_elements(AppiumBy.XPATH, '//*[@class="android.widget.Button"]')
                if toast_lists is not None and len(toast_lists) != 0:
                    for toast_text in toast_lists:
                        if toast_text != "会话已过期请重新登录":
                            self.driver.Appnium_swipe(500)
                            self.driver.Appnium_click(AppiumBy.XPATH, '//*[@text="驾驶乐"]')
                        else:
                            self.wait.WaitElement(2, (AppiumBy.XPATH, '//*[@text="确定"]'))
                else:
                    time.sleep(2)
                    self.driver.Appnium_swipe(500)
                    self.wait.WaitElement(2, (AppiumBy.XPATH, '//*[@text="驾驶乐"]'), "小程序不存在该页面")
        except NoSuchElementException as e:
            self.logging.info("---------------------NoSuchElement-------------------------------")
            raise print(e)
