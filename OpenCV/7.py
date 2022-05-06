#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import cv2 as cv

ori_img_path = r"C:\Users\1\Desktop\test\test.jpg"

# 二值处理 + 反二值处理
# img = cv.imread(ori_img_path)
# gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# r, d = cv.threshold(gray_img, 120, 255, cv.THRESH_BINARY)  # 二值处理 像素点>=阈值，灰度值设定最大值255 像素点<=阈值，灰度值设定最小值0
# r1, d1 = cv.threshold(gray_img, 120, 255, cv.THRESH_BINARY_INV)  # 反二值处理 同理 相反
# cv.imshow('ori', img)
# cv.imshow('result', d)
# cv.waitKey()
# cv.destroyAllWindows()

# 截断阈值化 把图片比较亮的像素处理成阈值，其他部分保持不变
# img = cv.imread(ori_img_path)
# gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# r2, d2 = cv.threshold(gray_img, 100, 255, cv.THRESH_TRUNC)  # 像素点>阈值,设定为阈值  像素点<阈值,不改变 修改比较亮的像素为阈值,其余不变
# cv.imshow('ori', img)
# cv.imshow('result', d2)
# cv.waitKey()
# cv.destroyAllWindows()

# 阈值化为0 + 反阈值化为0
img = cv.imread(ori_img_path)
gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
r3, d3 = cv.threshold(gray_img, 100, 255, cv.THRESH_TOZERO)  # 阈值化为0 像素点<阈值,设置为0 修改比较暗的部分,亮的部分不改
r4, d4 = cv.threshold(gray_img, 100, 255, cv.THRESH_TOZERO_INV)  # 反阈值化为0 同理,相反
cv.imshow('ori', img)
cv.imshow('result', d3)
cv.waitKey()
cv.destroyAllWindows()
