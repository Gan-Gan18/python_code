#!/usr/bin/env python
# encoding: utf-8

import glob
import os
from shutil import move


def copyFile(file_path, save_dir, count, dir_name):
    # i是用来计算文件的数量，k是用来计算新建文件夹的数量
    i = 0
    k = 0

    # 如果目录不存在，则创建
    if not os.path.isdir(save_dir):
        os.makedirs(save_dir)

    # 通过glob.glob来获取原始路径下，所有'.jpg'文件
    imageList = glob.glob(os.path.join(file_path, '*.jpg'))

    for allImgDir in imageList:
        print(allImgDir)
        # 获取文件名称（包括后缀）
        imgDir = os.path.basename(allImgDir)
        # print(imgDir)

        # 拼接路径与文件名
        from_imgPath = file_path + '/' + imgDir
        # 新建的文件夹
        to_path = save_dir + "\\" + dir_name + str(k)

        # 如果 to_path 目录不存在，则创建
        if not os.path.isdir(to_path):
            os.makedirs(to_path)
        move(from_imgPath, to_path)

        i += 1
        if (i % count) == 0:
            print('新建一个文件夹')
            k += 1


if __name__ == '__main__':
    inputfile = r'E:\dataset\1224\image/'
    outfile = r'E:\dataset\1224/分组/'
    count = int('3830')
    dir_name = '1224_'
    # 指定找到文件后，另存为的文件夹路径
    save_dir = os.path.abspath(outfile)
    # 指定文件的原始路径
    file_path = os.path.abspath(inputfile)
    copyFile(file_path, save_dir, count, dir_name)
