import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from 运营平台自动化.pom.public.logincode import Login2
import time
from selenium import webdriver


class Adduser(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        Login2().test_login2(self.driver)
        self.action = ActionChains(self.driver)

    def test_adduser(self):
        # 显性等待，等待元素出现才进行操作，如果在秒50秒后元素没有出现就报错
        element_adduser = WebDriverWait(self.driver, timeout=50, poll_frequency=0.5, ignored_exceptions=None).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="wrapper"]/div[2]/nav/ul[1]/li[3]/a/span')), "找不到该元素")
        if element_adduser:
            self.action.move_to_element(element_adduser).perform()
        else:
            print(element_adduser)
        # 使用模拟鼠标移动和鼠标单击跳转到客户中心
        element1 = WebDriverWait(self.driver, timeout=50, poll_frequency=0.5, ignored_exceptions=None).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="wrapper"]/div[2]/nav/ul[1]/li[3]/ul[1]/li[1]/ul[1]/li[2]')), "找不到该元素")
        if element1:
            a = self.driver.find_element(By.XPATH, '//*[@id="wrapper"]/div[2]/nav/ul[1]/li[3]/ul[1]/li[1]/ul[1]/li[2]')
            self.action.move_to_element(a).perform()
            self.action.click(a).perform()
        else:
            print(element1)
        # 切换到嵌入的网页
        frame = WebDriverWait(self.driver, timeout=50, poll_frequency=0.5, ignored_exceptions=None).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="page-content"]/iframe[2]')), "找不到该iframe元素")
        if element1:
            self.driver.switch_to.frame(frame)
        else:
            print(frame)
        # 点击添加会员按钮
        useradd = self.driver.find_element(By.XPATH, '//*[@id="index"]/div[2]/div/div[2]/div/div[1]/div/button[1]')
        useradd.click()
        time.sleep(5)
        # 切换到弹窗窗口
        win = self.driver.window_handles
        time.sleep(2)
        self.driver.switch_to.window(win[0])
        # 切换到会员信息弹窗界面
        frame = self.driver.find_element(By.XPATH,
                                         '//*[@class="layui-layer layui-layer-iframe  layer-ext-adaptive"]/div['
                                         '2]/iframe[1]')
        self.driver.switch_to.frame(frame)
        # ---输入新增会员必填信息---
        # 显性等待，等待元素出现才进行操作，如果在秒10秒后元素没有出现就报错
        element2 = WebDriverWait(self.driver, timeout=10, poll_frequency=0.5, ignored_exceptions=None).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="addMember"]/form/div[1]/div[1]/div/input')), "找不到该元素")
        if element2:
            # 如果昵称的element0元素出现，就填写信息
            self.driver.find_element(By.XPATH, '//*[@id="addMember"]/form/div[1]/div[1]/div/input').send_keys('202384')
        else:
            print(element2)
        self.driver.find_element(By.XPATH, '//*[@id="addMember"]/form/div[1]/div[2]/div/input').send_keys('202384')
        self.driver.find_element(By.XPATH, '//*[@id="addMember"]/form/div[1]/div[5]/div/input').send_keys('15898112315')
        # 点击保存按钮
        self.driver.find_element(By.XPATH, '//*[@id="actions"]/button').click()
        # 测试断言判断

        if len(self.driver.find_element(By.XPATH, '//*[@id="addMember"]/form/div[1]/div[1]/div/input').text) == '':  # 输入的用户名为空的断言判断
            self.assertEqual(self.driver.find_element(By.XPATH, '//*[@id="addMember"]/form/div[1]/div[1]/div/input').text, '请输入用户名', '昵称为空时的提示语测试不通过')
        elif len(self.driver.find_element(By.XPATH, '//*[@id="addMember"]/form/div[1]/div[2]/div/input').text) == '':  # 输入密码为空的断言判断
            self.assertEqual(self.driver.find_element(By.XPATH, '//*[@id="addMember"]/form/div[1]/div[2]/div/input]').text, '请输入密码', '姓名为空时的提示语测试不通过')
        elif len(self.driver.find_element(By.XPATH, '//*[@id="addMember"]/form/div[1]/div[5]/div/input').text) == '':  # 输入验证码为空的断言判断
            self.assertEqual(self.driver.find_element(By.XPATH, '//*[@id="addMember"]/form/div[1]/div[5]/div/input]').text, '请输入正确的电话号码',
                             '电话号码为空时的提示语测试不通过')
        else:  # 填写数据都不为空时
            element = WebDriverWait(self.driver, timeout=10, poll_frequency=0.5, ignored_exceptions=None).until(
                EC.presence_of_element_located((By.XPATH, '//*[@class="layui-layer layui-layer-dialog layui-layer-border layui-layer-msg layui-layer-hui"]')),
                "找不到该元素")
            if element:
                # 如果昵称的element0元素出现，就填写信息
                if len(self.driver.find_element(By.XPATH,
                                                '//*[@class="layui-layer layui-layer-dialog layui-layer-border layui-layer-msg layui-layer-hui"]').text) == 10:  # 验证码错误的断言判断
                    self.assertEqual(self.driver.find_element(By.XPATH, '//*[@class="layui-layer layui-layer-dialog '
                                                                        'layui-layer-border layui-layer-msg '
                                                                        'layui-layer-hui"]').text, '请输入正确的电话号码',
                                     '测试不通过')
                elif len(self.driver.find_element(By.XPATH, '//*[@class="layui-layer layui-layer-dialog '
                                                            'layui-layer-border layui-layer-msg '
                                                            'layui-layer-hui"]').text) == 4:  # 登录成功的断言判断
                    self.assertEqual(self.driver.find_element(By.XPATH, '//*[@class="layui-layer layui-layer-dialog '
                                                                        'layui-layer-border layui-layer-msg '
                                                                        'layui-layer-hui"]').text, '操作失败', '测试不通过')
                else:
                    pass
            else:
                print(element2)

    def tearDown(self) -> None:
        pass


if __name__ == '__main__':
    suite = unittest.TestSuite()
    load_case = unittest.TestLoader().loadTestsFromTestCase(Adduser)
    suite.addTest(load_case)
    unittest.TextTestRunner().run(suite)
