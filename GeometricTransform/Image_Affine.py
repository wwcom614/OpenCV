import cv2
import numpy as np

#图片仿射变换

# 1：彩色读取图片
img = cv2.imread(r'D:\testimages\animal\cat.jpg',1)

height = img.shape[0]
width = img.shape[1]

#建立映射关系：左上角、左下角、右上角
matSrc = np.float32([[0,0], [0,height-1], [width-1,0]])
matDest = np.float32([[30,80], [300,height-200], [width-400,100]])

#组合
matAffine = cv2.getAffineTransform(matSrc, matDest)
affineImg = cv2.warpAffine(src=img, M=matAffine, dsize=(width, height))
cv2.imshow('affineImg',affineImg)
cv2.waitKey(0)