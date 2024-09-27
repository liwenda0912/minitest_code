import pymysql
from exceptionx import TryExcept
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base


@TryExcept
class Connect:

    """
      sqlalchemy配置连接mysql数据库
    """
    @staticmethod
    def sqlalchemy_():
        # 使用sqlalchemy
        host = "localhost"
        user = "root"
        password = "123456"
        database = "testRunningdata"
        port = "3306"
        sql_ = 'mysql'
        Base = declarative_base()

        """        
        # 创建连接引擎
        """
        engine = create_engine(f''+sql_+'://'+user+':'+password+'@'+host+':'+port+'/'+database+'?charset=utf8', echo=True)
        print(engine)
        Base.metadata.create_all(engine)
        DBSession = sessionmaker(bind=engine)
        session_ = DBSession()
        return session_

    """
       pymysql配置连接mysql数据库
    """
    # # noinspection PyBroadException
    #
    #     connection = pymysql.Connection(
    #         host="localhost",
    #         user="root",
    #         password="root",
    #         database="yourdatabase"
    #     )
    #     Cursor = connection.cursor()
