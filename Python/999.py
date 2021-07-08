import numpy as np
import PIL.Image
import glob
import os
import cv2
# path = r'C:\Users\1\Desktop\20210629160534\src\Segmentation_result'
#
#
# for file_name in glob.glob(os.path.join(path, '*.png')):
#     img = PIL.Image.open(file_name)
#     img_dtype = np.array(img)
#     # img = img.convert('RGB')
#     print(img.getbands)
#     print(img_dtype.dtype)


img = cv2.imread(r'E:\PycharmProjects\Pytorch_Retinaface\data\widerface\train\images\0--Parade\0_Parade_marchingband_1_849.png')
shapes = img.shape
# height, width, _ = img.shape

print(shapes)