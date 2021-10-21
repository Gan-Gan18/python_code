import os
import random
import shutil

"""
多个子文件夹 对各个文件夹下的数据随机提取 指定提取的总数量 存放于另一个路径下
"""

ori_path = r"E:\dataset\jcp_data\warninglight\20211015\images\0003_20210922_145351"
copy_path = r"E:\dataset\jcp_data\warninglight\20211015\images\label"
if not os.path.exists(copy_path):
    os.makedirs(copy_path)

file_list = []
for root, dirs, files in os.walk(ori_path):
    for file in files:
        file_list.append(os.path.join(root, file))

sample = random.sample(file_list, 250)
for name in sample:
    print(name)
    shutil.move(name, copy_path)



