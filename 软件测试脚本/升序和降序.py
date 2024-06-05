import os

a = [-1, -2, 3, 5, 6]
b = (1, 2.5, 5, -4)
# 排序小到大
a.sort()
print(a)
# 排序大到小
a.reverse()
print(a)
c = sorted(b)

print(c)
# 列表利用sort（）和reverse()分别进行升序和降序
# 而其他再利用sorted（）里的reverse=True表示降序，默认表示升序

file = os.path.dirname(__file__)+'\\测试结果\\'
print(file)