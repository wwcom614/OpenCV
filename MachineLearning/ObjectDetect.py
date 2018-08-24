import cv2
import numpy as np


# 基于OpenCV内部Hog特征提取+SVM训练出的模型进行识别,SVM学习的是Hog特征

# 1.样本准备：posNum和negNum的比例大概是1:2~1:3
# 里面包含要识别物体的图片样本数量
posNum = 820
# 里面不包含要识别物体的图片样本数量
negNum = 1931


# 2. Hog特征 超参数设置
# window，一般比图片小，一般是block整数倍，窗体在图像中滑动
winSize = (64,128)
# block模块，block在window内滑动
blockSize = (16,16)
blockStride = (8,8)
# 单元cell模块，cell在block内固定不滑动
cellSize = (8,8)
# 1个block中有4个cell
cellNum = 4
# 1个cell中包含1个圆，9个bin，每个bin 40度
binNum = 9

# 3.创建hog
hog = cv2.HOGDescriptor(winSize, blockSize, blockStride, cellSize, binNum)

# 4.从图片像素计算出hog特征中的featureArray
featureNum = int(( (winSize[0]-blockSize[0])/blockStride[0]+1) * ((winSize[1]-blockSize[1])/blockStride[1]+1) * cellNum * binNum)
print("featureNum:", featureNum)  # 3780

# 上面的前posNum行是正样本图片计算结果，后面的是negNum行负样本图片计算结果
featureArray = np.zeros(shape=((posNum+negNum), featureNum), dtype=np.float32)
labelArray = np.zeros(shape=((posNum+negNum),1), dtype=np.int32)


# 使用HOGDescriptor计算hog特征中的featureArray
# 遍历  正样本图片(包含要检测物体)
for i in range(0, posNum):
    pathFileName = "D:/video2images/pos/"+str(i+1)+".jpg"
    # 0:灰度读取图片，1：彩色读取图片
    img = cv2.imread(filename=pathFileName, flags=1)
    # 计算该图片的hog特征
    hist = hog.compute(img=img, winStride=blockStride)
    for j in range(featureNum):
        featureArray[i,j] = hist[j]
    # 都是正样本，所以都是1
    labelArray[i,0] = 1

# 遍历  负样本图片(不包含要检测物体)
for i in range(0, negNum):
    pathFileName = "D:/video2images/neg/"+str(i+1)+".jpg"
    # 0:灰度读取图片，1：彩色读取图片
    img = cv2.imread(filename=pathFileName, flags=1)
    # 计算该图片的hog特征
    hist = hog.compute(img=img, winStride=blockStride)
    for j in range(featureNum):
        # 上面的前posNum行是正样本图片计算结果，后面的是negNum行负样本图片计算结果
        featureArray[i+posNum,j] = hist[j]
    # 上面的前posNum行是正样本,下面的都是负样本，所以都是-1
    labelArray[i+posNum,0] = -1

print("featureArray:", featureArray)
print("labelArray:", labelArray)

# 6.创建SVM训练模型
svm = cv2.ml.SVM_create()
# 设置SVM模型属性
svm.setType(cv2.ml.SVM_C_SVC)  #分类器
svm.setKernel(cv2.ml.SVM_LINEAR) # 注意必须使用线性SVM进行训练，因为HogDescriptor检测函数只支持线性检测！
svm.setC(0.01)

# 7.SVM训练hog特征，最终创建myhog
# 理论参考https://blog.csdn.net/heroacool/article/details/50579955
svm.train(featureArray, cv2.ml.ROW_SAMPLE, labelArray)

# 整个过程
# 7.1 全零alpha -> alphaMat
# 7.2 全零supportVectorMat
# 7.3 resultMat = -1 * alphaMat * supportVectorMat
# 7.4 rho = svm.getDecisionFunction(0,alpha)
# 7.5 得到SVM的检测子参数myDetect = resultMat “+”  rho
# 7.6 创建myhog
# 7.7并设置SVM的检测子参数myDetect

# 7.1 全零alpha -> alphaMat
# alpha向量，如果自己训练样本，需要训练计算
alpha = np.zeros((1),np.float32)
# 支持向量矩阵
alphaMat = np.zeros((1,1),np.float32)
# 将alpha向量的数据复制到alphaMat中
alphaMat[0,0] = alpha

# 7.2 全零supportVectorMat
# 支持向量矩阵，如果自己训练样本，需要训练计算
supportVectorMat = np.zeros((1,featureNum),np.float32)

# 7.3 resultMat = -1 * alphaMat * supportVectorMat
resultMat = np.zeros((1,featureNum),np.float32)
resultMat = -1 * alphaMat * supportVectorMat

# 7.4 rho = svm.getDecisionFunction(0,alpha)
# 获得SVM的决策函数中的rho参数,即偏移量
rho = svm.getDecisionFunction(0,alpha)

# 7.5 得到SVM的检测子参数myDetect = resultMat “+”  rho
myDetect = np.zeros((featureNum+1),np.float32)
# 将resultMat中的数据复制到数组myDetector中
for i in range(0,featureNum):
    myDetect[i] = resultMat[0,i]
# 然后在最后添加偏移量rho，得到检测子
myDetect[featureNum] = rho[0]

# 7.6创建myhog
myHog = cv2.HOGDescriptor()

# 7.7并设置SVM的检测子参数myDetect
myHog.setSVMDetector(myDetect)

# 8.读入图片进行物体检测，提取预测目标的左上角坐标x，y，以及目标的宽w和高h
imgTest = cv2.imread('D:/video2images/test.jpg',1)
# hitThreshold： HOG特征与SVM最优超平面间的最大距离，大于这个值的才作为目标返回
# winStride和scale都是比较重要的参数，需要合理的设置。一个合适参数能够大大提升检测精确度，同时也不会使检测时间太长
# winStride：Hog检测窗口移动时的步长(水平及竖直)，必须是块移动blockStride的整数倍
# scale: 缩放系数，参数越小，检测时间也长。 通常scale在1.01-1.5这个区间。检测窗口是固定不变的，是待检测图像按照比例系数缩小
# padding:在原图外围添加像素，适当的pad可以提高检测的准确率（可能pad后能检测到边角的目标).常见的pad size 有(8, 8), (16, 16), (24, 24), (32, 32).gpu版本必须是(0,0)
# finalThreshold：检测结果聚类参数。
# useMeanshiftGrouping:聚类方式选择的参数
objs = myHog.detectMultiScale(img=imgTest,hitThreshold=0,winStride=blockStride, padding=(32,32),scale=1.05,finalThreshold=2)
print(objs)

x = int(objs[0][0][0])
y = int(objs[0][0][1])
w = int(objs[0][0][2])
h = int(objs[0][0][3])

# 9.在原图像将目标用绿色矩形标识
cv2.rectangle(img=imgTest, pt1=(x,y), pt2=(x+w,y+h), color=(0,255,0), thickness=2, lineType=cv2.LINE_AA)
cv2.imshow('dst',imgTest)
cv2.waitKey(0)
