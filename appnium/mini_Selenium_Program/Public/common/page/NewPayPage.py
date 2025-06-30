from selenium.webdriver import ActionChains

from appnium.mini_Selenium_Program.Public.Utils.SeleniumUtils import Driver, Waiting


class NewPayPage(object):
    def __init__(self, **kwargs):
        self.appnium = kwargs.get("appium")
        self.driver = Driver(self.appnium)
        self.wait = Waiting(self.appnium)
        self.action = ActionChains(self.appnium)

    # 该页面的汇总流程方法
    def main_(self):
        pass

    # 选择安心充
    def InsureSelect(self):
        pass

    def selectPreferentialPlans(self):
        pass

    def parkingLotMode(self):
        pass

    def Coupon(self):
        pass

    # 释放页面执行完成的资源
    def __del__(self):
        self.appnium.quit()

