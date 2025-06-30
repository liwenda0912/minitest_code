import unittest


class test_u(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def test_(self):
        # 倒序
        list = [2.5, 9, 6, 5.3, 8.5]
        for i in range(len(list)):
            for j in range(len(list)):
                if list[i] > list[j]:
                    list[i], list[j] = list[j], list[i]
        print(list)
        list = [2.5, 9, 6, 5.3, 8.5]
        for i in range(len(list)):
            for j in range(len(list)-1):
                if list[j] > list[j+1]:
                    list[j+1], list[j] = list[j], list[j+1]
        print(list)

    def tearDown(self) -> None:
        pass
