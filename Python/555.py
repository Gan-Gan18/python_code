#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import os

path = r'F:\wangj\data\sdg\dl'

for dirs in os.listdir(path):
    if os.path.isdir(os.path.join(path, dirs)):
        with open(r'F:\wangj\data\sdg\dl\dirs_name.txt', 'a') as f:
            f.write(dirs + '\n')
        f.close()
