import pytesseract
from PIL import Image


def cut_img_by_xy(path1, x_min, x_max, y_min, y_max, path2):
    img = Image.open(path1)
    crop = img.crop((x_min, y_min, x_max, y_max))
    crop.save(path2)


if __name__ == "__main__":
    img_path = '1.png'
    # 转换通道
    img = Image.open(img_path)
    w, h = img.size
    img = img.convert("RGB")
    img.save(img_path)
    # 切割小图片
    # 整体切割.
    print(w, h)
    cut_img_by_xy(img_path, 20, 46, 0, 34, "2.jpg")
    cut_img_by_xy(img_path, 47, 68, 0, 34, "3.jpg")
    cut_img_by_xy(img_path, 68, 88, 0, 34, "4.jpg")
    cut_img_by_xy(img_path, 88, 111, 0, 34, "5.jpg")

