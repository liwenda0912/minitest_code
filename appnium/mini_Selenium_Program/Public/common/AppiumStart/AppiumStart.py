from appium import webdriver
from exceptionx import Retry

from appnium.mini_Selenium_Program.Public.common.AppiumStart.Simulator_Start import ConnectSimulator, Simulator_Start, \
    AppiumApp_start, cmdProcessServer
from appnium.mini_Selenium_Program.Public.common.Logger.Logger import Logger
from appnium.mini_Selenium_Program.Public.conf.StartAppiumConf import StartAppium


# 启动模拟器配置并换唤醒测试微信（唤醒测试app）


@Retry(sleep=3, count=3)
class AppiumStart:
    def __init__(self):
        Logger().logging()
        self.url_ = 'http://127.0.0.1:4723/wd/hub'
        self.desired_caps = StartAppium().options()
        Simulator_Start()
        AppiumApp_start()
        ConnectSimulator("adb devices", "adb connect 127.0.0.1:7555")
        self.Appnium = self.appnium_onload()

    def appnium_onload(self):
        while True:
            if cmdProcessServer("4723") == "服务已经启动":
                Appnium = webdriver.Remote(command_executor=self.url_, options=self.desired_caps)
                break
        return Appnium
