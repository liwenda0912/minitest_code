import time

from appnium.启动appium import StartAppium
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium import webdriver

desired_caps = StartAppium().desired_caps
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
time.sleep(500)
driver.find_element(AppiumBy.CLASS_NAME, 'android.widget.TextView').click()
driver.find_element(AppiumBy.CLASS_NAME, 'android.widget.EditText').send_keys('2.0')
driver.find_element(AppiumBy.CLASS_NAME, 'android.widget.ImageView').click()
driver.find_element(AppiumBy.XPATH,
                    '//*[@resource-id="cn.evking.evcharge:id/stationName_tv" and @text="2.0协议站"]').click()
time.sleep(1)
driver.find_element(AppiumBy.XPATH, '//*[@resource-id="cn.evking.evcharge:id/tv_tab_title" and @text="桩详情"]').click()
start = driver.find_element(AppiumBy.XPATH, '//*[@text="桩详情"]')
end = driver.find_element(AppiumBy.XPATH, '//*[@resource-id="cn.evking.evcharge:id/stationName_tv" and @text="2.0协议站"]')
driver.scroll(start, end)
driver.find_element(AppiumBy.XPATH, '//*[@text="直流快充480kW"]').click()
time.sleep(1)
driver.find_element(AppiumBy.XPATH, '//*[@text="选择车辆"]').click()
time.sleep(1)
driver.find_element(AppiumBy.XPATH, '//*[@text="京Asdsdsd"]').click()
driver.find_element(AppiumBy.XPATH, '//*[@text="确认选择"]').click()
time.sleep(1)
driver.find_element(AppiumBy.XPATH, '//*[@text="立即充电"]').click()
time.sleep(1)
driver.find_element(AppiumBy.XPATH, '//*[@text="开始充电"]').click()
time.sleep(1)
driver.find_element(AppiumBy.XPATH, '//*[@text="取消"]').click()
element = WebDriverWait(driver, timeout=500, poll_frequency=0.5, ignored_exceptions=None).until(
    EC.presence_of_element_located((AppiumBy.XPATH, '//*[@text="00:01:35"]')), "找不到该元素")
if element:
    driver.find_element(AppiumBy.XPATH, '//*[@text="结束充电"]').click()
else:
    print(element)
driver.find_element(AppiumBy.XPATH, '//*[@text="确定"]').click()
driver.quit()
