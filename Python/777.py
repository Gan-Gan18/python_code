import os
import random
import shutil

ori_dir = r'E:\dataset\gbCoin_data\2021\20210607-ori\raw_202105210929\02\反面\工位4'
copy_dir = r'E:\dataset\gbCoin_data\2021\20210607-ori\raw_202105210929\01\反面\工位4'
files = os.listdir(ori_dir)
file_list = []
for file in files:
    file_list.append(file.split('.')[0])

sample = random.sample(file_list, 730)
print(len(sample))
for name in sample:
    print(name)
    shutil.move(ori_dir + '/' + name + '.png', copy_dir)
    # shutil.copy(ori_dir + '/' + name + '.json', copy_dir)
