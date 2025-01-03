import os
import time


def keyboard(*loc):
    print("执行搜狗键盘")
    os.system("adb -s 127.0.0.1:7555 shell ime list -s")
    os.system("adb -s 127.0.0.1:7555 shell settings put secure default_input_method com.sohu.inputmethod.sogou/.SogouIME")
    loc[0].click(loc[1]).perform()


def getHtml(appnium):
    with open("source.txt", "w", encoding='utf-8') as t:
        t.write(appnium.page_source)
        t.close()


def enterKey(**kwargs):
    time.sleep(2)
    size = kwargs.get("appnium").get_window_size()
    kwargs.get("wait").Appnium_wait(2)
    kwargs.get("driver").actionPress([1000, 1732], [1062, 1920], window_size=[size["width"], size["height"]])


def adbKeyboard(*loc):
    time.sleep(2)
    os.system("adb -s 127.0.0.1:7555 shell settings put secure default_input_method com.android.adbkeyboard/.AdbIME")
    # # 点击
    loc[0].click(loc[1]).perform()
    time.sleep(2)
    os.system("adb -s 127.0.0.1:7555 shell am broadcast -a ADB_INPUT_TEXT  --es msg " + loc[2])

