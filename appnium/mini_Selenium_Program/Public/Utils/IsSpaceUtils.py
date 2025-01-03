# 判断换行，空格
def isSpace(loc):
    if loc.isspace():
        print(loc.isspace())
        return True
    else:
        return False


def isEmpty(loc):
    if len(loc) == 0:
        return True
    else:
        return False


def isNotSpace(loc):
    if loc.isspace():
        return False
    else:
        return True


def isNotEmpty(loc):
    if len(loc) == 0:
        return False
    else:
        return True


def splitPrice(choice_pay):
    for i in choice_pay.split("元"):
        if isNotEmpty(i):
            return i


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
