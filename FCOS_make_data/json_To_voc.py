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

# 1.json数据路径+voc数据保存路径
label_json_path = r"E:\dataset\TieKeYan\20220613\label-json\huishou/"
voc_saved_path = r"E:\dataset\TieKeYan\20220613\label-json\voc-huishou/"

# 2.创建相关文件夹
if not os.path.exists(voc_saved_path + "Annotations/"):
    os.makedirs(voc_saved_path + "Annotations/")
if not os.path.exists(voc_saved_path + "JPEGImages/"):
    os.makedirs(voc_saved_path + "JPEGImages/")
if not os.path.exists(voc_saved_path + "ImageSets/Main/"):
    os.makedirs(voc_saved_path + "ImageSets/Main/")

# 3.获取待处理文件
files = glob(label_json_path + "*.jpg")
files = [os.path.basename(i).split(".jpg")[0] for i in files]

# 4.读取json并写入xml
c = 0
for json_name in files:
    c += 1

    # 读取json信息  io.open()以指定模式打开文件
    json_filename = label_json_path + json_name + ".json"
    json_file = json.load(io.open(json_filename, "r", encoding="utf-8"))
    print("json_file", json_filename)

    # 按特定格式遍历写入xml数据
    height, width, channels = cv2.imread(label_json_path + json_name + ".jpg").shape
    with codecs.open(voc_saved_path + "Annotations/" + json_name + ".xml", "w", "utf-8") as xml:
        xml.write('<annotation>\n')
        xml.write('\t<folder>' + 'picture' + '</folder>\n')
        xml.write('\t<filename>' + json_name + ".jpg" + '</filename>\n')
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

        '''
        选择标注的标签名
        '''
        # 金库label标签
        # json_label = ['red','green','blue','white','black','other','none']
        # json_label = ['0','1', '2', '3', '4', '5']
        # json_label = ['6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18','19','20','21']
        # json_label = ['1', '2', '3','4']
        # json_label = ['moneybag','box']
        # 疲劳
        # json_label = ['yan','phone']
        # 检测棚label标签
        # json_label = ['light','flicker','dark']
        # json_label = ['pole']
        # json_label = ['open','close']
        # json_label = ['head0','head1','head2','clothes0','clothes1','clothes2']
        # json_label = ['clothes', 'rope']
        json_label = ['1','2','3','4','5','6']

        # 获取json文件中的标注信息（points坐标点+label标签名）
        for multi in json_file["shapes"]:
            points = np.array(multi["points"])
            name = multi["label"]
            if name not in json_label:
                print('Wrong label name:' + name)
                continue

            # 取标注框的坐标点（左下角+右上角）
            xmin = int(min(points[:, 0]))
            xmax = int(max(points[:, 0]))
            ymin = int(min(points[:, 1]))
            ymax = int(max(points[:, 1]))

            if xmax <= xmin:
                c += 1
                print("***********************x<", json_name, xmax, xmin)
                pass
            elif ymax <= ymin:
                c += 1
                print("*************************y<", json_name, ymax, ymin)
                pass
            elif ymax >= height - 1:
                ymax = height - 4
                print("*************************y>height", json_name, ymax, ymin)
            elif xmax >= width - 1:
                xmax = width - 4
                print("*************************x>width", json_name, ymax, ymin)
            elif xmin < 0:
                xmin = 0
            elif ymin < 0:
                ymin = 0

            # 写入框的坐标点和其他参数
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
        xml.write('</annotation>')
        print(c)

# 5.复制图片到 VOC/JPEGImages/下
image_files = glob(label_json_path + "*.jpg")
for image in image_files:
    shutil.copy(image, voc_saved_path + "JPEGImages/")
print("copy image files to VOC007/JPEGImages/")

# 6.划分训练集和测试集并写入文件
trainval_file = open(voc_saved_path + '/ImageSets/Main/trainval.txt', 'w')
train_file = open(voc_saved_path + '/ImageSets/Main/train.txt', 'w')
val_file = open(voc_saved_path + '/ImageSets/Main/val.txt', 'w')

total_files = glob(voc_saved_path + "Annotations/*.xml")
total_files = [i.split("/")[-1].split(".xml")[0] for i in total_files]
for file in total_files:
    trainval_file.write(file + "\n")

# train_test_split()函数将样本划分为训练集和测试集  test_size划分比例  random_state随机数种子
train_files, val_files = train_test_split(total_files, test_size=0.15, random_state=42)
for file in train_files:
    train_file.write(file + "\n")
for file in val_files:
    val_file.write(file + "\n")

trainval_file.close()
train_file.close()
val_file.close()
