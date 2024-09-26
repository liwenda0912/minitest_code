import pymysql
from exceptionx import TryExcept
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base


@TryExcept
class Connect:
    pass
    # # noinspection PyBroadException
    #
    #     connection = pymysql.Connection(
    #         host="localhost",
    #         user="root",
    #         password="root",
    #         database="yourdatabase"
    #     )
    #     Cursor = connection.cursor()


def sqlalchemy_():
    # 使用sqlalchemy
    host = "localhost",
    user = "root",
    password = "123456",
    database = "testRunningdata"
    port = "3306"
    Base = declarative_base()

    # 创建连接引擎
    engine = create_engine(f'mysql://root:123456@localhost:3306/testRunningdata?charset=utf8', echo=True)
    Base.metadata.create_all(engine)
    DBSession = sessionmaker(bind=engine)
    session_ = DBSession()
    return session_
