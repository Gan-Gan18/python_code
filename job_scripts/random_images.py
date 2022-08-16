#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import os
import random
import shutil
import glob

"""
对文件夹下的数据随机提取 指定提取的总数量 存放于另一个路径下
"""

ori_path = r"E:\dataset\RMB_data\BaiGuo\Currency-OriginalImage2"
copy_path = r"E:\dataset\RMB_data\BaiGuo\Lable"
if not os.path.exists(copy_path):
    os.makedirs(copy_path)

# file_1 = []
# for file1 in glob.glob(os.path.join(ori_path, '*.jpg')):
#     file_1.append(file1)
# random_file = random.sample(file_1, 200)
# for temp in random_file:
#     print(temp)
#     shutil.move(temp, copy_path)

file_1 = []
for root, dirs, files in os.walk(ori_path):
    for file in files:
        file_1.append(file)
random_file = random.sample(file_1, 2000)
for temp in random_file:
    for root, dirs, files in os.walk(ori_path):
        for file in files:
            if file == temp:
                full_path = os.path.join(root, file)
                print(full_path)
                shutil.copy(full_path, copy_path)
