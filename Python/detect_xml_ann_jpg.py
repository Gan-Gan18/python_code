# !/usr/bin/env python
# encoding: utf-8

import os


def get_ann_jpg_data(ann_dir, jpg_dir, result):
    ann_list = []
    jpg_list = []
    for ann in os.listdir(ann_dir):
        ann_list.append(ann)
        for jpg in os.listdir(jpg_dir):
            jpg_list.append(jpg)
            if ann.split('.')[0] == jpg.split('.')[0]:
                get_result = ann.split('.')[0] + '\n'
                with open(result, 'a') as f:
                    f.write(get_result)
                f.close()


def detect(result, main_txt):
    result_data = []
    main_data = []
    clean_data = []

    with open(result, 'r')as f:
        for each in f.readlines():
            result_data.append(each.replace('\n', ''))
    f.close()
    with open(main_txt, 'r')as f:
        for each in f.readlines():
            main_data.append(each.replace('\n', ''))
    f.close()

    for tmp in main_data:
        if tmp in result_data:
            clean_data.append(tmp)
            with open(r'E:\dataset\ZhongChe_data\sdg\voc_20210326\ImageSets\Main\result_trainval.txt', 'a') as f:
                f.write(tmp + '\n')
            f.close()


if __name__ == '__main__':
    ann_dir = r'E:\dataset\ZhongChe_data\sdg\voc_20210326\Annotations'
    jpg_dir = r'E:\dataset\ZhongChe_data\sdg\voc_20210326\JPEGImages'
    result = r'E:\dataset\ZhongChe_data\sdg\voc_20210326\result.txt'
    main_txt = r'E:\dataset\ZhongChe_data\sdg\voc_20210326\ImageSets\Main\trainval.txt'
    get_ann_jpg_data(ann_dir, jpg_dir, result)
    detect(result, main_txt)
