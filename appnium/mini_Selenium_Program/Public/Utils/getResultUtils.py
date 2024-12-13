import re

from appnium.mini_Selenium_Program.Public.Utils.IsSpaceUtils import isNotEmpty


class getResultUtils(object):
    @staticmethod
    def getTestName(a):
        TestName = []
        for i in a:
            if "<div class='testcase'>" in i:
                for j in re.split("<.*?><div class='testcase'>", i):
                    for name in j.split("</div></td>\n"):
                        if name is not None and name != '' and name.isspace() is not True:
                            TestName.append(name)
        return TestName

    @staticmethod
    def getTestResult(a):
        result_ = []
        for i in a:
            if "button" and "btn btn-danger btn-xs collapsed" in i:
                for result in re.split(r'<.*?>', i):
                    if result.isspace() is not True:
                        result_.append(result)
        return result_

    @staticmethod
    def getTestPeopleName(a):
        textName = []
        text_ = ["执行人:", "测试人员 :"]
        num = 0
        while True:
            for i in a:
                if text_[num] in i:
                    # if "测试人员 : " in i:
                    for text in re.split(r'<.*?>', i):
                        if text != '\n' and text != '':
                            textName.append(text)
                    return "".join(textName)
            if len(textName) == 0:
                num = 1
            else:
                break

    @staticmethod
    def getTestResult_detail(a):
        totalDetail = []
        startIndex = []
        for i in a:
            if "collapse in" in i:
                startIndex.append(a.index(i))
        s = []
        for index in range(0, len(startIndex)):
            for j in range(startIndex[index] + 2, 100000):
                if "</pre>" in a[j]:
                    break
                else:
                    if a[j] != '\n':
                        for text in a[j].split('\n'):
                            if text != "" and text.isspace() is not True:
                                for text_ in text.split('\n'):
                                    s.append(text_)
            totalDetail.append("".join(s))
            s.clear()
        return totalDetail

    @staticmethod
    def totalTestData(a):
        startIndex = []
        totalDetail_ = []
        for i in a:
            if " warning" in i:
                startIndex.append(a.index(i))
        for index in range(0, len(startIndex)):
            for j in range(startIndex[index] + 1, 100000):
                if "</tr>" in a[j]:
                    break
                else:
                    for text in re.split("<.*?>", a[j]):
                        if text != "" and text.isspace() is not True:
                            if text != "详细" and '收起':
                                totalDetail_.append(text)
        return totalDetail_


