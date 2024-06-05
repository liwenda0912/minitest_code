import pytesseract
import cv2
from PIL import Image


# 图片处理函数
def Handle_Img():
    # 打开图片
    img = cv2.imread("../picture/checkcode.png")
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
    # o = cv2.morphologyEx(img, cv2.MORPH_OPEN, k)
    c = cv2.morphologyEx(img, cv2.MORPH_CLOSE, k)
    # cv2.imshow('1', C)
    # cv2.waitKey()
    # cv2.destroyAllWindows()
    cv2.imwrite('../picture/handle.png', c)


def Get_CheckCode():
    img = Image.open('../picture/handle.png')
    crop = img.crop((10, 0, 116, 33))
    crop.save('../picture/handled.png')
    # 验证码识别
    text = pytesseract.image_to_string(crop)
    checkcode = text.strip()
    return checkcode
