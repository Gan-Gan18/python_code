# -*- coding: utf-8 -*-
import os
import cv2

parantFold='Z:/dataset/rmbProject/coin/colorsegment/20200518/aligned/'
imageFold=parantFold+'img/'
imageSaveFold=parantFold+'imgResize/'

if not os.path.exists(imageSaveFold):
    os.makedirs(imageSaveFold)
    

ratio=0.5


fileList=os.listdir(imageFold)

for file in fileList:
    imgFileName=imageFold+file
#    pureName=os.path.basename(imgFileName).split('.')[0]
    imageData=cv2.imread(imgFileName)

    h,w,c=imageData.shape
    reH,reW=int(ratio*h),int(ratio*w)
    imageDataResize=cv2.resize( imageData,(reH,reW) ,cv2.INTER_NEAREST )
    
    cv2.imwrite( imageSaveFold+file,imageDataResize )

