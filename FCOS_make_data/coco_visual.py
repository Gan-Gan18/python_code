#coding: utf-8

import json
import os
import cv2
from collections import defaultdict

def parase_json_file(js_file):
    with open(js_file, 'r') as f:
        js_content = json.load(f)
        # print("js_content: {}".format(js_content))
        for key, value in js_content.items():
            print("key: {}, \nvalue: {}\n".format(key, value))
        # print(len(js_content))
        images = js_content['images']
        annotations = js_content['annotations']
        categories = js_content['categories']

        return images, annotations, categories

if __name__ == '__main__':
    # COLORS = [(0, 0, 255), (255, 0, 0),(0,255,255),(0,255,0),(255,255,255)]
    COLORS = [(0, 0, 255), (255, 0, 0), (0, 255, 255), (0, 255, 0)]
    # COLORS = [(0, 0, 0),(0, 0, 255), (0, 100,98), (255,0,0), (255, 255, 255), (0, 0, 0),(0,255,0)]
    image_root = r'E:\dataset\jcp_data\rope_clothes\COCO\val2014\images_0629/'
    js_file = r'E:\dataset\jcp_data\rope_clothes\COCO\val2014\annotations_0629\instances_val2014.json'
    images, annotations, categories = parase_json_file(js_file)
    id_to_categories = {}
    for category in categories:
        id_to_categories[category['id']] = category
    # id_to_categories = [{category['id']: category} for category in categories]
    # print("id_to_categories: {}".format(id_to_categories))
    # print("images: {}".format(images))
    # print("annotations: {}".format(annotations))
    # print("categories: {}".format(categories))
    img2anns = defaultdict(list)
    for ann in annotations:
        image_id = ann['image_id']
        img2anns[image_id].append(ann)
    id2name = {}
    for img in images:
        img_id = img['id']
        img_name = img['file_name']
        id2name[img_id] = img_name

    for img_id,img_name in id2name.items():
        image_bgr = cv2.imread(image_root+img_name)
        anns = img2anns[img_id]
        for annotation in anns:
            bbox = annotation['bbox']
            category_id = annotation['category_id']
            print(".....................",COLORS[category_id % len(COLORS)])
            category_name = id_to_categories[category_id]['name']
            cv2.rectangle(image_bgr, (bbox[0], bbox[1]), (bbox[0] + bbox[2], bbox[1] + bbox[3]),
                          COLORS[category_id % len(COLORS)], 3)
            # cv2.putText(image_bgr, 'label:{}, class:{}'.format(category_id, category_name), (bbox[0], bbox[1]),
            #             cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 255), 3)
        cv2.imwrite(r'E:\dataset\jcp_data\rope_clothes\COCO\val2014\result/'+img_name, image_bgr)
        # cv2.waitKey()
        # cv2.destroyAllWindows()