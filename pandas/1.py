#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import pandas as pd
import numpy as np

# 1.一维数据 Series()

a = pd.Series([8, 10, 9, 111, 20, 15, 1245], index=list('abcdefg'))
# print(a)

dic = {'name': 'gyj',
       'age': '26',
       'job': 'AI',
       'other': 'every thing is ok!',
       }
info = pd.Series(dic)
# print(info)  # 字典 随机排序

# print(info[0])  # 显示某个值
# print(info[[0,2,3]])  # 显示多个不连续值
# print(info[0:2])  # 显示多个连续值
# print(info[['name','job']])  # 通过索引值查找
# print(info.index)  # 索引
# print(info.values)  # 值


# 2.二维数据 DataFrame()
c = np.arange(1, 13).reshape(3, 4)
d = pd.DataFrame(c, index=list('123'), columns=list('ABCD'))  # index:行索引   columns:列索引
# print(d)

e = {'name': ['abc', 'def'],  # 通过字典创建
     'age': ['35', '65'],
     'QQ': ['4366742', '3576424'],
     'wechat': ['gh452', 'fgg35']
     }
person_info = pd.DataFrame(e, columns=['name', 'age', 'QQ', 'wechat'])  # 指定列索引排序
# print(person_info)

f = [{'name': 'abc', 'age': '35', 'QQ': '4366742', 'wechat': 'gh452'},  # 通过列表创建
     {'name': 'def', 'QQ': '3576424', 'wechat': 'fgg35'}
     ]
g = pd.DataFrame(f, columns=['name', 'age', 'QQ', 'wechat'])  # 指定列索引排序
# print(g)
# print(g[:1])  # 取某行
# print(g['age'])  # 取某列
# print(g[['name','QQ']])  # 取多列

# loc通过标签索引获取值
# print(g.loc[1])  # print(g.loc[1,:])  取某行
# print(g.loc[[0,1]])  # 取多行
# print(g.loc[:,'name'])  # 取某列
# print(g.loc[:, ['name', 'age']])  # 取多列
# print(g.loc[0,'QQ'])  # 取某行某列
# print(g.loc[0:1,['name','age']])  # 取多行多列

# iloc通过位置获取值
# print(g.iloc[0])  # print(g.iloc[0,])   取某行
# print(g.iloc[:,3])  # 取某列
# print(g.iloc[1,3])  # 取某行某列
# print(g.iloc[[0,1],[1,3]])  # 取多行多列
