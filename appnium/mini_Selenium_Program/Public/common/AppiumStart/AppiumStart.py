from appium import webdriver
from exceptionx import Retry
from appnium.mini_Selenium_Program.Public.Utils.Simulator_Start import ConnectSimulator
from appnium.mini_Selenium_Program.Public.conf.StartAppiumConf import StartAppium


# 启动模拟器配置并换唤醒测试微信（唤醒测试app）

@Retry(sleep=3, count=3)
class AppiumStart:
    def __init__(self):
        ConnectSimulator()
        self.url_ = 'http://127.0.0.1:4723/wd/hub'
        self.desired_caps = StartAppium().option
        self.Appnium = webdriver.Remote(command_executor=self.url_ , options=self.desired_caps)
