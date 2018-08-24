import cv2
import random
import numpy as np

#图片加毛玻璃效果

#用该像素附近8*8个像素中的某个像素替代
def frostedGlassImage(image):
    height = image.shape[0]
    width = image.shape[1]
    #用该像素附近8*8个像素中的某个像素替代
    frostedGlassImg = np.zeros(shape=(height,width,3),dtype=np.uint8)
    for i in range(0, height-8):
        for j in range(0, width-8):
            randomInt8 = int(random.random() * 8) #0~8
            frostedGlassImg[i,j] = image[i+randomInt8,j+randomInt8]

    return  frostedGlassImg

# 1：彩色读取图片
img = cv2.imread(r'D:\testimages\house\house1.jpg',1)
frostedGlassImg = frostedGlassImage(img)
cv2.imshow('frostedGlassImg',frostedGlassImg)
cv2.waitKey(0)

