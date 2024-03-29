# coding: utf-8

import os
import time
import cv2
from tqdm import tqdm


def get_strdata():
    localtime = time.localtime(time.time())

    return time.strftime("%Y%m%d", localtime)


def get_file_list(root_path):
    '''
    获取root_path目录下的所有文件
    '''
    file_list = []
    for root, dirs, files in os.walk(root_path):
        for file in files:
            filename = os.path.join(root, file)
            file_list.append(filename)

    return file_list


def files_filter(files, postfixs):
    filtered_files = []
    for file in files:
        postfix = file.split('.')[1]
        if postfix.lower() in postfixs:
            filtered_files.append(file)

    return filtered_files


def video_to_images(video_file, image_save_path=None, prefix_name=None, interval=1):
    '''
    视频文件转图像文件
    :param video_path:
    :param image_name:
    :param interval:
    :return:
    '''
    if image_save_path is None:
        postfix = '.'+video_file.split('.')[1]
        image_save_path = video_file.replace(postfix, '_images')
    if not os.path.exists(image_save_path):
        os.makedirs(image_save_path)

    if prefix_name is None:
        video_name = os.path.basename(video_file).split('.')[0]
        # prefix_name = get_strdata() + '_' + video_name
        prefix_name = video_name


    cap = cv2.VideoCapture(video_file)
    frame_num = 0
    save_count = 0
    while (True and cap.isOpened()):
        ret, frame = cap.read()
        if ret:
            frame_num += 1
            if frame_num % interval == 0:
                save_name = os.path.join(image_save_path, "{}_{:0>6d}.jpg".format(prefix_name, frame_num))
                cv2.imwrite(save_name, frame)
                # print(save_name)
                save_count += 1
        else:
            break
    cap.release()


if __name__ == '__main__':
    video_path = r'E:\dataset\AR\20220715/'
    files = get_file_list(video_path)
    video_files = files_filter(files, ['mp4', 'MP4', 'mkv'])
    print(video_files)
    for i in tqdm(range(len(video_files))):
        video_to_images(video_files[i], interval=5)

    # video_file = r'E:\dataset\jcp_data\tantou\20220309\videos\cam1\192.168.31.194_01_20211126145021273_2.mp4'
    # video_to_images(video_file, interval=10)