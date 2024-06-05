import unittest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class Assert(unittest.TestCase):
    def assertTest(self, driver):
        self.driver = driver
        element_prompt = WebDriverWait(self.driver, timeout=50, poll_frequency=0.5).until(
            EC.presence_of_element_located((By.XPATH,
                                            '//*[@class="layui-layer layui-layer-dialog layui-layer-border layui-layer-msg layui-layer-hui"]')),
            '该元素找不到')
        if element_prompt:
            self.assertEqual(self.driver.find_element(By.XPATH,
                                                      '//*[@class="layui-layer layui-layer-dialog layui-layer-border layui-layer-msg layui-layer-hui"]').get_attribute(
                'innerText'), '保存成功', '保存失败')

        else:
            print(element_prompt)

    def assertTest_Send(self, driver):
        self.driver = driver
        element_prompt = WebDriverWait(self.driver, timeout=50, poll_frequency=0.5).until(
            EC.presence_of_element_located((By.XPATH,
                                            '//*[@class="layui-layer layui-layer-dialog layui-layer-border layui-layer-msg layui-layer-hui layui-anim layui-anim-00"]')),
            '该元素找不到')
        if element_prompt:
            self.assertEqual(self.driver.find_element(By.XPATH,
                                                      '//*[@class="layui-layer layui-layer-dialog layui-layer-border layui-layer-msg layui-layer-hui layui-anim layui-anim-00"]').get_attribute(
                'innerText'), '发放成功', '发放失败')
        else:
            print(element_prompt)
