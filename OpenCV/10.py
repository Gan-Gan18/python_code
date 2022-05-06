#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import cv2 as cv
import numpy as np

"""
边缘检测是基于灰度突变来分割图像的常用方法，实质是提取图像中不连续部分的特征
目前常见边缘检测算子有差分算子、Roberts算子、Sobel算子、Prewitt算子、Log 算子以及Canny 算子等
边缘检测是为了简化图像，通过边缘信息来代表图像携带的信息
"""

# 1. Canny算子边缘检测
'''
第一步：高斯滤波  对待滤波的像素点及其邻域点的灰度值进行加权平均，有效滤去图像中叠加的高频噪声
第二步：计算梯度图像与角度图像  图像当前像素点在 x 轴和 y 轴的斜切率的变化率，像素灰度值的变化率（相邻像素的加减）
第三步：对梯度图像进行非极大值抑制   使用非极大值抑制来寻找像素点局部最大值，将非极大值所对应的灰度值置0，剔除大部分非边缘像素点
第四步：滞后双阈值   若某一像素位置的幅值超过高阈值，该像素保留为边缘像素；小于高阈值，该像素被排除；在两者之间，该像素在连接到一个高于高阈值的像素时被保留
'''
# ori_img_path = r"C:\Users\1\Desktop\test\test.jpg"
# img = cv.imread(ori_img_path, 0)
# edges = cv.Canny(img, 100, 200)
# cv.imshow('edges', edges)


# 2.Roberts 算子
'''
利用局部差分算子寻找边缘,采用对角线方向相邻两象素之差近似梯度幅值检测边缘
检测垂直边缘的效果好于斜向边缘，定位精度高，对噪声敏感，无法抑制噪声的影响
采用 2 * 2 模板对区域内像素值进行计算
'''
# ori_img_path = r"C:\Users\1\Desktop\test\test.jpg"
# img = cv.imread(ori_img_path, cv.COLOR_BGR2GRAY)
# grayimg = cv.cvtColor(img, cv.COLOR_BGR2GRAY)  # 转灰度
#
# kernelx = np.array([[-1, 0], [0, 1]], dtype=int)  # 构建卷积核   2*2
# kernely = np.array([[0, -1], [1, 0]], dtype=int)
# x = cv.filter2D(grayimg, cv.CV_16S, kernelx)  # 对灰度图进行卷积运算
# y = cv.filter2D(grayimg, cv.CV_16S, kernely)
#
# absX = cv.convertScaleAbs(x)  # 计算x,y方向的绝对值 转换为uint8
# absY = cv.convertScaleAbs(y)
# roberts = cv.addWeighted(absX, 0.5, absY, 0.5, 0)  # 图像融合
# cv.imshow('src', img)
# cv.imshow('roberts', roberts)


# 3.Prewitt 算子
'''
利用像素点上下、左右邻点的灰度差在边缘处达到极值检测边缘
去掉部分伪边缘，对噪声具有平滑作用,适合用来识别噪声较多、灰度渐变的图像
采用 3 * 3 模板对区域内像素值进行计算
'''
# ori_img_path = r"C:\Users\1\Desktop\test\test.jpg"
# img = cv.imread(ori_img_path, cv.COLOR_BGR2GRAY)
# grayimg = cv.cvtColor(img, cv.COLOR_BGR2GRAY)  # 转灰度
#
# kernelx = np.array([[1, 1, 1], [0, 0, 0], [-1, -1, -1]], dtype=int)  # 构建卷积核  3*3
# kernely = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]], dtype=int)
# x = cv.filter2D(grayimg, cv.CV_16S, kernelx)  # 对灰度图进行卷积运算
# y = cv.filter2D(grayimg, cv.CV_16S, kernely)
#
# absX = cv.convertScaleAbs(x)  # 计算x,y方向的绝对值 转换为uint8
# absY = cv.convertScaleAbs(y)
# Prewitt = cv.addWeighted(absX, 0.5, absY, 0.5, 0)  # 图像融合
# cv.imshow('src', img)
# cv.imshow('roberts', Prewitt)


# 4.Sobel 算子
'''
离散微分算子,结合高斯平滑和微分求导 增加权重概念
相邻点的距离远近对当前像素点的影响不同，距离越近对应当前像素的影响越大，实现图像锐化并突出边缘轮
根据像素点上下、左右邻点灰度加权差，在边缘处达到极值检测边缘，对噪声具有平滑作用，结果具有更多的抗噪性，常用于对精度要求不高的处理
'''
# ori_img_path = r"C:\Users\1\Desktop\test\test.jpg"
# img = cv.imread(ori_img_path, cv.COLOR_BGR2GRAY)
# grayimg = cv.cvtColor(img, cv.COLOR_BGR2GRAY)  # 转灰度
#
# x = cv.Sobel(grayimg, cv.CV_16S, 1, 0)  # Sobel算子
# y = cv.Sobel(grayimg, cv.CV_16S, 0, 1)
#
# absX = cv.convertScaleAbs(x)  # 计算x,y方向的绝对值 转换为uint8
# absY = cv.convertScaleAbs(y)
# Sobel = cv.addWeighted(absX, 0.5, absY, 0.5, 0)  # 图像融合
# cv.imshow('src', img)
# cv.imshow('roberts', Sobel)


# 5.Laplacian 算子
'''
Laplacian算子常用于图像增强领域和边缘提取,判断图像中心像素灰度值与它周围其他像素的灰度值
如果中心像素灰度更高，则提升中心像素的灰度；反之降低中心像素的灰度，从而实现图像锐化操作
对邻域中心像素的四方向或八方向求梯度，再将梯度相加判断中心像素灰度与邻域内其他像素灰度的关系，最后通过梯度运算的结果对像素灰度进行调整
四邻域是对邻域中心像素的四方向求梯度，八邻域是对八方向求梯度
'''
ori_img_path = r"C:\Users\1\Desktop\test\test.jpg"
img = cv.imread(ori_img_path, cv.COLOR_BGR2GRAY)
grayimg = cv.cvtColor(img, cv.COLOR_BGR2GRAY)  # 转灰度

result = cv.Laplacian(grayimg, cv.CV_16S, ksize=3)  # laplacian 算子
result_laplacian = cv.convertScaleAbs(result)  # 计算绝对值 转换为uint8

cv.imshow('src', img)
cv.imshow('laplacian', result_laplacian)

cv.waitKey()
cv.destroyAllWindows()
