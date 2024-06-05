import os
import time
import unittest
from HTMLTestRunner import HTMLTestRunner
import requests
from 软件测试脚本.very自动化项目.public.Login import Login
from selenium import webdriver
from selenium.webdriver.common.by import By


class Modify_UserMessage(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        Login().open1(self.driver)
        self.driver.implicitly_wait(5)
        time.sleep(2)

    def test_modify_User_Message(self):
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH, '//*[@id="usermenu"]/li[2]/a').click()
        self.driver.find_element(By.XPATH, '//*[@id="nickname"]').clear()
        self.driver.find_element(By.XPATH, '//*[@id="nickname"]').send_keys('li')
        self.driver.find_element(By.XPATH, '//*[@id="qq"]').clear()
        self.driver.find_element(By.XPATH, '//*[@id="qq"]').send_keys('12345678')
        self.driver.find_element(By.XPATH, '//*[@id="profile-form"]/dl[3]/dd/label[2]/input').click()
        self.driver.find_element(By.XPATH, '//*[@id="birth_year"]/option[77]').click()
        self.driver.find_element(By.XPATH, '//*[@id="birth_month"]/option[8]').click()
        self.driver.find_element(By.XPATH, '//*[@id="birth_day"]/option[2]').click()
        self.driver.find_element(By.XPATH, '//*[@id="signature"]').clear()
        self.driver.find_element(By.XPATH, '//*[@id="signature"]').send_keys('12345678')
        self.driver.find_element(By.XPATH, '//*[@id="profile-form"]/div/button').click()
        time.sleep(2)
        self.assertEqual(self.driver.find_element(By.XPATH, '//*[@id="nickname"]').get_attribute('value'), 'li', '测试不通过')

    def tearDown(self) -> None:
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
