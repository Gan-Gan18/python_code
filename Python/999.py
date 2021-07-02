import numpy as np
import PIL.Image
import glob
import os

path = r'C:\Users\1\Desktop\20210629160534\src\Segmentation_result'


for file_name in glob.glob(os.path.join(path, '*.png')):
    img = PIL.Image.open(file_name)
    img_dtype = np.array(img)
    # img = img.convert('RGB')
    print(img.getbands)
    print(img_dtype.dtype)