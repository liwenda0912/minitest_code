# 判断换行，空格
"""

   判断元素是否为换行，空格

"""


def isSpace(loc):
    if loc.isspace():
        print(loc.isspace())
        return True
    else:
        return False


def isNotSpace(loc):
    if loc.isspace():
        return False
    else:
        return True


"""

   判断元素是否为""或者[]

"""


def isEmpty(loc):
    if len(loc) == 0:
        return True
    else:
        return False


def isNotEmpty(loc):
    if len(loc) == 0:
        return False
    else:
        return True


"""
  过滤元单位
"""


def splitPrice(choice_pay):
    for i in choice_pay.split("元"):
        if isNotEmpty(i):
            return i


"""
   判断元素是否为none
"""


def isNotNone(loc):
    if loc is not None:
        return True
    else:
        return False


def isNone(loc):
    if loc is None:
        return True
    else:
        return False


def Split(s, type_):
    list_ = []
    totalDetail = []
    if type_ == "space":
        for text in s.split('\n'):
            if text != "" and text.isspace() is not True:
                list_.append(text)
        totalDetail.append("".join(list_))
        return totalDetail
    else:
        for text in s.split(type_):
            if text != "" and text.isspace() is not True:
                list_.append(text)
        return list_
