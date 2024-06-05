from jiwu import data
from music.music import readfile  # 导包的应用


class Father:
    def __eat(self):  # 私有函数，不能直接在外面被使用
        print('father:eat')

    def eat(self):  # 私有函数，不能直接在外面被使用
        print('father:hunger')
        self.__eat()


class Son(Father):
    def __init__(self):
        print("构造函数")
        data()
        readfile()

    def eat(self):
        print('son:eat')  # 重载
        super().eat()  # 子类调用父类方法

    def __del__(self):
        print("析构方法")


if __name__ == "__main__":
    def method(obj):  # 多态
        obj.eat()

    s = Son()
    f = Father()
    method(s)
