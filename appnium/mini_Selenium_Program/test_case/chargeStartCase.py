"""
   # <---定点进入对应充电站--->
"""
import unittest
from selenium.webdriver import ActionChains
from appnium.mini_Selenium_Program.Public.Utils.SeleniumUtils import Driver, Waiting
from appium.webdriver.common.appiumby import AppiumBy

from appnium.mini_Selenium_Program.Public.Utils.keyboardUtils import getHtml
from appnium.mini_Selenium_Program.Public.common.AppiumStart.AppiumStart import AppiumStart
from appnium.mini_Selenium_Program.test_case.Charge_user_login import Charge_user_login
from appnium.mini_Selenium_Program.test_case.Coupon_Select import Coupon_Select
from appnium.mini_Selenium_Program.test_case.Search_Station import Search_Station


class chargeStartCase(unittest.TestCase):
    def setUp(self) -> None:
        self.appnium = AppiumStart().Appnium
        self.driver = Driver(self.appnium)
        self.wait = Waiting(self.appnium)
        self.action = ActionChains(self.appnium)
        self.text = Charge_user_login(self.appnium).test_chargeUserLogin()

    def test_chargeStation(self):
        # 能源车充电站
        if self.text == "____this part done_____":
            self.contexts_list = self.appnium.contexts
            Search_Station(self.appnium, self.contexts_list).searchStation()
            self.driver.Switch_Win(
                AppiumBy.XPATH,
                '//*[contains(@class,"device-info-detail device-info-detail")]')
            # 判断是否为电单车站点详情
            if "插座" in self.appnium.page_source:
                pass
            else:
                if "站桩概况" in self.appnium.page_source:
                    self.NewStationDetail()
                else:
                    self.olderStationDetail("old")
            # 切换到枪详情界面
            # self.wait.Appnium_wait(2)
            # for i in self.appnium.window_handles:
            #     self.appnium.switch_to.window(i)
            #     self.wait.Appnium_wait(2)
            #     el = self.driver.Find_elements(AppiumBy.XPATH,
            #                                    '//*[contains(@class,"charge-button charge-button d-flex d-flex align-items-center align-items-center justify-content-center justify-content-center")]')
            #     if el is not None:
            #         break
            # 切换到固定窗口
            self.driver.Switch_Win(AppiumBy.XPATH,
                                   '//*[contains(@class,"charge-button charge-button d-flex d-flex align-items-center align-items-center justify-content-center justify-content-center")]')
            # 关闭更换枪口弹窗
            self.ChoicePileWay()
            # 选中启动充电方式
            chose_pay = "现金钱包"
            pay_options_lists = self.driver.Find_elements(AppiumBy.XPATH,
                                                          '//*[@class="_div tab--_div wuc-tab-item-more tab--wuc-tab-item-more"]')
            for pay_options in pay_options_lists:
                if pay_options.text == chose_pay:
                    pay_options.click()
            # 查看是否存在优惠卡券可选择
            self.wait.WaitElement(2, (AppiumBy.XPATH,
                                      '//*[contains(@class,"agreement-body agreement-body d-flex d-flex align-items-center align-items-center")]'),
                                  "元素找不到")

            if self.driver.Find_elements(AppiumBy.XPATH,
                                         '//*[contains(@class,"agreement-body agreement-body d-flex d-flex align-items-center align-items-center")]') is not None:
                Coupon_Select(self.appnium).coupon_select(chose_coupon="能量抵扣卡", option_=2, chose_discount=0)
            # # 启动充电
            self.wait.Appnium_wait(50)
            if self.driver.Find_element(AppiumBy.XPATH,
                                        '//*[contains(@class,"car-detail main--car-detail")]').text == "添加车辆信息，享限时免费停车权益":
                self.driver.Appnium_click(AppiumBy.XPATH, '//*[contains(@class,"add-button main--add-button")]')

            self.driver.Appnium_click(AppiumBy.XPATH,
                                      '//*[contains(@class,"charge-button charge-button d-flex d-flex align-items-center align-items-center justify-content-center justify-content-center")]')
            print("运行到这里了，枪详情")

    def tearDown(self) -> None:
        self.appnium.quit()

    # @staticmethod
    # def test_exception():
    #     raise Exception

    # def exceptHandle(appnium, e):
    #     appnium.quit()
    #     print("出现了:", e)
    #     suite = unittest.TestSuite()
    #     load_case = unittest.TestLoader().loadTestsFromTestCase(chargeStartCase)
    #     suite.addTest(load_case)
    #     unittest.TextTestRunner().run(suite)
    #     print("重新启动完成")
    def olderStationDetail(self, type_):
        if type_ == "old":
            class_ = "device-info-detail device-info-detail"
        else:
            class_ = "interface-item item--interface-item"
        print(class_)
        current_context = self.appnium.current_window_handle
        print(current_context)
        for i in self.appnium.find_elements(
                AppiumBy.XPATH,
                '//*[contains(@class,"'+class_+'")]'):
            pileNum = "240020210730200102"
            if pileNum in i.text:
                print("准备滑动")
                self.wait.Appnium_wait(2)
                self.action.scroll_to_element(i).perform()
                current_context = self.appnium.current_window_handle
                print(current_context)
                # 切换到app界面
                self.appnium.switch_to.context(self.contexts_list[0])
                self.appnium.swipe(400, 900, 400, 600, 200)
                # 切换到小程序界面（H5，webview界面）
                self.appnium.switch_to.context(self.contexts_list[1])
                self.wait.Appnium_wait(5)
                self.appnium.switch_to.window(current_context)
                print(i.text)
                self.action.move_to_element(i).click().perform()
                break

    def NewStationDetail(self):
        # print(self.driver.Find_elements(AppiumBy.XPATH, '//*[contains(@text, "站桩概况")]'))
        if "站桩详情" in self.appnium.page_source:
            self.driver.Find_element(AppiumBy.XPATH, '//*[contains(@class, "right-detail")]').click()
            self.driver.Switch_Win(AppiumBy.XPATH, '//*[contains(@text, "240020210730200102")]')
        self.olderStationDetail("new")
        # else:
        #     getHtml(self.appnium)
        #     self.wait.WaitElement(2, (AppiumBy.XPATH, '//*[contains(@text, "240020210730200102")]'), "找不这个桩编号")

    def ChoicePileWay(self):
        self.driver.Switch_Win(AppiumBy.XPATH, '//*[@text="更换充电位"]')
        getHtml(self.appnium)
        close_list = self.driver.Find_elements(AppiumBy.XPATH, '//*[contains(@class, "popup-close popup-close")]')
        if len(close_list) != 0:
            for close_ in close_list:
                close_.click()
