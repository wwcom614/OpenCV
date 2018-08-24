import cv2

# 基于OpenCV内部Haar特征+Adaboost训练出的模型进行识别

# 1. load XML
face_xml = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
eye_xml = cv2.CascadeClassifier('haarcascade_eye.xml')

# 2. load picture
img = cv2.imread(r'D:\photo\girls.jpg')

# 3.标准化彩色图片大小
from OpenCV.GeometricTransform.Image_Resize_Fixed import resizeImageFixed
scaleImg = resizeImageFixed(image=img, resizeHeight=540, resizeWidth=770)


# 5.灰度化，并直方图均衡化，去除光照暗亮影响
from OpenCV.SpecialEffect.equalizeHist import grayEqualizeHist
equalizeHistImg = grayEqualizeHist(image=scaleImg)

# 5.检测人脸:
# image必须转为灰度图像，
# scaleFactor--表示在前后两次相继的扫描中，搜索窗口的比例系数。默认为1.1即每次搜索窗口依次扩大10%
# scaleFactor缩放系数，参数越小，检测时间也长。 通常scale在1.01-1.5这个区间
# 人脸的范围大于minSize个像素，小于maxSize个像素
'''
minNeighbors--表示构成检测目标的相邻矩形的最小个数(默认为3个)。
        如果组成检测目标的小矩形的个数和小于 min_neighbors - 1 都会被排除。
        如果min_neighbors 为 0, 则函数不做任何操作就返回所有的被检候选矩形框，
        这种设定值一般用在用户自定义对检测结果的组合程序上；
'''

# 参数1：image–待检测图片，一般为灰度图像加快检测速度；
# 参数2：objects–被检测物体的矩形框向量组；
# 参数3：scaleFactor–表示在前后两次相继的扫描中，搜索窗口的比例系数。默认为1.1即每次搜索窗口依次扩大10%;
# 参数4：minNeighbors–表示构成检测目标的相邻矩形的最小个数(默认为3个)。 如果组成检测目标的小矩形的个数和小于 min_neighbors - 1 都会被排除。如果min_neighbors 为 0, 则函数不做任何操作就返回所有的被检候选矩形框；
# 参数5：flags–要么使用默认值，要么使用CV_HAAR_DO_CANNY_PRUNING，函数将会使用Canny边缘检测来排除边缘过多或过少的区域， 因为这些区域通常不会是人脸所在区域；
# 参数6、7：minSize和maxSize用来限制得到的目标区域的范围。如果视频中误检到很多无用的小方框，那么就把minSize的尺寸改大一些，默认的为30*30。
faces = face_xml.detectMultiScale(image=equalizeHistImg, scaleFactor=1.1, minNeighbors=3, minSize=(30,30))
print("图片中的人脸数量：", len(faces))

# 6.在归一化后的彩色原图像中将人脸框出来
for (fx,fy,fw,fh) in faces:
    cv2.rectangle(img=scaleImg, pt1=(fx,fy), pt2=(fx+fw,fy+fh), color=(0,255,0), thickness=2, lineType=cv2.LINE_AA)

    # 1.识别眼睛所需的图像灰色区域，肯定是人脸内，所以先把人脸选出来，灰度的
    grayFace = equalizeHistImg[fy:fy+fh, fx:fx+fw]
    # 2.检测眼睛:  image必须转为灰度图像
    eyes = eye_xml.detectMultiScale(image=grayFace)
    print("图片中的眼睛数量：", len(eyes))

    # 3.在归一化后的彩色原图像中将人脸框出来
    colorFace = scaleImg[fy:fy+fh, fx:fx+fw]
    for (ex,ey,ew,eh) in eyes:
        # 注意这个img是在colorFace基础上画框
        cv2.rectangle(img=colorFace, pt1=(ex,ey), pt2=(ex+fw,ey+eh), color=(255,0,0), thickness=2, lineType=cv2.LINE_AA)

cv2.imshow('Faces and eyes detect', scaleImg)
cv2.waitKey(0)



