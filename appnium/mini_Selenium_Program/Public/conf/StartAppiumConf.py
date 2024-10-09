import json

from appium.options.common import AppiumOptions
from appium.options.android import UiAutomator2Options


class StartAppium:
    desired_caps = {
        'enable_bidi': True,
        'platformName': 'Android',
        'deviceName': '127.0.0.1:7555',
        'chromeOptions': {'androidProcess': 'com.tencent.mm:appbrand0'},
        'platformVersion': '12',
        'setCompressedLayoutHierarchy': True,
        'noReset': True,
        'newCommandTimeout': "100000",
        'appPackage': 'com.tencent.mm',
        'setWebContentsDebuggingEnabled': True,
        'appActivity': '.ui.LauncherUI',
        'recreateChromeDriverSessions': True,
        'automationName': "UiAutomator2",
        'unicodeKeyboard': True,
        'resetKeyboard': True
    }
    option = UiAutomator2Options().load_capabilities(desired_caps)






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
