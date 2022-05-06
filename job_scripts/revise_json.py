#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import json
import os
import glob
import shutil

"""
批量修改json文件中的标签名、文件名等...
解决在标注过程中将标签名打错,或后期处理时临时需要更改原文件名等问题...
"""


def revise_json(ori_json_file, revise_json_file):
    ori_file = open(ori_json_file, "r")
    revise_file = open(revise_json_file, "w")

    json_data = json.load(ori_file)
    imagePath = json_data["imagePath"]
    # new_imagePath = imagePath.split(".")[0]
    basename = os.path.basename(ori_json_file)
    new_imagePath = basename.split('.')[0]
    json_data["imagePath"] = new_imagePath + '.jpg'

    revise_file.write(json.dumps(json_data))
    ori_file.close()
    revise_file.close()


def copy_newJson():
    for newJson_file in os.listdir(revise_filePath):
        shutil.copy(os.path.join(revise_filePath, newJson_file), ori_filePath)
    shutil.rmtree(revise_filePath)


if __name__ == '__main__':
    ori_filePath = r'E:\dataset\jcp_data\tantou\20211208\2/'
    revise_filePath = r'E:\dataset\jcp_data\tantou\20211208\3/'
    if not os.path.exists(revise_filePath):
        os.makedirs(revise_filePath)

    for json_file in glob.glob(os.path.join(ori_filePath, '*.json')):
        ori_json_file = json_file
        # print(os.path.basename(ori_json_file))
        revise_json_file = revise_filePath + os.path.basename(json_file)
        print(revise_json_file)
        revise_json(ori_json_file, revise_json_file)
    copy_newJson()
