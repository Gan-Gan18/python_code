#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import pandas as pd
import datetime

path6 = r'E:\DataAnalysis\01_pandas_exercise\exercise_data\wind.data'
data = pd.read_table(path6, sep='\s+', parse_dates=[[0, 1, 2]])
# read_table()读取txt或其他格式文件 sep='\s+'匹配任意空白字符 parse_dates=[[0,1,2]]解析对应日期列
print(data.head())


def fix_century(x):  # 修复年份bug
    if x.year > 1989:
        year = x.year - 100
    else:
        year = x.year
    return datetime.date(year, x.month, x.day)
data['Yr_Mo_Dy'] = data['Yr_Mo_Dy'].apply(fix_century)
print(data.head())

data["Yr_Mo_Dy"] = pd.to_datetime(data["Yr_Mo_Dy"])  # 将时间列数据转为时间数据类型datetime64
data = data.set_index("Yr_Mo_Dy")  # 设置索引
print(data.head())

print(data.isnull().sum())  # 统计各列缺失值个数总和
print(data.shape[0] - data.isnull().sum())  # 统计各列完整值个数总和
print(data.mean().mean())  # 对每列数据求平均值 再求每列平均值的平均值

loc_stats = pd.DataFrame()
loc_stats['min'] = data.min()
loc_stats['max'] = data.max()
loc_stats['mean'] = data.mean()
loc_stats['std'] = data.std()
print(loc_stats)

day_stats = pd.DataFrame()
day_stats['min'] = data.min(axis=1)
day_stats['max'] = data.max(axis=1)
day_stats['mean'] = data.mean(axis=1)
day_stats['std'] = data.std(axis=1)
print(day_stats.head())

data['date'] = data.index
data['month'] = data['date'].apply(lambda date : date.month)
data['year'] = data['date'].apply(lambda date : date.year)
data['day'] = data['date'].apply(lambda date : date.day)
january_winds = data.query('month==1')
print(january_winds.loc[:,'RPT':'MAL'].mean())

