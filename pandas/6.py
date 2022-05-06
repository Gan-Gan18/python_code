#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import pandas as pd
import numpy as np

# 1.读取csv文件(tsv、txt)
# csv = pd.read_csv(r'C:\Users\1\Desktop\test\pandas\cars.csv')  # tsv、txt文件同样使用read_csv()
# df = pd.DataFrame(csv)
# print(df)

# 2.数据透视表
data = pd.read_excel(r'C:\Users\1\Desktop\test\pandas\6.xlsx')
df = pd.DataFrame(data)
# pivot_table()制作数据透视表 index=透视表列名  columns=透视表行名  values=数据求和  aggfunc=np.sum格式化数据
table = df.pivot_table(index='名字', columns='折扣', values='原价', aggfunc=np.sum)
df1 = pd.DataFrame(table)
df1['总计'] = df1[[0.2, 4.2, 8.2]].sum(axis=1)
print(df1)
