import time
import unittest

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver


class Public(object):
    def __init__(self, driver, url):
        self.driver = driver
        self.base_url = url
        self.action = ActionChains(self.driver)

    # 打开网页
    def Open_url(self):
        self.driver.get(self.base_url)

    # 获取元素
    def Find_element(self, *loc):
        self.driver.find_element(*loc)

    # 批量获取元素
    def Find_elements(self, *loc):
        self.driver.find_elements(*loc)

    # 元素点击
    def Click(self, *loc):
        self.driver.find_element(*loc).click()

    # 清除key值
    def ClearKey(self, *loc):
        self.driver.find_element(*loc).clear()

    # 输入框传值
    def Send_key(self, *args):
        self.driver.find_element(*args[0]).send_keys(args[1])

    # # 模拟鼠标移动显性等等
    # def Action_WaitElement(self, *args):
    #     element = WebDriverWait(self.driver, timeout=50, poll_frequency=0.5, ignored_exceptions=None).until(
    #         EC.presence_of_element_located((args[0])), "找不到该元素")
    #     if element:
    #         self.action.move_to_element(element).perform()
    #     else:
    #         print(element)

        # 模拟鼠标移动显性等等
    def Action_WaitElements(self, *args):
        element = WebDriverWait(self.driver, timeout=50, poll_frequency=0.5, ignored_exceptions=None).until(
            EC.presence_of_element_located((args[0])), "找不到该元素")
        if element:
            self.action.move_to_element(element).perform()
            self.action.click(element)
        else:
            print(element)

    # 元素显性等待
    def WaitElement(self, *args):
        element = WebDriverWait(self.driver, timeout=50, poll_frequency=0.5, ignored_exceptions=None).until(
            EC.presence_of_element_located((args[0])), args[1])
        if element:
            # self.driver.find_element(*args[0]).send_keys(args[1])
            self.driver.find_element(*args[0]).click()
        else:
            print(element)

        # 元素显性等待

    def WaitElements(self, *args):
        element = WebDriverWait(self.driver, timeout=50, poll_frequency=0.5, ignored_exceptions=None).until(
            EC.presence_of_all_elements_located((args[0])), args[1])
        if element:
            # self.driver.find_element(*args[0]).send_keys(args[1])
            self.driver.find_element(*args[0]).click()
        else:
            print(element)

    # def AssertEqual(self, *loc, num):
    #     if num == 1:
    #         self.assertEqual(self.driver.find_element(*loc[0]), loc[1], loc[2])
    #
    #     elif num == 2:
    #         self.assertWarns(self.driver.find_element(*loc[0]), loc[1], loc[2])
    # 弹窗或者页签切换
    def Switch_Window(self):
        win = self.driver.window_handles
        time.sleep(2)
        self.driver.switch_to.window(win[0])

    # 嵌入式网页切换
    def Frame_switch_window(self, *loc):
        iframe = WebDriverWait(self.driver, timeout=50, poll_frequency=0.5, ignored_exceptions=None).until(
            EC.presence_of_element_located((loc[0])), loc[1])
        if iframe:
            self.driver.switch_to.frame(iframe)
        else:
            print(iframe)

    # 元素截屏
    def ScreenShot(self, *loc):
        self.driver.find_element(*loc[0]).screenshot(loc[1])

    def Find_element_Text(self, *loc):
        text = self.driver.find_element(*loc).get_attribute('innerText')
        return text

    def Find_element_Class(self, *loc):
        text = self.driver.find_element(*loc).get_attribute('class')
        return text

    def Find_element_Is_Displayed(self, *loc):
        result = self.driver.find_element(*loc).is_displayed()
        return result
