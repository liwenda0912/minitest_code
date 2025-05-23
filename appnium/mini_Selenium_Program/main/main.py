import logging
import re
import cv2
import numpy as np
import requests

from appnium.mini_Selenium_Program.Public.Utils.IsSpaceUtils import isSpace, isNotEmpty
from appnium.mini_Selenium_Program.Public.Utils.SqlalchemySqlUtils import SqlServer
from appnium.mini_Selenium_Program.Public.conf.SqlConnectConf import Connect
from appnium.mini_Selenium_Program.Public.model import TestResultBase
from appnium.mini_Selenium_Program.test_report.report.TestReport import report


def carKeyBoardSelect(carName):
    # keyboard_list = "555888"
    # for n in carName:
    #     if n =
    #     print(n)
    print("粤".lower() == "粤".lower())
    # if carName.index(n) == 0:
    #     print(carName.index(n))
    # elif carName.index(n) == 1:
    #     print(carName.index(n))
    # # 判断获取的车辆号码是否超过8位
    # elif carName.index(n) == 8:
    #     print("第9位")
    #     break
    # else:
    #     continue
    # for i in keyboard_list:
    #     if i == n:
    #         break
    #     else:
    #         continue


def logger(func):
    def wrapper(*args, **kwargs):
        print("Logging before function execution")
        result = func(*args, **kwargs)
        print("Logging after function execution")
        print(result)
        return result

    return wrapper


@logger
def add(a, b):
    return a + b


from functools import wraps


def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Something is happening before the function is called.")
        result = func(*args, **kwargs)
        print("Something is happening after the function is called.")
        return result

    return wrapper

@my_decorator
def example():
    """This is an example function."""
    print("Hello from a function.")


def test():

    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("错误：无法打开摄像头！")
        exit()

    # 创建滑动条窗口
    cv2.namedWindow("TrackBars")
    cv2.resizeWindow("TrackBars", 640, 240)
    cv2.createTrackbar("Hue Min", "TrackBars", 0, 179, lambda x: None)
    cv2.createTrackbar("Hue Max", "TrackBars", 179, 179, lambda x: None)
    cv2.createTrackbar("Sat Min", "TrackBars", 0, 255, lambda x: None)
    cv2.createTrackbar("Sat Max", "TrackBars", 255, 255, lambda x: None)
    cv2.createTrackbar("Val Min", "TrackBars", 0, 255, lambda x: None)
    cv2.createTrackbar("Val Max", "TrackBars", 255, 255, lambda x: None)

    while True:
        success, img = cap.read()
        if not success:
            print("警告：未接收到画面，跳过本帧...")
            continue

        imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

        # 获取滑动条值
        h_min = cv2.getTrackbarPos("Hue Min", "TrackBars")
        h_max = cv2.getTrackbarPos("Hue Max", "TrackBars")
        s_min = cv2.getTrackbarPos("Sat Min", "TrackBars")
        s_max = cv2.getTrackbarPos("Sat Max", "TrackBars")
        v_min = cv2.getTrackbarPos("Val Min", "TrackBars")
        v_max = cv2.getTrackbarPos("Val Max", "TrackBars")

        # 生成掩膜和结果
        lower = np.array([h_min, s_min, v_min])
        upper = np.array([h_max, s_max, v_max])
        mask = cv2.inRange(imgHSV, lower, upper)
        imgResult = cv2.bitwise_and(img, img, mask=mask)

        # 修复：将单通道mask转为3通道
        mask_3ch = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)

        # 堆叠显示
        imgStack = np.vstack([
            np.hstack([img, imgHSV]),
            np.hstack([mask_3ch, imgResult])
        ])
        cv2.imshow("Stacked Images", imgStack)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
if __name__ == '__main__':
    test()
    # i = "15\n是"
    # print(i.replace("\n", '')) # print(img_text("../picture/timingChargeResult.png"))


    # def d(**kwargs):
    #
    #     print(kwargs.get("y").get("hour"))
    #     print(kwargs.get("y") is None)
    #
    # d(y={"hour":"10","min":"50"})

    # text = "10\n时"
    # print(text.replace("\n",''))


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
# # 倒叙排序
# def sort():
#     list_list = [1, 5, 8, 6, 7]
#     for i in range(len(list_list)):
#         for j in range(len(list_list)):
#             if list_list[i] > list_list[j]:
#                 list_list[i], list_list[j] = list_list[j], list_list[i]
#         print(list_list)

# if __name__ == '__main__':
#     url = "http://a.openapi.evking.com.cn/api/chargeStation/page"
#     data = {"pageNo": 1,
#             "pageSize": 10}
#     params = {}
#     headers = {
#         "accept": "application/json, text/plain, */*",
#         "Utoken": "23FBC13E3B12894BF371539C0FD13326",
#         "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0"
#     }
#     s = requests.request(url=url, headers=headers, json=data, method="post", params=params)
#     j = s.json()
#     print(j)
#     print(j.get("data").get("total"))

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
# "test_ddt_json_excle", "liwenda")
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
