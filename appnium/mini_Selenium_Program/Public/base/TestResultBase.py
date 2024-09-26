import datetime
import time
import pymysql
from datetime import datetime
from sqlalchemy import Column, String, create_engine, Integer, Date
from sqlalchemy.orm import declarative_base, sessionmaker
# from appnium.mini_Selenium_Program.Public.Utils.SqlConnect import SqlServer
from appnium.mini_Selenium_Program.Public.conf.SqlConnectConf import Connect

Base = declarative_base()


class TestResultBase(Base):
    # 表的名字:
    __tablename__ = 'user'
    # 表的结构:
    id = Column(Integer, primary_key=True, autoincrement=True)

    # id = Column(int, primary_key=True, blank=False)
    username = Column(String(50), nullable=False)
    password = Column(String(50))
    address = Column(String(255))
    phone = Column(String(255))
    alias = Column(String(10))
    city = Column(String(255))
    province = Column(String(255))
    zip = Column(Integer)
    date_ = Column(Date)

    def __init__(self, username, password, address, phone, alias, city, province, zip, date_):
        self.username = username
        self.zip = zip
        self.password = password
        self.city = city
        self.province = province
        self.date_ = date_
        self.alias = alias
        self.address = address
        self.phone = phone

    def __repr__(self) -> str:
        return f"TestResultBase(username={self.username!r}, password={self.password!r}, address={self.address!r}," \
               f" phone={self.phone!r}, city={self.city!r}, zip={self.zip!r}, province={self.province!r}" \
               f", alias={self.alias!r}, date_={self.date_!r})"

    # def select_(self, **kwargs):
    #     code = self.session.query(TestResultBase).filter_by(id=1).all()
    #     self.session.commit()
    #     for item in code:
    #         print(item.username)
    #
    # def update_(self, **kwargs):
    #     code = self.session.query(kwargs.get("base")).filter_by(id=kwargs.get("id")).update(kwargs.get("set"))
    #     self.session.commit()
    #     if code == 1:
    #         return 1
    #     else:
    #         return 0
    #
    # def delete_(self, **kwargs):
    #     code = self.session.query(kwargs.get("base")).filter_by(kwargs.get("where")).delete()
    #     self.session.commit()
    #     if code == 1:
    #         return 1
    #     else:
    #         return 0
    #
    # def add_(self, **kwargs):
    #     code = kwargs.get("base")(kwargs.get("sql_"))
    #     self.session.add(code)
    #     self.session.commit()


#
if __name__ == '__main__':
    #     session = Connect.session_
    #     SqlServer(session).select_(id=1,base="44")

    #     current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    #
    #     host = "localhost",
    #     user = "root",
    #     password = "123456",
    #     database = "testRunningdata"
    #     port = "3306"
    # #
    # #
    #
    # 创建连接引擎
    engine = create_engine(f'mysql://root:123456@localhost:3306/testRunningdata?charset=utf8', echo=True)
    # 初始化数据库连接:
    # 创建DBSession类型:
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    # #     # 添加
    # #     add_user = TestResultBase("lw", "888888888", "广州", "51545555", "", "广州", "广东", 55555, current_time)
    # #     print(session.add(add_user))
    #     # 查询
    #     ssss = {"s":"id=2"}
    #     print(ssss.get("s"))
    #    user_ = session.query(TestResultBase).filter_by(id=1).all()
    #    for item in user_:
    #         print(item.username)

    # #     # 更新
    # print(session.query(TestResultBase).filter_by(id=1).update({'username': "Jack", "password": "222222"}))
# #     # 删除
# #     print(session.query(TestResultBase).filter_by(id=41).delete())
# #
#     session.commit()
