#-*- coding: utf-8 -*-
import os
import cv2

def getAllFiles(src_dir):
    filelist = []
    for file_ in os.listdir(src_dir):
        cur_file = os.path.join(src_dir, file_)
        if os.path.isdir(cur_file):
            filelist.extend(getAllFiles(cur_file))
        else:
            if cur_file.endswith('.bmp'):
                # cur_file = cur_file.decode("utf-8").encode('gbk')
                filelist.append(cur_file)
    return filelist

def split(src_dir, dst_dir):
    all_files = getAllFiles(src_dir)
    for file_ in all_files:
        image = cv2.imread(file_)
        file_name = file_.split('\\')[-1].split('.')[0]

        half_width = image.shape[1] // 2
        image1 = image[:, 0:half_width, :]
        image2 = image[:, half_width:, :]

        now_dst_dir = os.path.join(dst_dir, file_[len(src_dir)+1:file_.rfind('\\')])
        if not os.path.exists(now_dst_dir):
            os.makedirs(now_dst_dir)
        file_name1 = os.path.join(now_dst_dir, file_name + '_1.png')
        file_name2 = os.path.join(now_dst_dir, file_name + '_2.png')
        cv2.imwrite(file_name1, image1)
        cv2.imwrite(file_name2, image2)

if __name__ == '__main__':
    src_dir =r'C:\Users\46112\Desktop\gw4_kyb'
    src_dir = src_dir.encode("utf-8").decode('gbk')
    dst_dir = r'C:\Users\46112\Desktop\gw4_kyb\split'
    if not os.path.exists(dst_dir):
        os.makedirs(dst_dir)
    dst_dir = dst_dir.encode("utf-8").decode('gbk')
    split(src_dir, dst_dir)