import sys
import unittest
from HTMLTestRunner import HTMLTestRunner
import time
from BeautifulReport import BeautifulReport as bf
from appnium.mini_Selenium_Program.Public.Server.resultServer import  resultServer
from appnium.mini_Selenium_Program.Public.Utils.timeUtils.timeTransform import Transform
from appnium.mini_Selenium_Program.Public.common.Logger.Logger import Logger


def report(*loc):
    Logger(stream=sys.stdout).info("-------------------开始自动化测试，并生成测试报告----------------------------")
    runs = unittest.defaultTestLoader.discover(loc[0], pattern=loc[1]+".py")
    Logger(stream=sys.stdout).info("执行文件名为："+loc[1]+".py")
    startTime = time.strftime("%Y-%m-%d %H:%M:%S")
    time_ = time.strftime("%Y-%m-%d %H-%M-%S")
    filename = "ui自动化-" +time_+ r"-report.html"
    file = r"C:\Users\10260\PycharmProjects\soft-test-main\appnium\mini_Selenium_Program\test_report" + "\\"
    filename = file + filename
    # with open("res.txt", "w", encoding="utf-8") as file:
    #     runners = unittest.TextTestRunner(stream=file, verbosity=2)
    #     runners.run(runs)
    with open(filename, 'wb') as f:
        runner = HTMLTestRunner(f, verbosity=2, title=loc[1]+'测试报告', description='执行人:'+loc[2])
        runner.run(runs)

        Logger(stream=sys.stdout).info("-------------------自动化测试结束，并测试报告已生成-------------------------")
        Logger(stream=sys.stdout).info("报告位置目录路径：" + filename)
    endTime = time.strftime("%Y-%m-%d %H:%M:%S")
    resultServer(file=filename, startTime=Transform.encode_time(startTime), endTime=Transform.encode_time(endTime)).insert_()






