import time

from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# # 启动模拟器配置并换唤醒测试微信（唤醒测试app）
# class Init:
#     def __init__(self):
#         try:
#             self.url_ = 'http://127.0.0.1:4723/wd/hub'
#             ConnectSimulator()
#             self.desired_caps = StartAppium().option
#             self.Appnium = webdriver.Remote(command_executor=self.url_, options=self.desired_caps)
#         except EOFError:
#             print(EOFError)


# # 定义appium驱动
# class utils_use:
#     def __init__(self):
#         self.appnium = Init().Appnium
#         self.driver = Driver(self.appnium)
#         self.wait = Waiting(self.appnium)


# 等待类
class Waiting(object):
    def __init__(self, appnium):
        self.Appnium = appnium

    # 隐形等待
    def Appnium_wait(self, loc):
        self.Appnium.implicitly_wait(loc)

    # 等待页面出现 参数：activity（需要等待的目标） , timeout(最大超时时间) , interval（循环查询时间）
    def Appnium_wait_ac(self, *loc):
        self.Appnium.wait_activity(loc[0], loc[1], loc[2])

    # 元素显性等待
    # ---------arg是变量，*args是元组，**kwargs是字典-------
    def WaitElement(self, type_name, *args):
        driver = Driver(self.Appnium)
        element = WebDriverWait(self.Appnium, timeout=50, poll_frequency=0.5, ignored_exceptions=None).until(
            EC.presence_of_element_located((args[0])), args[1])
        if element:
            # input输入框传参
            if type_name == 1:
                driver.Appnium_SendKey(args[0], args[2])
            # 点击事件
            elif type_name == 2:
                driver.Appnium_click(*args[0])
            # 获取文案
            elif type_name == 3:
                text = driver.Appnium_Text(*args[0])
                return text
            # 切换到iframe界面
            elif type_name == 4:
                driver.Appnium_Switch_Frame(driver.Find_element(*args[0]))
            # 获取元素里面的某个值
            elif type_name == 5:
                text = self.Appnium.find_element(*args).get_attribute('text')
                return text
            # 清空输入框
            elif type_name == 6:
                driver.Appnium_Clear(*args[0])
            # 查找所有该元素
            elif type_name == 7:
                return driver.Find_elements(*args[0])

            elif type_name == 8:
                return driver.Find_element(*args[0])
            elif type_name == 9:
                return ActionChains(self.Appnium).click(element).perform()
        else:
            print(element)


"""元素element操作方法"""


class Driver(object):
    def __init__(self, appnium):
        self.Appnium = appnium

    # 查找element元素
    def Find_element(self, *loc):
        data = self.Appnium.find_element(*loc)
        return data

    # 查找多个某属性的element元素
    def Find_elements(self, *loc):
        data_lists = self.Appnium.find_elements(*loc)
        return data_lists

    # 点击事件
    def Appnium_click(self, *loc):
        self.Appnium.find_element(*loc).click()

    # 传参
    def Appnium_SendKey(self, *loc):
        print(loc[1])
        self.Appnium.find_element(*loc[0]).send_keys(loc[1])

    # 清除输入框参数
    def Appnium_Clear(self, *loc):
        self.Appnium.find_element(*loc).clear()

    # 提交按钮
    def Appnium_Submit(self, *loc):
        self.Appnium.find_element(*loc).submit()

        # # 获取view的组件多个元素    def Appnium_View(self, *loc):
        # el_text = self.Appnium.find_elements(*loc).get_attribute('view')
        # return el_text

    # 获取element的文案信息
    def Appnium_Text(self, *loc):
        text = self.Appnium.find_element(*loc).get_attribute('value')
        return text

    # 滚动
    def Appnium_Scroll(self, *loc):
        self.Appnium.scroll(loc[0], loc[1], loc[2])

    # 滑动（下滑）
    def Appnium_swipe(self, loc):
        size = self.Appnium.get_window_size()
        x1 = size["width"] * 0.5
        y1 = size["height"] * 0.25
        y2 = size["height"] * 0.85
        self.Appnium.swipe(x1, y1, x1, y2, loc)

    # 切换到iframe界面
    def Appnium_Switch_Frame(self, loc):
        self.Appnium.switch_to.frame(loc)

    # 切换到含有某个元素的地方，参数text_是切换到含有该文本的页，参数except_不做报错处理并执行下一步，*loc是xpath语句其作用是切换到有这个元素的页面
    def Switch_Win(self, *loc, **kwargs):
        time.sleep(5)
        for handle in self.Appnium.window_handles:
            self.Appnium.switch_to.window(handle)
            if kwargs.get("text_") is not None and len(kwargs.get("text_")) != 0:
                print("开始查询", kwargs.get("text_"))
                if kwargs.get("text_") in self.Appnium.page_source:
                    print("找到")
                    break
                else:
                    print("找不到元素")
            else:
                el = self.Find_elements(*loc)
                print(len(el))
                if 0 != len(el) and el is not None:
                    break
            # kwargs.get("except_") != 1 不做报错处理并执行下一步动作
            if self.Appnium.window_handles[len(self.Appnium.window_handles) - 1] == handle and kwargs.get(
                    "except_") != 1:
                raise Exception("该元素不存在！")
            else:
                return 1

    # 切换多个页面
    def Appnium_Switch_Window(self, num):
        wins = self.Appnium.window_handles
        if num == 1:
            self.Appnium.switch_to.window(wins[1])
        elif num == 0:
            self.Appnium.switch_to.window(wins[0])
        elif num == 2:
            self.Appnium.switch_to.window(wins[2])
        elif num == 3:
            self.Appnium.switch_to.window(wins[3])
        else:
            self.Appnium.switch_to.window(wins[-1])

    # 切换到h5的小程序界面
    def Appnium_Switch_Context(self, **kwargs):
        if kwargs.get("type") == 1:
            self.Appnium.switch_to.context(kwargs.get("context_"))
        elif kwargs.get("type") == 0:
            self.Appnium.switch_to.context(kwargs.get("context_"))

    # def Appnium_Close(self):
    #     self.Appnium.close()
    #
    # def Appnium_Quit(self):
    #     self.Appnium.quit()
    # 执行js语句
    def Appnium_execute_script(self, *loc):
        self.Appnium.execute_script(loc[0], loc[1])

    # 模拟点击手机屏幕某处
    def actionPress(self, *loc, window_size):
        size = self.Appnium.get_window_size()
        bounds_x = (loc[0][0] + loc[1][0]) / 2
        bounds_y = (loc[0][1] + loc[1][1]) / 2
        x = size["width"] * (bounds_x / window_size[0])
        y = size["height"] * (bounds_y / window_size[1])
        self.Appnium.tap([(x, y)], 2000)

    # 返回中心坐标
    def getLocation(self, *loc):
        ele_coordinate = self.Appnium.find_element(*loc).location
        # 元素左上角横坐标
        x = ele_coordinate['x']
        # 元素左上角纵坐标
        y = ele_coordinate['y']
        ele_size = self.Appnium.find_element(*loc).size
        # 元素的宽
        width = ele_size['width']
        # 元素的高
        height = ele_size['height']
        return [x + width / 2, y + height / 2]


class utils_Option:
    # 去掉空格符
    @staticmethod
    def spilt(*args):
        string = args[0].split(args[1])
        new_string = utils_Option.join(string)
        return new_string

    # 组建字符重组列表中的元素
    @staticmethod
    def join(old_string):
        new_string = ''.join(old_string)
        return new_string

    # 给列表增加元素
    def append_(*args):
        new_string = args[0].append(args[1])
        return new_string
