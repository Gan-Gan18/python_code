# coding: utf-8

'''
    Labelme标注生成的json文件可视化

    当前仅支持bounding box的可视化
'''

import os
import json
import cv2
import shutil
import glob

COLORS = [(0, 255, 0), (0, 0, 255), (255, 0, 0), (0, 255, 255), (255, 255, 255)]


def make_if_not_exit(dir):
    """
    创建文件目录[若目录不存在]
    """
    if not os.path.exists(dir):
        os.makedirs(dir)


class LabelmeJsonParser(object):

    def __init__(self, json_filename, image_filename, save_images=False):
        # assert os.path.exists(json_filename), "{} not exist".format(json_filename)
        # assert os.path.exists(image_filename), "{} not exist".format(image_filename)
        self.json_filename = json_filename
        self.image_filename = image_filename
        self.save_images = save_images
        with open(json_filename, 'r') as f:
            self.json_content = json.load(f)
        # self._print_json_info()
        self._analyze_shapes()

        if self.save_images:
            root_path = os.path.dirname(json_filename)
            self.save_root = os.path.join(root_path, 'visualize_json')
            make_if_not_exit(self.save_root)

            save_path = os.path.join(self.save_root, 'ori')
            make_if_not_exit(save_path)
            shutil.copy(self.image_filename, save_path)
            shutil.copy(self.json_filename, save_path)

    def _print_json_info(self):
        for key, value in self.json_content.items():
            print("key: {}, \nvalue: {}\n".format(key, value))

    def _analyze_shapes(self):
        '''
        对self.json_content按shape和标签分类
        :return:
        '''
        self.shape_types = []
        self.shapes = {}
        for shape in self.json_content['shapes']:
            if shape['shape_type'] not in self.shape_types:
                self.shape_types.append(shape['shape_type'])
            if shape['label'] not in self.shapes.keys():
                self.shapes[shape['label']] = []
            self.shapes[shape['label']].append(shape)
        # print("self.shape_types: {}".format(self.shape_types))
        # print("self.shapes: {}".format(self.shapes))

    def _draw_image(self, image, shape):
        def get_points(points):
            point1 = (int(points[0][0]), int(points[0][1]))
            point2 = (int(points[1][0]), int(points[1][1]))
            return point1, point2

        shape_type = shape['shape_type']
        if shape_type == 'rectangle':
        # if shape_type == 'polygon':
            p1, p2 = get_points(shape['points'])
            cv2.rectangle(image, p1, p2, COLORS[0], 2)
        return image

    def visualize(self, shape_types=None):
        if shape_types is None:
            shape_types = self.shape_types
        for shape_type in shape_types:
            for label, shape_list in self.shapes.items():
                image = cv2.imread(self.image_filename)
                if self.save_images:
                    save_path = os.path.join(self.save_root, str(label))
                    make_if_not_exit(save_path)
                else:
                    cv2.namedWindow(self.image_filename, cv2.WINDOW_NORMAL)
                for shape in shape_list:
                    if shape["shape_type"] == shape_type:
                        image = self._draw_image(image, shape)

                if self.save_images:
                    save_name = os.path.join(save_path, os.path.basename(self.image_filename))
                    cv2.imwrite(save_name, image)
                else:
                    cv2.putText(image, "label: {}".format(label), (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 1.0,
                                (0, 0, 255), 2)
                    cv2.imshow(self.image_filename, image)
                    cv2.waitKey()
                    cv2.destroyAllWindows()


if __name__ == '__main__':
    labeled_root = r'E:\dataset\jcp_data\tantou\20211025_tantouyiwu\images\merge\check\stone'
    file_list = []
    for file in glob.glob(os.path.join(labeled_root, "*.json")):
        file_list.append(file)
    for json_file in file_list:
        image_file = json_file.split('.')[0] + '.jpg'
        if not os.path.exists(image_file):
            continue
        parser = LabelmeJsonParser(json_file, image_file, save_images=True)
        parser.visualize()
