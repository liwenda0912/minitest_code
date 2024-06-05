import os
import time
import unittest
from HTMLTestRunner import HTMLTestRunner


if __name__ == '__main__':
    # 被测试基本的路径
    # test_dir = './'
    test_dir = os.path.join(os.getcwd(), ".")
    # pattern脚本名称匹配规则
    discover = unittest.defaultTestLoader.discover(test_dir, pattern="s搜索.py")
    # 存放测试报告的文件夹
    report_dir = '.'
    # 报告命名格式化（当前时间）
    now = time.strftime('%Y-%m-%d %H%M%S')
    # 报告文件完整路径
    report_name = report_dir + '/' + now + 'result.html'
    # 打开文件再报告文件写入测试结果
    with open(report_name, 'wb') as f:
        runner = HTMLTestRunner(stream=f, title='Test Report', description='Test Case Result')
        runner.run(discover)

