from appnium.mini_Selenium_Program.Public.Utils.uilts import Driver, Waiting
from appium.webdriver.common.appiumby import AppiumBy


class Coupon_Select(object):
    def __init__(self, appium):
        self.appnium = appium
        self.driver = Driver(appium)
        self.wait = Waiting(self.appnium)

    def coupon_select(self):
        chose_coupon = 0
        # 进入优惠券界面
        # self.driver.Appnium_click()
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
            self.driver.Appnium_click(AppiumBy.XPATH, '//*[contains(@class,"d-flex d-flex align-items-center align-items-center")]')
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
            self.driver.Appnium_click(AppiumBy.XPATH, '//*[contains(@class,"d-flex d-flex align-items-center align-items-center")]')
            # 所有获取优惠方案
            chose_discount_text = self.appnium.find_elements()
            for discount_text in chose_discount_text:
                if "" in discount_text.text:
                    self.driver.Appnium_click()
                    # 点击确认选择优惠
                    self.driver.Appnium_click()
                    equal_text = discount_text.text
                    break
            # 点击取消退出选择优惠方案界面
            self.driver.Appnium_click()
