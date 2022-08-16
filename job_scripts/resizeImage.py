# -*- coding: utf-8 -*-
import os
import cv2


"""
按指定分辨率批量缩放图片
"""
rootPath = r'E:\dataset\RMB_data\BaiGuoHuoBi\guohui+code\20220627\20220629/'
ori_imageFold = rootPath + '1/'
resize_imageFold = rootPath + 'imgResize/'
if not os.path.exists(resize_imageFold):
    os.makedirs(resize_imageFold)

ratio = 0.5
fileList = os.listdir(ori_imageFold)
for file in fileList:
    imgFileName = ori_imageFold + file
    imageData = cv2.imread(imgFileName)
    h, w, c = imageData.shape

    reH, reW = int(ratio*h), int(ratio*w)
    # reH, reW = 1024, 1024
    imageDataResize = cv2.resize(imageData, (reW, reH), cv2.INTER_NEAREST)
    cv2.imwrite(resize_imageFold + file, imageDataResize)
    print(str(h) + ' ' + str(w) + '>>>>>' + str(reH) + ' ' + str(reW))
