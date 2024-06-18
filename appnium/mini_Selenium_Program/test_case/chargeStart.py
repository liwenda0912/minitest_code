# <---定点进入对应充电站--->
from http.client import RemoteDisconnected
import os
import time
import urllib3
from ddt import ddt, data
import unittest
from selenium.common.exceptions import WebDriverException
from selenium.webdriver import ActionChains
from appnium.mini_Selenium_Program.Public.Utils.Simulator_Start import ConnectSimulator
from appnium.mini_Selenium_Program.Public.Utils.uilts import Driver, Waiting, Init
from appium.webdriver.common.appiumby import AppiumBy
from appnium.mini_Selenium_Program.test_case.Charge_user_login import Charge_user_login


class chargeStart(unittest.TestCase):
    def setUp(self) -> None:
        try:
            self.appnium = Init().Appnium
            self.driver = Driver(self.appnium)
            self.wait = Waiting(self.appnium)
            self.action = ActionChains(self.appnium)
            self.text = Charge_user_login(self.appnium).test_chargeUserLogin()

        except WebDriverException as e:
            ConnectSimulator()
            exceptHandle(self.appnium, e)
        except urllib3.exceptions.ProtocolError as e:
            exceptHandle(self.appnium, e)

    def test_chargeStation(self):
        global equal_text
        try:
            if self.text == "____this part done_____":
                self.contexts_list = self.appnium.contexts
                searchStation(self.appnium, self.wait, self.action, self.contexts_list, self.driver)
                time.sleep(5)
                for i in self.appnium.find_elements(
                        AppiumBy.XPATH,
                        '//*[contains(@class,"device-info-detail device-info-detail")]'):
                    pileNum = "240020210730200101"
                    print(i.text)
                    if pileNum in i.text:
                        start_location = self.appnium.find_element(AppiumBy.XPATH,
                                                                   '//*[contains(@class,"row-flex row-flex flex-column flex-column flex-align-center flex-align-center")]')
                        self.driver.Appnium_Scroll(start_location, i, 5000)
                        time.sleep(5)
                        i.find_element(AppiumBy.XPATH,
                                       '//*[contains(@class,"row-flex row-flex flex-column flex-column flex-align-center flex-align-center")]').click()
                        time.sleep(10)
                        break
                    # 切换到枪详情界面
                print(self.appnium.current_window_handle, self.appnium.window_handles)
                self.driver.Appnium_Switch_Window(1)
                time.sleep(5)
                print(self.appnium.page_source)
                chose_pay = 0
                if chose_pay == "1":
                    # 选择启动充电方式
                    self.driver.Appnium_click()
                elif chose_pay == "2":
                    self.driver.Appnium_click()
                elif chose_pay == "3":
                    self.driver.Appnium_click()
                elif chose_pay == "4":
                    self.driver.Appnium_click()
                elif chose_pay == "5":
                    self.driver.Appnium_click()
                # # 选择优惠卡券
                chose_coupon = 0
                # 进入优惠券界面
                self.driver.Appnium_click()
                if chose_coupon == "1":
                    # 选择优惠券
                    self.driver.Appnium_click()
                # 选择抵扣卡
                elif chose_coupon == "2":
                    self.driver.Appnium_click()
                # 选择能量抵扣卡
                elif chose_coupon == "3":
                    self.driver.Appnium_click()
                # 不使用优惠券
                elif chose_coupon == "4":
                    # 进入优惠券界面
                    self.driver.Appnium_click()
                    button_text = self.appnium.find_elements()
                    for button in button_text:
                        if button.text == "取消":
                            self.driver.Appnium_click()
                        # 优惠券不存在选中的优惠券
                        else:
                            # 进入抵扣卡界面
                            self.driver.Appnium_click()
                            button_text = self.appnium.find_elements()
                            if button_text == "取消":
                                self.driver.Appnium_click()
                            # 抵扣卡界面不存在被选中的抵扣卡
                            else:
                                # 进入能量抵扣卡界面
                                self.driver.Appnium_click()
                                button_text = self.appnium.find_elements()
                                if button_text == "取消":
                                    self.driver.Appnium_click()
                # 选择优惠方案
                chose_discount = 0
                if chose_discount == "1":
                    # 进入优惠方案弹窗
                    self.driver.Appnium_click()
                    # 所有获取优惠方案
                    chose_discount_text = self.appnium.find_elements()
                    for discount_text in chose_discount_text:
                        if "" in discount_text.text:
                            self.driver.Appnium_click()
                            # 点击确认选择优惠
                            self.driver.Appnium_click()
                            equal_text = discount_text.text
                            break
                    # 点击取消退出选择优惠券界面
                    self.driver.Appnium_click()
                    self.assertEqual(equal_text, self.driver.Appnium_Text())

                # # 启动充电
                # self.driver.Appnium_click()
                # # 等待充电时长到达3分钟
                # self.wait.WaitElement()
                # # 点击结束充电
                # self.driver.Appnium_click()
                # # 切换到服务详情界面
                # self.driver.Appnium_Switch_Window()
                # # 对比价格
                # self.assertEqual()
                # self.assertEqual()
                # self.assertEqual()
                print("运行到这里了，枪详情-111")
                print(self.appnium.page_source)
        except EOFError:
            print(EOFError)
        except RemoteDisconnected as e:
            exceptHandle(self.appnium, e)
        except ConnectionAbortedError as e:
            exceptHandle(self.appnium, e)
        except WebDriverException as e:
            ConnectSimulator()
            exceptHandle(self.appnium, e)
        except urllib3.exceptions.ProtocolError as e:
            exceptHandle(self.appnium, e)

    def tearDown(self) -> None:
        self.appnium.quit()


def searchStation(*loc):
    appnium = loc[0]
    wait = loc[1]
    action = loc[2]
    contexts_list = loc[3]
    driver = loc[4]
    # try:
    wait.Appnium_wait_ac("WEBVIEW_com.tencent.mm:appbrand0", 50, 1)
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
        dates_message = appnium.find_elements(AppiumBy.XPATH,
                                              '//*[contains(@class,"station-card four--station-card")]')
        for i in dates_message:
            if "集团充" in i.text:
                print(i.text)
                i.click()
        time.sleep(3)
        driver.Appnium_Switch_Window(0)


def exceptHandle(appnium, e):
    appnium.quit()
    print("出现了:", e)
    suite = unittest.TestSuite()
    load_case = unittest.TestLoader().loadTestsFromTestCase(chargeStart)
    suite.addTest(load_case)
    unittest.TextTestRunner().run(suite)
    print("重新启动完成")
