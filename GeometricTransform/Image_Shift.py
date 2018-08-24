import cv2
import numpy as np

#图片位移

#横向移动
shift_X = 100
#纵向移动
shift_Y = 400

# 1：彩色读取图片
img = cv2.imread(r'D:\testimages\animal\cat.jpg',1)
imgInfo = img.shape
height = imgInfo[0]
width = imgInfo[1]

# 位移矩阵，关注第3个维度
matShift = np.float32([[1,0,shift_X],[0,1,shift_Y]])
# 位移关键函数和参数：cv2.warpAffine    matShift
shiftImg = cv2.warpAffine(src=img, M=matShift, dsize=(height,width))
cv2.imshow('shiftImg', shiftImg)
cv2.waitKey(0)

# 自己编码实现图片位移，shiftX横向移动，shiftY纵向移动
def shiftImage(image, shiftX, shiftY):
    shiftImg = np.zeros(image.shape,np.uint8)
    height = image.shape[0]
    width = image.shape[1]
    assert height>=shiftX>=0 and width>=shiftY>=0
    for i in range(0, height-shiftY):
        for j in range(0, width-shiftX):
            #注：Image的i是高度方向，j是宽度方向
            shiftImg[i+shiftY, j+shiftX] = image[i,j]
    return shiftImg

shiftImg = shiftImage(img, 400, 100)
cv2.imshow('shiftImg', shiftImg)
cv2.waitKey(0)
