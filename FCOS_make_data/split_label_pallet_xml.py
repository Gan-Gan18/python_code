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
try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET

# 1.标签路径
root_xml =r"E:\dataset\jinku_data\label_pallet\1015\img\check\VOC2007\Annotations/"
#root_xml ="D:\\VOC2007_0\\Annotations"
saved_path = r"E:\dataset\jinku_data\label_pallet\1015\img\check\VOC2007_new_label/"
# x_border= [352,953]
# y_border= [40,697]
if os.path.exists(saved_path):
    shutil.rmtree(saved_path)
def parse_xml(xml_file):
    tree = ET.parse(xml_file)  # <class 'xml.etree.ElementTree.ElementTree'>
    root = tree.getroot()
    bboxes = []
    color =[]
    for obj in root.findall('object'):
      bbox = obj.find('bndbox')
      label = obj.find('name').text
      #xiugai
      # if label not in['4','5']:
      #     continue

      # if label not in ['0','1', '2','3']:
      #      continue

      if label not in ['6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18','19']:
            continue
      bboxes.append((int(bbox.find('xmin').text),
                     int(bbox.find('ymin').text),
                     int(bbox.find('xmax').text),
                     int(bbox.find('ymax').text),
                     label))

    return bboxes


def listDir(rootDir, image_list,endwith):
    files = os.listdir(rootDir)
    for filename in os.listdir(rootDir):
        pathname = os.path.join(rootDir, filename)
        if os.path.isfile(pathname):
            if pathname.split(".")[-1] in [endwith]:
                image_list.append(pathname)
        else:
            listDir(pathname, image_list,endwith)

rootDir =r"E:\dataset\jinku_data\label_pallet\1015\img\check\VOC2007\JPEGImages"
#rootDir  ="D:\\VOC2007_0\\JPEGImages"
image_list = []
listDir(rootDir, image_list,"jpg")

# 2.创建要求文件夹
if not os.path.exists(saved_path + "Annotations"):
    os.makedirs(saved_path + "Annotations")
if not os.path.exists(saved_path + "JPEGImages/"):
    os.makedirs(saved_path + "JPEGImages/")
if not os.path.exists(saved_path + "ImageSets/Main/"):
    os.makedirs(saved_path + "ImageSets/Main/")
c = 0
for i in range(len(image_list)):
    img = cv2.imread(image_list[i])
    height, width, channels = img.shape
    img_name = os.path.basename(image_list[i]).split(".jpg")[0]
    xml_name = os.path.basename(image_list[i]).split(".jpg")[0]+".xml"
    #print(xml_name)
    xml_names=root_xml + "/"+xml_name
    if os.path.exists(xml_names) is False:
        continue
    bboxes= parse_xml(xml_names)
    with codecs.open(saved_path + "Annotations/" + img_name + ".xml", "w", "utf-8") as xml:
        xml.write('<annotation>\n')
        xml.write('\t<folder>' + 'picture' + '</folder>\n')
        xml.write('\t<filename>' + img_name + ".jpg" + '</filename>\n')
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
        # json_label = ['1', '2', '3', '4', '5']
        # json_label = ['1', '2', '3','4']
        # json_label = ['4', '5']
        # json_label = ['0','1', '2','3']
        # json_label = ['car','opendoor','closedoor']
        # json_label = ['yan','phone']
        # json_label = ['arm']
        # json_label = ['luggage', 'pack', 'bag', 'umbrella', 'electronics', 'other']
        json_label = ['6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18','19']
        for box in bboxes:
            name = box[4]
            if name not in json_label:
                # print(name)
                continue
            # if name == 'd':
            # sys.exit(0)
            if name != "clothes":
                xmin = box[0]
                ymin = box[1]
                xmax = box[2]
                ymax = box[3]
                # if xmin<x_border[0]or xmax>x_border[1] or ymin<y_border[0]or ymax>y_border[1]:
                #     print(xml_name)
                #     continue
                if xmax <= xmin:
                    c += 1
                    print("***********************x<", img_name, xmax, xmin)
                    pass
                elif ymax <= ymin:
                    c += 1
                    print("*************************y<", img_name, ymax, ymin)
                    pass
                elif ymax >= height - 1:
                    ymax = height - 4
                    print("*************************y>height", img_name, ymax, ymin)
                    # pass
                elif xmax >= width - 1:
                    xmax = width - 4
                    print("*************************x>width", img_name, ymax, ymin)

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
        # print(c)


# 5.复制图片到 VOC2007/JPEGImages/下
image_files = glob(rootDir + "\\*.jpg")
print("copy image files to VOC007/JPEGImages/")
for image in image_files:
    shutil.copy(image, saved_path + "JPEGImages/")

# 6.split files for txt
txtsavepath = saved_path + "ImageSets/Main/"
ftrainval = open(txtsavepath + '/trainval.txt', 'w')
ftest = open(txtsavepath + '/test1.txt', 'w')
ftrain = open(txtsavepath + '/train.txt', 'w')
fval = open(txtsavepath + '/test.txt', 'w')
total_files = glob("./VOC2007/Annotations/*.xml")
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

