import os
import time
import unittest
from HTMLTestRunner import HTMLTestRunner
from appnium.mini_Selenium_Program.Public.Utils.TestReport import report

if __name__ == '__main__':
    # # # suitt = unittest.TestSuite()
    # # # suitt.addTest(modify_UserMessage('test_modify_User_Message'))
    testfile = r"C:\Users\10260\PycharmProjects\soft-test-main\运营平台自动化\自动化项目"
    runs = unittest.defaultTestLoader.discover(testfile, pattern="test.py")
    filename = "自动化-" + time.strftime("%Y-%m-%d-%H-%M_%S") + r"-report.html"
    file = r"C:\Users\10260\PycharmProjects\soft-test-main\运营平台自动化\自动化项目" + "\\"
    filename = file + filename
    print(filename)
    with open(filename, 'wb') as f:
        runner = HTMLTestRunner(f, verbosity=2, title='示例测试报告', description='执行人：liwenda')
        runner.run(runs)

    # name = r"C:\Users\10260\PycharmProjects\soft-test-main\运营平台自动化\自动化项目"
    # report("test", testfile, "liwenda")
