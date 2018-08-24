学习图像处理OpenCV时，动手编码实践。

## GeometricTransform 
图像处理常用的一些几何变换操作
- Image_Read_Write.py：  
初识OpenCV，读写图片的基本操作。

- Image_Cut.py：  
图片剪切，可用于识别图像中人脸或者物体后剪切作为样本。

- Image_Mirror.py  
图片的水平镜像和垂直镜像。

- Image_Affine.py
尝试使用opencv仿射矩阵对图像进行仿射变换。

- Image_Rotate.py  
尝试使用OpenCV的旋转函数或仿射变换对图片进行旋转。 

- Image_Resize_Fixed.py、Image_Resize_Ratio.py  
尝试对图片大小进行固定大小或按比例缩放，固定方式可用于对图片大小归一化。

- Image_Shift.py
尝试对图像进行移动，仿射变换函数移动。

## SpecialEffect
-  Image_Mosaic.py  
给某区域打马赛克，实际是区域内某小块区域用某像素点替代。

-  Image_FrostedGlass.py  
毛玻璃效果，实际是区域内某小块区域使用随机像素点替代。

-  Image_Gray.py
彩色图片灰度化，用于某些图像识别前简化处理数据。b
  

-  Image_EdgeDetect.py
边缘检测，用于锐化图像，突出图像细节，更便于识别。

-  equalizeHist.py
直方图均衡化，用于去除图像光照影响，更便于识别。

-  Image_Draw.py
在图像上画线、矩形等形状，用于识别某物体后在原始图像上标注。

## VideoAndImage
- VideoToImage.py  
经常很难获取到大量样本图片，可以拍一段视频，然后用视频抽帧转为大量图片作为样本，封装了一个函数。
主要还是为了熟悉OpenCV，其实OpenCV底层使用的是ffmpeg，可以直接使用ffmpeg命令将视频抽帧为图片。

## MachineLearning
-  SVMClassfier.py  
手工构造了身高、体重数据，区分男孩、女孩，主要是尝试opencv提供的SVM函数进行分类。

-  FaceAndEyeDetect.py 
基于OpenCV内部Haar特征+Adaboost训练出的模型进行人脸识别+眼睛识别。识别之前，先标准化彩色图片大小；
然后灰度化，并直方图均衡化，去除光照暗亮影响。
经测试对比haarcascade_frontalface_alt.xml效果在opencv人脸识别中效果最好。
人脸识别后基于opencv画矩形标识人脸，并在标识区域继续识别人眼，然后画矩形标识。

-  ObjectDetect.py
基于opencv的物体检测。从各个角度拍了一段短视频(含光线变化)，视频中有某物体，然后将该视频抽帧成图片，作为含物体的正样本。
网上找了一些图片，不含该物体，作为负样本。正负样本比例大概是1:2~1:3。
基于OpenCV内部Hog特征提取+SVM训练出的模型进行识别,SVM学习的是Hog特征。模型训练好后，找一张含该物体的图片进行识别，并画矩形标识。
