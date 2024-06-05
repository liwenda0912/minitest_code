import os

import requests
import sys


def data():
    try:
        header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
        }
        data = requests.get(headers=header, url='http://cd.jiwu.com/fangjia/')
        print(data.headers)
        print(data.status_code)
        # print(type(1.2))
        # print(type(5))
        q = 'kk-1'
        # i = 1
        # a = 1 + i
        # b=q.split('-')
        # print(b[0]+b[1])
        print(q.isascii())
        b = set('12489')
        a = set('123489')
        b.update({'77'})
        print(a - b)
        print(b & a)
        print(b ^ a)
        print(a | b)
        print(b)
    except Exception as e:  # 有异常时且捕获异常时才会执行
        print('我是你', e)
        print(sys.exc_info())  # 打印异常位置
        raise TypeError("自定义异常")
    else:  # 没有异常时才执行
        print('hahaha')
    finally:  # 有没有异常都会执行
        print('你好')
        raise TypeError("自定义异常")  # 用raise来抛出异常
