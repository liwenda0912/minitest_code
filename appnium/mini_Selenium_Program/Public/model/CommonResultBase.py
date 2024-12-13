from sqlalchemy import Column, String, create_engine, Integer, Date, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker
# from appnium.mini_Selenium_Program.Public.Utils.SqlConnect import SqlServer
from appnium.mini_Selenium_Program.Public.conf.SqlConnectConf import Connect

Base = declarative_base()


class CommonResultBase(Base):
    """
        # 表的名字
        """
    __tablename__ = 'test_result'

    """   
       # 表的结构:
    """
    id = Column(Integer, primary_key=True, autoincrement=True)
    resultName = Column(String(50), nullable=False)
    resultReport = Column(String(50), nullable=False)
    TestPeople = Column(String(255))
    TestTime = Column(String(255), nullable=False)
    TestData = Column(String(10), nullable=False)
    state = Column(Integer, nullable=False)
    TestResult = Column(String(10), nullable=False)
    TestCaseId = Column(Integer, ForeignKey("test_case.id"), nullable=False)

    def __init__(self, resultName, resultReport, TestTime, TestData, TestPeople, TestResult, state, TestCaseId):
        self.TestData = TestData
        self.TestTime = TestTime
        self.resultName = resultName
        self.resultReport = resultReport
        self.TestPeople = TestPeople
        self.TestResult = TestResult
        self.state = state
        self.TestCaseId = TestCaseId

    def __repr__(self) -> str:
        return f"TestResultBase(id={self.id!r},resultName={self.resultName!r}, resultPeople={self.resultPeople!r}, TestData={self.TestData!r}," \
               f" resultReport={self.resultReport!r}, TestTime={self.TestTime!r}, TestResult={self.TestResult!r}, state={self.state!r}, TestCaseId={self.TestCaseId!r})"
