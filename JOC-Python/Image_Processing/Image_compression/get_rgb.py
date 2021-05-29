# -*- coding: utf-8 -*-
"""
Created on Mon May  3 09:00:45 2021

@author: User
"""

from PIL import Image
import numpy as np
im  = Image.open('F:/Spyder Codes/test_2.png') # dimensions are wifth =200 and height 100
print(im.size)
print(im.mode)

img = np.asanyarray(Image.open('F:/Spyder Codes/test_2.png'))
print("asanyarray")
print(img)

rgb_im = im.convert('RGB') # convert image to RGB matrix
print("RGB matrix")
print(rgb_im)

r,g,b = rgb_im.getpixel((199,0)) #get pixel RGB values

# get pixel RGB values (0,0) to (99,0) = RGB value 0,255,255
# from (100,0) = RGB values are 132,112,255

#RGB value of white is (255,255,255)
# RGB value of balck is (0,0,0)

#https://imagecolorpicker.com/en


#print(r,g,b)
 
