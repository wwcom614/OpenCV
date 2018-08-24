import cv2  # pip install opencv-python

#图片读取；2.封装格式解析；3.数据解码；4.数据加载
# 0:灰度读取图片，1：彩色读取图片
img = cv2.imread(r'D:\testimages\animal\dogs.jpg',1)
# 展现窗体名称
cv2.imshow('window name',img)
cv2.waitKey(0) #如果是正整数，表示等多少毫秒

# 图片写入
#有损压缩，cv2.IMWRITE_JPEG_QUALITY取值0~100，数字越小，图片压缩后存储越小，但质量越差
cv2.imwrite('dog.jpg', img, [cv2.IMWRITE_JPEG_QUALITY, 0])

#JPG是有损压缩，PNG是无损压缩，且PNG支持透明度属性。cv2.IMWRITE_PNG_COMPRESSION取值0~9，数字越大，图片压缩后存储越小，质量无损
cv2.imwrite('dog.png', img, [cv2.IMWRITE_PNG_COMPRESSION, 9])


# 像素操作
# OpenCV对图片不是使用RGB，而是使用bgr，(255,0,0)的意思是全蓝色
# img[200,100]是指的高度第200个，宽度第100个，那个像素点
(b,g,r) = img[200,100]
print((b,g,r))

for i in range(200, 500):
    img[i, 100] = (255,0,0)
cv2.imshow('window name',img)
cv2.waitKey(0) #如果是正整数，表示等多少毫秒


