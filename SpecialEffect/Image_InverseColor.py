import cv2
import numpy as np

# 灰度图片颜色反转   255-当前颜色值
def inverseGray(image):
    height = image.shape[0]
    width = image.shape[1]
    inverseGrayImage = np.zeros(shape=(height,width,1),dtype=np.uint8)

    for i in range(height):
        for j in range(width):
            grayPixel = 255- image[i,j]
            inverseGrayImage[i,j] = grayPixel
    return inverseGrayImage


# 彩色图片颜色反转   255-当前颜色值
def inverseColor(image):
    height = image.shape[0]
    width = image.shape[1]
    inverseColorImage = np.zeros(shape=(height,width,3),dtype=np.uint8)

    for i in range(height):
        for j in range(width):
            (b,g,r) = image[i,j]
            inverseColorImage[i,j] = (255-b, 255-g, 255-r)
    return inverseColorImage

# 0：灰度读取图片
greyReadImg = cv2.imread(r'D:\testimages\animal\cat.jpg',0)
inverseGrayImg = inverseGray(greyReadImg)
cv2.imshow('inverseGrayImg',inverseGrayImg)
cv2.waitKey(0)

# 1：彩色读取图片
img = cv2.imread(r'D:\testimages\animal\cat.jpg',1)
inverseColorImg = inverseColor(img)
cv2.imshow('inverseColorImg',inverseColorImg)
cv2.waitKey(0)