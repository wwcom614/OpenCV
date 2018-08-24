import cv2
import numpy as np


#图片按比例缩放 cv2.resize
def resizeImageRatio(image, hRatio, wRatio):
    assert hRatio>0 and wRatio>0
    resizeHeight = int(image.shape[0] * hRatio)
    resizeWidth = int(image.shape[1] * wRatio)
    resizeImg = cv2.resize(src=img,dsize=(resizeWidth, resizeHeight))
    return resizeImg

# 1：彩色读取图片
img = cv2.imread(r'D:\testimages\animal\cat.jpg',1)
resizeImg = resizeImageRatio(img, 0.5, 0.5)
cv2.imshow('resizeImg', resizeImg)
cv2.waitKey(0)


#图片缩放的4种算法：最近临域插值、双线性插值、像素关系重采样、立方插值

#理解最简单的最近临域插值原理后，自己写代码实现
def NearestInsert(image, ratio):
    height = image.shape[0]
    width = image.shape[1]
    assert height>0 and width>0 and ratio>0

    resizeHeight = int(height * ratio)
    resizeWidth = int(width * ratio)

    resizeImage = np.zeros((resizeHeight,resizeWidth,3), dtype=np.uint8)#0-255

    for i in range(resizeHeight):#行
        for j in range(resizeWidth):#列
            iResize = int(i*(height*1.0/resizeHeight))
            jResize = int(j*(width*1.0/resizeWidth))
            resizeImage[i,j] = img[iResize, jResize]

    return resizeImage

imgNearestInsert = NearestInsert(img ,0.3)
cv2.imshow('imgNearestInsert:',imgNearestInsert)
cv2.waitKey(0)

# 缩放矩阵方式
def matScaleImage(image, hRatio, wRatio):
    assert hRatio>0 and wRatio>0
    matScale = np.float32([[hRatio,0,0],[0,wRatio,0]])
    resizeHeight = int(image.shape[0] * hRatio)
    resizeWidth = int(image.shape[1] * wRatio)
    scaleImg = cv2.warpAffine(src=img, M=matScale, dsize=(resizeWidth, resizeHeight))
    return scaleImg


scaleImg = matScaleImage(img, 0.8, 0.8)
cv2.imshow('scaleImg', scaleImg)
cv2.waitKey(0)

