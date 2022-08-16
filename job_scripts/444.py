#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import json
import os
import glob
import shutil

ori_filePath = r'E:\dataset\AR\ori-videos\02\images\merge'

shapes_List = []

for json_file in glob.glob(os.path.join(ori_filePath, '*.json')):
    file_name = os.path.basename(json_file.split('.')[0])
    print(file_name)
    with open(json_file, 'r', encoding='utf-8') as jf:
        info = json.load(jf)
        imagePath = info["imagePath"]
        # label = info["shapes"]
        # for i in range(len(label)):
        #     if label[i]['label'] == 'hangming':
        #         label[i]['label'] = 'V100_hangming'
        #     # elif label[i]['label'] == 'hangming':
        #     #     label[i]['label'] = 'V1_hangming'
        #     # elif label[i]['label'] == 'code':
        #     #     label[i]['label'] = 'V1_code'
        #     # elif label[i]['label'] == 'mangwen':
        #     #     label[i]['label'] = 'V1_mangwen'
        #     # elif label[i]['label'] == 'tuanhua':
        #     #     label[i]['label'] = 'V1_tuanhua'
        #     # elif label[i]['label'] == 'wayinnum':
        #     #     label[i]['label'] = 'V1_wayinnum'
        #         with open(json_file, 'w', encoding='utf-8') as new_jf:
        #             json.dump(info, new_jf)

        new_imagePath = file_name
        info["imagePath"] = new_imagePath + '.jpg'
        # print(info["imagePath"])
        with open(json_file, 'w', encoding='utf-8') as new_jf:
            json.dump(info, new_jf)