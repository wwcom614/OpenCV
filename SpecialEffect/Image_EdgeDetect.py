import cv2
import numpy as np
import math

# 边缘检测需要3步处理：1.gray 2.gauss 3.canny

# 1.读取灰度图片
grayImg = cv2.imread(r'D:\testimages\house\house3.jpg',0)
# 2. 高斯滤波，可以滤除噪声点，但缺点是图像变模糊了
gaussImg = cv2.GaussianBlur(src=grayImg, ksize=(3,3), sigmaX=0)
# 3.调用canny方法, 经过卷积后，超出threshold的才显示
edgeImg = cv2.Canny(image=gaussImg, threshold1=50, threshold2=50)

cv2.imshow("edgeImg", edgeImg)
cv2.waitKey(0)

# 基于sobel算子+卷积+梯度实现边缘检测
'''
原理：
1.sobel算子模版
[1 2 1          [ 1 0 -1
 0 0 0            2 0 -2
 -1 -2 -1 ]       1 0 -1 ]
2.图片卷积 : [1 2 3 4] 与 [a b c d] 卷积： a*1+b*2+c*3+d*4 
3.阈值判决:  sqrt(a*a+b*b) > threshold
'''
def edgeDetectImage(image, threshold):
    assert threshold >0
    height = image.shape[0]
    width = image.shape[1]
    grayImg = cv2.cvtColor(src=image, code=cv2.COLOR_BGR2GRAY)
    # 注意字典第三个参数是1，每个像素点就一种元素，灰度的
    edgeImg = np.zeros(shape=(height,width,1),dtype=np.uint8)
    for i in range(height-2):
        for j in range(width-2):
            sobelx = grayImg[i,j]+grayImg[i+1,j]*2+grayImg[i+2,j]-grayImg[i,j+2]-grayImg[i+1,j+2]*2-grayImg[i+2,j+2]
            sobely = grayImg[i,j]+grayImg[i,j+1]*2+grayImg[i,j+2]-grayImg[i+2,j]-grayImg[i+2,j+1]*2-grayImg[i+2,j+2]
            gradient = math.sqrt(sobelx * sobelx + sobely * sobely)
            if gradient > threshold:
                edgeImg[i,j] = 255
            else:
                edgeImg[i,j] = 0
    return edgeImg

# 1.读取彩色图片
img = cv2.imread(r'D:\testimages\house\house3.jpg',1)
edgeImg = edgeDetectImage(img, 50)
cv2.imshow("edgeImg", edgeImg)
cv2.waitKey(0)






