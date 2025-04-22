import logging
import sys
import time
from selenium.webdriver import ActionChains

from appnium.mini_Selenium_Program.Public.Utils.IsSpaceUtils import isSpace, isEmpty, isNotSpace, isNotEmpty, \
    splitPrice, isNotNone
from appnium.mini_Selenium_Program.Public.Utils.SeleniumUtils import Driver, Waiting
from appium.webdriver.common.appiumby import AppiumBy
from appnium.mini_Selenium_Program.Public.Utils.imgHandleUtils import img_text_PointSize
from appnium.mini_Selenium_Program.Public.Utils.keyboardUtils import getHtml, adbKeyboard
from appnium.mini_Selenium_Program.Public.common.Logger.Logger import Logger
from appnium.mini_Selenium_Program.Public.common.page.AddCarPage import AddCarPage


class ChargeStartPage(object):
    def __init__(self, appium):
        self.appnium = appium
        self.driver = Driver(appium)
        self.wait = Waiting(self.appnium)
        self.action = ActionChains(self.appnium)

    # 该页面的汇总流程方法
    def startChargeStep(self, **kwargs):
        time.sleep(2)
        # 切换到固定窗口
        self.driver.Switch_Win(AppiumBy.XPATH,
                               '//*[starts-with(@class,"charge-button charge-button")]')
        # 关闭更换枪口弹窗
        self.CloseChoicePileWay()
        # 选择充电类型-定时，立即，并充等
        time_ = {"hour": {"TimeType": "hour", "text": "15时"}, "min": {"TimeType": "min", "text": "05分"}, "type": "time",
                 "action": "scroll"}
        self.parkingLotMode()
        self.TimingCharge(data=time_)
        # # 选中启动充电方式
        # self.ChoiceCharge(choice_pay=kwargs.get("choice_pay"), choice_pay_count=kwargs.get("choice_pay_count"),
        #                   carName=kwargs.get("carName"), companyName=kwargs.get("companyName"))
        # # 选择优惠方案，chose_discount等于1时使用优惠方案
        # self.PreferentialPlans(chose_discount=kwargs.get("PreferentialPlans"),
        #                        chose_discount_name=kwargs.get('chose_discount_name'))
        # # coupon_name为指定卡券名，不填则默认选中第一个
        # self.Coupon(option_=kwargs.get("coupon_option"), coupon_name=kwargs.get("coupon_name"))
        # # 是否选择车辆
        # self.SelectCar(carNum=kwargs.get("SelectCarNum"))
        # self.InsureSelect(boolean=False, station=kwargs.get("StationName"))
        # logging.info("运行到这里了，枪详情界面")
        self.wait.WaitElement(9, (AppiumBy.XPATH, "//*[starts-with(@class,'charge-button charge-button')]"), "元素找不到")
        # self.driver.Switch_Win(text_="跳转详情")
        self.OccupyPileRemark(choose='', option_="继续启动")
        self.appnium.save_screenshot("../picture/timingChargeResult.png")
        # 通过图片获取按钮点定位值并点击按钮，text为按钮文本
        self.driver.ScreenActionPress(PointSize=img_text_PointSize("../picture/timingChargeResult.png", text_="返回首页"))

    """
       占桩提醒弹窗
    """

    def OccupyPileRemark(self, **kwargs):
        if self.driver.Switch_Win(text_="占桩收费提醒", except_=1) != 1:
            logging.info("占桩收费提醒弹窗展示")
            # 是否点击不再展示提示占桩提示弹窗
            if kwargs.get("choose") is not None and len(kwargs.get("choose")) > 0:
                self.driver.Appnium_click()
            close_list = self.driver.Find_element(AppiumBy.XPATH,
                                                  '//*[contains(@class, "fee-btn fee-btn")]').find_elements(
                AppiumBy.TAG_NAME, 'wx-view')
            if len(close_list) > 0:
                for close_ in close_list:
                    if close_.text == kwargs.get("option_"):
                        close_.click()
                        logging.info("占桩收费提醒操作为：" + kwargs.get("option_"))
                        break
                    if len(close_list) == close_list.index(close_):
                        raise Exception("不存在弹窗按钮")

            else:
                pass

        else:
            logging.info("占位模式为车位占位计时")

    def parkingLotMode(self, **kwargs):
        if self.driver.Switch_Win(text_="选择对应车位降锁", except_=1) != 1:
            logging.info("占位模式为充电桩占桩计时")
            if kwargs.get("ParkingNum") is not None and len(kwargs.get("ParkingNum")) > 0:
                print()
            else:
                close_list = self.driver.Find_elements(AppiumBy.XPATH,
                                                       '//*[contains(@class, "right-span popup--right-span")]')
                if len(close_list) != 0:
                    for close_ in close_list:
                        close_.click()
                        logging.info("地锁弹窗已关闭！")
                        break
                else:
                    pass

        else:
            logging.info("占位模式为车位占位计时")

    """
       选择优惠卡券
    """

    def Coupon(self, **kwargs):
        # 优惠券选择方法可填option_和coupon_name参数，可以不填，option_不填为默认不选优惠卡券;coupon_name为指定卡券名，不填则默认选中第一个;
        def coupon_select():
            # 点击优惠卡券选择入口
            if self.public_click("优惠券包") is not False:
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
                            time.sleep(1)
                            list_ = self.driver.Find_elements(AppiumBy.XPATH,
                                                              '//*[contains(@class,"container two--container")]')
                            if list_ is not None:
                                for i in list_:
                                    # 判断是否被选中
                                    if len(i.find_elements(AppiumBy.XPATH,
                                                           '//*[contains(@class, "is-selected")]')) != 0:
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
                            logging.info("不使用任何优惠券")
                            break
            else:
                pass

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
            logging.info("开始选择卡券")
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
                            logging.info("已经选中 " + couponType + ":" + kwargs.get("coupon_name"))
                            break
                        else:
                            if list_.index(i) == len(list_ - 1):
                                logging.info("用户无" + kwargs.get("coupon_name") + "优惠券")
                            else:
                                pass
                    # 未指定选择优惠券时，默认选中第一张
                    else:
                        logging.info("默认选择第一张")
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

        # 返coupon_select方法
        return coupon_select()

    '''

        选择优惠方案

   '''

    def PreferentialPlans(self, **kwargs):
        # 选择优惠方案方法，chose_discount参数为1则使用优惠方案
        def selectPreferentialPlans():
            # 1 为使用优惠方案，0为不使用
            self.driver.Switch_Win(text_="启动充电")
            chose_discount = kwargs.get("chose_discount")
            if chose_discount == 1:
                getHtml(self.appnium)
                if '暂无充电优惠' not in self.driver.Find_element(AppiumBy.XPATH,
                                                            '//*[contains(@class, "coupon-content coupon-content")]').text:
                    # 轮询每一个优惠方案
                    discountSelect = discount_select()
                    for discount_text in discountSelect:
                        if kwargs.get("chose_discount_name") is not None and kwargs.get("coupon_name") != '':
                            if kwargs.get("chose_discount_name") in discount_text.text:
                                self.action.scroll_to_element(discount_text).perform()
                                self.action.click(discount_text).perform()
                                discount_text.find_element(AppiumBy.XPATH,
                                                           '//*[contains(@class,"checked")]')
                                logging.info("已选选中" + kwargs.get("chose_discount_name"))
                                self.DataMineDiscount()
                                break
                            else:
                                if discountSelect[len(discountSelect) - 1] == discount_text:
                                    logging.info("该优惠方案" + kwargs.get("chose_discount_name") + "不存在！")
                                    # 退出选中优惠弹窗
                                    self.DataMineDiscount()
                        else:
                            # 默认选择第一个
                            logging.info("默认选中第一个")
                            self.DataMineDiscount()
                            break
                else:
                    logging.info("用户在该站点无任何优惠方案")
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
                            logging.info("不使用优惠方案")
                            break
                        else:
                            continue
                # 点击确认按钮
                self.DataMineDiscount()

        # 获取优惠方案界面的列表数据
        def discount_select():
            # 所有获取优惠方案
            if self.public_click("优惠政策") is not False:
                self.driver.Switch_Win(text_="请选择优惠方案")
                # 获取优惠方案消息
                chose_discount_texts = self.driver.Find_elements(AppiumBy.XPATH,
                                                                 '//*[starts-with(@class, "agreement-item")]')
                return chose_discount_texts
            else:
                pass

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

    def ChoiceCharge(self, **kwargs):
        # 选择启动支付方
        def ChoiceChargingMethod():
            self.driver.Switch_Win(text_="启动充电")
            pay_options_text_list = []
            logging.info("开始选择启动方式")
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
                    pass
                # 判断是否为用户选中的支付方式
                if pay_options.text == choice_pay:
                    logging.info("已选中" + pay_options.text + "tab")
                    break
                else:
                    # 判断是否为列表最后一个
                    if len(pay_options_lists) - 1 == pay_options_lists.index(pay_options):
                        logging.info("不存在" + choice_pay + "支付方式！")
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
                    InSelectCardPopup(choice_pay, pay_options_text_list)
                    if choice_pay == "集团储值卡":
                        self.driver.Switch_Win(text_="请选择储值卡")
                        # 判断是否存在指定数据
                        if isNotSpace(companyName) and isNotEmpty(companyName):
                            self.wait.WaitElement(9,
                                                  (AppiumBy.XPATH, '//*[starts-with(@class,"uni-select__input-box")]'),
                                                  "元素找不到")
                            # 寻找集团名
                            companyName_list = self.wait.WaitElement(7, (
                                AppiumBy.XPATH, '//*[starts-with(@class,"uni-select__selector-item")]'),
                                                                     "页面无该元素")
                            for i in companyName_list:
                                # 判断当前数据是否为指定数据的值（companyName）
                                if i.text == companyName:
                                    self.action.click(i).perform()
                                    logging.info("已选中集团:" + companyName)
                                else:
                                    # 判断是否为列表最后一个数据
                                    if companyName_list.index(i) == len(companyName_list) - 1:
                                        logging.info("用户无" + companyName + "集团")
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
                            if float(splitPrice(
                                    cardPrice.find_element(AppiumBy.TAG_NAME, 'wx-view').text)) > 10 and check:
                                check = False
                                logging.info(
                                    "选中" + choice_pay + ":" + cardNameItem.text)
                                pass
                            else:
                                self.action.click(i).perform()
                                logging.info(
                                    "取消选择" + choice_pay + ":" + cardNameItem.text)
                    # 点击弹窗确认按钮
                    self.DataMineDiscount()
            elif choice_pay == "集团钱包" or choice_pay == "能量卡":
                # 点击进入选择能量卡/集团钱包的选择界面
                InSelectCardPopup(choice_pay, pay_options_text_list)
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
                            logging.info("以选中集团钱包：" + carName)
                            break
                        else:
                            if carNameItemList.index(cardItem) == len(carNameItemList) - 1:
                                logging.info("用户无" + choice_pay + ":" + carName)
                                break
                            else:
                                continue
                else:
                    logging.info("默认选" + choice_pay + "中第一个作为启动方式")
                # 点击弹窗确认按钮
                self.DataMineDiscount()
            else:
                logging.info("用户使用的启动方式为：" + choice_pay)
                pass

        # 点击选卡按钮
        def InSelectCardPopup(text, list_):
            list_card = self.wait.WaitElement(7, (AppiumBy.XPATH, '//*[starts-with(@class,"d-flex card--d-flex")]'),
                                              "页面无该元素")
            # 循序获取的列表并点击
            self.driver.circleList(list_=list_, list_card=list_card, type="card", text=text, action="click")

        # 返回choiceChargingMethod方法
        return ChoiceChargingMethod()

    #  关闭更换枪口弹窗
    def CloseChoicePileWay(self):
        # 判断是否存在更换充电位弹窗
        if self.driver.Switch_Win(text_="更换充电位", except_=1) == 1:
            logging.info("启动界面无更换充电位弹窗！")
            logging.info("启动界面无更换充电位弹窗！")
            pass
        else:
            close_list = self.driver.Find_elements(AppiumBy.XPATH, '//*[contains(@class, "popup-close popup-close")]')
            if len(close_list) != 0:
                for close_ in close_list:
                    close_.click()
                    logging.info("更换充电弹窗已经关闭成功！")
                    break
            else:
                pass

    # 选择车辆
    def SelectCar(self, **kwargs):
        if isNotNone(kwargs.get("carNum")) and isNotEmpty(kwargs.get("carNum")):

            # 是否存在默认车辆
            default_car = self.wait.WaitElement(8, (AppiumBy.XPATH,
                                                    '//*[starts-with(@class,"car-detail main--car-detail")]'), "元素不存在")
            if default_car.text == "添加车辆信息，便于识别部分站场停车费计算或减免出场":
                logging.info("用户未设置存在默认车辆！")
                # 模拟点击
                time.sleep(1)
                self.action.scroll_to_element(default_car).perform()
                time.sleep(1)
                self.action.click(default_car).perform()
                self.driver.Switch_Win(text_="充电车辆")
                carList = []
                buttonList = self.driver.Find_elements(AppiumBy.XPATH,
                                                       "//*[starts-with(@class, 'uni-button selectCar--uni-button')]")
                if kwargs.get("carNum") not in self.appnium.page_source:
                    self.driver.ActionsClick(buttonList, "添加车辆")
                    # 添加车辆操作
                    AddCarPage(self.appnium).addCarMessage(buttonList=buttonList, carNum=kwargs.get("carNum"))
                    self.driver.Switch_Win(text_="充电车辆")
                else:
                    # 是否在我的车辆里面
                    list_carNum = self.driver.Find_elements(AppiumBy.XPATH,
                                                            "//*[starts-with(@class, 'uni-list selectCar--uni-list')]")
                    if kwargs.get("carNum") in list_carNum[0].text:
                        carList = list_carNum[0].find_elements(AppiumBy.XPATH,
                                                               "//*[starts-with(@class,'car-no-inner')]")
                        pass
                    else:
                        # 点击集团车辆
                        self.wait.WaitElement(9, (AppiumBy.XPATH, "//*[contains(@text, '团体车辆')]"), '页面不存在该元素')
                        carList = list_carNum[1].find_elements(AppiumBy.XPATH,
                                                               "//*[starts-with(@class,'car-no-inner')]")
                # 点击车牌
                self.driver.ActionsClick(carList, kwargs.get("carNum"))
                self.driver.ActionsClick(buttonList, "确认选择")
                logging.info("已选择车牌" + kwargs.get("carNum") + "启动充电")
            else:
                logging.info("用户存在默认车辆！，并使用默认车辆启动充电")
                pass
        else:
            logging.info("不使用车牌启动充电！")
            pass

    def cancelPupop(self):
        win = self.appnium
        self.driver.Appnium_Switch_Window(win[0])

    # 优惠方案和卡券入口点击共用方法
    def public_click(self, text):
        getHtml(self.appnium)
        agreement_list = self.wait.WaitElement(7, (
            AppiumBy.XPATH, "//*[starts-with(@class, 'agreement-coupon agreement-coupon')]"), "元素不存在")
        if isNotEmpty(agreement_list) and isNotNone(agreement_list):
            for i in agreement_list:
                if text in i.text:
                    self.action.click(i).perform()
                    break
                else:
                    if agreement_list.index(i) == len(agreement_list) - 1:
                        raise Exception("元素不存在")
        else:
            logging.info("该支付方式下无" + text + "使用")
            return False

    # 勾选安心协议
    def InsureSelect(self, **kwargs):
        self.driver.Switch_Win(text_="启动充电")
        getHtml(self.appnium)
        insurance = self.driver.Find_elements(AppiumBy.XPATH, "//*[starts-with(@class, 'insurance insurance')]")
        # 勾选安心协议并且站点已开启安心充
        if kwargs.get("boolean") and isNotEmpty(insurance):
            insureObject = insurance[0].find_elements(AppiumBy.XPATH, '//*[starts-with(@class, "circle circle")]')
            if isNotEmpty(insureObject):
                logging.info(kwargs.get("station") + "已默认勾选安心充服务！")
                pass

            else:
                self.action.click(insurance[0]).perform()
                logging.info(kwargs.get("station") + "已勾选安心充服务！")
        # 不勾选安心协议并且站点已开启安心充
        elif kwargs.get("boolean") is not True and isNotEmpty(insurance):
            insureObject = insurance[0].find_elements(AppiumBy.XPATH, '//*[starts-with(@class, "circle circle")]')
            if isNotEmpty(insureObject):
                self.action.click(insurance[0]).perform()
                logging.info(kwargs.get("station") + "已取消勾选安心充服务！")

            else:
                logging.info(kwargs.get("station") + "已默认不勾选安心充服务！")
                pass
        # 站点无安心充服务
        else:
            logging.info(kwargs.get("station") + "无安心充服务！")
            pass

    def TimingCharge(self, **kwargs):
        def selectChargeTime():
            self.driver.Switch_Win(text_="启动充电")

            self.wait.WaitElement(9, (AppiumBy.XPATH, "//*[starts-with(@class, 'button-right button-right')]"),
                                  "元素不存在！")
            self.driver.Find_TagName_click("定时充电", (AppiumBy.TAG_NAME, "wx-label"), switch_text="立即充电")
            self.driver.Find_TagName_click("请选择定时充电时间", (AppiumBy.TAG_NAME, "wx-label"), switch_text="请选择定时充电时间")
            self.driver.Switch_Win(text_="确认")
            # 修改dom信息
            # element = self.driver.Find_element(AppiumBy.XPATH, "//*[starts-with(@class,'u-picker-view time--u-picker-view')]")
            # self.appnium.execute_script("arguments[0].value='[0,1,2]';", element)
            # time.sleep(2)
            # # 选择时
            self.driver.circleList(type=kwargs.get("data").get("type"),
                                   TimeType=kwargs.get("data").get("hour").get("TimeType"),
                                   text=kwargs.get("data").get("hour").get("text"),
                                   action=kwargs.get("data").get("action"))
            # # 选择分
            # self.driver.circleList(type=kwargs.get("data").get("type"), TimeType=kwargs.get("data").get("min").get("TimeType"),
            #                        text=kwargs.get("data").get("min").get("text"),
            #                        action=kwargs.get("data").get("action"))
            buttonList = self.driver.Find_elements(AppiumBy.XPATH,
                                                   "//*[starts-with(@class,'u-btn-picker time--u-btn-picker')]")
            self.driver.ActionsClick(buttonList, "确认")
            # if self.driver.Switch_Win(text_="请设置定时充电的时间为5分钟后", except_=1) != 1:
            #     buttonList = self.driver.Find_elements(AppiumBy.XPATH,
            #                                            "//*[starts-with(@class,'u-btn-picker time--u-btn-picker')]")
            #     for i in buttonList:
            #         i.click()
            #         logging.info("定时时间没有大于当前5分钟")
            #     self.TimingCharge()

        return selectChargeTime()

    def selectSoc(self):
        self

    # def timeSelect(self, **kwargs):
    #     if kwargs.get("type") == "card":
    #         list_ = kwargs.get("list_")
    #     else:
    #         if kwargs.get("type") == "hour":
    #             list_ = self.driver.Find_elements(AppiumBy.XPATH, '//*[starts-with(@class , "wx-picker-view-column")]')[
    #                 1].find_elements(AppiumBy.XPATH, '//*[starts-with(@class , "u-column-item time--u-column-item")]')
    #         else:
    #             list_ = self.driver.Find_elements(AppiumBy.XPATH, '//*[starts-with(@class , "wx-picker-view-column")]')[
    #                 2].find_elements(AppiumBy.XPATH, '//*[starts-with(@class , "u-column-item time--u-column-item")]')
    #     for i in list_:
    #         if kwargs.get("text") in i:
    #             if kwargs.get("action") == "click":
    #                 kwargs.get("list_card")[list_.index(i)].click()
    #                 logging.info("点击"+kwargs.get("text")+"成功")
    #                 break
    #             elif kwargs.get("action") == "actionClick":
    #                 self.action.click(i).preform()
    #                 logging.info("点击"+kwargs.get("text")+"成功")
    #                 break
    #             else:
    #                 self.action.scroll_to_element(i).perform()
    #                 logging.info("选择"+kwargs.get("text")+"成功")
    #                 break
    #         else:
    #             if len(list_) - 1 == list_.index(i):
    #                 logging.info("页面无"+kwargs.get("text") + "元素")
    #                 break
    #             else:
    #                 continue
