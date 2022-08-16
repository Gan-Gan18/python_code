#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import pandas as pd
path3 = r'E:\DataAnalysis\01_pandas_exercise\exercise_data\drinks.csv'
drinks = pd.read_csv(path3)

print(drinks.groupby('continent').beer_servings.mean())  # 对指定列数据聚合分类 再求每分类对应的另一列数据汇总求平均值
print(drinks.groupby('continent').wine_servings.describe())  # describe()返回指定列数据的描述性统计信息(统计值、平均数、标准差、最大最小值)
print(drinks.groupby('continent').mean())  # 对某一列数据聚合分类后 求每一类对应其他列数据的平均值
print(drinks.groupby('continent').median())  # 求中位数
print(drinks.groupby('continent').spirit_servings.agg(['mean','min','max']))  # agg()用于多个条件求值运算
