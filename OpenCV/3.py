#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import cv2 as cv
import numpy as np

ori_img_path = r"C:\Users\1\Desktop\test\test.jpg"
add_img_path = r'C:\Users\1\Desktop\test\test1.jpg'

# 图像加法
ori_img = cv.imread(ori_img_path, cv.IMREAD_UNCHANGED)
add_img = cv.imread(add_img_path, cv.IMREAD_UNCHANGED)
result1 = ori_img + add_img  # numpy 加法  新图像更偏绿色
result2 = cv.add(ori_img, add_img)  # cv.add 加法 新图像更偏白色
cv.imshow('ori_img', ori_img)
cv.imshow('result1', result1)
cv.imshow('result2', result2)
cv.waitKey()
cv.destroyAllWindows()

# 图像融合
ori_img = cv.imread(ori_img_path, cv.IMREAD_UNCHANGED)
add_img = cv.imread(add_img_path, cv.IMREAD_UNCHANGED)
result3 = cv.addWeighted(ori_img, 0.3, add_img, 0.7, 10)
cv.imshow('ori_img', ori_img)
cv.imshow('add_img', add_img)
cv.imshow('result3', result3)
cv.waitKey()
cv.destroyAllWindows()

# 改变颜色空间（转换通道格式）
ori_img = cv.imread(ori_img_path, cv.IMREAD_UNCHANGED)
result4 = cv.cvtColor(ori_img, cv.COLOR_BGR2GRAY)
cv.imshow('ori_img', ori_img)
cv.imshow('result4', result4)
cv.waitKey()
cv.destroyAllWindows()
