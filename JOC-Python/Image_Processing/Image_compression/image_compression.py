# -*- coding: utf-8 -*-
"""
Created on Wed May  5 16:47:00 2021

@author: User
"""

import numpy as np
from PIL import Image

im=Image.open('C:\Users\User\Desktop\JOC-Python\Codes_given_by_maam\image_compressiom\Lena1-8bitImage.png')  # open file and make object im; 256KB size
print(im.mode,im.size)
'''
The following is the explaination for open() method
#(PIL.Image.open(fp, mode='r') Opens and identifies the given image file.
#This is a lazy operation; this function identifies the file, but the file remains
# open and the actual image data is not read from the file until you try to process 
# the data (or call the load() method).
'''

pixelMap=im.load()  # load image


ImasArray = np.asanyarray(Image.open('Lena-image.png'))  #to see as matrix, try this
#ImasArray = np.asanyarray(Image.open('Lena1-8bitImage.png'))
print(ImasArray)  

img = Image.new(im.mode, im.size) # create a new image of same size and mode as lena or obj im; im.size -2-tuple containing (width, height) in pixels

pixelNew=img.load()

'''
original image is taking 8-bit per pixel (2^8=256)
for compression: we will only use 3 bit(2^3=8). ie: 8 bit to 3 bit mapping
# how to do? divide 2^8 by 2^3=2^5
# therefore, for any no between 0-31 assign 0, 32-63==>1; 64-95==>2; 96-127==>3 
128-159==>4; 160-191==>5; 192-223==>6;224-255==>7
'''

for i in range(img.size[0]):      # size[0] is width of image and size[1] is height of image
    for j in range(img.size[1]):
        if(pixelMap[i,j]>=0 and pixelMap[i,j]<=31):
            pixelNew[i,j]=0
        elif(pixelMap[i,j]>=32 and pixelMap[i,j]<=63):
            pixelNew[i,j]=1
        elif(pixelMap[i,j]>=64 and pixelMap[i,j]<=95):
            pixelNew[i,j]=2
        elif(pixelMap[i,j]>=96 and pixelMap[i,j]<=127):
            pixelNew[i,j]=3
        elif(pixelMap[i,j]>=128 and pixelMap[i,j]<=159):
            pixelNew[i,j]=4
        elif(pixelMap[i,j]>=160 and pixelMap[i,j]<=191):
            pixelNew[i,j]=5
        elif(pixelMap[i,j]>=192 and pixelMap[i,j]<=223):
            pixelNew[i,j]=6
        elif(pixelMap[i,j]>224 and pixelMap[i,j]<=255):
            pixelNew[i,j]=7

img.save('Lena-8bitImage-output.png')

ImasArray1 = np.asanyarray(Image.open('Lena-8bitImage-output.png'))
print(ImasArray1)  
            
