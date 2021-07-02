# coding=utf-8
import os
# import os.path
import shutil  # Python文件复制相应模块

label_dir = r'E:\dataset\ZhongChe_data\sdg\xml_check\VOC2007_0424\1\ori/'  # 所有xml文件所在文件夹
path = r'E:\dataset\ZhongChe_data\sdg\xml_check\VOC2007_0424\1\sdg_result0424/'  # 图片文件夹
annotion_dir =r'E:\dataset\ZhongChe_data\sdg\xml_check\VOC2007_0424\1\2'  # 粘贴对应图片名称的xml文件到指定文件夹
path_list = os.listdir(path)  # os.listdir(file)会历遍文件夹内的文件并返回一个列表
# print(path_list)
path_name = []  # 定义一个空列表,不需要path_list中的后缀名
# 利用循环历遍path_list列表并且利用split去掉后缀名
for i in path_list:
    path_name.append(i.split(".")[0])
# print(path_name)
# 排序一下
path_name.sort()
for file_name in path_name:
    # "a"表示以不覆盖的形式写入到文件中,当前文件夹如果没有"save.txt"会自动创建
    with open("save.txt", "a") as f:
        f.write(file_name + "\n")
        # print(file_name)
    f.close()
f = open("save.txt", "r")  # 设置文件对象
lines = f.readlines()
# print (lines)
s = []
for line in lines:
    line = line.strip()
    print(line)
    tempxmlname = '%s.xml' % line
    print(tempxmlname)
    xmlname = os.path.join(label_dir, tempxmlname)
    print(xmlname)
    os.listdir(label_dir)
    shutil.copy(xmlname, annotion_dir)