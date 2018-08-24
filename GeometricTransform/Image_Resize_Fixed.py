import cv2
import numpy as np

#图片缩放到固定大小 cv2.resize
def resizeImageFixed(image, resizeHeight=480, resizeWidth=640):
    assert resizeHeight>0 and resizeWidth>0
    resizeHeight = int(resizeHeight)
    resizeWidth = int(resizeWidth)
    resizeImg = cv2.resize(src=image,dsize=(resizeWidth, resizeHeight))
    return resizeImg


