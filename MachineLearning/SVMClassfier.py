import cv2
import numpy as np

# 学习如何使用OpenCV中的SVM
# SVM：寻求一个超平面，让分类的最近点离该超平面距离最大。
# 核函数可以将数据映射到高维空间，来解决在原始空间中线性不可分的问题

# 构造待训练样本数据，两列特征分别是身高和体重
train_girl = np.array([[155,48],[159,50],[164,53],[168,56],[172,60]])
train_boy = np.array([[155,48],[159,50],[164,53],[168,56],[172,60]])
train_data =  np.array(np.vstack((train_girl, train_boy)), dtype=np.float32)

# 训练label：0是girl，1是boy
train_label = np.array([[0],[0],[0],[0],[0],[1],[1],[1],[1],[1]])

# 构造测试数据
test_girl = np.array([167,55])
test_boy = np.array([[162,57],[162,58]])
test_data =  np.array(np.vstack((test_girl, test_boy)), dtype=np.float32)

# 测试label：0是girl，1是boy
test_label = np.array([[0],[1]])

#使用SVM之前，务必需要做数据标准化处理！使得各个维度单位一致
from sklearn.preprocessing import StandardScaler
standardScaler = StandardScaler()
standardScaler.fit(train_data)
train_data_standard = standardScaler.transform(train_data)

standardScaler.fit(test_data)
test_data_standard = standardScaler.transform(test_data)


# 创建SVM训练模型
svm = cv2.ml.SVM_create()
# 设置SVM模型属性
svm.setType(cv2.ml.SVM_C_SVC)  #分类器
svm.setKernel(cv2.ml.SVM_LINEAR) # 本次使用线性SVM核函数
svm.setC(0.01)

# 模型训练
svm.train(train_data_standard, cv2.ml.ROW_SAMPLE, train_label)

# 预测
(par1, par2) = svm.predict(test_data_standard)
print("par2:",par2)

