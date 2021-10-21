import os
import shutil
from collections import Counter


def merge_file(ori_path, merge_path):
    file_list = []
    basename_list = []

    """
    合并不重名文件
    """
    for dirs in os.listdir(ori_path):
        for file in os.listdir(ori_path + dirs):
            if file == 'same':
                continue
            else:
                file_list.append(ori_path + dirs + '/' + file)
                basename_list.append(file)
    for file in file_list:
        shutil.copy(file, merge_path)

    """
    提取重名文件
    """
    for root, dirs, files in os.walk(ori_path):
        list_dict = dict(Counter(basename_list))
        for key, value in list_dict.items():
            if value > 1:
                try:
                    shutil.copy(os.path.join(root, key), same_path)
                except (FileNotFoundError, shutil.SameFileError):
                    pass


if __name__ == "__main__":
    ori_path = r"D:\熊猫币挑图20211015\test\merge/"
    merge_path = ori_path + 'merge/'
    same_path = merge_path + 'same/'
    if not os.path.exists(same_path):
        os.makedirs(same_path)
    merge_file(ori_path, merge_path)
