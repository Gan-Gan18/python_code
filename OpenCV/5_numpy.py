#!/usr/bin/env python3
# -*- coding:utf-8 -*-

'''
数据增强类型：
 旋转 翻转 裁剪 变形 缩放 平移
 颜色变换 噪声 模糊 擦除
'''

import numpy as np
import cv2 as cv
import os
import skimage
import matplotlib.pyplot as plt
from PIL import Image

# 旋转
# img_path = r'E:\dataset\gbCoin\20220211\ori'
# save_path = r'E:\dataset\gbCoin\20220211\rotate'
#
# img_list = os.listdir(img_path)
# for img in img_list:
#     ori_img = cv.imread(os.path.join(img_path, img))
#     np_img = ori_img.transpose(1, 0, 2)
#     np_img1 = np_img[::-1]
#     cv.imwrite(os.path.join(save_path, img), np_img1)


# 缩放
# img_path = r'E:\dataset\gbCoin\20220211\ori'
# save_path = r'E:\dataset\gbCoin\20220211\zoom'
#
# img_list = os.listdir(img_path)
# for img in img_list:
#     ori_img = cv.imread(os.path.join(img_path, img))  # 读图
#     h, w = ori_img.shape[0:2]  # 获取图像高宽  2048*2048
#     # print(h, w)
#     r = 0.5  # 缩放比例
#     result_h = int(h * r)
#     result_w = int(w * r)
#
#     result_images = np.zeros((result_h, result_w, 3), np.uint8)  # 创建缩放图数组矩阵
#     for x in range(0, result_h):
#         for y in range(0, result_w):
#             xNew = int(x * (w * 1.0 / result_w))
#             yNew = int(y * (h * 1.0 / result_h))
#             result_images[x, y] = ori_img[xNew, yNew]
#     cv.imwrite(os.path.join(save_path, img), result_images)


# 高斯噪声
# img_path = r'E:\dataset\gbCoin\20220211\ori'
# save_path = r'E:\dataset\gbCoin\20220211\noise'
#
# img_list = os.listdir(img_path)
# for img in img_list:
#     ori_img = cv.imread(os.path.join(img_path, img))
#     img_data = np.array(ori_img)
#     img_noise = skimage.util.random_noise(img_data, mode='gaussian')  # seed=None, var=(30 / 255) ** 2
#     array2img = Image.fromarray(np.uint8(img_noise*255)).convert('RGB')
#     array2img.save(os.path.join(save_path, img))


# 裁剪
img_path = r'E:\dataset\gbCoin\20220211\ori'
save_path = r'E:\dataset\gbCoin\20220211\crop'

img_list = os.listdir(img_path)
for img in img_list:
    ori_img = Image.open(os.path.join(img_path, img))
    img_data = np.array(ori_img)
    crop_img = img_data[1000:1500, 1000:1500]
    array2img = Image.fromarray(crop_img)
    array2img.save(os.path.join(save_path, img))
