#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import PIL
from PIL import ImageFont, Image, ImageDraw
import os

# 设置字体，如果没有，也可以不设置
font = ImageFont.truetype(r"C:\Windows\Fonts\simsun.ttc", 40)

# 打开背景图片
ori_path = r'E:\dataset\TieKeYan\20220614\videos\3_images\add-pic\zhanli/'
save_path = r'E:\dataset\TieKeYan\20220614\videos\3_images\zhanli/'
imageFile = os.listdir(ori_path)
for img in imageFile:
    im1 = Image.open(ori_path + img)

    # 在图片上添加文字
    draw = ImageDraw.Draw(im1)
    # draw.text((1180, 660), "在岗", (255, 255, 255), font=font)
    # draw.text((940, 390), "打电话", (255, 255, 255), font=font)
    # draw.text((874, 296), "挥手", (255, 255, 255), font=font)
    draw.text((1180, 660), "站立", (255, 255, 255), font=font)
    # draw.text((1180, 660), "睡觉", (255, 255, 255), font=font)
    # draw.text((1180, 660), "离岗", (255, 255, 255), font=font)
    # 保存
    im1.save(save_path + img.split('.')[0] + ".png")
