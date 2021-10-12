import os
import random
import shutil


ori_path = r"E:\dataset\jcp_data\switch\20211012\images_1"
copy_path = r"E:\dataset\jcp_data\switch\20211012\copy"
file_list = []
for root, dirs, files in os.walk(ori_path):
    for file in files:
        file_list.append(os.path.join(root, file))

sample = random.sample(file_list, 1500)
for name in sample:
    print(name)
    shutil.move(name, copy_path)



