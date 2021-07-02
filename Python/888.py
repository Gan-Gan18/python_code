import os
import shutil

ori_path = r'E:\dataset\RMB_data\rmb_segmentation\20210427jiachaopiao'
copy_path = r'E:\dataset\RMB_data\rmb_segmentation\label_data_ori\red'

folders = os.listdir(ori_path)
for folder in folders:
    img_path = ori_path + '/' + folder
    files = os.listdir(img_path)

    for file in files:
        if file.split('.')[0] == '正面检测_全局检测_全局透红外':
            file_fullname = os.path.join(img_path, file)
            print(file_fullname)
            shutil.copy(file_fullname, copy_path + '/' + str(folder.split('-')[0:3]).replace('[','').replace(']','').replace("'",'').replace(',','-').replace(' ','') + '.jpg')










dir_list = []
tmp_list = []
for root,dirs,files in os.walk(ori_path):

    for each in dirs:
        dir_list.append(str(each.split('-')[0:3]))
    for tmp in dir_list:
        tmp_list.append(str(tmp).replace("'", "").replace(',', '').replace(' ', ''))


    for file in files:
        if file.split('.')[0] == '正面检测_全局检测_全局正白光':
            file_fullname = os.path.join(root,file)
            print(file_fullname)
