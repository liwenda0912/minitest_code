# 1.隐形等待时间 implicity_wait()
#    1.在时间范围内，定位到页面，则继续执行下面代码
#    2.超出时间，则抛出异常
# 2.强制等待 time.sleep()
# 3.显示等待：(需要特别关注一个元素是才使用）
#   1.明确等到某个元素出现，等不到就一直等，除非在固定时间之内都找不到就抛出异常 2.等到元素出现或者元素点击之后就继续执行下面代码 from selenium.webdriver.support.ui import
#   element = WebDriverWait(driver, timeout=5, poll_frequency=0.5, ignored_exceptions=None).until(
#     EC.presence_of_element_located((By.XPATH, '//*[@id="top-login"]/div[2]/a')), "找不到")
# 注危
# 指同时改置了隐形等待和显示等待，则以隐形等待为第一优先级，也就是说，若隐形等待时间大于显示等待，
# 显示等待时间设zhi无效，用为driver 若找不到元素，会优先等待隐形等待的时间。对强制等待没有影响。
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

# # 隐形等待
# driver.implicitly_wait(2)

driver.get('https://www.qq.com/')
# 显示等待：
element = WebDriverWait(driver, timeout=5, poll_frequency=0.5, ignored_exceptions=None).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="top-login"]/div[2]/a1')), "找不到")
if element:
    element.click()
else:
    print(element)
print(element)
# # 页面切换
# # 1.获取handle句柄的所有值
# handle = driver.window_handles
# print(handle)
# # 切换到要跳转的页面
# driver.switch_to.window(handle[1])
# # 内嵌frame标签的切换
# # 1.获取frame标签的属性
# frame = driver.find_element(By.ID, 'login_frame')
# # 2.跳转到frame里面的html页面
# driver.switch_to.frame(frame)
# # 进行密码登录
# driver.find_element(By.XPATH, '//*[@id="u"]').send_keys('1026083938')
# driver.find_element(By.XPATH, '//*[@id="p"]').send_keys('boring0912')
# driver.find_element(By.XPATH, '//*[@id="login_button"]').click()
# # close()是关闭当前页面，quit（）是关闭浏览器
# driver.quit()
