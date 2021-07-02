#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
import sys
import io
import numpy as np
import codecs
import json
from glob import glob
import cv2
import shutil
from sklearn.model_selection import train_test_split

# 1.标签路径
labelme_path = r"Y:\Data\ZNJT3\HuoHua_sdg_detect\RawData\label\20210421/"
saved_path = r"Y:\Data\ZNJT3\HuoHua_sdg_detect\TrainData\voc2007\20210421/"
# labelme_path ="/media/cbpm2016/D/wangman/data-e/merge_dir_0520-smokephone/"
# labelme_path ="/media/cbpm2016/smb/wangman/pole_704p_0806/"
# labelme_path = "/media/cbpm2016/E/dataset/DiTie_data/luggage/1224/merge_dir_1224/"
# saved_path = "/media/cbpm2016/E/wangman/caffe_project/RefineDet/VOC/VOC2007-diTie/luggage/VOC2007/"
# labelme_path = "/media/cbpm2016/E/dataset/DiTie_data/people/1217/merge_dir_1217/"
# saved_path = "/media/cbpm2016/E/wangman/caffe_project/RefineDet/VOC/VOC2007-diTie/people/VOC2007/"
# labelme_path = "/media/cbpm2016/E/dataset/DiTie_data/arm/0115/merge_dir_0115/"
# saved_path = "/media/cbpm2016/E/wangman/caffe_project/RefineDet/VOC/VOC2007-diTie/arm/VOC2007/"


# 2.创建要求文件夹
if not os.path.exists(saved_path + "Annotations"):
    os.makedirs(saved_path + "Annotations")
if not os.path.exists(saved_path + "JPEGImages/"):
    os.makedirs(saved_path + "JPEGImages/")
if not os.path.exists(saved_path + "ImageSets/Main/"):
    os.makedirs(saved_path + "ImageSets/Main/")

# 3.获取待处理文件
files = glob(labelme_path + "*.json")
# files = [i.split("/")[-1].split(".json")[0] for i in files]
files = [os.path.basename(i).split(".json")[0] for i in files]
# 4.读取标注信息并写入 xml
c = 0

