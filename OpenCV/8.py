#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

# 1.加噪声
# ori_img_path = r"C:\Users\1\Desktop\test\test.jpg"
# img = cv.imread(ori_img_path)
# h, w, c = img.shape
# for i in range(10000):
#     x = np.random.randint(0, h)
#     y = np.random.randint(0, w)
#     img[x, y, :] = 255
# cv.imwrite(r'C:\Users\1\Desktop\test\test_noise.jpg',img)

# 2.2D图像卷积 去除噪点效果较好 处理后的图片变模糊
# ori_img_path = r"C:\Users\1\Desktop\test\test_noise.jpg"
# img = cv.imread(ori_img_path, cv.IMREAD_UNCHANGED)
# kernel = np.ones((5, 5), np.float32) / 25
# result = cv.filter2D(img, -1, kernel)
# cv.imshow('result', result)
# cv.imshow('ori', img)


# 3.均值滤波 输入的核越大,降噪效果越好,同时图片越模糊
# ori_img_path = r"C:\Users\1\Desktop\test\test_noise.jpg"
# img = cv.imread(ori_img_path, cv.IMREAD_UNCHANGED)
# img_blur = cv.blur(img, (3,3))  # cv.blur()实现均值滤波
# cv.imshow('img_blur', img_blur)
# cv.imshow('ori', img)


# 4.方框滤波 若不进行归一化处理,图像像素溢出为白色
# ori_img_path = r"C:\Users\1\Desktop\test\test_noise.jpg"
# img = cv.imread(ori_img_path, cv.IMREAD_UNCHANGED)
# img_boxfilter = cv.boxFilter(img, -1, (5, 5), normalize=1)  # cv.boxFilter()实现方框滤波  归一化处理
# cv.imshow('img_boxfilter', img_boxfilter)
# cv.imshow('ori', img)


# 5.高斯滤波
# ori_img_path = r"C:\Users\1\Desktop\test\test_noise.jpg"
# img = cv.imread(ori_img_path, cv.IMREAD_UNCHANGED)
# img_gaussianblur = cv.GaussianBlur(img, (5, 5), 0)  # cv.GaussianBlur()实现高斯滤波  核大小必须为奇数 0为X方向方差,控制权重
# cv.imshow('img_gaussianblur', img_gaussianblur)
# cv.imshow('ori', img)


# 6.中值滤波 对原图像降噪后还原度较高,清晰度较高
ori_img_path = r"C:\Users\1\Desktop\test\test_noise.jpg"
img = cv.imread(ori_img_path, cv.IMREAD_UNCHANGED)
img_medianblur = cv.medianBlur(img, 3)  # cv.medianBlur()实现中值滤波  核大小必须为奇数
cv.imshow('img_medianblur', img_medianblur)
cv.imshow('ori', img)


cv.waitKey()
cv.destroyAllWindows()