import time

from selenium.webdriver import ActionChains
from appium.webdriver.common.appiumby import AppiumBy

from appnium.mini_Selenium_Program.Public.Utils.IsSpaceUtils import Split
from appnium.mini_Selenium_Program.Public.Utils.SeleniumUtils import Driver, Waiting
from appnium.mini_Selenium_Program.Public.Utils.imgHandleUtils import img_text_PointSize
from appnium.mini_Selenium_Program.Public.common.page.ChargeStartPage import ChargeStartPage


class MyPage(object):
    def __init__(self, **kwargs):
        self.appnium = kwargs.get("appium")
        self.driver = Driver(self.appnium)
        self.wait = Waiting(self.appnium)
        self.action = ActionChains(self.appnium)

    def selectEntrance(self, **kwargs):
        tabBar_list = self.driver.Find_elements(AppiumBy.XPATH,
                                                "//*[starts-with(@class,'u-tabbar__content__item__text tabbar--u-tabbar__content__item__text')]")
        for i in tabBar_list:
            if kwargs.get("tab_bar") in i.text:
                i.click()
            else:
                if tabBar_list.index(i) == len(tabBar_list) - 1:
                    raise Exception("该小程序无" + kwargs.get("tab_bar") + "tabbar")
        self.driver.Switch_Win(text_="余额")
        showMoreList = self.driver.Find_elements(AppiumBy.XPATH,
                                                 "//*[starts-with(@class,'d-flex d-flex align-items-center align-items-center')]")
        for c in showMoreList:
            self.action.scroll_to_element(c).perform()
            # 惯性滑动
            self.action.scroll_by_amount(c.location.get("x"), 300).perform()
            # 模拟鼠标移动点击
            time.sleep(2)
            self.action.move_to_element(c).click().perform()
        time.sleep(3)
        item_list = self.driver.Find_elements(AppiumBy.XPATH,
                                              "//*[starts-with(@class,'item-text item-text row-flex row-flex')]")
        for j in item_list:
            if kwargs.get("item_bar") in j.text:
                self.action.scroll_to_element(j).perform()
                self.action.scroll_by_amount(j.location.get("x"), 50).perform()
                time.sleep(2)
                j.click()
                break
            else:
                if item_list.index(j) == len(item_list) - 1:
                    raise Exception("该小程序的我的页面无" + kwargs.get("item_bar") + "入口")
        self.dateTimeChargeOrderListPage(page="", state="进行中", time='2025-05-18 06:31', buttonName='取消定时')

    def dateTimeChargeOrderListPage(self, **kwargs):
        time.sleep(5)
        self.driver.Switch_Win(text_="计划时间")
        list_ = self.driver.Find_elements(AppiumBy.XPATH,
                                          "//*[starts-with(@class,'order-list-box card--order-list-box')]")
        for i in list_:
            viewText = i.find_elements(AppiumBy.TAG_NAME, "wx-view")
            if kwargs.get("state") in i.text and kwargs.get("time") in i.text:
                if kwargs.get("page") == "详情界面":
                    self.action.move_to_element(i).click().perform()
                    self.driver.Switch_Win(text_="实时枪位")
                    for button in self.driver.Find_elements(AppiumBy.TAG_NAME, "wx-button"):
                        if button.text == kwargs.get("buttonName"):
                            button.click()
                            if kwargs.get("buttonName") == "取消定时":
                                ChargeStartPage(self.appnium).getScreenshot()
                                # 通过图片获取按钮点定位值并点击按钮，text为按钮文本
                                self.driver.ScreenActionPress(
                                    PointSize=img_text_PointSize("../picture/timingChargeResult.png", text_="关闭"))
                            else:
                                # 选择充电类型-定时，立即，并充等
                                time_ = {"time": {"date": {"TimeType": "date", "text": "2025-06-06"},
                                                  "datetime": {"TimeType": "hour", "text": "10:20"}}, "type": "time"}
                                self.driver.circleList(type=time_.get("type"), time=time_.get("time"))
                                buttonList = self.driver.Find_elements(AppiumBy.XPATH,
                                                                       "//*[starts-with(@class,'u-btn-picker time--u-btn-picker')]")
                                self.driver.ActionsClick(buttonList, "确认")
                            break
                else:
                    i.find_element(AppiumBy.XPATH, "//*[starts-with(@class,'close-btn card--close-btn')]").click()
                    ChargeStartPage(self.appnium).getScreenshot()
                    # 通过图片获取按钮点定位值并点击按钮，text为按钮文本
                    self.driver.ScreenActionPress(
                        PointSize=img_text_PointSize("../picture/timingChargeResult.png", text_="关闭"))
                    break
