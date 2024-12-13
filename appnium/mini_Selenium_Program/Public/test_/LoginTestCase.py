# # import goto
# # from goto import with_goto
# # from dominate.tags import label
# #
# #
# # #
# # # from appnium.mini_Selenium_Program.Public.Utils.ReleaseConnect import Release_conf, Quit_conf
# # # from appnium.mini_Selenium_Program.Public.Utils.Simulator_Start import AppiumApp_start, Simulator_Start ,ConnectSimulator
# # # from goto import with_goto
# # #
# import subprocess
# # #
# if __name__ == "__main__":
#
#     # 使用tasklist命令获取系统进程信息
#     cmd = "adb devices"
#     n = "adb connect 127.0.0.1:7555"
#     output = subprocess.check_output(cmd, shell=True)
#
#     # 将命令输出转换为字符
#     output_str = str(output)
#     lines = output_str.strip().split(" ")
#     # 分割字符串获取每一行
#     # 查找指定进程名称的状态
#     for line in lines:
#         if r"127.0.0.1:7555\tdevice" not in line:
#             output = subprocess.check_output(n, shell=True)
#             print(line)
#         # line_name = line.split(r"\r\n")
#         # for i in line_name:
#         #     if i == r"127.0.0.1:7555\tdevice":
#         #         print(i)
#         #         break
# # #     #
# # #     #         # 进程状态位于行的最后一列
# # #     #         # subprocess.run(['taskkill', '/IM', 'MuMuPlayer.exe'], check=True)
# # #     # Quit_conf()
# # #
# # #
# # #
import unittest
from ddt import ddt, data

# 测试用例
cases = [
    {'title': '登录成功', 'expected': {'code': 200, 'msg': '登录成功'}, 'data': ('kobe', '666')},
    {'title': '登录失败', 'expected': {'code': 201, 'msg': '用户名或者密码不正确'}, 'data': ('kobe', '888')},
    {'title': '用户名不能为空', 'expected': {'code': 201, 'msg': '用户名不能为空'}, 'data': ('', '666')},
    {'title': '密码不能为空', 'expected': {'code': 201, 'msg': '密码不能为空'}, 'data': ('kobe', '')},
    {'title': '用户名和密码不能为空', 'expected': {'code': 201, 'msg': '用户名和密码不能为空'}, 'data': ('', '')},
]


#
# #
# # # 数据驱动测试用例
@ddt
class LoginTestCase_(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print('开始')

    # def setUp(self) -> None:
    #     print('开始执行用例')

    @data(*cases)
    def test_login(self, case):
        print(case)
        self.assertEqual(case['expected'], self.login(case['data'][0], case['data'][1]), "不相等")

    def login(self, username, password):
        # print(username, password)
        if username == 'kobe' and password == '666':
            return {'code': 200, 'msg': '登录成功'}

        if username == 'kobe' and username != '' and password != '666' and password != '':
            return {'code': 201, 'msg': '用户名或者密码不正确'}

        if username == 'kobe' and password == '':
            return {'code': 201, 'msg': '密码不能为空'}

        if username == '' and password == '666':
            return {'code': 201, 'msg': '用户名不能为空'}

        if username == '' and password == '':
            return {'code': 201, 'msg': '用户名和密码不能为空'}

    # def tearDown(self) -> None:
    #     print('用例执行完毕')

    @classmethod
    def tearDownClass(cls) -> None:
        print('结束')


#
#
if __name__ == '__main__':
    # Charge_user_login()
    # chargeStart()
    # key = ke_code.get_keys()
    # for i in "2.0":
    #     d = key.get(i)
    #     print(d)
    LoginTestCase_()
#
# if __name__ == '__main__':
#     with open("../../test_case/source.txt", "w") as t:
#         t.write("55555")
#         t.close()
