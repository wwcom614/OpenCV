import cv2
import numpy as np

# 浮雕效果
# 灰度图片，当前像素值 - 下一个像素值 + depth的值作为当前像素值；大于255按255算；小于0按0算
def embossImage(image, depth):
    assert depth >0
    height = image.shape[0]
    width = image.shape[1]
    grayImg = cv2.cvtColor(src=image, code=cv2.COLOR_BGR2GRAY)
    # 注意字典第三个参数是1，每个像素点就一种元素，灰度的
    embossImg = np.zeros(shape=(height,width,1),dtype=np.uint8)
    for i in range(height):
        for j in range(width-1):
            currGray = int(grayImg[i,j])
            nextGray = int(grayImg[i,j+1])
            embossGray = currGray - nextGray + depth
            if embossGray > 255:
                embossGray = 255
            if embossGray < 0:
                embossGray = 0
            embossImg[i,j] = embossGray
    return embossImg

# 1.读取彩色图片
img = cv2.imread(r'D:\testimages\house\house3.jpg',1)
embossImg = embossImage(img, 150)
cv2.imshow("embossImg", embossImg)
cv2.waitKey(0)






