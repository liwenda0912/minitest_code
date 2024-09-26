import os

from selenium.webdriver import ActionChains

from appnium.mini_Selenium_Program.Public.Utils.uilts import Driver, Waiting, Init
from appium.webdriver.common.appiumby import AppiumBy
from appnium.mini_Selenium_Program.test_case.Charge_user_login import Charge_user_login


class Search_Station(object):
    def __init__(self, appium,ss):
        self.appnium = appium
        self.driver = Driver(appium)
        self.wait = Waiting(self.appnium)
        self.action = ActionChains(self.appnium)
        self.contexts_list = ss

    def searchStation(self):
        # try:
        # wait.Appnium_wait_ac("WEBVIEW_com.tencent.mm:appbrand0", 50, 1)
        login_text = self.driver.Find_elements(AppiumBy.XPATH,
                                               '//*[@class="_span benefits--_span data-v-f7b9a482 benefits--data-v-f7b9a482 login-css benefits--login-css"]')
        if login_text is not None and len(login_text) != 0:
            Charge_user_login(self.appnium).test_chargeUserLogin()
        else:
            print("运行到这里")
            self.wait.WaitElement(2, (AppiumBy.XPATH,
                                      '//*[contains(@class,"input-placeholder list--input-placeholder")]'), "该元素不存在页面中")
            win = self.appnium.window_handles
            self.appnium.switch_to.window(win[0])
            self.wait.Appnium_wait(5)
            el = self.driver.Find_element(AppiumBy.XPATH, '//*[@class="uni-input uni-input"]')
            # 唤起模拟器的手机键盘
            os.system("adb shell ime list -s")
            os.system("adb shell settings put secure default_input_method com.sohu.inputmethod.sogou/.SogouIME")
            # 回车点击
            self.action.click(el).perform()
            os.system("adb shell input text  2.0")
            # 切回app界面点击回车键
            self.appnium.switch_to.context(self.contexts_list[0])
            size = self.appnium.get_window_size()
            self.wait.Appnium_wait(3)
            self.driver.actionPress([1000, 1732], [1062, 1920], window_size=[size["width"], size["height"]])
            self.appnium.switch_to.context(self.contexts_list[1])
            # 回到小程序页面点击搜索的站点
            self.driver.Appnium_Switch_Window(1)
            dates_message = self.appnium.find_elements(AppiumBy.XPATH,
                                                       '//*[contains(@class,"station-card four--station-card")]')
            for i in dates_message:
                if "集团充" in i.text:
                    i.click()
            self.wait.Appnium_wait(2)
            self.driver.Appnium_Switch_Window(0)
