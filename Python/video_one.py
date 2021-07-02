# coding=utf-8
'''
In this example, we will load a RefineDet model and use it to detect objects.
'''

import argparse
import os
import cv2

cap = cv2.VideoCapture(r"E:\dataset\jinku_data\0220\segLoc.mp4")
count = 0
save_count = 0
save_path = r"E:\dataset\jinku_data\0220\images\0220_1"
if not os.path.exists(save_path):
    os.makedirs(save_path)
while (1):
    ret, frame = cap.read()
    # get a frame
    count += 1
    # print(count)
    if count %7 == 0:
        # if count < 8000:
        #     continue
        # frame = cv2.resize(frame, (1280, 720))
        name = save_path + "/%06d"%(count) + ".jpg"
        print(name)
        cv2.imwrite(name, frame)
        save_count += 1
        # print(save_count)
        # if save_count==50:
        #     print(save_count)
        #     break
    else:
        continue


