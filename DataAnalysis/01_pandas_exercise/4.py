#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import pandas as pd
import numpy as np
path4 = r'E:\DataAnalysis\01_pandas_exercise\exercise_data\US_Crime_Rates_1960_2014.csv'
crime = pd.read_csv(path4)

crime.Year = pd.to_datetime(crime.Year, format='%Y')  # to_datetime()将某列数据类型转换为时间序列类型
print(crime.info())  # info输出列信息
crime = crime.set_index('Year',drop=True)  # set_index以指定列数据重新设置行索引 drop=True删除已设置为索引的列 Flase保留
print(crime.head())
print('-----------------------------------------')

del crime['Total']  # 删除指定列
crime = crime.resample('10AS').sum()
# resample()按时间序列对所有列数据重新聚合采样 指定时间参数  对于上述代码 以每10年为单位依次计算各列数据每10年的总和
population = crime['Population'].resample('10AS').max()  # 以每10年为单位依次统计出指定列数据每10年中的最大值
crime['Population'] = population  # 更新列数据
print(crime)

print(crime.idxmax(0))  # 按列查找每一列最大值
