#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import pandas as pd

# 1.对数据求和 算平均数
# a = pd.read_excel(r'C:\Users\1\Desktop\test\pandas\5.xlsx')
# df = pd.DataFrame(a)
# sum = df[['原价', '折扣']].sum(axis=1)  # pandas中求和函数sum() 求平均数函数mean()
# avg = df[['原价', '折扣']].mean(axis=1)
# df['总和'] = sum
# df['平均'] = avg
# print(df)

# 2.清洗重复数据(删除)
# b = pd.read_excel(r'C:\Users\1\Desktop\test\pandas\5.xlsx')
# df = pd.DataFrame(b)
# df.drop_duplicates(subset='原价', inplace=True, keep='last')  # drop_duplicates()删除 subset=要清洗的列 keep选择保留前者还是后者
# print(df)

# 3.筛选出重复数据（不删除）
# c = pd.read_excel(r'C:\Users\1\Desktop\test\pandas\5.xlsx')
# df = pd.DataFrame(c)
# re = df.duplicated(subset='原价')
# re = re[re == True]  # 找出重复项
# print(df.iloc[re.index])

# 4.数据转置
d = pd.read_excel(r'C:\Users\1\Desktop\test\pandas\5.xlsx')
df = pd.DataFrame(d)
table = df.transpose()  # transpose()转置
print(table)
