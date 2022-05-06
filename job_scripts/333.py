#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import os
import shutil

file_path = r'E:\dataset\ZhongChe\sdg_huohua\20220506\haju.txt'
copy_path = r'E:\dataset\ZhongChe\sdg_huohua\20220506\哈局视频'
ori_path = r'F:\中车受电弓\所有视频数据\哈局视频/'
file_list = []
video_list = []
str_file = []
data = ''
text = open(file_path, 'r', encoding='utf-8')
for line in text.readlines():
    file_list.append(line.splitlines())
for file in file_list:
    str = ''.join(file)
    str_file.append(str)

for root, dirs, files in os.walk(ori_path):
    for file_name in files:
        for file in str_file:
                if file == file_name[:-4]:
                    video_path = os.path.join(root,file_name)
                    shutil.copy(video_path,copy_path)


