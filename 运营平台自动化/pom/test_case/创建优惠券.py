import time
import unittest
from 运营平台自动化.pom.public.logincode import Login2
from selenium import webdriver
from selenium.webdriver.common.by import By
from 运营平台自动化.pom.public.public import Public
from 运营平台自动化.pom.public.Assert import Assert


class Coupon(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        Login2().test_login2(self.driver)
        self.url = ''
        self.PUBLIC = Public(self.driver, self.url)

    def test_grant(self):
        # 显性等待，等待元素出现才进行操作，如果在秒50秒后元素没有出现就报错
        self.PUBLIC.Action_WaitElements((By.XPATH, '//*[@id="wrapper"]/div[2]/nav/ul[1]/li[2]/a/span'), '无法点击资源中心')
        # 访问优惠券管理界面
        self.PUBLIC.WaitElement((By.XPATH, '//*[@id="wrapper"]/div[2]/nav/ul[1]/li[2]/ul/li[2]/ul/li[3]'), '无法访问优惠券管理')
        # 切换到嵌入的网页
        self.PUBLIC.Frame_switch_window((By.XPATH, '//*[@id="page-content"]/iframe[2]'), '找不到该iframe元素')
        time.sleep(3)
        self.PUBLIC.Click(By.XPATH, '//*[@id="favourablecampaignRule"]/div/div[2]/div/div[1]/div/button')
        self.PUBLIC.Switch_Window()
        # 切换到弹窗窗口
        self.PUBLIC.Frame_switch_window((By.XPATH, '//*[@id="layui-layer-iframe1"]'), "找不到该iframe元素")
        self.PUBLIC.Send_key((By.XPATH, '//*[@id="prize"]/div/div/form/div[1]/div[2]/div/input'), '9-18-1')
        # 选择优惠券类型为电费，label[1]：1为电费抵扣，2为服务费抵扣，3为电费+服务费，默认是服务费
        self.PUBLIC.Click(By.XPATH, '//*[@id="prize"]/div/div/form/div[1]/div[3]/div/label[1]/span[1]/span')
        # 选择优惠方式为随机:label[1],1为固定满减，2为随机满减，3为固定折扣，4为随机扣减，默认是固定减满
        # self.PUBLIC.Click(By.XPATH, '//*[@id="prize"]/div/div/form/div[2]/div[2]/div/div/label[2]/span[2]')
        # self.PUBLIC.ClearKey(By.XPATH, '//*[@id="prize"]/div/div/form/div[2]/div[3]/div/div/input')
        self.PUBLIC.ClearKey(By.XPATH, '//*[@id="prize"]/div/div/form/div[2]/div[3]/div/div/input')
        # 减满条件：例如满多少钱使用
        self.PUBLIC.Send_key((By.XPATH, '//*[@id="prize"]/div/div/form/div[2]/div[3]/div/div/input'), '10')
        self.PUBLIC.Send_key((By.XPATH, '//*[@id="prize"]/div/div/form/div[2]/div[5]/div/div/input'), '2')
        # 使用时效类型,label[1]:1为使用时间范围，2为天，默认为1
        if self.driver.find_element(By.XPATH, '//*[@id="prize"]/div/div/form/div[3]/div[2]/div/label[1]').get_attribute(
                'class') == 'el-radio el-radio--small is-bordered is-checked':
            self.driver.execute_script('window.scrollTo(0,1229.560)')
            self.PUBLIC.Send_key((By.XPATH,
                                 '//*[@id="prize"]/div/div/form/div[3]/div[3]/div[1]/div/input'), '2023-08-29 00:00:00')
            # 结束时间
            self.PUBLIC.Click(By.XPATH, '//*[@id="prize"]/div/div/form/div[3]/div[3]/div[2]/div')
            self.PUBLIC.Send_key((By.XPATH, '//*[@id="prize"]/div/div/form/div[3]/div[3]/div[2]/div/input'), '2023-09-30 23:59:59')
            self.PUBLIC.Click(By.XPATH, '/html/body/div[7]/div[2]/button[2]')
        else:
            self.PUBLIC.Send_key((By.XPATH, '//*[@id="prize"]/div/div/form/div[3]/div[3]/div/div'), '10')
        # 使用时段,label[1]:1为全天优惠，2为分时优惠，默认是全天优惠
        self.PUBLIC.WaitElement((By.XPATH, '//*[@id="prize"]/div/div/form/div[3]/div[6]/div/label[3]'), '该元素找不到')
        # 优惠叠加,label[1]:1为可叠加，2为不可叠加使用，默认为不可叠加使用
        self.PUBLIC.Click(By.XPATH,
                          '//*[@id="prize"]/div/div/form/div[3]/div[7]/div[1]/label[1]/span[1]/span')
        # 保存按钮点击
        self.PUBLIC.Click(By.XPATH, '//*[@id="actions"]/button')
        time.sleep(2)
        self.PUBLIC.Click(By.XPATH, '//*[@class="layui-layer layui-layer-dialog"]/div[3]/a[1]')
        Assert().assertTest(self.driver)

    def tearDown(self) -> None:
        self.driver.close()


if __name__ == '__main__':
    unittest.main()


# def OldCode:
# element_operation_center = WebDriverWait(self.driver, timeout=50, poll_frequency=0.5,
#                                          ignored_exceptions=None).until(
#     EC.presence_of_element_located((By.XPATH, '//*[@id="wrapper"]/div[2]/nav/ul[1]/li[2]/a/span')), "找不到该元素")
# if element_operation_center:
#     self.action.move_to_element(element_operation_center).perform()
# else:
#     print(element_operation_center)
# element_coupon_manage = WebDriverWait(self.driver, timeout=50, poll_frequency=0.5,
#                                       ignored_exceptions=None).until(
#     EC.presence_of_element_located((By.XPATH, '//*[@id="wrapper"]/div[2]/nav/ul[1]/li[2]/ul/li[2]/ul/li[3]')),
#     '该元素没有在element界面')
# if element_coupon_manage:
#     self.action.move_to_element(element_coupon_manage).perform()
#     self.action.click(element_coupon_manage).perform()
# else:
#     print(element_coupon_manage)
# time.sleep(3)
# frame = WebDriverWait(self.driver, timeout=50, poll_frequency=0.5, ignored_exceptions=None).until(
#     EC.presence_of_element_located((By.XPATH, '//*[@id="page-content"]/iframe[2]')), "找不到该iframe元素")
# if frame:
#     self.driver.switch_to.frame(frame)
# else:
#     print(frame)
# self.driver.find_element(By.XPATH, '//*[@id="favourablecampaignRule"]/div/div[2]/div/div[1]/div/button').click()
# win = self.driver.window_handles
# time.sleep(2)
# self.driver.switch_to.window(win[0])
# iframe = WebDriverWait(self.driver, timeout=50, poll_frequency=0.5, ignored_exceptions=None).until(
#     EC.presence_of_element_located((By.XPATH, '//*[@id="layui-layer-iframe1"]')), "找不到该iframe元素")
# if iframe:
#     self.driver.switch_to.frame(iframe)
# else:
#     print(iframe)
# self.driver.find_element(By.XPATH, '//*[@id="prize"]/div/div/form/div[1]/div[2]/div/input').send_keys(
#     '9-18-1')
# self.driver.find_element(By.XPATH, '//*[@id="prize"]/div/div/form/div[1]/div[3]/div/label[1]/span[1]/span').click()
# self.driver.find_element(By.XPATH, '//*[@id="prize"]/div/div/form/div[2]/div[2]/div/div/label[2]/span[2]').click()
# self.driver.find_element(By.XPATH, '//*[@id="prize"]/div/div/form/div[2]/div[3]/div/div/input').clear()
# self.driver.find_element(By.XPATH, '//*[@id="prize"]/div/div/form/div[2]/div[3]/div/div/input').send_keys(
#     '10')
# self.driver.find_element(By.XPATH, '//*[@id="prize"]/div/div/form/div[2]/div[5]/div/div/input').send_keys('2')
# self.driver.find_element(By.XPATH, '//*[@id="prize"]/div/div/form/div[3]/div[2]/div/label[1]/span[2]').click()
# self.driver.find_element(By.XPATH,
#                          '//*[@id="prize"]/div/div/form/div[3]/div[3]/div[1]/div/input').send_keys(
#     '2023-08-29 00:00:00')
# self.driver.find_element(By.XPATH, '//*[@id="prize"]/div/div/form/div[3]/div[3]/div[2]/div').click()
# self.driver.find_element(By.XPATH,
#                          '//*[@id="prize"]/div/div/form/div[3]/div[3]/div[2]/div/input').send_keys(
#     '2023-09-30 23:59:59')
# self.driver.find_element(By.XPATH, '/html/body/div[7]/div[2]/button[2]').click()
# self.driver.find_element(By.XPATH, '//*[@id="prize"]/div/div/form/div[3]/div[3]/div/div').send_keys(
#     '10')
# self.driver.find_element(By.XPATH, '//*[@id="p rize"]/div/div/form/div[3]/div[4]/div/label[1]/span[2]').click()
# element_coupon_manage_site = WebDriverWait(self.driver, timeout=50, poll_frequency=0.5).until(
#     EC.presence_of_element_located((By.XPATH, '//*[@id="prize"]/div/div/form/div[3]/div[6]/div/label[3]')),
#     '该元素找不到')
# if element_coupon_manage_site:
#     # 使用站点,label[1]:1为自营站点，2为指定站点，3为所有充电站，默认为自营站点
#     self.driver.find_element(By.XPATH,
#                              '//*[@id="prize"]/div/div/form/div[3]/div[6]/div/label[3]').click()
#
# else:
#     print(element_coupon_manage_site)
# self.driver.find_element(By.XPATH,
#                          '//*[@id="prize"]/div/div/form/div[3]/div[7]/div[1]/label[1]/span[1]/span').click()
# time.sleep(2)
# self.driver.find_element(By.XPATH, '//*[@id="actions"]/button').click()
# self.driver.find_element(By.XPATH, '//*[@class="layui-layer layui-layer-dialog"]/div[3]/a[1]').click()
