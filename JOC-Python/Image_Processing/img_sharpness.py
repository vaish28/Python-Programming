# -*- coding: utf-8 -*-
"""
@author: Vaishnavi

Image sharpness
"""
from PIL import Image, ImageEnhance 
  
# Opening Image 
img = Image.open("blur1.png") 
  
# Creating object of Sharpness class 
im_s = ImageEnhance.Sharpness(img) 
  
# showing resultant image 
#An enhancement factor of 0.0 gives a blurred image, 
#a factor of 1.0 gives the original image, 
#and a factor of 2.0 gives a sharpened image.
#im_s.enhance(2.0).show()     # try 2.0 and 3

# saving resultant image 
im_s.enhance(2.0).save("blur1_IE_shrp20April2021.png")