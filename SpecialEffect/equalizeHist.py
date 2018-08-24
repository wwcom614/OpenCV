# 直方图均衡化实际是缩小原图像中小概率像素的灰度等级范围，而拉长大概率像素的灰度等级范围，
# 使得主要像素（有用像素）的对比度增加并减小极少像素（往往为无用数据）的灰度等级范围
# 对于背景和前景都太亮或者太暗的图像非常有用，这种方法尤其是可以带来X光图像中更好的骨骼结构显示
# 以及曝光过度或者曝光不足照片中更好的细节。这种方法的一个主要优势是它是一个相当直观的技术并且是可逆操作，
# 如果已知均衡化函数，那么就可以恢复原始的直方图，并且计算量也不大。
# 这种方法的一个缺点是它对处理的数据不加选择，它可能会增加背景噪声的对比度并且降低有用信号的对比度

import cv2

def grayEqualizeHist(image):
    grayImg = cv2.cvtColor(src=image, code=cv2.COLOR_BGR2GRAY)
    return cv2.equalizeHist(src=grayImg)

def bgrEqualizeHist(image):
    (b,g,r) = cv2.split(image)
    bHist = cv2.equalizeHist(src=b)
    gHist = cv2.equalizeHist(src=g)
    rHist = cv2.equalizeHist(src=r)
    return cv2.merge(bHist,gHist,rHist)

# 原始图像 均衡化后图像 彩色图像直方图均衡化 实际上,对彩色分量rgb分别做均衡化,会产生奇异的点,图像不和谐。
# 一般采用的是用yuv空间进行亮度的均衡
def yuvEqualizeHist(image):
    imgYUV = cv2.cvtColor(image,cv2.COLOR_BGR2YCrCb)
    channelYUV = cv2.split(imgYUV)
    channelYUV[0] = cv2.equalizeHist(channelYUV[0])
    channels = cv2.merge(channelYUV)
    return cv2.cvtColor(channels,cv2.COLOR_YCrCb2BGR)