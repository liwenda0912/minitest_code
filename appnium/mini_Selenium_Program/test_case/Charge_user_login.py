import time
import unittest
from http.client import RemoteDisconnected

from selenium.common.exceptions import WebDriverException
from appnium.mini_Selenium_Program.Public.MiniOpen import openMini
from appnium.mini_Selenium_Program.Public.Utils.Simulator_Start import AppiumApp_start, Simulator_Start, cmdProcess, \
    ConnectSimulator
from appnium.mini_Selenium_Program.Public.Utils.uilts import Driver, Waiting, Init
from appium.webdriver.common.appiumby import AppiumBy


class Charge_user_login(object):
    # # def setUp(self) -> None:
    #     Simulator_Start()
    #     AppiumApp_start()
    #     self.appnium = Init().Appnium
    #     self.driver = Driver(self.appnium)
    #     self.wait = Waiting(self.appnium)
    #     print("name")
    #     openMini(self.appnium).test_startMiniApp()

    def __init__(self, appnium):
        Simulator_Start()
        AppiumApp_start()
        self.appnium = appnium
        self.driver = Driver(self.appnium)
        self.wait = Waiting(self.appnium)
        openMini(self.appnium).test_startMiniApp()

        # self.driver = Driver(self.appnium)
        # self.wait = Waiting(self.appnium)

    def test_chargeUserLogin(self):
        try:
            if cmdProcess(r'K\r\nAppium.exe') == '服务已经启动' and cmdProcess(r'K\r\nMuMuPlayer.exe') == '服务已经启动':
                # 遍历上下文，找到小程序上下文
                print("执行到这里了")
                self.wait.Appnium_wait(2)
                print(self.appnium.contexts)
                self.appnium.wait_activity("WEBVIEW_com.tencent.mm:appbrand0", 50, 1)
                contexts_list = self.appnium.contexts
                size = self.appnium.get_window_size()
                for context in contexts_list:
                    if "WEBVIEW_com.tencent.mm:appbrand0" == context:
                        # 切换到小程序上下文
                        print("即将切换到webview名为" + context + "的界面！")
                        self.appnium.switch_to.context(contexts_list[1])
                        print("已经切换到小程序界面")
                        if "您当前已到达：" in self.appnium.page_source:
                            self.driver.Appnium_click(AppiumBy.XPATH,
                                                      '//*[contains(@class,"right-span popup--right-span _span popup--_span")]')
                            self.search(contexts_list, size)
                            return "____this part done_____"
                        else:
                            self.search(contexts_list, size)
                            return "____this part done_____"
            else:
                print("--------------------小程序所需服务未启动,无法驱动小程序！----------------------")
        except EOFError:
            pass
        except RemoteDisconnected:
            print("出现了'Remote end closed connection without response'情况,正在重新连接remote")
            Charge_user_login(self.appnium).test_chargeUserLogin()
            print("重新启动完成")
        except ConnectionAbortedError:
            print("出现了'ConnectionAbortedError: [WinError 10053] 你的主机中的软件中止了一个已建立的连接。")
            Charge_user_login(self.appnium).test_chargeUserLogin()
            print("重新启动完成")
        except WebDriverException:
            ConnectSimulator()
            print("出现了' Could not find a connected Android device.")
            Charge_user_login(self.appnium).test_chargeUserLogin()
            print("重新启动完成")
    #
    # def tearDown(self) -> None:
    #     self.appnium.quit()

    def search(self, contexts_list, size):
        # 存在两个界面，一个是小程序界面，一个是开发者调试器界面
        # 切换页面为1
        self.wait.Appnium_wait(2)
        # 在首页查找登录字段（定点查找）
        login_text = self.appnium.find_elements(AppiumBy.XPATH,
                                                '//*[@class="_span benefits--_span data-v-f7b9a482 benefits--data-v-f7b9a482 login-css benefits--login-css"]')
        if login_text is not None and len(login_text) != 0:
            self.wait.WaitElement(2, (AppiumBy.XPATH,
                                      '//*[@class="_span benefits--_span data-v-f7b9a482 benefits--data-v-f7b9a482 login-css benefits--login-css"]'),
                                  "元素找不到")
            # 返回app进行屏幕点击确定授权登录二次确定
            self.appnium.switch_to.context(contexts_list[0])
            self.driver.actionPress([541, 1059], [1020, 1227],
                                    window_size=[size["width"], size["height"]])
            # 返回小程序界面进行页面操作
            self.appnium.switch_to.context(contexts_list[1])
            # 切换页面为1
            self.driver.Appnium_Switch_Window(1)
            # 点击授权手机登录
            self.wait.WaitElement(2, (AppiumBy.XPATH,
                                      '//*[contains(@class,"default default round round auth auth")]'),
                                  "元素不存在！")
            # 切换回登录后的首页界面
            self.driver.Appnium_Switch_Window(1)

        # else:
        #     self.appnium.switch_to.context(contexts_list[0])
        #     self.driver.actionPress([864, 1815], [1080, 1899], window_size=[size["width"], size["height"]])
        #     self.appnium.switch_to.context(contexts_list[1])
        #     self.driver.Appnium_Switch_Window(win[1])
        #     break
        print("____this part done_____")

