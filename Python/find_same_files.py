# !/usr/bin/env python
# encoding: utf-8

import os
import glob
from PIL import Image
import shutil


def get_file_list():
    for file_name_1 in glob.glob(os.path.join(file_path_1, '*.jpg')):
        file_name_list_1.append(os.path.basename(file_name_1))

    for file_name_2 in glob.glob(os.path.join(file_path_2, '*.json')):
        file_name_list_2.append(os.path.basename(file_name_2))


def save_same_file():
    for item_1 in file_name_list_1:
        for item_2 in file_name_list_2:
            if item_1[:-4] == item_2[:-5]:
                same_file_path = os.path.join(file_path_2, item_2)
                print(same_file_path)
                # img = Image.open(same_file_path)
                # img.save(os.path.join(save_path, item_2))
                # os.remove(os.path.join(file_path_1, item_1))
                shutil.copy(same_file_path, save_path)
                shutil.copy(os.path.join(file_path_1, item_1), save_path)

if __name__ == '__main__':
    file_name_list_1 = []
    file_name_list_2 = []
    file_path_1 = r'E:\dataset\DiTie_data\hand\check_0706\merge\visualize_json\hand'
    file_path_2 = r'E:\dataset\DiTie_data\hand\check_0706\merge\visualize_json\ori'
    save_path = r'E:\dataset\DiTie_data\hand\check_0706\merge\visualize_json\result'
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    get_file_list()
    save_same_file()
