# !/usr/bin/env python
# encoding: utf-8

import os
import glob
from PIL import Image
import shutil


def get_file_list():
    for file_name_1 in glob.glob(os.path.join(file_path_1, '*.jpg')):
        file_name_list_1.append(os.path.basename(file_name_1))

    for file_name_2 in glob.glob(os.path.join(file_path_2, '*.png')):
        file_name_list_2.append(os.path.basename(file_name_2))


def save_same_file():
    for item_1 in file_name_list_1:
        for item_2 in file_name_list_2:
            if item_1[:-4] == item_2[:-19]:
                same_file_path = os.path.join(file_path_2, item_2)
                shutil.move(same_file_path, save_path)
                # shutil.copy(os.path.join(file_path_1, item_1), save_path)

if __name__ == '__main__':
    file_name_list_1 = []
    file_name_list_2 = []
    file_path_1 = r'E:\dataset\jinku_data\phone\20210802\images\20210803_no720\src'
    file_path_2 = r'E:\dataset\jinku_data\phone\20210802\images\20210803_no720\label'
    save_path = r'E:\dataset\jinku_data\phone\20210802\images\20210803_no720\src'
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    get_file_list()
    save_same_file()
