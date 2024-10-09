import unittest

from ddt import ddt, data

from appnium.mini_Selenium_Program.Public.Utils.TestDataUtils import DataController


@ddt
class test_(unittest.TestCase):
    da = DataController.read_excel(r"C:\Users\10260\PycharmProjects\soft-test-main\appnium\mini_Selenium_Program\data\1.xlsx",)

    @classmethod
    def setUpClass(cls) -> None:
        pass

    @data(*DataController.read_json(da, "测试"))
    def test_read_list_data(self, list_):
        print(list_)

    @classmethod
    def tearDownClass(cls) -> None:
        print('结束')