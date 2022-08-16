#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import numpy as np
import pandas as pd

raw_data_1 = {
        'subject_id': ['1', '2', '3', '4', '5'],
        'first_name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
        'last_name': ['Anderson', 'Ackerman', 'Ali', 'Aoni', 'Atiches']}
raw_data_2 = {
        'subject_id': ['4', '5', '6', '7', '8'],
        'first_name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
        'last_name': ['Bonder', 'Black', 'Balwner', 'Brice', 'Btisan']}
raw_data_3 = {
        'subject_id': ['1', '2', '3', '4', '5', '7', '8', '9', '10', '11'],
        'test_id': [51, 15, 15, 61, 16, 14, 15, 1, 61, 16]}

data1 = pd.DataFrame(raw_data_1, columns=['subject_id', 'first_name', 'last_name'])
data2 = pd.DataFrame(raw_data_2, columns=['subject_id', 'first_name', 'last_name'])
data3 = pd.DataFrame(raw_data_3, columns=['subject_id', 'test_id'])

all_data = pd.concat([data1,data2])  # concat() 多组数据合并 不指定axis 默认按行维度合并
print(all_data)
all_data_col = pd.concat([data1, data2],axis=1)  # axis=1 按列维度合并

print(pd.merge(all_data, data3, on='subject_id'))  # 按指定列的值将两组数据合并 要求两组数据同时拥有相同的列和值
print(pd.merge(data1, data2, on='subject_id', how='inner'))
# 按指定列的值将多组数据合并 how='inner'保留指定列值一致的行数据  'outer'保留一致的行数据 不一致的以Nan填充
# 'left'保持左边组数据不变 右边组数据向左边组数据添加 只保留指定列一致的行数据  'right'反之同理

