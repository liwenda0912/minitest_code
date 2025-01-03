import keyword

from appnium.mini_Selenium_Program.Public.Utils.SqlalchemySqlUtils import SqlServer
from appnium.mini_Selenium_Program.Public.Utils.getResultUtils import getResultUtils
from appnium.mini_Selenium_Program.Public.conf.SqlConnectConf import Connect
from appnium.mini_Selenium_Program.Public.model import CommonResultBase, CommonTestCaseTotal


class resultServer(object):
    def __init__(self, **kwargs):
        self.session = Connect().sqlalchemy_()
        self.file = kwargs.get('file')
        self.time = kwargs.get('startTime')
        self.endTime = kwargs.get('endTime')

    def insert_(self):
        try:
            with open(self.file, "r", encoding="utf-8") as f:
                #  读取生成的测试报告
                report = f.readlines()
                result = getResultUtils.getTestResult(report)
                testName = getResultUtils.getTestName(report)
                detail = getResultUtils.getTestResult_detail(report)
                testPeople = getResultUtils.getTestPeopleName(report)
                totalDetail = getResultUtils.totalTestData(report)
                # 执行用例统计
                if len(totalDetail) > 0:
                    # 判断是否存在该用例
                    state_ = 1
                    data = None
                    SqlServer(self.session).add_(
                        model=CommonTestCaseTotal.CommonTestCaseTotalBase(totalDetail[0], totalDetail[1],
                                                                          totalDetail[2],
                                                                          totalDetail[3],
                                                                          totalDetail[4], state_, self.time,
                                                                          self.endTime))
                    TestCaseId = SqlServer(self.session).select_(
                        dict_={"testCaseName": totalDetail[0], "startTime": self.time},
                        model=CommonTestCaseTotal.CommonTestCaseTotalBase)
                    # 测试用例详情信息入库
                    print(TestCaseId[0].id)
                    for i in range(0, len(result)):
                        SqlServer(self.session).add_(
                            model=CommonTestCaseTotal.CommonResultBase(testName[i], detail[i], self.time, data,
                                                                       testPeople,
                                                                       result[i], 1, TestCaseId[0].id))
                    return "添加成功"
                else:
                    raise print("测试数据获取失败！")
        except Exception:
            self.session.rollback()
