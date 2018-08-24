# -*-  coding: UTF-8 -*-

import cv2

# 经常很难获取到大量样本图片，可以拍一段视频，然后用视频抽帧转为大量图片，封装个函数吧

# pathVideo:视频文件完整路径和名称；
# interval: 视频采样间隔，每多少帧采集一张
# picNum: 打算采样图片数
# 采样输出的图片路径
def video2Images(pathVideo, interval=1, picNum=10, outPath="D:/video2images/"):
    assert interval > 0 and picNum > 0
    video = cv2.VideoCapture(pathVideo)
    if(video.isOpened):
        fps, width, height, totalFrame = videoFpsWidthHeight(video)
        print(pathVideo,"is opend!", " fps:",fps, ", width:",width, ", height:",height,", totalFrame:",totalFrame)
        if (totalFrame//interval < picNum):
            picNum = totalFrame//interval
            print("该视频使用采样间隔interval：%d ,最多只能采集 %d 张图片！" %(interval, picNum))
        i = 0
        p = 0  #当前已采集图片数量
        while(p < picNum):
            if(i % interval == 0):
                (flag, frame) = video.read()
                # flag为True表示读取成功
                if(flag):
                    p += 1
                    pathFileName = outPath + 'image' + str(p) + '.jpg'
                    #有损压缩，cv2.IMWRITE_JPEG_QUALITY取值0~100，数字越小，图片压缩后存储越小，但质量越差
                    cv2.imwrite(filename=pathFileName, img=frame, params=[cv2.IMWRITE_JPEG_QUALITY,100])
                    print("已采集图片 %d / %d" %(p, picNum))
                else:
                    print("视频读取第%d帧失败！")
            i += 1



# 获取一个可以打开视频的 fps、宽和高
def videoFpsWidthHeight(video):
    assert video.isOpened
    fps = video.get(cv2.CAP_PROP_FPS)
    width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
    totalFrame = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
    return fps, width, height, totalFrame

# 测试一下是否OK
video2Images(pathVideo='D:/video2images/1.mp4',interval=10, picNum=20)