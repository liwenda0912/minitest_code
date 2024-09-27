from exceptionx import TryExcept

# from appnium.mini_Selenium_Program.Public.base.TestResultBase import TestResultBase
# from appnium.mini_Selenium_Program.Public.conf.SqlConnectConf import Connect


# def Find_sql(*loc):
#     sql = "select * from uesr where name=" + loc[0] + " and id = " + loc[1] + ";"
#     Connect.Cursor.execute(sql)
#     result = Connect.Cursor.fetchall()
#     return result
#
#
# def delete_sql(*loc):
#     sql = 'delete from user where name=' + loc[0] + ';'
#     Connect.Cursor.execute(sql)
#     result = Connect.Cursor.fetchall()
#     return result
#
#
# def insert_sql(*loc):
#     sql = "insert into user(name,age) values(" + loc[0] + "" + loc[1] + ")"
#     Connect.Cursor.execute(sql)
#     result = Connect.Cursor.fetchall()
#     return result
#
#
# def updata_sql(loc, *args):
#     sql = "update user set name=" + args[0] + ", age =" + args[0] + "where  name = " + loc + ";"
#     Connect.Cursor.execute(sql)
#     result = Connect.Cursor.fetchall()
#     return result
from sqlalchemy import select
from sqlalchemy.orm import declarative_base, DeclarativeMeta

from appnium.mini_Selenium_Program.Public.model.TestResultBase import TestResultBase


@TryExcept
class SqlServer(object):
    """
       类的启动前的执行
    """
    def __init__(self, session):
        self.session = session

    """
    <-------------------查询-------------------->
    # 使用例子:
    # SqlServer(session).select_(dict_={"city": "广州", "address": "广州"}, model=TestResultBase.TestResultBase)"""
    def select_(self, **kwargs):
        query = self.session.query(kwargs.get("model"))
        for key, value in kwargs.get("dict_").items():
            query = query.filter(getattr(kwargs.get("model"), key) == value)
        code_q = query.all()
        return code_q

    """
    <-------------------更新-------------------->
    # 例子:
    #    # <------TestResultBase.TestResultBase是model对象---->
    #  SqlServer(session).update_(dict_={"city": "广州", "address": "广州"}, model=TestResultBase.TestResultBase,where={{'username': "Jack", "password": "222222"}})
    """
    def update_(self, **kwargs):
        query = self.session.query(kwargs.get("model"))
        for key, value in kwargs.get("dict_").items():
            query = query.filter(getattr(kwargs.get("model"), key) == value)
        code_ = query.update(kwargs.get("where"))
        self.session.commit()
        if code_ == 1:
            return code_
        else:
            return 0

    '''
      <-------------------删除-------------------->
      # 调用例子:SqlServer(session).delete_(dict_={"city": "广州", "address": "广州"}, model=TestResultBase.TestResultBase)
    '''
    def delete_(self, **kwargs):
        query = self.session.query(kwargs.get("model"))
        for key, value in kwargs.get("dict_").items():
            query = query.filter(getattr(kwargs.get("model"), key) == value)
        code = query.delete()
        self.session.commit()
        return code

    '''
    <-------------------插入或者增加-------------------->
    # 插入数据例子:
    # TestResultBase.TestResultBase是model对象
    # SqlServer(session).add_(TestResultBase.TestResultBase("lw0", "888888888", "广州", "51545555", "", "广州", "广东", 55555, current_time))
    '''
    def add_(self, **kwargs):
        add_ = kwargs.get("model")
        self.session.add(add_)
        self.session.commit()

    """
    <-------------------id查询-------------------->
    # 根据id去定点搜素
    # SqlServer(session).get_(TestResultBase.TestResultBase,1)
    # TestResultBase.TestResultBase是model对象
    # 1是id值
    """
    def get_(self, *loc):
        return self.session.get(loc[0], loc[1])

    """
       类的最后执行任务
    """
    def __del__(self):
        self.session.close()


"""
@TryExcept
class SqlServer_(object):
    def __init__(self, session):
        self.session = session

    # 例子:
    #    # <------TestResultBase.TestResultBase是model对象---->
    #  user = SqlServer(session).select_(
    # <---select是查询, where是搜索条件 --->
    #    select(TestResultBase.TestResultBase).where(TestResultBase.TestResultBase.username.in_(["lw0", "zwj"])))
    def select_(self, loc):
        list_ = self.session.scalars(loc)
        self.session.commit()
        return list_

    # 例子:
    #    # <------TestResultBase.TestResultBase是model对象---->
    #  user = SqlServer(session).select_(
    # <---select是查询, where是搜索条件 --->
    #    select(TestResultBase.TestResultBase).where(TestResultBase.TestResultBase.username.in_(["lw0", "zwj"])))
    # user.
    def update_(self, loc):
        patrick = self.session.scalars(loc).one()
        patrick.address = ","
        self.session.commit()

    # 调用例子:SqlServer(session).delete_(dict_={"city": "广州", "address": "广州"}, model=TestResultBase.TestResultBase)
    def delete_(self, **kwargs):
        if kwargs.get("type") == "id":
            list_ = self.session.get(kwargs.get("model"), kwargs.get("id"))
        elif kwargs.get("type") == "else":
            list_ = self.session.scalars(kwargs.get("select"))
            self.session.delete(list_)

    # 插入数据例子:
    # ------TestResultBase.TestResultBase是model对象---
    # SqlServer(session)
    #         .add_(TestResultBase.TestResultBase("lw0", "888888888", "广州", "51545555", "", "广州", "广东", 55555, current_time))
    def add_(self, loc):
        self.session.add(loc)
        print(self.session.add(loc))
        if self.code_ == 1:
            return self.code_
        else:
            return 0

    # 根据id去定点搜素
    def get_(self, *loc):
        return self.session.get(loc[0], loc[1])

    def __del__(self):
        self.session.commit()
        self.session.close()
"""
