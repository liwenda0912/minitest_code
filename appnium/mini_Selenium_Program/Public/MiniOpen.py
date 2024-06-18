import os

import time
from http.client import RemoteDisconnected

from appnium.mini_Selenium_Program.Public.Utils.uilts import Driver, Waiting, Init
from appium.webdriver.common.appiumby import AppiumBy
from appnium.mini_Selenium_Program.Public.Utils.Simulator_Start import ConnectSimulator
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import NoSuchElementException
from selenium.common.exceptions import WebDriverException
from appnium.mini_Selenium_Program.Public.Utils.uilts import utils_Option


class openMini(object):
    def __init__(self, appnium):
        ConnectSimulator()
        self.appnium = appnium
        self.driver = Driver(self.appnium)
        self.wait = Waiting(self.appnium)
        self.utils = utils_Option

    def test_startMiniApp(self):
        time.sleep(5)
        el_login = self.appnium.find_elements(AppiumBy.XPATH, '//*[@text="请填写微信密码"]')
        try:
            if el_login is not None and len(el_login) != 0:
                self.wait.Appnium_wait(5)
                wx_username = self.driver.Appnium_Text(AppiumBy.XPATH,
                                                       '//*[@resource-id="com.tencent.mm:id/iod"]')
                wx_username_new = self.utils.spilt(wx_username, " ")
                while True:
                    # 1是点击事件，2是点击事件，3是获取text元素
                    self.wait.WaitElement(2, (AppiumBy.XPATH, '//*[@text="请填写微信密码"]'), "无法找到该元素")
                    wx_passwd = str(input("请" + wx_username_new + "的输入wx密码："))
                    self.driver.Appnium_SendKey((AppiumBy.XPATH, '//*[@text="请填写微信密码"]'), "无法找到该元素", "da123456")
                    time.sleep(2)
                    self.driver.Appnium_click(AppiumBy.XPATH, '//*[@text="登录"]')
                    time.sleep(5)
                    el_login_msg = self.appnium.find_elements(AppiumBy.XPATH, '//*[@text="确定"]')
                    if el_login_msg is not None and len(el_login_msg) != 0:
                        self.wait.WaitElement(2, (AppiumBy.XPATH, '//*[@text="确定"]'), "元素找不到")
                        self.driver.Appnium_Clear(AppiumBy.XPATH, '//*[@class="android.widget.EditText"]')

                    #     login_error_msg = self.driver.Appnium_Text(AppiumBy.XPATH,
                    #                                                '//*[@class="android.widget.TextView" and @resource-id="com.tencent.mm:id/jlg"]')
                    #     print(login_error_msg)
                    #     if login_error_msg == "帐号或密码错误，请重新填写":
                    #         self.driver.Appnium_click(AppiumBy.XPATH,
                    #                                   '//*[@class="android.widget.Button" and @text="确认"]')
                    #         self.driver.Appnium_Clear(AppiumBy.XPATH,
                    #                                   '//*[@class="android.widget.EditText" and @resource-id="com.tencent.mm:id/cd7"]')
                    else:
                        break
                time.sleep(5)
                print("----------------------------登录成功！-------------------------------")
                self.driver.Appnium_swipe(500)
                self.driver.Appnium_click(AppiumBy.XPATH, '//*[@text="驾驶乐"]')
            else:
                print("-----------------------------已经登录了！---------------------------------")
                toast_lists = self.driver.Find_elements(AppiumBy.XPATH, '//*[@class="android.widget.Button"]')
                if toast_lists is not None and len(toast_lists) != 0:
                    for toast_text in toast_lists:
                        if toast_text != "会话已过期请重新登录":
                            self.driver.Appnium_swipe(500)
                            self.driver.Appnium_click(AppiumBy.XPATH, '//*[@text="驾驶乐"]')
                        else:
                            self.wait.WaitElement(2, (AppiumBy.XPATH, '//*[@text="确定"]'))
                else:
                    self.driver.Appnium_swipe(500)
                    self.wait.WaitElement(2, (AppiumBy.XPATH, '//*[@text="驾驶乐"]'), "小程序不存在该页面")
        except NoSuchElementException:
            time.sleep(5)
            print("---------------------NoSuchElement-------------------------------")
        # except EOFError:
        #     print(EOFError)
        # except RemoteDisconnected:
        #     self.test_startMiniApp()
        # except ConnectionAbortedError:
        #     print("出现了'ConnectionAbortedError: [WinError 10053] 你的主机中的软件中止了一个已建立的连接。")
        #     self.test_startMiniApp()
        # except WebDriverException:
        #     ConnectSimulator()
        #     print("出现了' Could not find a connected Android device.")
        #     self.test_startMiniApp()
        #     print("重新启动完成")
