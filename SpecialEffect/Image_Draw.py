import cv2
import numpy as np

# (height,width, 3或者1)
img = np.zeros(shape=(800,500,3),dtype=np.uint8)

cv2.line(img=img, pt1=(100,20), pt2=(400,20),color=(0,255,0),thickness=5, lineType=cv2.LINE_AA)
# thickness=-1是颜色填充
cv2.rectangle(img=img, pt1=(100,30), pt2=(400,120),color=(255,0,0), thickness=-1,lineType=cv2.LINE_AA)
cv2.circle(img=img, center=(250,180), radius=40, color=(0,0,255), thickness=4, lineType=cv2.LINE_AA)
# 椭圆横轴和纵轴的长度axes=(150,100)， 偏转的角度angle
cv2.ellipse(img=img, center=(250, 300), axes=(150,100), angle=0, startAngle=0, endAngle=180, color=(0,0,255), thickness=4, lineType=cv2.LINE_AA)

points = np.array([[50,400],[300,450],[280,490],[190,500],[50,400]])
points = points.reshape((-1,1,2))
cv2.polylines(img=img, pts=[points],isClosed=True, color=(0,255,255), thickness=2, lineType=cv2.LINE_AA)

cv2.putText(img=img, text="I LOVE YOU", org=(80, 550),fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1, color=(255,255,0), thickness=2, lineType=cv2.LINE_AA)

readImg = cv2.imread(r'D:\testimages\house\house3.jpg',3)

from OpenCV.GeometricTransform.Image_Resize_Ratio import resizeImage
imgCat = cv2.imread(r'D:\testimages\animal\cat.jpg',1)
resizeImg = resizeImage(imgCat, 0.1, 0.1)
height = resizeImg.shape[0]
width = resizeImg.shape[1]
for i in range(height):
    for j in range(width):
        img[i+600,j+200] = resizeImg[i,j]

cv2.imshow("img",img)
cv2.waitKey(0)