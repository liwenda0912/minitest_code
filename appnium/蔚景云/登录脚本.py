from appnium.启动appium import StartAppium
from appium.webdriver.common.appiumby import AppiumBy
from appium import webdriver


desired_caps = StartAppium().desired_caps
print(desired_caps)
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
driver.find_element(AppiumBy.XPATH, "//*[@resource-id='cn.evking.evcharge:id/tv_tab_title' and @text='我的']").click()
driver.find_element(AppiumBy.XPATH, "//*[@class='android.widget.TextView' and @text='注册/登录']").click()
driver.find_element(AppiumBy.XPATH, "//*[@class='android.widget.CheckBox' and @text='使用密码登录']").click()
driver.find_element(AppiumBy.XPATH, "//*[@class='android.widget.EditText' and @text='请输入手机号码']").send_keys('15767112315')
driver.find_element(AppiumBy.XPATH, "//*[@class='android.widget.EditText' and @text='请设置6~16位登录密码']").send_keys('da091234')
driver.find_element(AppiumBy.XPATH, "//*[@resource-id='cn.evking.evcharge:id/agreement_cb']").click()
driver.find_element(AppiumBy.XPATH, "//*[@resource-id='cn.evking.evcharge:id/register_btn']").click()
driver.quit()
