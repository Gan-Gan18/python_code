#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import cv2 as cv
import numpy as np

# 1.图像腐蚀
# ori_img_path = r"C:\Users\1\Desktop\test\test.jpg"
# img = cv.imread(ori_img_path)
# kernel = np.ones((5, 5), np.uint8)  # 卷积核
# result = cv.erode(img, kernel, iterations=5)  # cv.erode()实现图像腐蚀 iterations迭代次数,默认1次
# cv.imshow('result', result)
# cv.imshow('ori', img)

# 2.图像膨胀
# ori_img_path = r"C:\Users\1\Desktop\test\test.jpg"
# img = cv.imread(ori_img_path)
# kernel = np.ones((5, 5), np.uint8)  # 卷积核
# result = cv.dilate(img, kernel, iterations=1)  # cv.erode()实现图像腐蚀 iterations迭代次数,默认1次
# cv.imshow('result', result)
# cv.imshow('ori', img)

# 3.增加黑白噪声
# ori_img_path = r"C:\Users\1\Desktop\test\test.jpg"
# img = cv.imread(ori_img_path, cv.IMREAD_UNCHANGED)
# h, w, c = img.shape
# for i in range(10000):
#     x = np.random.randint(0, h)
#     y = np.random.randint(0, w)
#     # img[x, y, :] = 255  # 添加白噪声
#     img[x, y, :] = 0  # 添加黑噪声
# # cv.imwrite(r"C:\Users\1\Desktop\test\test_255.jpg", img)
# cv.imwrite(r"C:\Users\1\Desktop\test\test_0.jpg", img)

# 4.形态学开运算  去除图像白噪点 基于几何运算的滤波器
# ori_img_path = r"C:\Users\1\Desktop\test\test_255.jpg"
# img = cv.imread(ori_img_path, cv.IMREAD_UNCHANGED)
# kernel = np.ones((5, 5), np.uint8)
# result = cv.morphologyEx(img, cv.MORPH_OPEN, kernel)  # cv.morphologyEx()形态学扩展函数 调用cv.MORPH_OPEN实现开运算
# cv.imshow('result', result)

# 5.形态学闭运算  去除图像黑噪点 基于几何运算的滤波器
# ori_img_path = r"C:\Users\1\Desktop\test\test_0.jpg"
# img = cv.imread(ori_img_path, cv.IMREAD_UNCHANGED)
# kernel = np.ones((5, 5), np.uint8)
# result = cv.morphologyEx(img, cv.MORPH_CLOSE, kernel)  # cv.morphologyEx()形态学扩展函数 调用cv.MORPH_CLOSE实现闭运算
# cv.imshow('result', result)

# 6.形态学梯度运算  图像膨胀减去图像腐蚀后的结果 得到类似于图像轮廓的图形
# ori_img_path = r"C:\Users\1\Desktop\test\test.jpg"
# img = cv.imread(ori_img_path, cv.IMREAD_UNCHANGED)
# kernel = np.ones((5, 5), np.uint8)
# result = cv.morphologyEx(img, cv.MORPH_GRADIENT, kernel)  # cv.morphologyEx()形态学扩展函数 调用cv.MORPH_GRADIENT实现梯度运算
# cv.imshow('result', result)


# 7.顶帽运算  获取图像白点噪声 原始图像-开运算
# ori_img_path = r"C:\Users\1\Desktop\test\test_255.jpg"
# img = cv.imread(ori_img_path, cv.IMREAD_GRAYSCALE)
# kernel = np.ones((5, 5), np.uint8)

# open = cv.morphologyEx(img, cv.MORPH_OPEN, kernel)  # 开运算
# result = cv.morphologyEx(img, cv.MORPH_TOPHAT, kernel)  # 顶帽运算
# cv.imshow('result', result)


# 8.黑帽运算  获取图像内部小孔或前景色小黑点 闭运算图像-原始图像
ori_img_path = r"C:\Users\1\Desktop\test\test_0.jpg"
img = cv.imread(ori_img_path, cv.IMREAD_GRAYSCALE)
kernel = np.ones((5, 5), np.uint8)

result = cv.morphologyEx(img, cv.MORPH_BLACKHAT, kernel)  # 黑帽运算
cv.imshow('result', result)

cv.waitKey()
cv.destroyAllWindows()
