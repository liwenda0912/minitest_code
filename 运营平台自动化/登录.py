import cv2
import time
import unittest
import requests
import pytesseract
from PIL import Image
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from PIL import Image


# 图片处理函数
def handle_img():
    # 打开图片
    img = cv2.imread("1.png")
    # 灰度
    img = cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY)
    # 减低线噪
    h, w = img.shape[:2]
    for i in range(1, w - 1):
        for j in range(1, h - 1):
            count = 0
            if img[j, i - 1] > 245:
                count = count + 1
            if img[j, i + 1] > 245:
                count = count + 1
            if img[j - 1, i] > 245:
                count = count + 1
            if img[j + 1, i] > 245:
                count = count + 1
            if count > 2:
                img[j, i] = 255
    # 闭运算
    k = cv2.getStructuringElement(cv2.MORPH_RECT, (2, 3))  # 定义结构元素
    o = cv2.morphologyEx(img, cv2.MORPH_OPEN, k)
    c = cv2.morphologyEx(img, cv2.MORPH_CLOSE, k)
    # cv2.imshow('1', C)
    # cv2.waitKey()
    # cv2.destroyAllWindows()
    cv2.imwrite('3.png', c)


class Public_login:
    def public_login(self, driver):
        self.driver = driver
        self.driver.maximize_window()
        self.url = 'http://172.16.0.17:8303/user/evking_login'
        self.driver.get(self.url)
        # 填写登录账号
        self.driver.find_element(By.XPATH, '//*[@id="username"]').click()
        self.driver.find_element(By.XPATH, '//*[@id="username"]').send_keys('15767112315')
        # 填写登录密码
        self.driver.find_element(By.XPATH, '//*[@id="pwd"]').click()
        self.driver.find_element(By.XPATH, '//*[@id="pwd"]').send_keys('da091234')
        # 处理验证码图片
        while True:
            # 获取验证码
            self.driver.find_element(By.XPATH, '//*[@id="refreshCheckcode"]/span/i').click()
            time.sleep(2)
            self.driver.find_element(By.XPATH, '//*[@id="imgcheckcode"]').screenshot('1.png')
            handle_img()
            img = Image.open('3.png')
            crop = img.crop((10, 0, 116, 33))
            crop.save('4.png')
            # 验证码识别
            text = pytesseract.image_to_string(crop)
            text = text.strip()
            # 填写验证码
            self.driver.find_element(By.XPATH, '//*[@id="checkcode"]').click()
            self.driver.find_element(By.XPATH, '//*[@id="checkcode"]').clear()
            self.driver.find_element(By.XPATH, '//*[@id="checkcode"]').send_keys(text)
            self.driver.find_element(By.XPATH, '//*[@id="login"]').click()
            time.sleep(2)
            if self.driver.find_element(By.XPATH, '//*[@class="layui-layer layui-layer-dialog '
                                                  'layui-layer-border layui-layer-msg '
                                                  'layui-layer-hui"]').get_attribute('innerText') == '登录成功':
                break
                # if self.driver.find_element(By.XPATH, '//*[@id="username"]').text) == '':  # 输入的用户名为空的断言判断
                #     self.assertEqual(self.driver.find_element(By.XPATH, '//*[@id="username"]').text, '请输入用户名',
                #                      '账户为空时的提示语测试不通过')
                #     break
                # elif self.driver.find_element(By.XPATH, '//*[@id="pwd"]').text) == '':  # 输入密码为空的断言判断
                #     self.assertEqual(self.driver.find_element(By.XPATH, '//*[@id="pwd"]').text, '请输入密码',
                #                      '密码为空时的提示语测试不通过')
                #     break
                # elif self.driver.find_element(By.XPATH, '//*[@id="checkcode"]').text) == '':  # 输入验证码为空的断言判断
                #     self.assertEqual(self.driver.find_element(By.XPATH, '//*[@id="checkcode"]').text, '请输入验证码',
                #                      '验证码为空时的提示语测试不通过')
                #     break
                # else:  # 填写数据都不为空时
                #     pass
                # if len(self.driver.find_element(By.XPATH, '//*[@class="layui-layer layui-layer-dialog '
                #                                           'layui-layer-border layui-layer-msg '
                #                                           'layui-layer-hui"]').text) == 5:  # 验证码错误的断言判断
                #     self.assertEqual(self.driver.find_element(By.XPATH, '//*[@class="layui-layer layui-layer-dialog '
                #                                                         'layui-layer-border layui-layer-msg '
                #                                                         'layui-layer-hui"]').text, '验证码错误', '请重新启动')
                # elif len(self.driver.find_element(By.XPATH, '//*[@class="layui-layer layui-layer-dialog '
                #                                             'layui-layer-border layui-layer-msg '
                #                                             'layui-layer-hui"]').text) == 4:  # 登录成功的断言判断
                #     self.assertEqual(self.driver.find_element(By.XPATH, '//*[@class="layui-layer layui-layer-dialog '
                #                                                         'layui-layer-border layui-layer-msg '
                #                                                         'layui-layer-hui"]').text, '登录成功', '测试不通过')
                # else:  # 密码或者账号错误断言判断
                #     self.assertEqual(self.driver.find_element(By.XPATH, '//*[@class="layui-layer layui-layer-dialog '
                #                                                         'layui-layer-border layui-layer-msg '
                #                                                         'layui-layer-hui"]').text, '用户密码错误！登录次数还剩4次',
                #                      '测试不通过')

        # print(self.driver.find_element(By.XPATH, '//*[@id="username"]').text,
        #       self.driver.find_element(By.XPATH, '//*[@id="pwd"]').text,
        #       self.driver.find_element(By.XPATH, '//*[@id="checkcode"]').text)


