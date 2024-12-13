import logging
import re

import requests

from appnium.mini_Selenium_Program.Public.Utils.IsSpaceUtils import isSpace, isNotEmpty
from appnium.mini_Selenium_Program.Public.Utils.SqlalchemySqlUtils import SqlServer
from appnium.mini_Selenium_Program.Public.conf.SqlConnectConf import Connect
from appnium.mini_Selenium_Program.Public.model import TestResultBase
from appnium.mini_Selenium_Program.test_report.report.TestReport import report


# if __name__ == '__main__':
# session = Connect().sqlalchemy_()
#
#     """ <------------getattr--->定义查询过滤器的字典"""
#     #     # filter_dict = {
#     #     #     'city': '广州',
#     #     #     'address': '广州'
#     #     # }
#     #     # # 构建查询过滤器
#     #     # query = session.query(TestResultBase.TestResultBase)
#     #     # for key, value in filter_dict.items():
#     #     #     query = query.filter(getattr(TestResultBase.TestResultBase, key) == value)
#     #     #     print(getattr(TestResultBase.TestResultBase, key) == value)
#     #     # 执行查询并打印结果
#     #     # result = query.all()
#     #     # for user in result:
#     #     #     print(f"Name: {user.username}, Age: {user.password}")
#     #
#
#     '''<-----------------------根据id取查--------------------------------->'''
#     #     # user_ = session.query(TestResultBase.TestResultBase).filter_by(id=1).all()
#     #     # for item in user_:
#     #     #     print(item.username)
#     #     d = {"city": "广州", "address": "广州"}
#     #     # delete删除
#
# if SqlServer(session).delete_(dict_={"id": "8"}, model=TestResultBase.TestResultBase) == 1:
#     #     print("删除成功")
#     #     # print(session.query(TestResultBase.TestResultBase).filter_by(id=1).update({'username': "Jack", "password": "222222"}))
#     #     # session.commit()
#     #     # if SqlServer(session).update_(dict_={"city": "广州", "address": "广州"}, model=TestResultBase.TestResultBase,
#     #     #                               where={'username': "Jack", "password": "55552"}) == 1:
#     #     #     print("更新成功")
#     #     a = "lw", "888888888", "广州", "51545555", "", "广州", "广东", 55555, "2024-09-26 17:25:55"
#     #     SqlServer(session).add_(model=TestResultBase.TestResultBase("lw8888", "888888888", "广州", "51545555", "", "广州", "广东", 55555, current_time), values=a)
#     #     # insert增加
#     SqlServer(session).add_(model=TestResultBase.TestResultBase("lw0855", "888888888", "广州", "51545555", "", "广州", "广东", 55555, "2024-09-26 17:25:55"))
#     #     # update更新
#     #     # use = SqlServer(session).update_(select(TestResultBase.TestResultBase).where(TestResultBase.TestResultBase.username.in_(["lw0"])))
#     #     # select搜素
#     data = SqlServer(session).select_(dict_={"address": "广州"}, model=TestResultBase.TestResultBase)
#     print(data)
# #     user = SqlServer(session).select_(select(TestResultBase.TestResultBase).where(TestResultBase.TestResultBase.username.in_(["lw0", "zwj"])))
# #     # u = SqlServer(session).get_(TestResultBase.TestResultBase,1)
# # use = session.scalars(select(TestResultBase.TestResultBase).where(TestResultBase.TestResultBase.username.in_(["lw", "zwj"])))
# #     # session.commit()
# #     # print(u)
# #     #     # 添加
#     user = TestResultBase.TestResultBase
#     add_user = user("lw s", "888888888", "广州", "51545555", "", "广州", "广东", 55555, " ")
#     print(session.add(add_user))
# #
#

