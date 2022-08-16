#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import pandas as pd
path2 = r'E:\DataAnalysis\01_pandas_exercise\exercise_data\Euro2012_stats.csv'
euro2012 = pd.read_csv(path2)

print(euro2012.Goals)  # 输出指定列数据 或 print(euro2012['Goals'])
print(euro2012.info())  # 输出数据集信息(所有列信息)
print('-----------------------------------------')

discipline = euro2012[['Team','Yellow Cards','Red Cards']]  # 输出指定的多个列数据
print(discipline.sort_values(['Red Cards','Yellow Cards'],ascending=False))  # 对多个列先后进行排序
print(round(discipline['Yellow Cards'].mean()))  # 对指定列求平均数
print('-----------------------------------------')

print(euro2012[euro2012.Goals > 6])  # 在指定列中筛选满足条件的数据 输出所有满足条件的数据
print(euro2012[euro2012.Team.str.startswith('C')])  # .str将列数据转为字符串 .startswith查找指定开头的数据
print(euro2012.iloc[:, 0:7])  # .iloc切片操作 根据索引选取单行单列或多行多列
print(euro2012.loc[euro2012.Team.isin(['England','Italy']),['Team','Shooting Accuracy']])
# loc切片操作 根据表内数据标签、条件选取指定行列数据  .isin判断指定元素是否在该列中(筛选出指定元素)
