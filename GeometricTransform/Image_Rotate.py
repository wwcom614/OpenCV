import cv2
import numpy as np

#图片旋转

# 1：彩色读取图片
img = cv2.imread(r'D:\testimages\animal\cat.jpg',1)

height = img.shape[0]
width = img.shape[1]

#旋转矩阵：旋转中心点center  角度angle  缩放scale
matRotate = cv2.getRotationMatrix2D(center=(height*0.5, width*0.5), angle=45, scale=0.5)
rotateImg = cv2.warpAffine(src=img, M=matRotate, dsize=(width, height))
cv2.imshow('rotateImg',rotateImg)
cv2.waitKey(0)