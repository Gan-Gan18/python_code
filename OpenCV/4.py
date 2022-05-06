#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

ori_img_path = r"C:\Users\1\Desktop\test\test.jpg"

# 图像缩放resize 指定缩放大小
# ori_img = cv.imread(ori_img_path)
# print(ori_img.shape)  # shape 默认高,宽
# resize_img = cv.resize(ori_img, (1080, 720))  # resize shape 宽,高
# print(resize_img.shape)
# cv.imshow('ori_img', ori_img)
# cv.imshow('resize_img', resize_img)
# cv.waitKey()
# cv.destroyAllWindows()

# 图像缩放resize 按等比例缩放
# ori_img = cv.imread(ori_img_path)
# print(ori_img.shape)
# h, w = ori_img.shape[:2]
# r = 0.5
# resize_img = cv.resize(ori_img, (int(w * r), int(h * r)))
# print(resize_img.shape)
# cv.imshow('ori_img', ori_img)
# cv.imshow('resize_img', resize_img)
# cv.waitKey()
# cv.destroyAllWindows()

# 图像平移 仿射函数warpAffine()
# ori_img = cv.imread(ori_img_path)
# h, w = ori_img.shape[:2]
# tx = 50  # 平移距离tx
# ty = 100  # 平移距离ty
# M = [[1, 0, tx], [0, 1, ty]]
# affine = np.float32(M)  # 平移矩阵
# result = cv.warpAffine(ori_img, affine, (w, h))
# cv.imshow('ori_img', ori_img)
# cv.imshow('result', result)
# cv.waitKey()
# cv.destroyAllWindows()

# 图像旋转 getRotationMatrix2D()函数 warpAffine()函数
# ori_img = cv.imread(ori_img_path)
# h, w = ori_img.shape[:2]
# M = cv.getRotationMatrix2D((w / 2, h / 2), 30, 1)  # 旋转参数：旋转中心、旋转度数、图像缩放比例
# result = cv.warpAffine(ori_img, M, (w, h))  # 执行旋转：输入图、旋转参数、输出图宽高
# cv.imshow('result', result)
# cv.waitKey()
# cv.destroyAllWindows()

# 图像翻转
ori_img = cv.imread(ori_img_path)
img_1 = cv.flip(ori_img, 0)  # flipCode = 0 以 X 轴为对称轴翻转
img_2 = cv.flip(ori_img, 1)  # flipCode > 0 以 Y 轴为对称轴翻转
img_3 = cv.flip(ori_img, -1)
cv.imshow('ori_img', ori_img)
cv.imshow('img_1', img_1)
cv.waitKey()
cv.destroyAllWindows()
