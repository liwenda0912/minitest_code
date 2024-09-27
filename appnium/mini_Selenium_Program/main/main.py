from appnium.mini_Selenium_Program.Public.Utils.SqlConnect import SqlServer
from appnium.mini_Selenium_Program.Public.model import TestResultBase
from appnium.mini_Selenium_Program.Public.conf.SqlConnectConf import Connect

if __name__ == '__main__':
    session = Connect().sqlalchemy_()

    """ <------------getattr--->定义查询过滤器的字典"""
    #     # filter_dict = {
    #     #     'city': '广州',
    #     #     'address': '广州'
    #     # }
    #     # # 构建查询过滤器
    #     # query = session.query(TestResultBase.TestResultBase)
    #     # for key, value in filter_dict.items():
    #     #     query = query.filter(getattr(TestResultBase.TestResultBase, key) == value)
    #     #     print(getattr(TestResultBase.TestResultBase, key) == value)
    #     # 执行查询并打印结果
    #     # result = query.all()
    #     # for user in result:
    #     #     print(f"Name: {user.username}, Age: {user.password}")
    #

    '''<-----------------------根据id取查--------------------------------->'''
    #     # user_ = session.query(TestResultBase.TestResultBase).filter_by(id=1).all()
    #     # for item in user_:
    #     #     print(item.username)
    #     d = {"city": "广州", "address": "广州"}
    #     # delete删除

    if SqlServer(session).delete_(dict_={"id": "8"}, model=TestResultBase.TestResultBase) == 1:
        print("删除成功")
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
    data = SqlServer(session).select_(dict_={"city": "广州花都", "address": "广州"}, model=TestResultBase.TestResultBase)
    print(data)
#     user = SqlServer(session).select_(select(TestResultBase.TestResultBase).where(TestResultBase.TestResultBase.username.in_(["lw0", "zwj"])))
#     # u = SqlServer(session).get_(TestResultBase.TestResultBase,1)
# use = session.scalars(select(TestResultBase.TestResultBase).where(TestResultBase.TestResultBase.username.in_(["lw", "zwj"])))
#     # session.commit()
#     # print(u)
#     #     # 添加
#     # user = TestResultBase
#     # add_user = user("lw", "888888888", "广州", "51545555", "", "广州", "广东", 55555, current_time)
#     # print(session.add(add_user))
#
# # report(r"C:\Users\10260\PycharmProjects\soft-test-main\appnium\mini_Selenium_Program\test_case", "LoginTestCase", "liwenda")
