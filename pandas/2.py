#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import pandas as pd

# 1.创建excel文件
# a = {'name': ['abc', 'def'],
#      'age': ['35', '65'],
#      'QQ': ['4366742', '3576424'],
#      'wechat': ['gh452', 'fgg35']
#      }
# info = pd.DataFrame(a, columns=['name', 'age', 'QQ', 'wechat'])
# info.to_excel(r"C:\Users\1\Desktop\test\pandas\1.xlsx")
# print('done')


# 2.读取Excel文件
# people = pd.read_excel(r"C:\Users\1\Desktop\test\pandas\1.xlsx", header=None)
# people.columns = ['name', 'age', 'QQ', 'wechat']  # 自定义列名
# people.to_excel(r"C:\Users\1\Desktop\test\pandas\1.xlsx")  # 可覆盖修改原文件 也可另存

# d1 = pd.Series([10,20,30],index=[1,2,3],name='a')  # 用Series创建多组行、列、索引
# d2 = pd.Series([40,50,60],index=[1,2,3],name='b')
# d3 = pd.Series([70,80,90],index=[2,3,4],name='c')
# df = pd.DataFrame({d1.name:d1,d2.name:d2,d3.name:d3})  # Series创建的值转换到Dataframe，需要用字典的形式传入
# print(df)

