#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import pandas as pd
from matplotlib import pyplot as plt


# 1.绘制可视化图形
# price = pd.read_excel(r'C:\Users\1\Desktop\test\pandas\2.xlsx')
# df = pd.DataFrame(price)
# df.plot.bar(x='名字', y='原价', color='red')  # 获取并定义x轴y轴数据，参数需与表格内列名相同
#
# ax = plt.gca()
# ax.set_xticklabels(df['名字'], rotation=45, ha='right')  # 设置x轴标签信息，调整角度和旋转
#
# plt.xlabel('name')  # 设置x轴标题
# plt.ylabel('ori_price')  # 设置y轴标题
# plt.title('Price', fontsize=20, color='green')  # 设置大标题
# plt.tight_layout()  # 完全显示标签
# plt.savefig(r'C:\Users\1\Desktop\test\pandas\2.png')
# plt.show()

# 2.两张表数据联合
# name = pd.read_excel(r'C:\Users\1\Desktop\test\pandas\2.xlsx',sheet_name='Sheet1')
# price = pd.read_excel(r'C:\Users\1\Desktop\test\pandas\2.xlsx',sheet_name='Sheet2')
# df_name = pd.DataFrame(name)
# df_price = pd.DataFrame(price)
#
# result = name.merge(price,how='left',left_on='ID',right_on='ID').fillna(0)
#
# print(result)

# 3.数据校验
# def Score_flase(x):
#     if not 100 >= x.原价 >= 0:
#         print('名字为:{}的原价异常，数值为{}'.format(x.名字,x.原价))
#
# p = pd.read_excel(r'C:\Users\1\Desktop\test\pandas\3.xlsx')
# df = pd.DataFrame(p)
# df.apply(Score_flase, axis=1)  # axis=1从行查询

# 4.拆分列
file = pd.read_excel(r'C:\Users\1\Desktop\test\pandas\4.xlsx')
df = pd.DataFrame(file)
name = df['名字'].str.split(expand=True)
df['名字1'] = name[0]
df['名字2'] = name[1]
print(df)