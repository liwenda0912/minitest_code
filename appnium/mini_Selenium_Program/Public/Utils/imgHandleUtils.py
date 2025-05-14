# 图片处理函数
import logging
import sys

from PIL import Image

import cv2
from pytesseract import pytesseract

from appnium.mini_Selenium_Program.Public.Utils.IsSpaceUtils import isNotSpace

"""

  处理图片

"""


def handle_img(img_):
    # 打开图片
    img = cv2.imread(img_)
    # 灰度
    img = cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY)
    # 减低线噪
    h, w = img.shape[:2]
    for i in range(1, w - 1):
        for j in range(1, h - 1):
            count = 0
            if img[j, i - 1] > 245:
                count = count + 1
            if img[j, i + 1] > 245:
                count = count + 1
            if img[j - 1, i] > 245:
                count = count + 1
            if img[j + 1, i] > 245:
                count = count + 1
            if count > 2:
                img[j, i] = 255
    # 闭运算
    k = cv2.getStructuringElement(cv2.MORPH_RECT, (2, 3))  # 定义结构元素
    c = cv2.morphologyEx(img, cv2.MORPH_CLOSE, k)
    cv2.imwrite(img_, c)


"""

   获取按钮具体定位点比例

"""


def img_text_PointSize(img, **kwargs):
    handle_img(img)
    img = Image.open(img)
    crop = img.crop((60, 650, 1100, 1250))
    crop.save("../picture/timingChargeResultGreg.png")
    # 验证码识别
    # 识别中文
    lang = 'chi_sim'
    text = pytesseract.image_to_string(crop, lang)
    # text = text.strip()
    text_ = join(text)
    if "提示定时提交成功" in text_:
        logging.info("定时提交成功")
        # 裁剪图片，回显按钮的图片
        crop = img.crop([0, img.size[1] / 2, img.size[0] / 2, (img.size[1] * 3 / 4) * (6 / 7)])
        # 识别图片获取文字
        text = pytesseract.image_to_string(crop, lang)
        if kwargs.get("text_") in join(text):
            return {"x": 1 / 4, "y": 5 / 8}
        else:
            # 传递按钮在整个页面的位置
            return {"x": 3 / 4, "y": 5 / 8}
    else:
        if '是否取消定时充电' in text_:
            # 裁剪图片，回显按钮的图片
            crop = img.crop([0, img.size[1] / 2, img.size[0] / 2, (img.size[1] * 3 / 4) * (6 / 7)])
            # 识别图片获取文字
            text = pytesseract.image_to_string(crop, lang)
            if kwargs.get("text_") in join(text):
                return {"x": 1 / 4, "y": 5 / 8}
            else:
                # 传递按钮在整个页面的位置
                return {"x": 3 / 4, "y": 5 / 8}
        else:
          logging.info("定时提交必须大于当前时间5分钟")
          return {"x": 1 / 2, "y": 5 / 8}


"""

   合并字符
   
"""


def join(text):
    text_list = []
    for i in text:
        if isNotSpace(i):
            text_list.append(i)
        else:
            continue
    text = "".join(text_list)
    return text
