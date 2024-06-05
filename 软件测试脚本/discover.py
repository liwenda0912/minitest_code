import os
import time
import unittest
from HTMLTestRunner import HTMLTestRunner
filename = time.strftime("%Y-%m-%d-%H-%M_%S")+r".html"
file = os.path.dirname(__file__)+'\\测试结果\\'
filename = file+filename
runs = unittest.defaultTestLoader.discover('p',pattern="*.py")
re = unittest.TestResult()
print(re.__dict__)
with open(r'D:\PycharmProjects\软件测试脚本\2022-08-19 184846result.html', 'wb') as f:
    runner = HTMLTestRunner(f, verbosity=2, title='示例测试报告', description='执行人：liwenda')
    runner.run(runs)
# with open(filename, 'a') as f:
#     runner = unittest.TextTestRunner(f, descriptions='测试报告', verbosity=2)
#     runner.run(runs)
