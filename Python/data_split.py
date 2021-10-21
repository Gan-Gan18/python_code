#!/usr/bin/env python
# encoding: utf-8

import glob
import os
import shutil

"""
单个文件夹下 对所有文件数据按指定数量分发 并存放在不同文件夹下
"""


def split_file(ori_path, split_path, split_dir_name, each_dir_count):
    # i是用来计算文件的数量，k是用来计算新建文件夹的数量
    i = 0
    k = 1
    if not os.path.isdir(split_path):
        os.makedirs(split_path)

    imageList = glob.glob(os.path.join(ori_path, '*.png'))
    for file in imageList:
        print(file)
        save_path = split_path + split_dir_name + str(k)
        if not os.path.isdir(save_path):
            os.makedirs(save_path)
        shutil.copy(file, save_path)
        i += 1
        if (i % each_dir_count) == 0:
            k += 1


if __name__ == '__main__':
    ori_path = r'D:\熊猫币挑图20211015\test\merge/'
    split_path = r'D:\熊猫币挑图20211015\test/'
    split_dir_name = '1020_'
    each_dir_count = int('100')
    split_file(ori_path, split_path, split_dir_name, each_dir_count)
