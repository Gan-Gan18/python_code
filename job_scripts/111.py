#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import os
import json
import glob

root_path = r'E:\dataset\jcp_data\test-0321\json'
bbox_txt = r'E:\dataset\jcp_data\test-0321\bbox.txt'
add_info = []
jsonFile = []
null = None

text = open(bbox_txt, 'r', encoding='utf-8')
for line in text.readlines():
    new_name = {"label": "person", "points": eval(line.strip()), "group_id": null, "shape_type": "rectangle",
                "flags": {}}
    add_info.append(new_name)

for json_file in glob.glob(os.path.join(root_path, "*.json")):
    jsonFile.append(json_file)
    print('process: ' + json_file)

for a in range(len(add_info)):
    with open(jsonFile[a], 'r') as jf:
        info = json.load(jf)
        info['shapes'].append(add_info[a])
        with open(jsonFile[a], 'w', encoding='utf-8') as new_jf:
            json.dump(info, new_jf)
