# <---定点进入对应充电站--->
import pyautogui
import os
import time
from ddt import ddt, data
import unittest

from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from appnium.mini_Selenium_Program.Public.MiniOpen import openMini
from appnium.mini_Selenium_Program.Public.Utils.uilts import Driver, Waiting, Init
from appium.webdriver.common.appiumby import AppiumBy
from appnium.mini_Selenium_Program.Public.MiniOpen import openMini
from appnium.mini_Selenium_Program.test_case.Charge_user_login import Charge_user_login
from appnium.mini_Selenium_Program.Public.Utils.key_code import ke_code


class chargeStart(unittest.TestCase):
    def setUp(self) -> None:
        self.appnium = Init().Appnium
        self.driver = Driver(self.appnium)
        self.wait = Waiting(self.appnium)
        self.action = ActionChains(self.appnium)
        self.text = Charge_user_login(self.appnium).test_chargeUserLogin()
        self.contexts_list = self.appnium.contexts

    def test_chargeStation(self):
        searchStation(self.appnium, self.wait, self.action, self.contexts_list, self.driver)

    def tearDown(self) -> None:
        self.appnium.quit()


def searchStation(*loc):
    appnium = loc[0]
    wait = loc[1]
    action = loc[2]
    contexts_list = loc[3]
    driver = loc[4]
    try:
        login_text = appnium.find_elements(AppiumBy.XPATH,
                                           '//*[@class="_span benefits--_span data-v-f7b9a482 benefits--data-v-f7b9a482 login-css benefits--login-css"]')
        if login_text is not None and len(login_text) != 0:
            Charge_user_login(appnium).test_chargeUserLogin()
        else:
            print("运行到这里")

            wait.WaitElement(2, (AppiumBy.XPATH,
                                 '//*[contains(@class,"input-placeholder list--input-placeholder")]'),
                             "该元素不存在页面中")
            win = appnium.window_handles
            appnium.switch_to.window(win[0])
            time.sleep(2)
            el = appnium.find_element(AppiumBy.XPATH, '//*[@class="uni-input uni-input"]')
            os.system("adb shell ime list -s")
            os.system("adb shell settings put secure default_input_method com.sohu.inputmethod.sogou/.SogouIME")
            action.click(el).perform()
            os.system("adb shell input text  2.0")
            # 切回app界面点击回车键
            appnium.switch_to.context(contexts_list[0])
            size = appnium.get_window_size()
            driver.actionPress([1000, 1732], [1062, 1920], window_size=[size["width"], size["height"]])
            appnium.switch_to.context(contexts_list[1])
            # 回到小程序页面点击搜索的站点
            driver.Appnium_Switch_Window(1)

            wait.WaitElement(2, (
                AppiumBy.XPATH,
                '//*[contains(@class,"station-name four--station-name")]'),
                             "元素不存在该页面67")
            time.sleep(5)
            driver.Appnium_Switch_Window(0)
            time.sleep(4)
            for i in appnium.find_elements(
                    AppiumBy.XPATH,
                    '//*[contains(@class,"device-info-detail device-info-detail")]'):
                print(i.text)
                pileNum = "240020210730200101"
                if pileNum in i.text:
                    start_location = driver.Find_element(AppiumBy.XPATH, '//*[contains(@class,"station-title station-title")]')
                    driver.Appnium_Scroll(start_location, i)
                    i.click()
                    time.sleep(10)

            print(appnium.page_source)
            # for i in :
            #     print(i.text+"5555")

    except EOFError:
        pass
