#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import pandas as pd

# 1.excel列与列计算（计算所有单元格）
# ex2 = pd.read_excel(r'C:\Users\1\Desktop\test\pandas\2.xlsx')
# df = pd.DataFrame(ex2)
# now_price = df['原价'] * df['折扣']
# df['现价'] = now_price
# print(df)

# 2.计算部分单元格数据
# ex2 = pd.read_excel(r'C:\Users\1\Desktop\test\pandas\2.xlsx')
# df = pd.DataFrame(ex2)
# for i in range(4, 10):
#     df['现价'].at[i] = df['原价'].at[i] * df['折扣'].at[i]  # 遍历索引取值 单元格与单元格进行计算
# print(df)

# 3.列增值
# ex2 = pd.read_excel(r'C:\Users\1\Desktop\test\pandas\2.xlsx')
# df = pd.DataFrame(ex2)
# df['原价'] = df['原价'].apply(lambda x:x+5)  # apply函数遍历每一行DataFrame的数据，将所有结果组合成一个Series数据结构并返回
# print(df)

# 4.Excel排序
# ex2 = pd.read_excel(r'C:\Users\1\Desktop\test\pandas\2.xlsx')
# df = pd.DataFrame(ex2)
# df.sort_values(by=['原价'],inplace=True,ascending=[False])  # by=要排序的列名，ascending=True从小到大，Flase从大到小,对应by
# print(df)

# 5.数据筛选
ex2 = pd.read_excel(r'C:\Users\1\Desktop\test\pandas\2.xlsx')
df = pd.DataFrame(ex2)
fin = df.loc[df['原价'].apply(lambda x:x>13 and x<19)]
print(fin)