#!/usr/bin/env python
# -*- coding:utf-8 -*-

from __future__ import print_function
import glob
import os
import sys
import numpy as np
import labelme
import PIL
import shutil

"""
根据labelme标注设定的标签名
获取每个标签名对应的id,包括_background_
id从0开始
"""
def get_label_name_id():
    """
    根据labelme标注的标签名修改 添加
    """
    json_label_name = ['_background_', '1']  # 金库铁笼
    # json_label_name =['_background_', 'sdg']  #受电弓倾斜
    # json_label_name = ['_background_', '1', '2', '3']  # 探头异物分割
    # json_label_name =['_background_', 'deformation']
    # json_label_name = ['_background_', 'missing']
    # json_label_name = ['_background_', 'normal']
    name_id = {}
    for name in json_label_name:
        ids = json_label_name.index(name)
        name_id[name] = ids
    return name_id


"""
定义每种标签类别的颜色值：rgb通道
按照标签名和id顺序依次设定
"""
def label_colormap(n_label=256, value=None):
    def bitget(byteval, idx):
        return (byteval & (1 << idx)) != 0

    cmap = np.zeros((n_label, 3), dtype=np.uint8)
    for i in range(0, n_label):
        id = i
        r, g, b = 0, 0, 0
        for j in range(0, 8):
            r = np.bitwise_or(r, (bitget(id, 0) << 7 - j))
            g = np.bitwise_or(g, (bitget(id, 1) << 7 - j))
            b = np.bitwise_or(b, (bitget(id, 2) << 7 - j))
            id = id >> 3
        cmap[i, 0] = r
        cmap[i, 1] = g
        cmap[i, 2] = b

    """
    自定义分割颜色 背景+标签 多个标签按0,1,2,3...设定
    """
    cmap[0, :] = [128, 128, 128]  # _background_  m默认
    cmap[1, :] = [128, 0, 0]
    # cmap[2, :] = [0, 0, 142]
    # cmap[3, :] = [0, 136, 0]
    # cmap[4, :] = [255,170,0]
    # cmap[5, :] = []

    if value is not None:
        hsv = color_module.rgb2hsv(cmap.reshape(1, -1, 3))
        if isinstance(value, float):
            hsv[:, 1:, 2] = hsv[:, 1:, 2].astype(float) * value
        else:
            assert isinstance(value, int)
            hsv[:, 1:, 2] = value
        cmap = color_module.hsv2rgb(hsv).reshape(-1, 3)
    return cmap


def lblsave(filename, lbl):
    if lbl.min() >= -1 and lbl.max() < 255:
        lbl_pil = PIL.Image.fromarray(lbl.astype(np.uint8), mode="P")
        colormap = label_colormap()
        lbl_pil.putpalette(colormap.flatten())
        lbl_pil.save(filename)


"""
根据labelme标注生成的json文件
用labelme库解析json
生成分割图片.png格式
"""


def convert_to_seg():
    for filename in glob.glob(os.path.join(root_path, "*.json")):
        print("Generating seg_result from:", filename)

        base_name = os.path.splitext(os.path.basename(filename))[0]
        save_ori_file = os.path.join(save_path, base_name + ".jpg")
        save_seg_file = os.path.join(save_path, base_name + "_color_mask.png")

        label_file = labelme.LabelFile(filename=filename)
        with open(save_ori_file, "wb") as f:
            f.write(label_file.imageData)
        img = labelme.utils.img_data_to_arr(label_file.imageData)

        lbl, _ = labelme.utils.shapes_to_label(
            img_shape=img.shape,
            shapes=label_file.shapes,
            label_name_to_value=get_label_name_id(),
        )
        lblsave(save_seg_file, lbl)


def copy_ori_img():
    for img in glob.glob(os.path.join(root_path, '*.jpg')):
        shutil.copy(img, save_path)


if __name__ == "__main__":
    root_path = r"E:\dataset\jcp_data\tantou\20220505\1/"
    save_path = root_path + "Segmentation_result/"
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    convert_to_seg()
    copy_ori_img()