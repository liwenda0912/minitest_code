import logging
import sys

"""
#
# %(name)
# s：Logger的名字
# %(levelno)
# s：打印日志级别的数值
# %(levelname)
# s：打印日志级别的名称
# %(pathname)
# s：打印当前执行程序的路径，其实就是sys.argv[0]
# %(filename)
# s：打印当前执行程序名
# %(funcName)
# s：打印日志的当前函数
# %(lineno)
# d：打印日志的当前行号
# %(asctime)
# s：打印日志的时间
# %(thread)
# d：打印线程ID
# %(threadName)
# s：打印线程名称
# %(process)
# d：打印进程ID
# %(message)
# s：打印日志信息
"""


class Logger(object):
    def __init__(self, **kwargs):
        self.logger = logging.getLogger('LOGGER')
        if kwargs.get("stream") is not None:
            self.stream_handler = logging.StreamHandler(stream=sys.stdout)
        else:
            self.stream_handler = logging.StreamHandler()
        if not self.logger.handlers:
            self.formatter = logging.Formatter(
                '%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')
            self.stream_handler.setFormatter(self.formatter)
            self.stream_handler.setLevel(logging.DEBUG)
            self.logger.addHandler(self.stream_handler)

    # 由于严重的问题，程序的某些功能已经不能正常执行
    def logger_Error(self, e):
        self.logger.setLevel(level=logging.ERROR)
        self.logger.error(e)

    # 确认程序按预期运行。
    def info(self, loc):
        self.logger.setLevel(level=logging.INFO)
        self.logger.info(loc)

    # 详细的信息，通常只有试图诊断问题的开发人员才会感兴趣。
    def logger_Debug(self, **loc):
        self.logger.setLevel(level=logging.DEBUG)
        self.logger.debug(loc)

    # 一般用来打印警告信息
    def logger_Warning(self, **loc):
        self.logger.setLevel(level=logging.WARNING)
        self.logger.warning(loc)

    # 严重的错误，表明程序已不能继续执行
    def logger_Critical(self, **loc):
        self.logger.setLevel(level=logging.CRITICAL)
        self.logger.critical(loc)

    # 直接使用logging打印日志
    @staticmethod
    def logger_BasicConfig():
        logging.basicConfig(format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s',
                            level=logging.DEBUG)

    def __del__(self):
        self.logger.removeHandler(self.stream_handler)


if __name__ == "__main__":
    Logger().logger_Error("sss")
    Logger(stream=sys.stdout).info("sss")
    Logger(stream=sys.stdout).info("sss5555")
