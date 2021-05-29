# -*- coding: utf-8 -*-
"""
Created on Sun May 23 19:47:24 2021

@author: User
"""

import cv2

# use input images blur1, blur3, blur4... file type PNG or JPG

#add your path here
img = cv2.imread('path/blur1.png')  # reading file

print('Color image-blur1.png: Its Shape is :',img.shape,'\n')  # row X Col X channels

print('Image Matrix of Color image-blur1.png:\n',img,'\n')   # matrix/3D array printed

#CLAHE (Contrast Limited Adaptive Histogram Equalization) to improve the contrast of the image

clahe = cv2.createCLAHE()    # create a CLAHE object

# to convert image to gray scale   

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

print('Converted Gray imag of blur1.png: Its Shape is :',gray_img.shape,'\n')  # row X Col

print('Image Matrix of converted grey image-blur1.png:\n',gray_img,'\n')   # matrix/2D array printed

enh_img = clahe.apply(gray_img)    # Apply CLAHE

cv2.imwrite('blur1_after_20Apr2021.png', enh_img)  

print("enhancing of image done!")

