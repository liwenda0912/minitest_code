# 警告窗口处理
# 在WebDriver中处理JavaScript所生成的
# alert
# confirm
# prompt
# 十分简单，具体做法是使用
#  switch to alert()
# 方法定位到 alert/confirm/prompt，然后使用
# text：返回 （获取）alert/confirm/prompt 中的文字信息。
# accept（）：接受现有警告框。
# dismiss（）：放弃现有警告框。
# send_ keys(keysToSend)：发送文本至警告框。
# 模式窗口:必须点掉，不然操作不了其他动作
# 非模式窗口；与模式窗口相反

# 警告框：alert是个模式框，该怎么使用代码的方式大抹作他？
# 1、driver对象是在当的页面窗口内，但是不在alter上．并且我们没办法去定位这个窗口的元素
# 2. driver.switch_to.alter(）：暂时将测览器对像driver父给alter用
# 3.操作：
# text：返回 （获取）alert/confirm/prompt 中的文字信息。
# accept（）：接受现有警告框。
# dismiss（）：放弃现有警告框。
# send_ keys(keysToSend)：发送文本至警告框。

import time

from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="chromedriver")
driver.get('https://www.baidu.com')
action = ActionChains(driver)

driver.find_element(By.XPATH, '//*[@id="s-usersetting-top"]').click()
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="s-user-setting-menu"]/div/a[1]/span').click()
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="se-setting-7"]/a[2]').click()
time.sleep(2)

# 配置alert的弹框操作
alert = driver.switch_to.alert

# 打印弹框里的文本信息
print(alert.text)

# 接受alert的弹框操作（点击确认）
alert.accept()

# 放弃alert弹框操作
# alert.dismiss()

driver.close()
