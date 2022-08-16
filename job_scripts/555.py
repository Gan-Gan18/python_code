#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import os

root_path = r'E:\dataset\RMB_data\BaiGuoHuoBi\JiaoDai\split/'
for i in range(1, 100):
    print(i)
    split_path = os.path.join(root_path, str(i))
    if not os.path.exists(split_path):
        os.makedirs(split_path)
