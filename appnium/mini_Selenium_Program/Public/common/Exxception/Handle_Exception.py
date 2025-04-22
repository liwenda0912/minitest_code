import logging
import sys
import traceback

# 配置日志
from appnium.mini_Selenium_Program.Public.common.Logger.Logger import Logger


# 定义全局异常处理器
def handle_exception(exc_type, exc_value, exc_traceback):
    Logger().logging()
    # 检查是否是 KeyboardInterrupt（如 Ctrl+C），如果是则不记录日志
    if issubclass(exc_type, KeyboardInterrupt):
        logging.info("KeyboardInterrupt detected. Exiting gracefully.")
        sys.__excepthook__(exc_type, exc_value, exc_traceback)
        return

    # 记录异常信息
    logging.error("Uncaught exception", exc_info=(exc_type, exc_value, exc_traceback))
    # 打印完整的堆栈信息
    logging.error("Traceback:", exc_info=False)
    logging.error(traceback.format_exception(exc_type, exc_value, exc_traceback))


# 设置全局异常处理器
sys.excepthook = handle_exception


# # 测试代码
# def test_function():
#     raise NoSuchElementException("This is a test exception")
#
#
# def main():
#     test_function()
#
#
# if __name__ == "__main__":
#     main()
