import os
import shutil

ori_path = r"E:\dataset\AR\ori-videos\02\images/"
merge_path = r'E:\dataset\AR\ori-videos\02\images\merge'
if not os.path.exists(merge_path):
    os.makedirs(merge_path)
file_list = []
for dirs in os.listdir(ori_path):
    # for child_dir in os.listdir(ori_path + dirs):
    #     if child_dir == 'Algtest.log':
    #         continue
    #
    #     for file in os.listdir(os.path.join(ori_path, dirs) + '/' + child_dir):
    #         if file.endswith('.jpg'):
    #             file_list.append(os.path.join(ori_path, dirs) + '/' + child_dir + '/' + file)
    for file_1 in os.listdir(ori_path + dirs):
        print(file_1)
        shutil.copy(ori_path+dirs+'/'+file_1, merge_path)
