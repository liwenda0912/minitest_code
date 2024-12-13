import time


class Transform:
    @staticmethod
    def encode_time(time_):
        # coding:UTF-8
        # 转换成时间数组
        timeArray = time.strptime(time_, "%Y-%m-%d %H:%M:%S")
        # 转换成时间戳
        timestamp = time.mktime(timeArray)
        return timestamp

    @staticmethod
    def decode_time(time_):
        # coding:UTF-8
        # 转换成时间数组
        timeArray = time.strptime(time_, "%Y-%m-%d %H:%M:%S")
        # 转换成新的时间格式(20160505-20:28:54)
        dt_new = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
        return dt_new


