# pytest是一个非常成熟的全功能的Python测试框架，主要特点如下： 1.简单灵活，容易上手，文档丰富： 2.支持参数化，可以细粒度地控制要测试的测试用例：
# 3.能够支持简单的单元测试和复杂的功能测试，还可以用做selenium/appium 等自动化测试、接口自动化测试 (pytest-requests)；
# 4.pytest具有很多第三方插件，并且可以自定义扩展，比较好用的如pytest-selenium（ 集成selenium)
# 、pytest-html（完美html测试报告生成）、pytest-rerunfailures（失败case重复执行）、pytest-xdist pytest-xdist （多cpu并发）
# 5.测试用例的skip和xfail处理;
# 6. 可以很好的和CI工具结合，例如jenkins
# Pytest编写规则:
#
# 测试文件以test_开头（以_test为结尾）
# 测试的类以Test开头；
# 测试的方法以test_开头
# 断言使用基本的assert


# 通过pytest.raises()捕获测试用例可能抛出的异常
# def test_zero():
#     num = 0
#     with pytest.raises(ZeroDivisionError) as e
#          num = 1/0
#     exc_msg = e.value.args[0]
#     print(exc_msg)
import json
import os
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

print(os.path.dirname(__file__))


class TestLiWenDa:
    def setup_method(self, method):
        self.driver = webdriver.Chrome(executable_path="chromedriver")
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_liwenda(self):
        self.driver.implicitly_wait(6)
        self.driver.get("https://www.baidu.com/")
        self.driver.find_element(By.ID, "kw").send_keys("taobao")
        self.driver.find_element(By.ID, "su").click()
        self.driver.find_element(By.XPATH, '//*[@id="3001"]/div/div/div/div[1]/h3/div/a[1]').click()
        self.driver.close()

    # def div(self):
    #     return 1 / 0
    #
    # def test_name(self):
    #     a = 'division by zero'
    #     with pytest.raises(ZeroDivisionError) as e:  # 当不是异常时就抛出异常
    #         self.div()
    #     assert 'division by zero' in str(e.value)  # 设置断言使异常可以不抛出


# class TestFixture():
# data = json.loads(open('1.json', 'r').read())
#    执行顺序：
# 1• pytest我到以test开始或者结尼的py文件，再大找到以test开始的方法，并执行方法test_ user_pwd
# 2．执行该方法时发现传入的参数里有跟fixture中机同名字的users.
# 3. pytest认定 users是fixture，执行users方法，试收json文件并解析成python对象
# 4．才始真正执行test_user_pwd方法，users的返回值传入该方法
# # fixture允许 我们向fixture传递参数，参数必须是可迭代的对象（列表，元祖），对象有几条数据fixture就运行几次，相应测试用例就运行几次
# @pytest.fixture(params=data)
# def users(self, request):
#     return request.param
#
# def test_user(self, users):
#     a = users['ps']
#     assert len(a) >= 3

# # 给pytest用例传递参数并识别字符串的字符和eval类似，
# # mark.parametrize装饰器现象成为数据表格。
# @pytest.mark.parametrize('test_input,result', [("1+2", 3), ("2*3", 6), ("pow(2,3)", 8)])
# def test_eval(self, test_input, result):
#     assert eval(test_input) == result


# 测试用例报告生成
# 使用pytest-html包
# 应用 pytest   *.py --html=report.html
# 或者在pytest.main(['--html=./report.html', 'test-1.py'])
if __name__ == "__main__":
    pytest.main()
    # pytest.main(['--html=./report.html', 'test-1.py'])
