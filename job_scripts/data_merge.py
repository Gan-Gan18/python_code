import os
import shutil

ori_path = r"Y:\Data\ZNJT\ZhongChe_diTie\LabelData\arm\20210114\arm_0114_01/"
# merge_path = ori_path + 'merge/'
merge_path = r'Y:\Data\ZNJT\ZhongChe_diTie\LabelData\arm\20210114\arm_0114_01\merge'
if not os.path.exists(merge_path):
    os.makedirs(merge_path)
file_list = []
for dirs in os.listdir(ori_path):
    for file in os.listdir(ori_path + dirs):
        file_list.append(ori_path + dirs + '/' + file)

for file in file_list:
    shutil.move(file, merge_path)
