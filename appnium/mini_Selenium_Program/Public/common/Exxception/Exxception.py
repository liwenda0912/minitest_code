# import logging
# import unittest
# from appnium.mini_Selenium_Program.test_case.chargeStartCase import chargeStartCase
# import sys
# import traceback
#
#
# class Exxception:
#     def __init__(self):
#         # self.chargeStart = chargeStartCase
#         pass
#
#     @staticmethod
#     def global_exception_handler(exc_type, exc_value, exc_traceback):
#         if exc_type is KeyboardInterrupt:
#             # 如果是键盘中断（用户按下Ctrl+C），不做处理
#             return
#         # 打印异常信息
#         print(f"Unhandled exception encountered: {exc_type.__name__}: {exc_value}")
#         traceback.print_exception(exc_type, exc_value, exc_traceback)
#
#     # 自定义异常处理函数
#     @staticmethod
#     def handle_exception(exc_type, exc_value, exc_traceback):
#             if issubclass(exc_type, KeyboardInterrupt):
#                 # 忽略键盘中断异常
#                 sys.__excepthook__(exc_type, exc_value, exc_traceback)
#                 return
#
#             # 记录异常信息到日志
#             logging.error("Uncaught exception", exc_info=(exc_type, exc_value, exc_traceback))
#
#         # 设置自定义异常处理函数
#     sys.excepthook = handle_exception
#         # 在这里可以添加发送异常信息到服务器的代码
#
#     # def ExxceptionHandle(appnium, e):
#     #     appnium.quit()
#     #     print("出现了:", e)
#     #     suite = unittest.TestSuite()
#     #     load_case = unittest.TestLoader().loadTestsFromTestCase(chargeStartCase)
#     #     suite.addTest(load_case)
#     #     unittest.TextTestRunner().run(suite)
#     #     print("重新启动完成")
#
#     def __del__(self):
#         pass
#
#
# # 设置全局异常处理器
# # sys.excepthook = Exxception.global_exception_handler
