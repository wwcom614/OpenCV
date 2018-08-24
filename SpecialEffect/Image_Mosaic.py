import cv2

#图片矩形马赛克

#打马赛克的区域, 横向startX~endX， 纵向startY~endY
#这片区域内，每10*10个像素使用同一个像素替代
def mosaicImage(image, startX, endX, startY, endY):
    for areai in range(startY, endY):
        for areaj in range(startX, endX):
            #马赛克大小为10*10像素
            if areai%10==0 and areaj%10==0:
                for i in range(10):
                    for j in range(10):
                        image[areai+i,areaj+j] = image[areai,areaj]

    return  image

# 1：彩色读取图片
img = cv2.imread(r'D:\testimages\house\house3.jpg',1)
mosaicImg = mosaicImage(img,800,950,300,600)
cv2.imshow('mosaicImg',mosaicImg)
cv2.waitKey(0)

