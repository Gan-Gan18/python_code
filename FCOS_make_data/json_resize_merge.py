"""
将所有文件合并到一个目录下面

"""
import os
import sys
import json
import io
import cv2
import numpy as np
import random
import os.path as osp
import glob


def listDir(rootDir, image_list, endwith1):
    files = os.listdir(rootDir)
    for filename in os.listdir(rootDir):
        pathname = os.path.join(rootDir, filename)
        if os.path.isfile(pathname):
            if pathname.split(".")[-1] in [endwith1]:
                image_list.append(pathname)
        else:
            listDir(pathname ,image_list,endwith1)

image_list = []

rootDir = r"E:\dataset\jcp_data\rope_clothes\20210324"
# save_dir = "D:\data\\pole_720p_0806\\"
save_dir = r"E:\dataset\jcp_data\rope_clothes\merge_0324\\"
img_name_prex ="0324000"
if not os.path.exists(save_dir):
    os.makedirs(save_dir)
# 金库
# size = [1280,720]
# 检测棚
# size = [704,576]

listDir(rootDir, image_list,"jpg")
count=0
for image_file in image_list:
    json_file = image_file.split(".jpg")[0] + ".json"
    if not os.path.exists(json_file):
        continue
    ori_json_file = json.load(open(json_file, 'r'))
    print(json_file)
    ori_shapes = ori_json_file['shapes']
    ori_shapes1 = []
    data = ori_json_file['imageData']

    # image_ori = cv2.imread(image_file)
    # image = cv2.resize(image_ori,(size[0],size[1]))
    #
    #
    #
    # scale_h = size[1]/image_ori.shape[0]
    # scale_w = size[0]/image_ori.shape[1]
    #
    # ori_h,ori_,c =image.shape
    # if data is not None:
    #     ori_json_file['imageData'] = None
    #     ori_json_file['"imageWidth"'] = size[0]
    #     ori_json_file['imageHeight'] = size[1]
    for j in range(len(ori_shapes)):
        tmp={}
        # tmp["shape_type"] = ori_shapes[j]["shape_type"]
        a = list(ori_shapes[j].keys())
        if "flags"in a:
            tmp["flags"] = ori_shapes[j]["flags"]
        if "shape_type" in a:
            tmp["shape_type"] = ori_shapes[j]["shape_type"]
        if "group_id" not in a:
            tmp['line_color'] = ori_shapes[j]["line_color"]
            tmp['fill_color'] = ori_shapes[j]["fill_color"]
        elif "group_id" in a:
            tmp["group_id"] = ori_shapes[j]["group_id"]
        tmp["label"] = ori_shapes[j]["label"]
        points = np.array(ori_shapes[j]['points'])

        shape = points.shape
        xmin = min(points[:,0])*scale_w
        ymin = min(points[:,1])*scale_h
        xmax =max(points[:, 0])*scale_w
        ymax =max(points[:, 1])*scale_h
        tempxy = []
        # if xmin > 1000:
        #     continue
        if points.shape[0] == 2:
            tempxy.append([xmin, ymin])
            tempxy.append([xmax, ymax])
        elif points.shape[0] == 4:
            tempxy.append([xmin, ymin])
            tempxy.append([xmax, ymin])
            tempxy.append([xmax, ymax])
            tempxy.append([xmin, ymax])

        tmp['points'] = tempxy
        ori_shapes1.append(tmp)
    ori_json_file["shapes"]=ori_shapes1
    name = json_file.split("\\")[0].split("/")[-1]
    count+=1

    if image is not None:
        save_image = save_dir+img_name_prex+str(count)+".jpg"
        # save_image = save_dir+str(count)+".jpg"
        cv2.imwrite(save_image,image)
        ori_json_file["imagePath"] = img_name_prex+str(count)+".jpg"
        save_json = save_dir+img_name_prex+str(count)+".json"
        # ori_json_file["imagePath"] = str(count)+".jpg"
        # save_json = save_dir+str(count)+".json"
        with open(save_json, "w") as f:
            json.dump(ori_json_file,f)
        # print(save_image,save_json)




# def draw_rectangle():
#     ori_img_files = glob.glob(read_folder + '*.jpg')
#     ori_json_files = glob.glob(read_folder + '*.json')
#     for i in range(len(ori_json_files)):
#         json_name = ori_json_files[i].split("\\")[-1].split(".")[0]
#         imag_name = ori_json_files[i].split("\\")[0]+"\\"+json_name+".jpg"
#         ori_img = cv2.imread(imag_name)
#         # write_name = osp.join("D:/data/detect/full_SDG/first-SDG_xg",osp.basename(imag_name))
#         # cv2.imwrite(write_name,ori_img)
#         ori_json_file = json.load(open(ori_json_files[i], 'r'))
#         ori_shapes = ori_json_file['shapes']
#         for j in range(len(ori_shapes)):
#             points = np.array(ori_shapes[j]['points'])
#             label = ori_shapes[j]["label"]
#             print(label,imag_name)
#             if label=="f":
#                 print("")
#             xmin = min(points[:, 0])
#             xmax = max(points[:, 0])
#             ymin = min(points[:, 1])
#             ymax = max(points[:, 1])
#             cv2.rectangle(ori_img,(xmin,ymin),(xmax,ymax), (0, 0, 255), 1)
#         # with open(osp.join("D:/data/detect/full_SDG/first-SDG_xg",osp.basename(ori_json_files[i])),"w") as f:
#         #    json.dump(ori_json_file,f)
#     # print("done")
# draw_rectangle()


