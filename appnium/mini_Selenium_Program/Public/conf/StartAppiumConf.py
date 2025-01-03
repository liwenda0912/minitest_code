import json
import logging

from appium.options.common import AppiumOptions
from appium.options.android import UiAutomator2Options


class StartAppium(object):
    def __init__(self, **kwargs):
        self.process = 'com.tencent.mm:appbrand0'
        self.deviceName = '127.0.0.1:7555'
        self.platformName = 'Android'
        self.appPackage = 'com.tencent.mm'
        self.appActivity = '.ui.LauncherUI'
        self.platformVersion = '12'
        self.newCommandTimeout = 1200
        self.automationName = "UiAutomator2"
        self.desired_caps = {
            'enable_bidi': True,
            'platformName': self.platformName,
            'deviceName': self.deviceName,
            'chromeOptions': {'androidProcess': self.process},
            'platformVersion': self.platformVersion,
            'setCompressedLayoutHierarchy': True,
            'noReset': True,
            'newCommandTimeout': self.newCommandTimeout,
            'appPackage': self.appPackage,
            'setWebContentsDebuggingEnabled': True,
            'appActivity': self.appActivity,
            'recreateChromeDriverSessions': True,
            'automationName': self.automationName,
            'unicodeKeyboard': True,
            'resetKeyboard': True,
            'uiautomator2ServerInstallTimeout': 20000,
            'settings': {"enableMultiWindows": True}
        }

    def options(self):
        option = UiAutomator2Options().load_capabilities(self.desired_caps)
        logging.info("启动配置：" + str(self.desired_caps))
        return option

    # option = AppiumOptions()
    # option.set_capability('platformName', 'Android')
    # option.set_capability('platformVersion', '12')
    # option.set_capability('deviceName', '127.0.0.1:7555')
    # option.set_capability('noReset', True)
    # option.set_capability('detach', True)
    # option.set_capability('appPackage', 'com.tencent.mm')
    # option.set_capability('appActivity', '.ui.LauncherUI')
    # # option.set_capability('chromedriverExecutableDir',
    # #                       r'C:\Users\10260\AppData\Local\Programs\Appium\resources\app\node_modules\appium\node_modules\appium-chromedriver\chromedriver\win')
    # option.set_capability('recreateChromeDriverSessions', True)
    # option.set_capability('chromeOptions', ('androidProcess','com.tencent.mm:appbrand0')")
    # option.set_capability('automationName', 'UiAutomator2')
    # options = {
    #     # 操作系统名称Android或IOS
    #     'platformName': 'Android',
    #     # 设备名
    #     'deviceName': '127.0.0.1:62001',
    #     # Android版本
    #     'platformVersion': '7.1.2',
    #     # apk 包名
    #     'appPackage': 'com.tencent.mm',
    #     # apk 的 launcherActivity
    #     'appActivity': '.ui.LauncherUI',
    #     # 默认初始提示框取消
    #     'noReset': True
    # }
