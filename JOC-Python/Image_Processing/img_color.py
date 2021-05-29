# -*- coding: utf-8 -*-
"""
@author: Vaishnavi

Image color
"""
from PIL import Image, ImageEnhance 
  
# Opening Image 
img = Image.open("blur1.png") 
  
# Creating object of color class 
im_cl = ImageEnhance.Color(img) 
  
# showing resultant image 
#An enhancement factor of 0.0 gives a black and white image. 
#A factor of 1.0 gives the original image.
#im_cl.enhance(2.0).show()    # try:3.0, 4.0 

# saving resultant image
im_cl.enhance(2.0).save("blur1_IE_colr.png")   # try:3.0, 4.0






