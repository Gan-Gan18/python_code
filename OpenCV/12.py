#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import cv2 as cv
import numpy as np

# 1.寻找图像轮廓
# ori_img_path = r"C:\Users\1\Desktop\test\test.jpg"
# img = cv.imread(ori_img_path)
# gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# ret, thresh = cv.threshold(gray_img, 127, 255, 0)
# contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
# print(len(contours))

# 2.绘制轮廓
# ori_img_path = r"C:\Users\1\Desktop\test\test.jpg"
# img = cv.imread(ori_img_path)
# gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# ret, thresh = cv.threshold(gray_img, 127, 255, 0)
# contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
# cv.drawContours(img, contours, -1, (0,255,0), 3)
# cv.imshow('draw', img)

# 3.特征矩
# ori_img_path = r"C:\Users\1\Desktop\test\test.jpg"
# img = cv.imread(ori_img_path)
# gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# ret, thresh = cv.threshold(gray_img, 127, 255, 0)
# contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
# cnt = contours[0]
# M = cv.moments(cnt)  # 获取图像矩
# print(M)
#
# cx = int(M['m10'] / M['m00'])  # 质心
# cy = int(M['m01'] / M['m00'])
# print(f'质心为：[{cx}, {cy}]')


# 4.轮廓外接矩形
ori_img_path = r"C:\Users\1\Desktop\test\test.jpg"
img = cv.imread(ori_img_path)
gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
ret, thresh = cv.threshold(gray_img, 127, 255, 0)
contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
cnt = contours[0]

x,y,w,h = cv.boundingRect(cnt)  # 外接正矩形 函数返回四个值，矩形框左上角的坐标 (x, y) 、宽度 w 和高度 h
cv.rectangle(img, (x,y),(x+w,y+h),(0,255,0),2)

min_rect = cv.minAreaRect(cnt)  # 外接最小矩形 函数返回值信息为包括中心点坐标 (x,y) ，宽高 (w, h) 和旋转角度
print(min_rect)

box = cv.boxPoints(min_rect)
box = np.int0(box)
cv.drawContours(img, [box],0,(0,0,255),2)
cv.imshow('draw',img)




cv.waitKey()
cv.destroyAllWindows()