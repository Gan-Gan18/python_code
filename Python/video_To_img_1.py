#!/usr/bin/env python
# coding=utf-8

import os
import cv2

# 视频路径和图片保存路径
root_path = r"E:\dataset\jcp_data\warninglight\20211015/"
videos_path = root_path + "videos"  # videos文件夹下可以包含多个子文件夹
images_path = root_path + "images"
if not os.path.exists(images_path):
    os.makedirs(images_path)

# 遍历读取视频文件---支持多级目录下的视频文件遍历
i = 0
file_count = 0
for root, dirs, files in os.walk(videos_path):
    for file_name in files:
        file_count += 1
        i += 1
        if os.path.isdir(file_name):
            continue

        # 使用“日期+后缀”对文件夹命名
        # os.mkdir(images_path + '/' + '0803_%d' % i)
        # img_full_path = os.path.join(images_path, '0803_%d' % i) + '/'
        # 使用“原视频名”对文件夹命名
        os.mkdir(images_path + '/' + file_name.split('.')[0])
        img_full_path = os.path.join(images_path, file_name.split('.')[0]) + '/'

        videos_full_path = os.path.join(root, file_name)
        cap = cv2.VideoCapture(videos_full_path)
        print('\nStart processing：' + file_name)

        # 以指定帧数抽取图片并保存
        frame_count = 0
        ret = True
        while ret:
            ret, frame = cap.read()
            frame_count += 1
            if frame_count % 1 == 0:  # 帧数
                # if frame_count < 1000:
                #     continue
                # frame = cv2.resize(frame, (1280, 720))  # 图片分辨率大小
                # name = img_full_path + "0803%d%02d.jpg" % (i, frame_count)
                name = img_full_path + file_name.split('.')[0] + "_%06d.jpg" % frame_count
                cv2.imwrite(name, frame)
print('\n******All the videos have been processed！******')
