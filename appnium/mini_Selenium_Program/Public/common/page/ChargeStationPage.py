import logging
import sys
import time

from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver import ActionChains

from appnium.mini_Selenium_Program.Public.Utils.SeleniumUtils import Driver, Waiting
from appnium.mini_Selenium_Program.Public.Utils.keyboardUtils import getHtml


class chargeStation(object):
    def __init__(self, **kwargs):
        self.appnium = kwargs.get("appium")
        self.driver = Driver(self.appnium)
        self.wait = Waiting(self.appnium)
        self.action = ActionChains(self.appnium)
        self.contexts_list = kwargs.get("contexts_list")

    # 使用station方法时只需填写pileNum参数即可
    def stationType(self, **kwargs):
        self.driver.Switch_Win(
            text_="费用说明")
        # 判断是否为电单车站点详情
        getHtml(self.appnium)
        if "充电插座概况" in self.appnium.page_source:
            pass
        else:
            if "站桩概况" in self.appnium.page_source:
                logging.info("新界面")
                return self.NewStationDetail(pileNum=kwargs.get("pileNum"))
            else:
                logging.info("站场页面为旧ui")
                return self.OlderStationDetail(type="old", pileNum=kwargs.get("pileNum"))

    # 使用OlderStationDetail方法时要填写pileNum和type参数
    def OlderStationDetail(self, **kwargs):
        if kwargs.get("type") == "old":
            class_ = "device-info-detail device-info-detail"
        else:
            class_ = "interface-item item--interface-item"
        for i in self.appnium.find_elements(
                AppiumBy.XPATH,
                '//*[contains(@class,"' + class_ + '")]'):
            if kwargs.get("pileNum") in i.text:
                logging.info("准备滑动")
                self.wait.Appnium_wait(2)
                self.action.scroll_to_element(i).perform()
                current_context = self.appnium.current_window_handle
                # 切换到app界面
                self.appnium.switch_to.context(self.contexts_list[0])
                self.appnium.swipe(400, 900, 400, 600, 200)
                # 切换到小程序界面（H5，webview界面）
                self.appnium.switch_to.context(self.contexts_list[1])
                self.wait.Appnium_wait(5)
                self.appnium.switch_to.window(current_context)
                self.action.move_to_element(i).click().perform()
                break
        return True

    # 使用NewStationDetail方法时只需填写pileNum参数即可
    def NewStationDetail(self, **kwargs):
        if "站桩详情" in self.appnium.page_source:
            self.driver.Find_element(AppiumBy.XPATH, '//*[contains(@class, "right-detail")]').click()
            self.driver.Switch_Win(text_=kwargs.get("pileNum"))
        self.OlderStationDetail(type="new", pileNum=kwargs.get("pileNum"))
