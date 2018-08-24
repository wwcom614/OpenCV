import cv2
import numpy as np

# 2张图片某部分融合

#融合占比，第1张图片占RATIO，第2张图片占1-RATIO
RATIO=0.4

car1Image = cv2.imread(r'D:\testimages\car\car1.jpg',1)
car4Image = cv2.imread(r'D:\trainimages\car\car4.jpg',1)

from OpenCV.GeometricTransform.Image_Cut import ImageCut
car1ImageCut = ImageCut(car1Image,200,800,100,600)
car4ImageCut = ImageCut(car4Image,200,800,100,600)

mergeImg = np.zeros(shape=(600,500),dtype=np.uint8)
mergeImg = cv2.addWeighted(src1=car1ImageCut,alpha=RATIO, src2=car4ImageCut,beta=1-RATIO,gamma=0)
cv2.imshow("mergeImg",mergeImg)
cv2.waitKey(0)
