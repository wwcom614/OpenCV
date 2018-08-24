import cv2
import numpy as np

# 颜色映射，可以定义一个大的颜色映射map；还可以用个公式

# 1.读取彩色图片
img = cv2.imread(r'D:\testimages\house\house3.jpg',1)
height = img.shape[0]
width = img.shape[1]

mapImg = np.zeros(shape=(height,width,3),dtype=np.uint8)
for i in range(height):
    for j in  range(width):
        (b,g,r) = img[i,j]
        b = b * 1.5
        if b > 255:
            b = 255
        g = g * 1.3
        if g > 255:
            g = 255
        mapImg[i,j] = (b,g,r)

cv2.imshow("img", img)
cv2.imshow("mapImg", mapImg)
cv2.waitKey(0)