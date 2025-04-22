# import logging
# import os
# import sys
# import time
#
# """
# #
# # %(name)
# # s：Logger的名字
# # %(levelno)
# # s：打印日志级别的数值
# # %(levelname)
# # s：打印日志级别的名称
# # %(pathname)
# # s：打印当前执行程序的路径，其实就是sys.argv[0]
# # %(filename)
# # s：打印当前执行程序名
# # %(funcName)
# # s：打印日志的当前函数
# # %(lineno)
# # d：打印日志的当前行号
# # %(asctime)
# # s：打印日志的时间
# # %(thread)
# # d：打印线程ID
# # %(threadName)
# # s：打印线程名称
# # %(process)
# # d：打印进程ID
# # %(message)
# # s：打印日志信息
# """
#
#
# # 自定义异常处理函数
# def handle_exception(exc_type, exc_value, exc_traceback):
#     if issubclass(exc_type, KeyboardInterrupt):
#         # 忽略键盘中断异常
#         sys.__excepthook__(exc_type, exc_value, exc_traceback)
#         return
#
#     # 记录异常信息到日志
#     logging.error("Uncaught exception", exc_info=(exc_type, exc_value, exc_traceback))
#
#
# class Logger(object):
#     def __init__(self, **kwargs):
#         logging.basicConfig(level=logging.INFO,
#                             handlers=[
#                                 logging.FileHandler(r'log/' + time.strftime('%Y-%m-%d', time.localtime()) + '.log',
#                                                     encoding="utf-8"),
#                                 # 将日志写入文件
#                                 logging.StreamHandler()  # 将日志输出到控制台
#                             ],
#                             format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')
#
#
# #     # 由于严重的问题，程序的某些功能已经不能正常执行
# #     def logger_Error(self, e):
# #         logging.error(e)
# #
# #     # 确认程序按预期运行。
# #     def info(self, loc):
# #         logging.info(loc)
# #
# #     # 详细的信息，通常只有试图诊断问题的开发人员才会感兴趣。
# #     def logger_Debug(self, **loc):
# #         logging.debug(loc)
# #
# #     # 一般用来打印警告信息
# #     def logger_Warning(self, **loc):
# #         logging.warning(loc)
# #
# #     # 严重的错误，表明程序已不能继续执行
# #     def logger_Critical(self, **loc):
# #         logging.critical(loc)
# #
# #
# #
# #
# #
# # # 自定义异常处理函数
# # def handle_exception(exc_type, exc_value, exc_traceback):
# #     if issubclass(exc_type, KeyboardInterrupt):
# #         # 忽略键盘中断异常
# #         sys.__excepthook__(exc_type, exc_value, exc_traceback)
# #         return
# #
# #     # 记录异常信息到日志
# #     logging.error("Uncaught exception", exc_info=(exc_type, exc_value, exc_traceback))
# #
# #
# # # 设置自定义异常处理函数
# # sys.excepthook = handle_exception
# #
# #
# # # 重定向 sys.stdout 和 sys.stderr
# # class LoggerWriter:
# #     def __init__(self, logger, level):
# #         self.logger = logger
# #         self.level = level
# #
# #     def write(self, message):
# #         self.logger.log(self.level, message.strip())
# #
# #     def flush(self):
# #         pass
# #
# #
# # # 将 sys.stdout 和 sys.stderr 重定向到日志
# # sys.stdout = LoggerWriter(logging.getLogger(), logging.INFO)
# # sys.stderr = LoggerWriter(logging.getLogger(), logging.ERROR)
import logging
import os
import sys
import time
import tracemalloc
import warnings


class LoggerWriter:
    def __init__(self, logger, level):
        self.logger = logger
        self.level = level

    def write(self, message):
        self.logger.log(self.level, message.strip())

    def flush(self):
        pass


class Logger(object):
    @staticmethod
    def logging():
        # 确保日志目录存在
        log_dir = "log"
        os.makedirs(log_dir, exist_ok=True)
        # 启用 tracemalloc
        tracemalloc.start()
        # 配置日志
        logging.basicConfig(
            level=logging.DEBUG,
            handlers=[
                logging.FileHandler(r'log/' + time.strftime('%Y-%m-%d', time.localtime()) + '.log',
                                    encoding="utf-8"),
                # 将日志写入文件
                logging.StreamHandler()  # 将日志输出到控制台
            ],
            format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')

        # 设置自定义异常处理函数
        # # 将 sys.stdout 和 sys.stderr 重定向到日志
        # sys.stdout = LoggerWriter(logging.getLogger(), logging.INFO)
        # sys.stderr = LoggerWriter(logging.getLogger(), logging.ERROR)

        # 捕获 ResourceWarning
        def handle_resource_warning(message, category, filename, lineno, file=None, line=None):
            logging.warning(f"ResourceWarning: {message}")
            snapshot = tracemalloc.take_snapshot()
            top_stats = snapshot.statistics('lineno')
            for stat in top_stats[:10]:  # 打印前 10 个最占用内存的堆栈信息
                logging.warning(stat)

        # 注册 ResourceWarning 处理器
        warnings.simplefilter('always', ResourceWarning)
        warnings.showwarning = handle_resource_warning
        return logging

