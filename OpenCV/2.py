#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import cv2 as cv
import numpy as np

img_path = r"C:\Users\1\Desktop\test\test.jpg"

# 图像形状（宽 高 通道数）
color_img = cv.imread(img_path, cv.IMREAD_ANYCOLOR)
print(color_img.shape)
gray_img = cv.imread(img_path, cv.IMREAD_GRAYSCALE)
print(gray_img.shape)

# 图像像素数量 size
color_img = cv.imread(img_path, cv.IMREAD_ANYCOLOR)
print(color_img.size)
gray_img = cv.imread(img_path, cv.IMREAD_GRAYSCALE)
print(gray_img.size)

# 图像类型 dtype
color_img = cv.imread(img_path, cv.IMREAD_ANYCOLOR)
print(color_img.dtype)
gray_img = cv.imread(img_path, cv.IMREAD_GRAYSCALE)
print(gray_img.dtype)

# ROI 感兴趣区域
color_img = cv.imread(img_path, cv.IMREAD_UNCHANGED)
roi_img = color_img[100:500,500:1000] # 获取 ROI 区域
color_img[50:450,100:600]=roi_img  # 将ROI区域像素值赋值给原图指定区域，合成一张图像
cv.imshow('color_img',color_img)
cv.imshow('roi_img',roi_img)
cv.waitKey()
cv.destroyAllWindows()

# 拆分图像通道
color_img = cv.imread(img_path, cv.IMREAD_UNCHANGED)
b, g, r = cv.split(color_img)  # 使用 cv.split 拆分 耗时
# b1 = color_img[:, :, 0]  # 使用 numpy索引 拆分
# g1 = color_img[:, :, 1]
# r1 = color_img[:, :, 2]
cv.imshow('B', b)
cv.imshow('G', g)
cv.imshow('R', r)
cv.waitKey()
cv.destroyAllWindows()

# 合并图像通道
color_img = cv.imread(img_path, cv.IMREAD_UNCHANGED)
b, g, r = cv.split(color_img)  # 使用 cv.split 拆分
m = cv.merge([b, g, r])  # 使用 cv.merge 合并
cv.imshow('merge', m)
cv.waitKey()
cv.destroyAllWindows()

# 提取单通道
color_img = cv.imread(img_path, cv.IMREAD_UNCHANGED)
rows, cols, chn = color_img.shape
b = color_img[:, :, 0]
g = np.zeros((rows, cols), dtype=color_img.dtype)
r = np.zeros((rows, cols), dtype=color_img.dtype)

m = cv.merge([b, g, r])
cv.imshow('merge', m)
cv.waitKey()
cv.destroyAllWindows()
