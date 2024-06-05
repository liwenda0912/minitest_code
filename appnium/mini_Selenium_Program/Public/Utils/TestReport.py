import unittest
from HTMLTestRunner import HTMLTestRunner
import time


def report(*loc):
    print("-------------------开始自动化测试，并生成测试报告----------------------------")
    runs = unittest.defaultTestLoader.discover(loc[0], pattern=loc[1]+".py")
    filename = "自动化-" + time.strftime("%Y-%m-%d-%H-%M_%S") + r"-report.html"
    file = r"C:\Users\10260\PycharmProjects\soft-test-main\appnium\mini_Selenium_Program\test_report" + "\\"
    filename = file + filename
    with open(filename, 'wb') as f:
        runner = HTMLTestRunner(f, verbosity=2, title='示例测试报告', description='执行人:'+loc[2])
        runner.run(runs)
        print("-------------------自动化测试结束，并测试报告已生成-------------------------")
        print("报告位置目录路径：" + filename)




