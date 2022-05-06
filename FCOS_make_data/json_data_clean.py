# coding: utf-8

import os
import shutil

def get_file_list(root_path, postfix=None):
    '''
    获取root_path目录下的所有后缀名为postfix的文件
    '''
    file_list = []
    for root, dirs, files in os.walk(root_path):
        for file in files:
            filename = os.path.join(root, file)
            file_list.append(filename)
    # print(file_list)

    if postfix:
        file_list = list(filter(lambda filename: filename.endswith(postfix), file_list))

    return file_list


if __name__ == '__main__':
    root_dir = r'E:\dataset\jinku_data\20211224\output_image\20211227\1\visualize_json'
    dirs = os.listdir(root_dir)
    dirs = [os.path.join(root_dir, dir) for dir in dirs]
    dirs = [dir for dir in dirs if os.path.isdir(dir) and 'ori' not in dir]
    dirs = [dir for dir in dirs if os.path.isdir(dir) and 'result' not in dir] # ori：原始数据 result: 存放结果
    fileset_list = []
    # print("dirs: ", dirs)
    for dir in dirs:
        file_list = get_file_list(dir)
        basename_list = [os.path.basename(file) for file in file_list]
        # print(basename_list)
        fileset_list.append(set(basename_list))
try:
    common_fileset = fileset_list[1]

    for fileset in fileset_list:
        # print(fileset)
        common_fileset = common_fileset | fileset
    # print(common_fileset)
    save_dir = os.path.join(root_dir, 'result')
    if os.path.exists(save_dir):
        shutil.rmtree(save_dir)
    os.mkdir(save_dir)
    for file in common_fileset:
        image_file = os.path.join(root_dir, 'ori', file)
        if "Thumbs.db" in image_file:
            continue
        shutil.copy(image_file, save_dir)

        json_file = os.path.join(root_dir, 'ori', file.split('.')[0]+'.json')
        if os.path.exists(json_file):
            shutil.copy(json_file, save_dir)
except IndexError:
    pass