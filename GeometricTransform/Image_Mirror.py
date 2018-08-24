# -*-  coding: UTF-8 -*-

import cv2
import numpy as np

#图片镜像

# 1：彩色读取图片
img = cv2.imread(r'D:\testimages\plane\plane1.jpg',1)

# V是垂直镜像，H是水平镜像
def mirrorImage(image, direction):
    assert direction == "V" or "H"
    height = image.shape[0]
    width = image.shape[1]
    deep = image.shape[2]
    if (direction == "V"): #垂直方向镜像
        mirImage = np.zeros((height*2, width, deep), np.uint8) #0~255
        for i in range(0, height):
            for j in range(0, width):
                #注：Image的i是高度方向，j是宽度方向
                mirImage[i, j] = image[i,j]
                mirImage[height*2-i-1,j] = image[i,j]
        for j in range(width): #镜像分割线
            mirImage[height, j] = (0,255,0) #bgr
    elif(direction == "H"):#水平方向镜像
        mirImage = np.zeros((height, width*2, deep), np.uint8) #0~255
        for i in range(0, height):
            for j in range(0, width):
                #注：Image的i是高度方向，j是宽度方向
                mirImage[i, j] = image[i,j]
                mirImage[i, width*2-j-1] = image[i,j]
        for i in range(height): #镜像分割线
            mirImage[i, width] = (0,255,0) #bgr
    else:
        return "please input V(垂直镜像) or H（水平镜像）"

    return mirImage

vMirrorImg = mirrorImage(img, direction='V')
cv2.imshow('vMirrorImg', vMirrorImg)
cv2.waitKey(0)

hMirrorImg = mirrorImage(img, direction='H')
cv2.imshow('hMirrorImg', hMirrorImg)
cv2.waitKey(0)