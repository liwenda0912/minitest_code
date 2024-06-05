import time

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy


class StartAppium:
    desired_caps = {
        # 操作系统名称Android或IOS
        'platformName': 'Android',
        # 设备名
        'deviceName': '127.0.0.1:62001',
        # Android版本
        'platformVersion': '7.1.2',
        # apk 包名
        'appPackage': 'com.tencent.mm',
        # apk 的 launcherActivity
        'appActivity': '.ui.LauncherUI',
        # 默认初始提示框取消
        'noReset': True
    }



# driver.find_element(AppiumBy.CLASS_NAME, 'android.widget.TextView').click()
# driver.find_element(AppiumBy.CLASS_NAME, 'android.widget.EditText').send_keys('2.0')
# driver.find_element(AppiumBy.CLASS_NAME, 'android.widget.ImageView').click()
