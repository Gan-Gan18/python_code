#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import pandas as pd
path1 = r'E:\DataAnalysis\01_pandas_exercise\exercise_data\chipotle.tsv'
chipo = pd.read_csv(path1, sep='\t')  # .tsv文件分隔符默认是制表符'\t',需要指定

print(chipo.head(10))  # .head()输出显示前10行
print(chipo.shape[1])  # .shape()输出文件总行列数 shape[0]显示行数 shape[1]显示列数
print(chipo.columns)  # .columns输出所有列名
print(chipo.index)  # .index输出索引(行)
print('-----------------------------------------')

c = chipo[['item_name', 'quantity']].groupby(['item_name'], as_index=False).agg({'quantity': sum})
# groupby()对某一列数据聚合分组(分类)  as_index=True不显示索引值 False显示索引值  agg()对gropuby分类对应数值计算 对列操作
c.sort_values(['quantity'], ascending=False, inplace=True)
# sort_values()按照指定行或列数据排序  ascending=True升序 False降序  inplace=True替换原数据 False不替换
print(c.head())  # 默认输出前5行数据 也可指定
print('-----------------------------------------')

print(chipo['item_name'].nunique())  # nunique()统计指定列的唯一值的个数(类别数) 返回计数数值
print(chipo['choice_description'].value_counts().head())  # value_counts() 对指定列数据统计不同值个数及排序 默认降序
print(chipo['quantity'].sum())  # 对指定列数据求和
print('-----------------------------------------')

f = lambda x: float(x[1:-1])  # 显示为浮点数
print(chipo['item_price'].apply(f))  # apply()遍历指定列数据 对所有数据执行同样操作
chipo['sub_total'] = round(chipo['quantity'] * chipo['item_price'].apply(f), 2)
# round()返回某个浮点数的四舍五入值 指定保留几位小数
print(chipo['sub_total'].sum())

mean = chipo[['order_id','sub_total']].groupby(by=['order_id']).agg({'sub_total':sum})['sub_total'].mean()
# 对某一列数据分类聚合 计算对应的另一列数据的和 用类别数求这个和的平均数
print(round(mean, 2))

