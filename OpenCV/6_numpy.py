#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import numpy as np
from PIL import Image
import os
import json
import io
from matplotlib import pyplot as plt
import shutil

ori_label_path = r'E:\dataset\jcp_data\20220323/'
save_path = r'E:\dataset\jcp_data\20220323result/'
img_file = []
for file in os.listdir(ori_label_path):
    if file.split('.')[1] == 'jpg':
        img_file.append(file)
for img in img_file:
    img_file_fullPath = ori_label_path + img
    # print(img_file_fullPath)
    images = np.array(Image.open(img_file_fullPath))
    y, x = images.shape[:2]
    # print(y, x)
    json_file_fullPath = ori_label_path + '%s.json' % img.split('.')[0]
    load_json_file = json.load(io.open(json_file_fullPath, "r", encoding="utf-8"))
    # bbox_count = 0
    for multi in load_json_file["shapes"]:
        points = np.array(multi["points"])
        xmin = int(min(points[:, 0]))  # 取数组第0列所有元素中最小值
        xmax = int(max(points[:, 0]))
        ymin = int(min(points[:, 1]))
        ymax = int(max(points[:, 1]))
        if xmax > int(x) or ymax > int(y):
            with open(r'E:\dataset\jcp_data\result.txt','a') as f:
                f.write(img + '\n')
            shutil.copy(img_file_fullPath, save_path)
            # shutil.copy(json_file_fullPath, save_path)
            print(img)







    #     crop_img = images[ymin:ymax, xmin:xmax]
    # crop_img = images[618:700, 459:685]
    # array2img = Image.fromarray(crop_img)
    # array2img.save(save_path + '%s' % (img.split('.')[0]) + '.jpg')
        # bbox_count += 1