# def getTestName(a):
#     TestName = []
#     for i in a:
#         if "<div class='testcase'>" in i:
#             for j in re.split("<.*?><div class='testcase'>",i):
#                 for name in j.split("</div></td>\n"):
#                     if name is not None and name != '' and name != '    ':
#                         TestName.append(name)
#     return TestName
#
#
# def getTestResult(a):
#     result_ = []
#     for i in a:
#         if "button" and "btn btn-danger btn-xs collapsed" in i:
#             for result in re.split(r'<.*?>', i):
#                 if result != '\n' and result != '    ':
#                     result_.append(result)
#     return result_
#
#
# def getTestName_(a):
#     textName = []
#     for i in a:
#         if "测试人员 : " in i:
#             print(re.split(r'<.*?>', i))
#             for text in re.split(r'<.*?>', i):
#                 if text != '\n' and text != '':
#                     textName.append(text)
#             return "".join(textName)
#
#
# def getTestResult_detail(a):
#     totalDetail = []
#     startIndex = []
#     for i in a:
#         if "collapse in" in i:
#             startIndex.append(a.index(i))
#     s = []
#     for index in range(0, len(startIndex)):
#         for j in range(startIndex[index] + 2, 100000):
#             if "</pre>" in a[j]:
#                 break
#             else:
#                 if a[j] != '\n':
#                     for text in a[j].split('\n'):
#                         print(text)
#                         if text != "" and text != '    ':
#                             for text_ in text.split('\n'):
#                                  s.append(text_)
#         totalDetail.append("".join(s))
#         s.clear()
#     return totalDetail
#
#
# def totalTestData(a):
#     startIndex = []
#     totalDetail_ = []
#     for i in a:
#         if " warning" in i:
#             startIndex.append(a.index(i))
#     for index in range(0, len(startIndex)):
#         for j in range(startIndex[index] + 1, 100000):
#             if "</tr>" in a[j]:
#                 break
#             else:
#                     for text in re.split("<.*?>", a[j]):
#                         if text != "" and text != '    ' and text != '\n':
#                             if text != "详细" and '收起':
#                                 totalDetail_.append(text)
#     return totalDetail_
#
# 正序排序
# def sort():
#     list_ = [1, 5, 10, 2, 6]
#     for i in range(len(list_)):
#         for j in range(len(list_) - i - 1):
#             print(j,j+1)
#             if list_[j] > list_[j+1]:
#                 list_[j],list_[j+1] = list_[j+1],list_[j]
#         print(list_)
# 倒叙排序
def sort():
    list_list = [1, 5, 8, 6, 7]
    for i in range(len(list_list)):
        for j in range(len(list_list)):
            if list_list[i] > list_list[j]:
                list_list[i], list_list[j] = list_list[j], list_list[i]
        print(list_list)


if __name__ == '__main__':
    url = "http://a.openapi.evking.com.cn/api/chargeStation/page"
    data = {"pageNo": 1,
            "pageSize": 10}
    params= {}
    headers = {
        "accept": "application/json, text/plain, */*",
        "Utoken": "23FBC13E3B12894BF371539C0FD13326",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0"
    }
    s = requests.request(url=url, headers=headers, json=data, method="post",params=params)
    j = s.json()
    print(j)
    print(j.get("data").get("total"))

    # text = ['', '    ',  '          ', "\n"]
    # for i in text:
    #         if len(i) == 0:
    #            print(i+"98955")
    #            print(text.index(i))

    #     with open(
    #             r"C:\Users\10260\PycharmProjects\soft-test-main\appnium\mini_Selenium_Program\test_report\ui自动化-2024-10-22 17-10-40-report.html",
    #             "r", encoding="utf-8") as f:
    #         a = f.readlines()
    #         print(getTestResult_detail(a))
    #         print()
    #         print(getTestResult(a))
    #         print(totalTestData(a))
    #
    # s = report(r"C:\Users\10260\PycharmProjects\soft-test-main\appnium\mini_Selenium_Program\public\test_",
    #            "test_ddt_json_excle", "liwenda")
    # print(logging.WARNING)
    # pay_options_lists = ["11", "2", "4", "10"]
    # for pay_options in pay_options_lists:
    #     if pay_options == "10":
    #         print(10)
    #         break
    #     else:
    #         print(pay_options)
    #         if len(pay_options_lists)-1 == pay_options_lists.index(pay_options):
    #
    #             raise Exception("20" + "不存在任何页面！")
    #         else:
    #             pass
