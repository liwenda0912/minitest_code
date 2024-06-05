import unittest


# 单元测试中五个特殊的方法的使用，包括使用场景及执行顺序：
#   setup（）单元测试开始就执行的,test_用例名（）（用例的操作步骤），tearDown（）单元测试最后的步骤，顺序就是依次执行下去。
#   setup（），主要进行测试用例的资源初始化，前提条件
#   test_用例名 测试用例，要把测试用例的步骤写在该方法中
#   tearDown（）主要进行测试用例的资源释放
#   @ classmethod注解的方式是类方法，不用创建对象也能用的方法，在对象进内存之前就已经存在的方法，随着类一起进入内存
#   setupClass  给当前单元测试类的所有测试用例进行初始化的
#   tearDownClass  给当前单元测试类的所有用例进行资源释放
#   setUpClass 和setup()的区别：
#            setUp（)不需要@classmethod注解：setupClass需要@classmethod注解
#            setup()实例方法。就需要创建对象再调用：setupclass类方法，不耑要对象也可以调用
#            setup()再每一个测试用例执行之前运行一次：setupclass方法在测试执行之前只执行一次
#            setup()是对一条用例的初始化，每个测试用例都要初始一遍：setupclass方法对所有测试用例都进行了初始化，不用对测试用例一个一个进行初始化。
# TestLoader:（用来加载测试用，然后结合测试集使用）
#     1.创建TestLoader对象：1oader = unittest. TestLoader()
#     2、使用1oader的方法1oadtestsfromName()将折定的测试用例加载到测试集里
#          1oadtestsfromName(）的参数比较灵活(理解、会用即可）
#        1、可以是模典名：unitMymath
#        2。可以是模块中的类名：unitMymath. unitMymath
#        3、可以是模块中类中的某个用例：unitnymath. unitnlymath.test_add_1
#
#    3.使用1oader的discover方法（必须掌握）将指定的文件(模块）中的测试用例一次性加载
#                 unittest.defaultTestLoader.discover()
#     通过指定路径下所有匹配pattern的.py文件全部加载
#     suite = unittest.defaultTestLoader.discover(start_dir="p", pattern="*.py")
#     unittest.TextTestRunner().run(suite)

class TestCase1(unittest.TestCase):
    # @classmethod
    # def setUpClass(cls) -> None:
    #     print('setUp')
    #
    # @classmethod
    # def tearDownClass(cls) -> None:
    #     print('tearDown')
    def setUp(self) -> None:
        print("setup")
    def test_case(self):
        print(1)
    def tearDown(self) -> None:
        print('tearDown')
    def test_1(self):
        print(2)


if __name__ == "__main__":
    # unittest.main()
    print('nihao')
    # 测试集的使用
    # suitt = unittest.TestSuite()
    # suitt.addTest(TestCase("test_1"))
    # runner = unittest.TextTestRunner()
    # runner.run(suitt)

    # loadTestsFromTestCase的使用
    # suite = unittest.TestSuite()
    # load_case = unittest.TestLoader().loadTestsFromTestCase(TestCase1)
    # suite.addTest(load_case)
    # unittest.TextTestRunner().run(suite)

    # loadTestsFromName的使用
    # suite = unittest.TestSuite()
    # load_case = unittest.TestLoader().loadTestsFromName("test_1",module=TestCase1)
    # suite.addTest(load_case)
    # unittest.TextTestRunner().run(suite)

    # 通过指定路径下所有匹配pattern的.py文件全部加载
    suite = unittest.defaultTestLoader.discover(start_dir="p", pattern="*.py")
    unittest.TextTestRunner().run(suite)