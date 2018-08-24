import cv2
import numpy as np

#图片灰度化

#方法1：读取灰度化
# 0：灰度读取图片
greyReadImg = cv2.imread(r'D:\testimages\animal\cat.jpg',0)
cv2.imshow('greyRead',greyReadImg)
cv2.waitKey(0)

#方法2：cvtColor
# 1：彩色读取图片
img = cv2.imread(r'D:\testimages\animal\cat.jpg',1)
# 颜色空间转换
cvtColorImg = cv2.cvtColor(src=img,code=cv2.COLOR_BGR2GRAY)
cv2.imshow('cvtColorImg',cvtColorImg)
cv2.waitKey(0)

#自己编写函数实现 /3平均
def grayImage1(image):
    height = image.shape[0]
    width = image.shape[1]
    grayImg = np.zeros(shape=(height, width),dtype=np.uint8)
    #灰度图片 R=G=B , (R+G+B)/3
    for i in range(height):
        for j in  range(width):
            (b,g,r) = image[i,j]
            gray = (int(b)+int(g)+int(r))/3
            grayImg[i,j] = np.uint8(gray)
    return grayImg
cv2.imshow('grayImage',grayImage1(img))
cv2.waitKey(0)

#自己编写函数实现 ，心理学算法
def grayImage2(image):
    height = image.shape[0]
    width = image.shape[1]
    grayImg = np.zeros(shape=(height, width),dtype=np.uint8)
    for i in range(height):
        for j in  range(width):
            (b,g,r) = image[i,j]
            b = int(b)
            g = int(g)
            g = int(g)
            #gray = b*0.114 + g*0.587+r*0.299
            #性能优化  >>2是除以4，<<1是乘以2
            gray = (b + (g<<1) + r)>>2
            grayImg[i,j] = np.uint8(gray)
    return grayImg
cv2.imshow('grayImage',grayImage2(img))
cv2.waitKey(0)