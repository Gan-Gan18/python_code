import glob
import json
from tqdm import tqdm
import os
path = r'E:\dataset\ZhongChe_data\20200401_015755_result/'
json_list=[]
json_name=os.listdir(path)
label_list = []
file_list = glob.glob(os.path.join(path, '*.json'))
for file in tqdm(file_list):
    # 打开文件取出数据并修改，然后存入变量
    with open(file, 'r') as f:
        data = json.load(f)
        # shapes = data['shapes']
        for key,value in f.items():
            # shape['label'] = shape['label'].replace('sdasd', '')
            if f['imagePath'] == "*.bmg":
                f['imagePath'] = "*.jpg"
            # elif shape['label'] == 'p1':
            #     shape['label'] = '1'
            # elif shape['label'] == 'p2':
            #     shape['label'] = '2'
            # elif shape['label'] == 'p3':
            #     shape['label'] = '3'
            # elif shape['label'] == 'p4':
            #     shape['label'] = '4'
        # if shape['label'] not in label_list:
        #     label_list.append(shape['label'])
    # 打开文件并覆盖写入修改后内容
    with open(file, 'w') as f:
        json.dump(data, f)


for i in label_list:
    print(i)




