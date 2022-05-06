#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import cv2 as cv
from matplotlib import pyplot as plt
img_path = r"C:\Users\1\Desktop\test\test.jpg"

# 灰度图
gray_img = cv.imread(img_path, cv.IMREAD_GRAYSCALE)
print(gray_img[20, 30])
print(gray_img.item(20, 30))  # 使用 Numpy 进行像素读取

gray_img[20, 30] = 255  # 修改像素值
print(gray_img[20, 30])

cv.imshow('gray_img', gray_img)
cv.waitKey()
cv.destroyAllWindows()

# 彩色图
color_img = cv.imread(img_path, cv.IMREAD_COLOR)
print(color_img[20, 30])
# b = color_img[20, 30, 0]
# g = color_img[20, 30, 1]
# r = color_img[20, 30, 2]

color_img[20, 30] = [0, 0, 0]  # 单点修改像素值
color_img[50:100, 50:100] = [255, 255, 255]  # 对区域修改像素值
color_img.itemset((20, 30, 0), 255)  # 使用 Numpy 修改像素 array.itemset()
color_img.itemset((20, 30, 1), 255)
color_img.itemset((20, 30, 2), 255)
print(color_img[20, 30])

# cv.imshow('color_img', color_img)
# cv.waitKey()
# cv.destroyAllWindows()
color_img2 = cv.cvtColor(color_img, cv.COLOR_BGR2RGB)  # 使用 Matplotlib 显示图像 cv.COLOR_BGR2RGB
plt.imshow(color_img2)
plt.show()
