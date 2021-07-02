# !/usr/bin/env python
# encoding: utf-8

import os
import glob
from PIL import Image


def get_file_list():
    for file_name_1 in glob.glob(os.path.join(file_path_1, '*.png')):
        file_name_list_1.append(os.path.basename(file_name_1))

    for file_name_2 in glob.glob(os.path.join(file_path_2, '*.png')):
        file_name_list_2.append(os.path.basename(file_name_2))


def save_same_file():
    for item_1 in file_name_list_1:
        for item_2 in file_name_list_2:
            # if item_1[:-5] == item_2[:-5]:
            if item_1[:-4] == item_2:
                same_file_path = os.path.join(file_path_2, item_2)
                img = Image.open(same_file_path)
                img.save(os.path.join(save_path, item_2))
                os.remove(os.path.join(file_path_1, item_1))


if __name__ == '__main__':
    file_name_list_1 = []
    file_name_list_2 = []
    file_path_1 = r'E:\dataset\gbCoin_data\2021\20210607-ori\raw_202105210929\01\01\20210622\zhankeng'
    file_path_2 = r'D:\阿里云盘下载\202105260914\202105260914\反面'
    save_path = r'E:\dataset\gbCoin_data\2021\20210607-ori\raw_202105210929\01\01\20210622\zhankeng'
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    get_file_list()
    save_same_file()
