#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import os
import random
import shutil
import glob

"""
对文件夹下的数据随机提取 指定提取的总数量 存放于另一个路径下
"""

ori_path = r"Y:\Data\ZNJT\ZhongChe_sdg_huohua\RawData\images\20220328_AF-BF\运行收集视频数据\CR400BF-images_croped"
copy_path = r"Y:\Data\ZNJT\ZhongChe_sdg_huohua\RawData\images\20220328_AF-BF\DetectData\crop"
if not os.path.exists(copy_path):
    os.makedirs(copy_path)

file_1 = []
for file1 in glob.glob(os.path.join(ori_path, '*.jpg')):
    file_1.append(file1)

random_file = random.sample(file_1, 200)
for temp in random_file:
    # for file2 in glob.glob(os.path.join(ori_path, '*.json')):
    #     if temp.split('.')[0] == file2.split('.')[0]:
    print(temp)
    shutil.move(temp, copy_path)
            # shutil.move(file2, copy_path)
