import cv2
from matplotlib import pyplot as plt


class Picture:
    img = cv2.imread("")
    # 灰度
    img = cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY)
    img_color = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
    threshold_image = cv2.adaptiveThreshold(img_color, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
    blurred_image = cv2.GaussianBlur(img, (5, 5), 0)

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
    o = cv2.morphologyEx(img, cv2.MORPH_OPEN, k)
    C = cv2.morphologyEx(img, cv2.MORPH_CLOSE, k)
    # cv2.imshow('1', C)
    # cv2.waitKey()
    # cv2.destroyAllWindows()

    cv2.imwrite('3.png', C)
    plt.subplot(1, 4, 1)
    plt.title('Original Image')
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.subplot(1, 3, 2)
    plt.title('Blurred Image')
    plt.imshow(blurred_image, cmap='gray')
    plt.subplot(1, 3, 3)
    plt.title('Thresholded Image')
    plt.imshow(threshold_image, cmap='gray')
    plt.show()


if __name__ == '__main__':
    Picture()
