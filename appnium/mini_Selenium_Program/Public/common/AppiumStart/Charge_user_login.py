import logging
import sys

from appnium.mini_Selenium_Program.Public.common.AppiumStart.MiniOpen import openMini
from appnium.mini_Selenium_Program.Public.Utils.SeleniumUtils import Driver, Waiting
from appium.webdriver.common.appiumby import AppiumBy



class Charge_user_login(object):
    def __init__(self, appnium):
        self.appnium = appnium
        self.driver = Driver(self.appnium)
        self.wait = Waiting(self.appnium)
        openMini(self.appnium).test_startMiniApp()

    def test_chargeUserLogin(self):
        # 遍历上下文，找到小程序上下文
        logging.info("访问小程序中。。。")
        self.appnium.wait_activity("WEBVIEW_com.tencent.mm:appbrand0", 50, 1)
        contexts_list = self.appnium.contexts
        size = self.appnium.get_window_size()
        for context in contexts_list:
            if "WEBVIEW_com.tencent.mm:appbrand0" == context:
                # 切换到小程序上下文
                logging.info("即将切换到webview名为" + context + "的界面！")
                self.appnium.switch_to.context(contexts_list[1])
                logging.info("已经切换到小程序界面")
                if "您当前已到达：" in self.appnium.page_source:
                    self.driver.Appnium_click(AppiumBy.XPATH,
                                              '//*[contains(@class,"right-span popup--right-span")]')
                    self.LoginCheck(contexts_list, size)
                    return "____this part done_____"
                else:
                    self.LoginCheck(contexts_list, size)
                    return "____this part done_____"
            else:
                if context == contexts_list[len(contexts_list) - 1]:
                    raise Exception("无法切换到小程序界面")

    # 验证是否用户登录(旧版授权登录操作)
    def LoginCheck(self, contexts_list, size):
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
            # 模拟用户手动点击操作
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
        logging.info("用户已登录！")
        print("____this part done_____")
