# -*- coding=utf-8 -*-
# !/usr/bin/python

import sys
import os
import shutil
import numpy as np
import json
import xml.etree.ElementTree as ET

# 检测框的ID起始值
START_BOUNDING_BOX_ID = 1

# 类别列表无必要预先创建，程序中会根据所有图像中包含的ID来创建并更新
# PRE_DEFINE_CATEGORIES = {"none": 0, "red": 1, "other": 2, "blue": 3, "white": 4, "black": 5, "green": 6}  # jk clothes

# PRE_DEFINE_CATEGORIES = {"1":0,"2":1,"3":2,"4":3,"5":4}      # jk box_label
# PRE_DEFINE_CATEGORIES = {"1":0,"2":1,"3":2,"0":3}
# PRE_DEFINE_CATEGORIES = {"4":0,"5":1}

# PRE_DEFINE_CATEGORIES = {"1":0,"2":1,"3":2,"4":3}     # jk moneybag
# PRE_DEFINE_CATEGORIES = {"moneybag":0,"box":1}

# PRE_DEFINE_CATEGORIES = {"light":0,"flicker":1,"dark":2}    # jcp warning_light
# PRE_DEFINE_CATEGORIES = {"open":0,"close":1}    # jcp switch
# PRE_DEFINE_CATEGORIES ={"head0":0,"head1":1,"head2":2,"clothes0":3,"clothes1":4,"clothes2":5}     # jcp hat_clothes
PRE_DEFINE_CATEGORIES = {"clothes": 0, "rope": 1}     # jcp rope_clothes


def get(root, name):
    vars = root.findall(name)
    return vars


def get_and_check(root, name, length):
    vars = root.findall(name)
    if len(vars) == 0:
        raise NotImplementedError('Can not find %s in %s.' % (name, root.tag))
    if 0 < length != len(vars):
        raise NotImplementedError('The size of %s is supposed to be %d, but is %d.' % (name, length, len(vars)))
    if length == 1:
        vars = vars[0]
    return vars


# 获取图片名并转换为int
def get_filename_as_int(filename):
    try:
        filename = os.path.splitext(filename)[0]
        return int(filename)
    except:
        raise NotImplementedError('Filename %s is supposed to be an integer.' % (filename))


def convert(xml_list, xml_dir, json_file):
    """
    :param xml_list: 需要转换的XML文件列表
    :param xml_dir: XML的存储文件夹
    :param json_file: 导出json文件的路径
    :return: None
    """

    # 生成的json文件基本结构
    json_dict = {"images": [],
                 "type": "instances",
                 "annotations": [],
                 "categories": []}
    """
    获取图片基本信息 并写入json文件'images'字典中
    """
    list_fp = xml_list
    categories = PRE_DEFINE_CATEGORIES
    bnd_id = START_BOUNDING_BOX_ID
    for line in list_fp:
        line = line.strip()
        print("~~~~~ Processing {}".format(line))

        # 读取和解析xml文件
        xml_f = os.path.join(xml_dir, line)
        tree = ET.parse(xml_f)
        root = tree.getroot()
        path = get(root, 'path')

        # 读取图片名
        if len(path) == 1:
            filename = os.path.basename(path[0].text)
        elif len(path) == 0:
            filename = get_and_check(root, 'filename', 1).text
        else:
            raise NotImplementedError('%d paths found in %s' % (len(path), line))

        image_id = get_filename_as_int(filename)  # 图片ID
        size = get_and_check(root, 'size', 1)

        width = int(get_and_check(size, 'width', 1).text)
        height = int(get_and_check(size, 'height', 1).text)
        image = {'file_name': filename,
                 'height': height,
                 'width': width,
                 'id': image_id}
        json_dict['images'].append(image)

        """
        获取标注框的坐标点 并写入json文件'annotations'字典
        """
        for obj in get(root, 'object'):
            # 取出标注框类别名称
            category = get_and_check(obj, 'name', 1).text
            # 更新类别ID字典
            if category not in categories:
                new_id = len(categories)
                categories[category] = new_id
            category_id = categories[category]

            # 获取坐标点 并写入对应字段
            bndbox = get_and_check(obj, 'bndbox', 1)
            xmin = int(get_and_check(bndbox, 'xmin', 1).text) - 1
            ymin = int(get_and_check(bndbox, 'ymin', 1).text) - 1
            xmax = int(get_and_check(bndbox, 'xmax', 1).text)
            ymax = int(get_and_check(bndbox, 'ymax', 1).text)
            assert (xmax > xmin)
            assert (ymax > ymin)
            o_width = abs(xmax - xmin)  # abs()返回数值的绝对值
            o_height = abs(ymax - ymin)
            annotation = dict()
            annotation['area'] = o_width * o_height
            annotation['iscrowd'] = 0
            annotation['image_id'] = image_id
            annotation['bbox'] = [xmin, ymin, o_width, o_height]
            annotation['category_id'] = category_id
            annotation['id'] = bnd_id
            annotation['ignore'] = 0
            annotation['segmentation'] = [[xmin, ymin, xmin, ymax, xmax, ymax, xmax, ymin]]
            json_dict['annotations'].append(annotation)
            bnd_id += 1

    # 获取类别和ID 并写入json文件'categories'字典
    for cate, cid in categories.items():
        cat = {'supercategory': 'none', 'id': cid, 'name': cate}
        json_dict['categories'].append(cat)

    # 整体写入json 并导出json文件
    json_fp = open(json_file, 'w')
    json_str = json.dumps(json_dict)  # json.dumps()将字典转化为字符串
    json_fp.write(json_str)
    json_fp.close()


if __name__ == '__main__':
    root_path = r"E:\dataset\jcp_data\rope_clothes\VOC2007_all/"
    coco_path = r"E:\dataset\jcp_data\rope_clothes\coco/"

    # 自动创建对应文件夹
    train_ann = coco_path + 'train2014/annotations_0730/'
    train_img = coco_path + 'train2014/images_0730/'
    val_ann = coco_path + 'val2014/annotations_0730/'
    val_img = coco_path + 'val2014/images_0730/'
    if not os.path.exists(train_ann):
        os.makedirs(train_ann)
    if not os.path.exists(train_img):
        os.makedirs(train_img)
    if not os.path.exists(val_ann):
        os.makedirs(val_ann)
    if not os.path.exists(val_img):
        os.makedirs(val_img)

    # 获取xml文件列表
    xml_dir = os.path.join(root_path, 'Annotations')
    xml_labels = os.listdir(os.path.join(root_path, 'Annotations'))
    np.random.shuffle(xml_labels)
    split_point = int(len(xml_labels) / 18)

    # 划分train data训练集
    xml_list = xml_labels[split_point:]
    json_file = os.path.join(train_ann, 'instances_train2014.json')
    convert(xml_list, xml_dir, json_file)
    for xml_file in xml_list:
        img_name = xml_file[:-4] + '.jpg'
        shutil.copy(os.path.join(root_path, 'JPEGImages', img_name),
                    os.path.join(train_img, img_name))

    # 划分validation data验证集
    xml_list = xml_labels[0:split_point]
    json_file = os.path.join(val_ann, 'instances_val2014.json')
    convert(xml_list, xml_dir, json_file)
    for xml_file in xml_list:
        img_name = xml_file[:-4] + '.jpg'
        shutil.copy(os.path.join(root_path, 'JPEGImages', img_name),
                    os.path.join(val_img, img_name))