for json_file_ in files:
    c += 1
    json_filename = labelme_path + json_file_ + ".json"
    json_file = json.load(io.open(json_filename, "r", encoding="utf-8"))
    # print("json_file",json_file)
    height, width, channels = cv2.imread(labelme_path + json_file_ + ".jpg").shape

    with codecs.open(saved_path + "Annotations/" + json_file_ + ".xml", "w", "utf-8") as xml:
        xml.write('<annotation>\n')
        xml.write('\t<folder>' + 'picture' + '</folder>\n')
        xml.write('\t<filename>' + json_file_ + ".jpg" + '</filename>\n')
        xml.write('\t<source>\n')
        xml.write('\t\t<database>The UAV autolanding</database>\n')
        xml.write('\t\t<annotation>UAV AutoLanding</annotation>\n')
        xml.write('\t\t<image>flickr</image>\n')
        xml.write('\t\t<flickrid>NULL</flickrid>\n')
        xml.write('\t</source>\n')
        xml.write('\t<owner>\n')
        xml.write('\t\t<flickrid>NULL</flickrid>\n')
        xml.write('\t\t<name>ChaojieZhu</name>\n')
        xml.write('\t</owner>\n')
        xml.write('\t<size>\n')
        xml.write('\t\t<width>' + str(width) + '</width>\n')
        xml.write('\t\t<height>' + str(height) + '</height>\n')
        xml.write('\t\t<depth>' + str(channels) + '</depth>\n')
        xml.write('\t</size>\n')
        xml.write('\t\t<segmented>0</segmented>\n')
        # json_label = ['red','green','blue','white','black','other','none']
        # json_label = ['1']
        # json_label = ['1','2','3','4','5']
        # json_label = ['1','2','3']
        # json_label = ['car']
        # json_label = ['yan','phone','other']
        # json_label = ['pole']
        # json_label = ['head']
        # json_label = ['arm','luggage','pack','bag','umbrella','electronics','other']
        # json_label = ['arm']
        json_label = ['1', '2']
        # json_label = ['luggage','pack','bag','electronics','other']
        # json_label = ['head']
        # json_label = ['arm']
        for multi in json_file["shapes"]:
            points = np.array(multi["points"])
            name = multi["label"]
            if name not in json_label:
                print(name)
                continue
            # if name == 'd':
            # sys.exit(0)
            if name != "clothes":
                xmin = int(min(points[:, 0]))
                xmax = int(max(points[:, 0]))
                ymin = int(min(points[:, 1]))
                ymax = int(max(points[:, 1]))
                label = multi["label"]
                if xmax <= xmin:
                    c += 1
                    print("***********************x<", json_file_, xmax, xmin)
                    pass
                elif ymax <= ymin:
                    c += 1
                    print("*************************y<", json_file_, ymax, ymin)
                    pass
                elif ymax >= height - 1:
                    ymax = height - 4
                    print("*************************y>height", json_file_, ymax, ymin)
                    # pass
                elif xmax >= width - 1:
                    xmax = width - 4
                    print("*************************x>width", json_file_, ymax, ymin)
                elif xmin < 0:
                    xmin = 0
                elif ymin < 0:
                    ymin = 0
                xml.write('\t<object>\n')
                xml.write('\t\t<name>' + name + '</name>\n')
                xml.write('\t\t<pose>Unspecified</pose>\n')
                xml.write('\t\t<truncated>1</truncated>\n')
                xml.write('\t\t<difficult>0</difficult>\n')
                xml.write('\t\t<bndbox>\n')
                xml.write('\t\t\t<xmin>' + str(xmin) + '</xmin>\n')
                xml.write('\t\t\t<ymin>' + str(ymin) + '</ymin>\n')
                xml.write('\t\t\t<xmax>' + str(xmax) + '</xmax>\n')
                xml.write('\t\t\t<ymax>' + str(ymax) + '</ymax>\n')
                xml.write('\t\t</bndbox>\n')
                xml.write('\t</object>\n')
                # print(json_filename, xmin, ymin, xmax, ymax, label)
        xml.write('</annotation>')
        print(c)

        #     xmin = min(points[:, 0])
        #     xmax = max(points[:, 0])
        #     ymin = min(points[:, 1])
        #     ymax = max(points[:, 1])
        #     label = multi["label"]
        #     if xmax <= xmin:
        #         pass
        #     elif ymax <= ymin:
        #         pass
        #     else:
        #         xml.write('\t<object>\n')
        #         xml.write('\t\t<name>' + name + '</name>\n')
        #         xml.write('\t\t<pose>Unspecified</pose>\n')
        #         xml.write('\t\t<truncated>1</truncated>\n')
        #         xml.write('\t\t<difficult>0</difficult>\n')
        #         xml.write('\t\t<bndbox>\n')
        #         xml.write('\t\t\t<xmin>' + str(xmin) + '</xmin>\n')
        #         xml.write('\t\t\t<ymin>' + str(ymin) + '</ymin>\n')
        #         xml.write('\t\t\t<xmax>' + str(xmax) + '</xmax>\n')
        #         xml.write('\t\t\t<ymax>' + str(ymax) + '</ymax>\n')
        #         xml.write('\t\t</bndbox>\n')
        #         xml.write('\t</object>\n')
        #         print(json_filename, xmin, ymin, xmax, ymax, label)
        # xml.write('</annotation>')

# 5.复制图片到 VOC2007/JPEGImages/下
image_files = glob(labelme_path + "*.jpg")
print("copy image files to VOC2007/JPEGImages/")
for image in image_files:
    shutil.copy(image, saved_path + "JPEGImages/")

# 6.split files for txt
txtsavepath = saved_path + "ImageSets/Main/"
ftrainval = open(txtsavepath + '/trainval.txt', 'w')
ftest = open(txtsavepath + '/test1.txt', 'w')
ftrain = open(txtsavepath + '/train.txt', 'w')
fval = open(txtsavepath + '/test.txt', 'w')
total_files = glob(r"Y:\Data\ZNJT3\HuoHua_sdg_detect\TrainData\voc2007\20210421\Annotations/*.xml")
total_files = [i.split("/")[-1].split(".xml")[0] for i in total_files]
# test_filepath = ""
for file in total_files:
    ftrainval.write(file + "\n")
# test
# for file in os.listdir(test_filepath):
#    ftest.write(file.split(".jpg")[0] + "\n")
# split
train_files, val_files = train_test_split(total_files, test_size=0.15, random_state=42)
# train
for file in train_files:
    ftrain.write(file + "\n")
# val
for file in val_files:
    fval.write(file + "\n")

ftrainval.close()
ftrain.close()
fval.close()
# ftest.close()
