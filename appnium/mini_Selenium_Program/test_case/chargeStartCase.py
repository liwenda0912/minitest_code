"""
   # <---定点进入对应充电站--->
"""
import logging
import sys
import time
import unittest
from selenium.webdriver import ActionChains
from appnium.mini_Selenium_Program.Public.Utils.SeleniumUtils import Driver, Waiting

from appnium.mini_Selenium_Program.Public.common.AppiumStart.AppiumStart import AppiumStart
from appnium.mini_Selenium_Program.Public.common.AppiumStart.Charge_user_login import Charge_user_login
from appnium.mini_Selenium_Program.Public.common.Logger.Logger import Logger
from appnium.mini_Selenium_Program.Public.common.page.ChargeStationPage import chargeStation
from appnium.mini_Selenium_Program.Public.common.page.ChargeStartPage import ChargeStartPage
from appnium.mini_Selenium_Program.Public.common.page.Search_StationPage import Search_Station


class chargeStartCase(unittest.TestCase):
    def setUp(self) -> None:
        self.logging = Logger(stream=sys.stdout)
        self.logging.info("-------------自动化测试开始！---------------")
        self.appnium = AppiumStart().Appnium
        self.driver = Driver(self.appnium)
        self.wait = Waiting(self.appnium)
        self.action = ActionChains(self.appnium)
        self.text = Charge_user_login(self.appnium).test_chargeUserLogin()
        self.ChargeStartPage = ChargeStartPage(self.appnium)

    def test_chargeStation(self):
        # 能源车充电站
        if self.text == "____this part done_____":
            self.contexts_list = self.appnium.contexts
            self.chargeStation = chargeStation(appium=self.appnium, contexts_list=self.contexts_list)
            self.Search_Station = Search_Station(appium=self.appnium, contexts_list=self.contexts_list)
            self.Search_Station.searchStation(StationName="蔚景云协议站")
            # 判断站点类型
            self.chargeStation.stationType(pileNum="240020210730200102")
            # 访问启动界面
            self.ChargeStartPage.startChargeStep(coupon_option="", PreferentialPlans=1, SelectCarNum="津D8sd55", coupon_name="",
                                                 chose_discount_name='超级会员', choice_pay="集团储值卡", choice_pay_count=1,
                                                 carName="power", companyName="power", StationName="蔚景云协议站")
            time.sleep(20)

    def tearDown(self) -> None:
        self.appnium.quit()
