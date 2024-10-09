from appium.webdriver.common.appiumby import AppiumBy
from appnium.mini_Selenium_Program.Public.Utils.SeleniumUtils import Driver, Waiting


class WeChatLoginIndex(object):
    def __init__(self, appnium):
        self.appnium = appnium
        self.driver = Driver(self.appnium)
        self.wait = Waiting(self.appnium)

    def LoginIndex(self):
        el_login = self.appnium.find_elements(AppiumBy.XPATH, '//*[@text="登录"]')
        if el_login is not None and len(el_login) != 0:
            self.wait.WaitElement(2, (AppiumBy.XPATH, '//*[@text="登录"]'), "无法找到该元素")
            el_login_ = self.appnium.find_elements(AppiumBy.XPATH, '//*[@text="国家/地区"]')
            if el_login_ is not None and len(el_login) != 0:
                self.wait.WaitElement(2, (AppiumBy.XPATH, '//*[@text="用微信号/QQ号/邮箱登录"]'), "无法找到该元素")




