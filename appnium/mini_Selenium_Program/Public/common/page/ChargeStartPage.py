import logging
import sys
import time
from selenium.webdriver import ActionChains

from appnium.mini_Selenium_Program.Public.Utils.IsSpaceUtils import isSpace, isEmpty, isNotSpace, isNotEmpty, splitPrice
from appnium.mini_Selenium_Program.Public.Utils.SeleniumUtils import Driver, Waiting
from appium.webdriver.common.appiumby import AppiumBy
from appnium.mini_Selenium_Program.Public.Utils.keyboardUtils import getHtml
from appnium.mini_Selenium_Program.Public.common.Logger.Logger import Logger


class ChargeStartPage(object):
    def __init__(self, appium):
        self.appnium = appium
        self.driver = Driver(appium)
        self.wait = Waiting(self.appnium)
        self.action = ActionChains(self.appnium)

    # 该页面的汇总流程方法
    def startChargeStep(self, **kwargs):
        time.sleep(5)
        # 切换到固定窗口
        self.driver.Switch_Win(AppiumBy.XPATH,
                               '//*[contains(@class,"charge-button charge-button d-flex d-flex align-items-center align-items-center justify-content-center justify-content-center")]')
        # 关闭更换枪口弹窗
        self.CloseChoicePileWay()
        # 选中启动充电方式
        self.ChoiceChargingMethod(choice_pay=kwargs.get("choice_pay"), choice_pay_count=kwargs.get("choice_pay_count"),
                                  carName=kwargs.get("carName"), companyName=kwargs.get("companyName"))
        # 选择优惠方案，chose_discount等于1时使用优惠方案
        self.PreferentialPlans(chose_discount=kwargs.get("PreferentialPlans"),
                               chose_discount_name=kwargs.get('chose_discount_name'))
        # 查看是否存在优惠卡券可选择
        if self.driver.Find_elements(AppiumBy.XPATH,
                                     '//*[contains(@class,"agreement-body agreement-body d-flex d-flex align-items-center align-items-center")]') is not None or []:
            # coupon_name为指定卡券名，不填则默认选中第一个
            self.Coupon(option_=kwargs.get("coupon_option"), coupon_name=kwargs.get("coupon_name"))

        # 是否选择车辆
        self.SelectCar(carName=kwargs.get("SelectCarNum"))
        logging.info("运行到这里了，枪详情界面")

    def Coupon(self, **kwargs):
        # 优惠券选择方法可填option_和coupon_name参数，可以不填，option_不填为默认不选优惠卡券;coupon_name为指定卡券名，不填则默认选中第一个;
        def coupon_select():
            self.wait.WaitElement(2, (AppiumBy.XPATH,
                                      '//*[contains(@class,"agreement-body agreement-body d-flex d-flex align-items-center align-items-center")]'),
                                  "元素找不到")
            self.driver.Switch_Win(text_="选择优惠")
            # 进入优惠券界面
            if kwargs.get("option_") == "优惠券" and kwargs.get("coupon_name") is not None and len(
                    kwargs.get("coupon_name")) > 0:
                # 选择优惠券
                coupon_select_tab("优惠券")
                # 将coupon_name传进coupon_select_item里面
                coupon_select_item("优惠券")
            # 选择抵扣卡
            elif kwargs.get("option_") == "抵扣卡" and kwargs.get("coupon_name") is not None and len(
                    kwargs.get("coupon_name")) > 0:
                coupon_select_tab("抵扣卡")
                coupon_select_item("抵扣卡")
            # 选择能量抵扣卡
            elif kwargs.get("option_") == "能量抵扣卡" and kwargs.get("coupon_name") is not None and len(
                    kwargs.get("coupon_name")) > 0:
                coupon_select_tab("能量抵扣卡")
                coupon_select_item("能量抵扣卡")
            # 不使用优惠券
            else:
                check = False
                # 进入优惠券界面
                for name_ in ("优惠券", "抵扣卡", "能量抵扣卡"):
                    # 判断是否全部退出优惠券
                    if check is not True:
                        coupon_select_tab(name_)
                        list_ = self.driver.Find_elements(AppiumBy.XPATH,
                                                          '//*[contains(@class,"container two--container")]')
                        getHtml(self.appnium)
                        if list_ is not None:
                            for i in list_:
                                # 判断元素是否被选中
                                if len(i.find_elements(AppiumBy.XPATH, '//*[contains(@class, "is-selected")]')) != 0:
                                    time.sleep(1)
                                    self.action.click(i).perform()
                                    check = True
                                    break
                                else:
                                    # 只查找每个列表的2个的状态（小程序被选中的卡券都在列表的第一个位置）
                                    if list_.index(i) == 0:
                                        break
                                    else:
                                        pass
                    else:
                        print(check)
                        Logger(stream=sys.stdout).info("不使用任何优惠券")
                        break

        # 选择优惠卡券tab
        def coupon_select_tab(chose_coupon):
            for chose in self.driver.Find_elements(AppiumBy.XPATH,
                                                   '//*[contains(@class,"item-name tab--item-name")]'):
                # 判断chose是否等于要选中的tab名
                if chose_coupon == chose.text:
                    chose.click()
                    break

        # 选择优惠卡券
        def coupon_select_item(couponType):
            print("开始选择卡券")
            Logger(stream=sys.stdout).info("开始选择卡券")
            # 获取所有优惠卡券里的element
            list_ = self.driver.Find_elements(AppiumBy.XPATH, '//*[contains(@class,"container two--container")]')
            for i in list_:
                time.sleep(2)
                # 获取到的数据是否为优惠卡券里面的数据
                if i.text in self.driver.Find_element(AppiumBy.XPATH, "//*[contains(@class, 'col two--col')]").text:
                    # 是否指定优惠券
                    if kwargs.get("coupon_name") is not None and kwargs.get("coupon_name") != "" and len(
                            kwargs.get("coupon_name")) > 0:
                        # 判断每个优惠卡券是否为用户要选择的优惠卡券
                        if kwargs.get("coupon_name") in i.text:
                            # 点击优惠卡券的radio选择框
                            i.find_element(AppiumBy.XPATH, '//*[contains(@class, "radio two--radio")]').click()
                            Logger(stream=sys.stdout).info("已经选中 " + couponType + ":" + kwargs.get("coupon_name"))
                            break
                        else:
                            if list_.index(i) == len(list_ - 1):
                                Logger(stream=sys.stdout).info("用户无" + kwargs.get("coupon_name") + "优惠券")
                            else:
                                pass
                    # 未指定选择优惠券时，默认选中第一张
                    else:
                        Logger(stream=sys.stdout).info("默认选择第一张")
                        # 该优惠卡券是否被默认选中
                        if len(i.find_element(AppiumBy.XPATH,
                                              '//*[contains(@class, "radio two--radio")]').find_elements(AppiumBy.XPATH,
                                                                                                         '//*[contains(@class, "is-selected")]')) != 0:
                            # 点击退出选择优惠界面
                            i.find_element(AppiumBy.XPATH,
                                           '//*[contains(@class, "coupon-head two--coupon-head")]').find_element(
                                AppiumBy.TAG_NAME, 'wx-uni-icons').click()
                            break
                        else:
                            i.find_element(AppiumBy.XPATH, '//*[contains(@class, "radio two--radio")]').click()
                            break

        return coupon_select()

    '''

        优惠方案

   '''

    def PreferentialPlans(self, **kwargs):
        # 选择优惠方案方法，chose_discount参数为1则使用优惠方案
        def selectPreferentialPlans():
            time.sleep(2)
            # 1 为使用优惠方案，0为不使用
            chose_discount = kwargs.get("chose_discount")
            if chose_discount == 1:
                if '暂无充电优惠' not in self.driver.Find_element(AppiumBy.XPATH,
                                                            '//*[contains(@class, "price-detail price-detail")]').text:
                    # 轮询每一个优惠方案
                    discountSelect = discount_select()
                    for discount_text in discountSelect:
                        if kwargs.get("chose_discount_name") is not None and kwargs.get("coupon_name") != '':
                            if kwargs.get("chose_discount_name") in discount_text.text:
                                self.action.scroll_to_element(discount_text).perform()
                                self.action.click(discount_text).perform()
                                discount_text.find_element(AppiumBy.XPATH,
                                                           '//*[contains(@class,"checked")]')
                                Logger(stream=sys.stdout).info("已选选中" + kwargs.get("chose_discount_name"))
                                self.DataMineDiscount()
                                break
                            else:
                                if discountSelect[len(discountSelect) - 1] == discount_text:
                                    Logger(stream=sys.stdout).info("该优惠方案" + kwargs.get("chose_discount_name") + "不存在！")
                                    # 退出选中优惠弹窗
                                    self.DataMineDiscount()
                        else:
                            # 默认选择第一个
                            Logger(stream=sys.stdout).info("默认选中第一个")
                            self.DataMineDiscount()
                            break
                else:
                    Logger(stream=sys.stdout).info("用户在该站点无任何优惠方案")
                    logging.info("用户在该站点无任何优惠方案")
            # 不使用优惠方案
            else:
                check = False
                # 轮询每一个优惠方案
                for discount_text in discount_select():
                    if len(discount_text.find_elements(AppiumBy.XPATH, '//*[contains(@class,"checked")]')) != 0:
                        for discount in discount_text.find_elements(AppiumBy.XPATH, '//*[contains(@class,"checked")]'):
                            # 判断是否存在class为is-checked元素
                            if len(discount.find_elements(AppiumBy.XPATH, '//*[contains(@class,"is-checked")]')) != 0:
                                # 取消以选择的优惠方案
                                discount_text.find_element(AppiumBy.XPATH, '//*[contains(@class, "checked")]').click()
                                check = True
                            break
                        # 退出最外层循环
                        if check:
                            Logger(stream=sys.stdout).info("不使用优惠方案")
                            break
                        else:
                            continue
                # 点击确认按钮
                self.DataMineDiscount()

        # 获取优惠方案界面的列表数据
        def discount_select():
            # 所有获取优惠方案
            self.wait.WaitElement(2, (AppiumBy.XPATH, '//*[contains(@class, "price-detail price-detail")]'),
                                  "小程序优惠模块不存在！")
            self.driver.Switch_Win(text_="请选择优惠方案")
            # 获取优惠方案消息
            chose_discount_texts = self.driver.Find_elements(AppiumBy.XPATH,
                                                             '//*[starts-with(@class, "agreement-item")]')
            # chose_discount_text_ = self.driver.Find_elements(AppiumBy.XPATH, '//*[starts-with(@class, "agreement-type")]')
            # chose_discount_text = self.driver.Find_elements(AppiumBy.XPATH, '//*[starts-with(@class, "agreement-name")]')
            return chose_discount_texts

        # 返回优惠方案操作结果
        return selectPreferentialPlans()

    # 寻找弹窗的确认按钮
    def DataMineDiscount(self):
        for TagName in self.driver.Find_element(AppiumBy.XPATH,
                                                '//*[contains(@class ,"popup-head")]').find_elements(AppiumBy.TAG_NAME,
                                                                                                     'wx-view'):
            if TagName.text == "确认":
                TagName.click()
                break
            else:
                continue

    # 选择启动支付方
    def ChoiceChargingMethod(self, **kwargs):
        time.sleep(5)
        pay_options_text_list = []
        Logger(stream=sys.stdout).info("开始选择启动方式")
        choice_pay = kwargs.get("choice_pay")

        choice_pay_count = kwargs.get("choice_pay_count")
        pay_options_lists = self.driver.Find_elements(AppiumBy.XPATH,
                                                      '//*[contains(@class, "_div tab--_div ")]')
        for pay_options in pay_options_lists:
            pay_options.click()
            time.sleep(2)
            # 记录并筛选掉不用选卡或钱包的pay方式
            if pay_options.text not in ["现金钱包", "信用付"]:
                pay_options_text_list.append(pay_options.text)
            else:
                continue
            # 判断是否为用户选中的支付方式
            if pay_options.text == choice_pay:
                Logger(stream=sys.stdout).info("已选中" + pay_options.text + "tab")
                break
            else:
                # 判断是否为列表最后一个
                if len(pay_options_lists) - 1 == pay_options_lists.index(pay_options):
                    Logger(stream=sys.stdout).info("不存在" + choice_pay + "支付方式！")
                    raise Exception("不存在" + choice_pay + "支付方式！")
                else:
                    continue

        carName = kwargs.get("carName")
        companyName = kwargs.get("companyName")
        if choice_pay == "集团储值卡" or choice_pay == "个人储值卡":
            if choice_pay_count != 1:
                pass
            # 只选一张
            else:
                # 点击进入选择集团储值卡 / 个人储值卡的选择界面
                # 点击选卡弹窗(测试)
                self.InSelectCardPopup(choice_pay, pay_options_text_list)
                if choice_pay == "集团储值卡":
                    self.driver.Switch_Win(text_="请选择集团储值卡")
                    # 判断是否存在指定数据
                    if isNotSpace(companyName) and isNotEmpty(companyName):
                        self.wait.WaitElement(9, (AppiumBy.XPATH, '//*[starts-with(@class,"uni-select__input-box")]'),
                                              "元素找不到")
                        # 寻找集团名
                        companyName_list = self.wait.WaitElement(7, (
                            AppiumBy.XPATH, '//*[starts-with(@class,"uni-select__selector-item")]'),
                                                                 "页面无该元素")
                        for i in companyName_list:
                            # 判断当前数据是否为指定数据的值（companyName）
                            if i.text == companyName:
                                self.action.click(i).perform()
                                Logger(stream=sys.stdout).info("已选中集团:" + companyName)
                            else:
                                # 判断是否为列表最后一个数据
                                if companyName_list.index(i) == len(companyName_list) - 1:
                                    Logger(stream=sys.stdout).info("用户无" + companyName + "集团")
                                else:
                                    continue
                    else:
                        pass
                else:
                    self.driver.Switch_Win(text_="请选择储值卡")
                # 获取弹窗的集团储值卡 / 储值卡列表信息
                carNameItemList = self.wait.WaitElement(7, (AppiumBy.XPATH, '//*[starts-with(@class,"card-item")]'),
                                                        "页面无该元素")
                # 用于只选择一张大于10元的储值卡的校验值
                check = True
                if len(carNameItemList) >= 1:
                    for i in carNameItemList:
                        cardPrice = i.find_element(AppiumBy.XPATH, "//*[starts-with(@class,'card-price')]")
                        # 判断金额是是否大于10，否点击取消勾选
                        cardNameItem = i.find_element(AppiumBy.XPATH, "//*[starts-with(@class,'card-name')]")
                        # 判断卡的金额是否大于10
                        if float(splitPrice(cardPrice.find_element(AppiumBy.TAG_NAME, 'wx-view').text)) > 10 and check:
                            check = False
                            Logger(stream=sys.stdout).info(
                                "选中" + choice_pay + ":" + cardNameItem.text)
                            pass
                        else:
                            self.action.click(i).perform()
                            Logger(stream=sys.stdout).info(
                                "取消选择" + choice_pay + ":" + cardNameItem.text)

        elif choice_pay == "集团钱包" or choice_pay == "能量卡":
            # 点击进入选择能量卡/集团钱包的选择界面
            self.InSelectCardPopup(choice_pay, pay_options_text_list)
            # self.wait.WaitElement(2, (AppiumBy.XPATH, '//*[starts-with(@class,"d-flex card--d-flex")]'), "页面无该元素")
            if choice_pay == "集团钱包":
                self.driver.Switch_Win(text_="请选择集团")
            else:
                self.driver.Switch_Win(text_="请选择能量卡")

            # 获取弹窗的能量卡/集团钱包列表信息
            carNameItemList = self.wait.WaitElement(7, (AppiumBy.XPATH, '//*[starts-with(@class,"card-item")]'),
                                                    "页面无该元素")
            # carName是否为空，是默认选择第一张
            if isNotSpace(carName) and isNotEmpty(carName):
                for cardItem in carNameItemList:
                    # 判断卡名是否存在卡包里
                    if carName in cardItem.text:
                        self.action.click(cardItem).perform()
                        Logger(stream=sys.stdout).info("以选中集团钱包：" + carName)
                        break
                    else:
                        if carNameItemList.index(cardItem) == len(carNameItemList) - 1:
                            Logger(stream=sys.stdout).info("用户无" + choice_pay + ":" + carName)
                            break
                        else:
                            continue
            else:
                Logger(stream=sys.stdout).info("默认选" + choice_pay + "中第一个作为启动方式")
        else:
            Logger(stream=sys.stdout).info("用户使用的启动方式为：" + choice_pay)
        # 点击弹窗确认按钮
        self.DataMineDiscount()

    #  关闭更换枪口弹窗
    def CloseChoicePileWay(self):
        # 判断是否存在更换充电位弹窗
        if self.driver.Switch_Win(text_="更换充电位", except_=1) == 1:
            logging.info("启动界面无更换充电位弹窗！")
            Logger(stream=sys.stdout).info("启动界面无更换充电位弹窗！")
            pass
        else:
            close_list = self.driver.Find_elements(AppiumBy.XPATH, '//*[contains(@class, "popup-close popup-close")]')
            if len(close_list) != 0:
                for close_ in close_list:
                    close_.click()
                    Logger(stream=sys.stdout).info("更换充电弹窗已经关闭成功！")
                    break
            else:
                pass

    # 点击选卡按钮
    def InSelectCardPopup(self, text, list_):
        list_car = self.wait.WaitElement(7, (AppiumBy.XPATH, '//*[starts-with(@class,"d-flex card--d-flex")]'),
                                         "页面无该元素")
        for i in list_:
            if text in i:
                list_car[list_.index(i)].click()
                break
            else:
                if len(list_) - 1 == list_.index(i):
                    Logger(stream=sys.stdout).info("页面无该元素")
                    break
                else:
                    continue

    # 未验证
    def SelectCar(self, **kwargs):
        if kwargs.get("carNum") is not None:
            # 是否选择车辆
            if self.wait.WaitElement(8, (AppiumBy.XPATH,
                                         '//*[contains(@class,"car-detail main--car-detail")]')).text == "添加车辆信息，享限时免费停车权益":
                logging.info("用户未存在默认车辆！")
                self.driver.Appnium_click(AppiumBy.XPATH, '//*[contains(@class,"add-button main--add-button")]')
                self.driver.Switch_Win(text_="充电车辆")
                if kwargs.get("carNum") not in self.appnium.page_source:
                    self.wait.WaitElement(2, (AppiumBy.XPATH, "//*[contains(@text, '添加车辆')]"))
                    # 添加车辆操作
                else:
                    if kwargs.get("carNum") not in self.driver.Find_elements().text:
                        self.wait.WaitElement(2, (AppiumBy.XPATH, "//*[contains(@text, '我的车辆')]"))
                        self.driver.Appnium_click(AppiumBy.XPATH, "//*[contains(@text," + kwargs.get("carNum") + ")]")
                    else:
                        self.wait.WaitElement(2, (AppiumBy.XPATH, "//*[contains(@text, '团队车辆')]"))
                        self.driver.Appnium_click(AppiumBy.XPATH, "//*[contains(@text," + kwargs.get("carNum") + "))]")
                self.wait.WaitElement(2, (AppiumBy.XPATH, "//*[contains(@text,'确认选择')]"))
            else:
                logging.info("用户存在默认车辆！，并使用默认车辆启动充电")
                pass
        else:
            Logger(stream=sys.stdout).info("不选择用车辆启动充电")
            pass

    def cancelPupop(self):
        win = self.appnium
        self.driver.Appnium_Switch_Window(win[0])
