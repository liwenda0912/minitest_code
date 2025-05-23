"""
   # <---定点进入对应充电站--->
"""
import atexit
import logging
import sys
import time
import traceback
import unittest
from selenium.webdriver import ActionChains
from appnium.mini_Selenium_Program.Public.Utils.SeleniumUtils import Driver, Waiting
from appnium.mini_Selenium_Program.Public.common.AppiumStart.AppiumStart import AppiumStart
from appnium.mini_Selenium_Program.Public.common.AppiumStart.Charge_user_login import Charge_user_login
from appnium.mini_Selenium_Program.Public.common.page.ChargeStationPage import chargeStation
from appnium.mini_Selenium_Program.Public.common.page.ChargeStartPage import ChargeStartPage
from appnium.mini_Selenium_Program.Public.common.page.MYPage import MyPage
from appnium.mini_Selenium_Program.Public.common.page.Search_StationPage import Search_Station


class chargeStartCase(unittest.TestCase):
    def setUp(self) -> None:
        self.appnium = AppiumStart().Appnium
        self.driver = Driver(self.appnium)
        self.wait = Waiting(self.appnium)
        self.action = ActionChains(self.appnium)
        self.text = Charge_user_login(self.appnium).test_chargeUserLogin()
        self.ChargeStartPage = ChargeStartPage(self.appnium)
        logging.info("-------------自动化测试开始！---------------")

    def test_chargeStation(self):
        try:
            # 能源车充电站
            if self.text == "____this part done_____":
                self.contexts_list = self.appnium.contexts
                # 搜索界面
                self.Search_Station = Search_Station(appium=self.appnium, contexts_list=self.contexts_list)
                self.Search_Station.searchStation(StationName="蔚景云协议站")
                # 定时订单界面
                MyPage(appium=self.appnium).selectEntrance(tab_bar="我的",item_bar="定时订单")
                # 站界面
                self.chargeStation = chargeStation(appium=self.appnium, contexts_list=self.contexts_list)
                self.chargeStation.stationType(pileNum="240020210730200102")
                # 访问启动界面
                self.ChargeStartPage.startChargeStep(coupon_option="", PreferentialPlans=1, SelectCarNum="津D8sd55",
                                                     coupon_name="",
                                                     chose_discount_name='超级会员', choice_pay="集团储值卡", choice_pay_count=1,
                                                     carName="power", companyName="power", StationName="蔚景云协议站")
        except Exception as e:
            # 捕获异常并记录日志
            logging.error("Uncaught exception during test execution", exc_info=True)
            # 打印完整的堆栈信息
            logging.error(e)
            logging.error("Traceback:", exc_info=False)
            logging.error(traceback.format_exc())
            raise Exception(e)

    def tearDown(self) -> None:
        self.appnium.quit()
