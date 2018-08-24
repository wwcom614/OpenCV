import cv2

#图片剪切

START_X = 100
END_X = 200
START_Y = 300
END_Y = 400

def ImageCut(image, startX, endX, startY, endY):
    assert startX>0 and endX>startX and startY>0 and endY>startY
    return image[startX:endX, startY:endY]

# 1：彩色读取图片
img = cv2.imread(r'D:\testimages\animal\cat.jpg',1)
cutImg = ImageCut(img, START_X, END_X, START_Y, END_Y)
cv2.imshow('cutImg', cutImg)
cv2.waitKey(0)