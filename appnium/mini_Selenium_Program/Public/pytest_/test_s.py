import pytest


def test_num():
    lists = [5, 9, 8, 210, 1, 86]
    for i in range(len(lists)):
        for j in range(len(lists) - 1 - i):
            if lists[j] > lists[j + 1]:
                lists[j + 1], lists[j] = lists[j], lists[j + 1]
    print(lists)


def test_nums():
    lists = [4, 86, 5, 9, 8, 210, 1, 97, 0.21]
    for i in range(len(lists)):
        for j in range(len(lists) - 1):
            if lists[j] > lists[j + 1]:
                lists[j + 1], lists[j] = lists[j], lists[j + 1]
    print(lists)


# 倒叙排序
def sort():
    list_list = [1, 5, 8, 6, 7]
    for i in range(len(list_list)):
        for j in range(len(list_list)):
            if list_list[i] > list_list[j]:
                list_list[i], list_list[j] = list_list[j], list_list[i]
        print(list_list)
    for i in range(len(list_list)):
        for j in range(len(list_list) - 1):
            if list_list[j] > list_list[j + 1]:
                list_list[j + 1], list_list[j] = list_list[j], list_list[j + 1]
        print(list_list)


if __name__ == "__main__":
    # test_num()
    # sort()
    # test_nums()
    pytest.main()
