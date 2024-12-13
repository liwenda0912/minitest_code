import logging
import os
import sys
import time
from selenium.webdriver import ActionChains
from appnium.mini_Selenium_Program.Public.Utils.SeleniumUtils import Driver, Waiting
from appium.webdriver.common.appiumby import AppiumBy
from appnium.mini_Selenium_Program.Public.Utils.keyboardUtils import keyboard, enterKey, getHtml
from appnium.mini_Selenium_Program.Public.common.AppiumStart.Charge_user_login import Charge_user_login
from appnium.mini_Selenium_Program.Public.common.Logger.Logger import Logger


class Search_Station(object):
    def __init__(self, **kwargs):
        self.appnium = kwargs.get("appium")
        self.driver = Driver(self.appnium)
        self.wait = Waiting(self.appnium)
        self.action = ActionChains(self.appnium)
        self.contexts_list = kwargs.get("contexts_list")

    def searchStation(self, **kwargs):
        login_text = self.driver.Find_elements(AppiumBy.XPATH,
                                               '//*[@class="_span benefits--_span data-v-f7b9a482 benefits--data-v-f7b9a482 login-css benefits--login-css"]')
        if login_text is not None and len(login_text) != 0:
            Charge_user_login(self.appnium).test_chargeUserLogin()
        else:
            Logger(stream=sys.stdout).info("<-----------开始站点搜索-------------->")
            # getHtml(self.appnium)
            self.ActionKeyBoard(searchStationName="蔚景云协议站")

    def ActionKeyBoard(self, **kwargs):
        self.wait.WaitElement(2, (AppiumBy.XPATH,
                                  '//*[starts-with(@class,"search-logo label--search-logo")]'),
                              "该元素不存在页面中")
        win = self.appnium.window_handles
        self.appnium.switch_to.window(win[0])
        self.wait.Appnium_wait(2)
        el = self.driver.Find_element(AppiumBy.XPATH, '//*[@class="uni-input uni-input"]')
        # # 唤起模拟器的手机键盘
        # os.system("adb shell ime list -s")
        time.sleep(2)
        os.system("adb -s 127.0.0.1:7555 shell settings put secure default_input_method com.android.adbkeyboard/.AdbIME")
        # # 点击
        self.action.click(el).perform()
        time.sleep(2)
        searchStationName = kwargs.get("searchStationName")
        os.system("adb -s 127.0.0.1:7555 shell am broadcast -a ADB_INPUT_TEXT  --es msg " + searchStationName)
        # 切回app界面点击回车键
        self.wait.Appnium_wait(5)
        keyboard(self.action, el)
        self.appnium.switch_to.context(self.contexts_list[0])
        # 模拟点击屏幕
        enterKey(appnium=self.appnium, driver=self.driver, wait=self.wait)
        self.appnium.switch_to.context(self.contexts_list[1])
        # 回到小程序页面点击搜索的站点
        self.driver.Appnium_Switch_Window(1)
        # 获取搜索后的所有站点
        dates_message = self.wait.WaitElement(7, (AppiumBy.XPATH,
                                                  '//*[contains(@class,"station-card four--station-card")]'),
                                              "搜索列表不存在")
        # print(self.wait.WaitElement(5, (AppiumBy.XPATH,
        #                                 '//*[contains(@class,"input-placeholder station-list--input-placeholder")]'),
        #                             "该元素不存在页面中"))
        # if self.wait.WaitElement(5, (AppiumBy.XPATH,
        #                              '//*[contains(@class,"input-placeholder station-list--input-placeholder")]'),
        #                          "该元素不存在页面中") == searchStationName:
        if len(dates_message) != 0:
            for i in dates_message:
                if searchStationName in i.text:
                    i.click()
                    Logger(stream=sys.stdout).info("进入搜索站点详情页中")
                    break
                else:
                    raise Exception("列表没有找到要搜索的站点信息！")
        else:
            raise Exception("按照站点名称搜索不到对应的站点！，键盘输入过快导致输入款无法输入并进行检索。")
        # else:
        #     self.ActionKeyBoard(searchStationName=searchStationName)
