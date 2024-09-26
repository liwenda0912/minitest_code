# from datetime import datetime
# from uu import test
#
# from sqlalchemy import select
#
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
#
# from appnium.mini_Selenium_Program.Public.base.TestResultBase import TestResultBase
#
# import appnium.mini_Selenium_Program.Public.base.TestResultBase
# from appnium.mini_Selenium_Program.Public.Utils.SqlConnect import SqlServer
# from appnium.mini_Selenium_Program.Public.Utils.uilts import Init
# import os
# from appnium.mini_Selenium_Program.Public.Utils.TestReport import report
# from appnium.mini_Selenium_Program.Public.base import TestResultBase
# from appnium.mini_Selenium_Program.Public.conf.SqlConnectConf import Connect, sqlalchemy_
#
# # from appnium.mini_Selenium_Program.Public.base.TestResultBase import TestResultBase
#
#
# if __name__ == '__main__':
#     session = sqlalchemy_()
#     # # # 定义查询过滤器的字典
#     # filter_dict = {
#     #     'city': '广州',
#     #     'address': '广州'
#     # }
#     #
#     # # 构建查询过滤器
#     # query = session.query(TestResultBase.TestResultBase)
#     # for key, value in filter_dict.items():
#     #     query = query.filter(getattr(TestResultBase.TestResultBase, key) == value)
#     #     print(getattr(TestResultBase.TestResultBase, key) == value)
#
#     # 执行查询并打印结果
#     # result = query.all()
#     # for user in result:
#     #     print(f"Name: {user.username}, Age: {user.password}")
#     # #
#     # engine = create_engine(f'mysql://root:123456@localhost:3306/testRunningdata?charset=utf8',echo=True)
#     # # 初始化数据库连接:
#     # # 创建DBSession类型:
#     current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#     #
#     # DBSession = sessionmaker(bind=engine)
#     # session = DBSession()
#
#     #
#     # user_ = session.query(TestResultBase.TestResultBase).filter_by(id=1).all()
#     # for item in user_:
#     #     print(item.username)
#     d = {"city": "广州", "address": "广州"}
#     # delete删除
#     # if SqlServer(session).delete_(dict_={"city": "广州", "address": "广州"}, model=TestResultBase.TestResultBase) == 1:
#     #     print("删除成功")
#     # print(session.query(TestResultBase.TestResultBase).filter_by(id=1).update({'username': "Jack", "password": "222222"}))
#     # session.commit()
#     # if SqlServer(session).update_(dict_={"city": "广州", "address": "广州"}, model=TestResultBase.TestResultBase,
#     #                               where={'username': "Jack", "password": "55552"}) == 1:
#     #     print("更新成功")
#     a = "lw", "888888888", "广州", "51545555", "", "广州", "广东", 55555, "2024-09-26 17:25:55"
#     SqlServer(session).add_(model=TestResultBase.TestResultBase("lw8888", "888888888", "广州", "51545555", "", "广州", "广东", 55555, current_time), values=a)
#     # insert增加
#     # SqlServer(session).add_(TestResultBase.TestResultBase("lw0", "888888888", "广州", "51545555", "", "广州", "广东", 55555, current_time))
#     # update更新
#     # use = SqlServer(session).update_(select(TestResultBase.TestResultBase).where(TestResultBase.TestResultBase.username.in_(["lw0"])))
#     # select搜素
#     # user = SqlServer(session).select_(select(TestResultBase.TestResultBase).where(TestResultBase.TestResultBase.username.in_(["lw0", "zwj"])))
#     # u = SqlServer(session).get_(TestResultBase.TestResultBase,1)
#     # use = session.scalars(select(TestResultBase.TestResultBase).where(TestResultBase.TestResultBase.username.in_(["lw", "zwj"])))
#     # session.commit()
#     # print(u)
#     #     # 添加
#     # user = TestResultBase
#     # add_user = user("lw", "888888888", "广州", "51545555", "", "广州", "广东", 55555, current_time)
#     # print(session.add(add_user))
#
# # report(r"C:\Users\10260\PycharmProjects\soft-test-main\appnium\mini_Selenium_Program\test_case", "LoginTestCase", "liwenda")
