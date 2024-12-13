from sqlalchemy import Column, String, create_engine, Integer, Date, ForeignKey
from sqlalchemy.dialects.mysql import LONGTEXT
from sqlalchemy.orm import declarative_base, sessionmaker
# from appnium.mini_Selenium_Program.Public.Utils.SqlConnect import SqlServer
from appnium.mini_Selenium_Program.Public.conf.SqlConnectConf import Connect

Base = declarative_base()


class CommonTestCaseTotalBase(Base):
    """
        # 表的名字
        """
    __tablename__ = 'test_case'

    """   
       # 表的结构:
    """
    id = Column(Integer, primary_key=True, autoincrement=True)
    testCaseName = Column(String(100), nullable=False)
    caseTotal = Column(Integer, nullable=False)
    TestCaseSuccess = Column(Integer, nullable=False)
    TestCaseFail = Column(Integer, nullable=False)
    TestCaseError = Column(Integer, nullable=False)
    state = Column(Integer, nullable=False)
    startTime = Column(Integer)
    endTime = Column(Integer)

    def __init__(self, testCaseName, caseTotal, TestCaseSuccess, TestCaseFail, TestCaseError, state, startTime,
                 endTime):
        self.testCaseName = testCaseName
        self.caseTotal = caseTotal
        self.TestCaseSuccess = TestCaseSuccess
        self.TestCaseFail = TestCaseFail
        self.TestCaseError = TestCaseError
        self.state = state
        self.startTime = startTime
        self.endTime = endTime

    def __repr__(self) -> str:
        return f"TestResultBase(id={self.id!r},testCaseName={self.testCaseName!r}, caseTotal={self.caseTotal!r}, TestCaseSuccess={self.TestCaseSuccess!r}," \
               f" TestCaseFail={self.TestCaseFail!r}, TestCaseError={self.TestCaseError!r}, state={self.state!r}, startTime={self.startTime!r}, endTime={self.endTime!r})"


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
    resultDetail = Column(LONGTEXT, nullable=False)
    TestPeople = Column(String(255))
    TestTime = Column(String(255), nullable=False)
    TestData = Column(String(10), nullable=False)
    state = Column(Integer, nullable=False)
    TestResult = Column(String(10), nullable=False)
    TestCaseId = Column(Integer, ForeignKey("test_case.id"), nullable=False)

    def __init__(self, resultName, resultDetail, TestTime, TestData, TestPeople, TestResult, state, TestCaseId):
        self.TestData = TestData
        self.TestTime = TestTime
        self.resultName = resultName
        self.resultDetail = resultDetail
        self.TestPeople = TestPeople
        self.TestResult = TestResult
        self.state = state
        self.TestCaseId = TestCaseId

    def __repr__(self) -> str:
        return f"TestResultBase(id={self.id!r},resultName={self.resultName!r}, resultPeople={self.resultPeople!r}, TestData={self.TestData!r}," \
               f" resultDetail={self.resultDetail!r}, TestTime={self.TestTime!r}, TestResult={self.TestResult!r}, state={self.state!r}, TestCaseId={self.TestCaseId!r})"
