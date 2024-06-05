from selenium import webdriver
from selenium.webdriver.common.by import By
import os


def a(*args):
    print("绝对路径" + os.path.abspath("__file__"), "当前目录：" + os.getcwd())
    driver = webdriver.Chrome()
    url = 'https://www.baidu.com'
    driver.get(url)
    driver_obj = (By.XPATH, '//*[@id="kw"]')
    print(driver_obj)
    driver.find_element(a)