class Login(unittest.TestCase):

    def setUp(self) -> None:
        pass

    # def test_login1(self):
    #     self.driver = webdriver.Chrome()

    def test_login(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.url = 'http://172.16.0.17:8303/user/evking_login'
        self.driver.get(self.url)
        # 填写登录账号
        self.driver.find_element(By.XPATH, '//*[@id="username"]').click()
        self.driver.find_element(By.XPATH, '//*[@id="username"]').send_keys('15767112315')
        # 填写登录密码
        self.driver.find_element(By.XPATH, '//*[@id="pwd"]').click()
        self.driver.find_element(By.XPATH, '//*[@id="pwd"]').send_keys('da091234')
        # 处理验证码图片
        while True:
            # 获取验证码
            self.driver.find_element(By.XPATH, '//*[@id="refreshCheckcode"]/span/i').click()
            time.sleep(2)
            self.driver.find_element(By.XPATH, '//*[@id="imgcheckcode"]').screenshot('1.png')
            handle_img()
            img = Image.open('3.png')
            crop = img.crop((10, 0, 116, 33))
            crop.save('4.png')
            # 验证码识别
            text = pytesseract.image_to_string(crop)
            text = text.strip()
            # 填写验证码
            self.driver.find_element(By.XPATH, '//*[@id="checkcode"]').click()
            self.driver.find_element(By.XPATH, '//*[@id="checkcode"]').clear()
            self.driver.find_element(By.XPATH, '//*[@id="checkcode"]').send_keys(text)
            self.driver.find_element(By.XPATH, '//*[@id="login"]').click()
            time.sleep(2)
            if self.driver.find_element(By.XPATH, '//*[@class="layui-layer layui-layer-dialog '
                                                  'layui-layer-border layui-layer-msg '
                                                  'layui-layer-hui"]').get_attribute('innerText') == '登录成功':
                break
                # if self.driver.find_element(By.XPATH, '//*[@id="username"]').text == '':  # 输入的用户名为空的断言判断
                #     self.assertEqual(self.driver.find_element(By.XPATH, '//*[@id="username"]').text, '请输入用户名',
                #                      '账户为空时的提示语测试不通过')
                #     break
                # elif self.driver.find_element(By.XPATH, '//*[@id="pwd"]').text == '':  # 输入密码为空的断言判断
                #     self.assertEqual(self.driver.find_element(By.XPATH, '//*[@id="pwd"]').text, '请输入密码','密码为空时的提示语测试不通过')
                #     break
                # elif self.driver.find_element(By.XPATH, '//*[@id="checkcode"]').text == '':  # 输入验证码为空的断言判断
                #     self.assertEqual(self.driver.find_element(By.XPATH, '//*[@id="checkcode"]').text, '请输入验证码',
                #                      '验证码为空时的提示语测试不通过')
                #     break
                # else:  # 填写数据都不为空时
                #     pass
                # if len(self.driver.find_element(By.XPATH, '//*[@class="layui-layer layui-layer-dialog '
                #                                           'layui-layer-border layui-layer-msg '
                #                                           'layui-layer-hui"]').text) == 5:  # 验证码错误的断言判断
                #     self.assertEqual(self.driver.find_element(By.XPATH, '//*[@class="layui-layer layui-layer-dialog '
                #                                                         'layui-layer-border layui-layer-msg '
                #                                                         'layui-layer-hui"]').text, '验证码错误', '请重新启动')
                # elif len(self.driver.find_element(By.XPATH, '//*[@class="layui-layer layui-layer-dialog '
                #                                             'layui-layer-border layui-layer-msg '
                #                                             'layui-layer-hui"]').text) == 4:  # 登录成功的断言判断
                #     self.assertEqual(self.driver.find_element(By.XPATH, '//*[@class="layui-layer layui-layer-dialog '
                #                                                         'layui-layer-border layui-layer-msg '
                #                                                         'layui-layer-hui"]').text, '登录成功', '测试不通过')
                # else:  # 密码或者账号错误断言判断
                #     self.assertEqual(self.driver.find_element(By.XPATH, '//*[@class="layui-layer layui-layer-dialog '
                #                                                         'layui-layer-border layui-layer-msg '
                #                                                         'layui-layer-hui"]').text, '用户密码错误！登录次数还剩4次',
                #                      '测试不通过')

    def tearDown(self) -> None:
        result = 1
        pass

# if __name__ == '__main__':
#     unittest.main()
