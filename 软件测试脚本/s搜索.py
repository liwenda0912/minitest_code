# -*- coding: utf-8 -*-
import os
from datetime import datetime

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from HTMLTestRunner import HTMLTestRunner
import unittest, time, re


class Taobao(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='chromedriver')
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_taobao(self):
        name = '淘宝'
        driver = self.driver
        driver.get(
            "https://www.baidu.com/s?wd=%E6%9D%8E%E6%96%87%E8%BE%BE&rsv_spt=1&rsv_iqid=0x95014bd900003160&issp=1&f=3&rsv_bp=1&rsv_idx=2&ie=utf-8&tn=baiduhome_pg&rsv_enter=1&rsv_dl=ih_1&rsv_sug3=1&rsv_sug1=1&rsv_sug7=001&rsv_sug2=1&rsv_btype=i&rsp=1&rsv_sug9=es_2_1&rsv_sug4=1176&rsv_sug=9")
        driver.find_element(By.XPATH, "//img[@alt='到百度首页']").click()
        driver.get("https://www.baidu.com/")
        driver.find_element(By.CSS_SELECTOR, '#kw').send_keys(name)
        driver.find_element(By.XPATH, '//*[@id="su"]').click()
        self.assertEqual("百度为您找到相关结果约100,000,0000个",
                         driver.find_element(By.XPATH, "//div[@id='tsn_inner']/div[2]/span").text, '断言失败')  # 断言判断
        driver.find_element(By.XPATH, '//*[@id="3001"]/div/div[1]/div/div/h3/div/a[1]').click()
        driver.get(
            "https://uland.taobao.com/sem/tbsearch?refpid=mm_26632258_3504122_32538762&keyword=%E6%B7%98%E5%AE%9D&clk1=c486cc775021d2acc4d5857795591106&upsId=c486cc775021d2acc4d5857795591106")
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | win_ser_1 | ]]
        driver.find_element(By.ID, "J_search_key").click()
        driver.find_element(By.XPATH, "//input[@value='搜索']").click()

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


# def report():
#     name = './' + '123.html'
#     with open(name, 'wb')as f:
#         suite = unittest.TestSuite()  # 创建测试套件，将测试用例添加至套件中  TestSuite测试集
#         suite.addTest(Taobao)# 生成测试报告
#         runner = HTMLTestRunner(stream=f, title='雇员涨薪', description='雇员信息执行结果')
#         runner.run(suite)
#         f.close()
# class report:
#     import os
#     print("done")
#     report = os.path.join(r'D:\PycharmProjects\软件测试脚本\2022-08-19 184846result.html')
#     st = unittest.TestSuite()
#     st.addTests([Taobao('test_taobao')])
#     with open(r'D:\PycharmProjects\软件测试脚本\2022-08-19 184846result.html', 'wb') as f:
#         runner = HTMLTestRunner(f, verbosity=2, title='示例测试报告', description='执行人：liwenda')
#         runner.run(st)


if __name__ == "__main__":
    # unittest.main()
    suitt = unittest.TestSuite()
    suitt.addTest(Taobao('test_taobao'))
    with open(r'D:\PycharmProjects\软件测试脚本\测试结果\2022-08-19 184846result.html', 'wb') as f:
        runner = HTMLTestRunner(f, verbosity=2, title='示例测试报告', description='执行人：liwenda')
        runner.run(suitt)
