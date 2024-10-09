import os


def keyboard(*loc):
    print("执行搜狗键盘")
    os.system("adb shell ime list -s")
    os.system("adb shell settings put secure default_input_method com.sohu.inputmethod.sogou/.SogouIME")
    loc[0].click(loc[1]).perform()


def getHtml(appnium):
    with open("source.txt", "w", encoding='utf-8') as t:
        t.write(appnium.page_source)
        t.close()


def enterKey(**kwargs):
    size = kwargs.get("appnium").get_window_size()
    print(size)
    kwargs.get("wait").Appnium_wait(2)
    kwargs.get("driver").actionPress([1000, 1732], [1062, 1920], window_size=[size["width"], size["height"]])