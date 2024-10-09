from appnium.mini_Selenium_Program.Public.Utils.SeleniumUtils import Driver, Waiting
from appium.webdriver.common.appiumby import AppiumBy

from appnium.mini_Selenium_Program.Public.Utils.keyboardUtils import getHtml


class Coupon_Select(object):
    def __init__(self, appium):
        self.appnium = appium
        self.driver = Driver(appium)
        self.wait = Waiting(self.appnium)

    def coupon_select(self, **kwargs):
        chose_coupon = kwargs.get("chose_coupon")
        self.driver.Switch_Win(AppiumBy.XPATH, '//*[@text="选择优惠"]')
        self.wait.Appnium_wait(5)
        # 进入优惠券界面
        # self.driver.Appnium_click()
        if kwargs.get("option_") == 1:
            # 选择优惠券
            self.coupon_select_tab("优惠券")
            self.coupon_select_item(**kwargs)

        # 选择抵扣卡
        elif kwargs.get("option_") == 2:
            self.coupon_select_tab("抵扣卡")
            self.coupon_select_item(**kwargs)
        # 选择能量抵扣卡
        elif kwargs.get("option_") == 3:
            self.coupon_select_tab("能量抵扣卡")
            self.coupon_select_item(**kwargs)
        # 不使用优惠券
        elif kwargs.get("option_") == 4:
            # 进入优惠券界面
            for name_ in ("优惠券", "抵扣卡", "能量抵扣卡"):
                self.coupon_select_tab(name_)
                list_ = self.driver.Find_elements(AppiumBy.XPATH, '//*[contains(@class,"container two--container")]')
                if list_ is not None:
                    for i in list_:
                        # 判断元素是否被选中
                        if i.is_selected():
                            i.find_element(AppiumBy.XPATH,
                                           '//*[contains(@class,"radio two--radio")]').click()
                            break
        # 选择优惠方案
        chose_discount = kwargs.get("chose_discount")
        if chose_discount == 1:
            if '暂无充电优惠' not in self.driver.Find_element(AppiumBy.XPATH,
                                                        '//*[contains(@class, "price-detail price-detail")]').text:
                # 轮询每一个优惠方案
                for discount_text in self.discount_select():
                    if kwargs.get("chose_discount_name") in discount_text.text:
                        discount_text.find_element(AppiumBy.XPATH,
                                                   '//*[contains(@class,"checked")]').click()
                        # 点击确认选择优惠
                        self.driver.Appnium_click(AppiumBy.XPATH, '//*[@text="确定"]')
                        break
                    else:
                        # 默认选择第一个
                        self.driver.Appnium_click(AppiumBy.XPATH, '//*[@text="确定"]')
                        break
        else:
            # 轮询每一个优惠方案
            for discount_text in self.discount_select():
                print(len(self.driver.Find_elements(AppiumBy.XPATH, '//*[contains(@class,"is-checked")]')))
                if len(discount_text.find_elements(AppiumBy.XPATH, '//*[contains(@class,"is-checked")]')) != 0:
                    # 取消选择优惠方法
                    discount_text.click()
                    # self.driver.Appnium_click(AppiumBy.XPATH, '//*[contains(@class,"is-checked"])')
                    # 点击确认选择优惠
                    self.driver.Appnium_click(AppiumBy.XPATH, '//*[@text="确定"]')
                    break

    # 选择优惠卡券tab
    def coupon_select_tab(self, chose_coupon):
        for chose in self.driver.Find_elements(AppiumBy.XPATH, '//*[contains(@class,"item-name tab--item-name")]'):
            if chose_coupon == chose.text:
                chose.click()
                break

    # 选择优惠卡券
    def coupon_select_item(self, **kwargs):
        # 获取所有优惠卡券里的element
        list_ = self.driver.Find_elements(AppiumBy.XPATH, '//*[contains(@class,"container two--container")]')
        for i in list_:
            # 判断每个优惠券的文本是否选择优惠卡券弹窗里面
            if i.text in self.driver.Find_element(AppiumBy.XPATH, "//*[contains(@class, 'col two--col')]").text:
                if kwargs.get("coupon_name") is not None or kwargs.get("coupon_name") == '':
                    # 判断每个优惠卡券是否为用户要选择的优惠卡券
                    if kwargs.get("coupon_name") in i.text:
                        # 点击优惠卡券的radio选择框
                        i.find_element(AppiumBy.XPATH, '//*[contains(@class, "radio two--radio")]').click()
                        break
                else:
                    i.find_element(AppiumBy.XPATH, '//*[contains(@class, "radio two--radio")]').click()
                    break

    # 获取优惠方案界面的列表数据
    def discount_select(self):
        # 所有获取优惠方案
        self.wait.WaitElement(2, (AppiumBy.XPATH, '//*[contains(@class, "price-detail price-detail")]'),
                              "元素不存在！")
        self.driver.Switch_Win(AppiumBy.XPATH, '//*[@text="请选择优惠方案"]')
        chose_discount_text = self.driver.Find_elements(AppiumBy.XPATH,
                                                        '//*[contains(@class, "agreement-name")]')
        return chose_discount_text
