# -*- coding: utf-8 -*-
"""
@author: Vaishnavi

Image Contrast
"""
from PIL import Image, ImageEnhance 
  
# Opening Image 
img = Image.open("blur1.png") 
  
# Creating object of contrast class 
im_c = ImageEnhance.Contrast(img) 
  
# showing resultant image
#An enhancement factor of 0.0 gives a solid grey image. 
#A factor of 1.0 gives the original image. 
#im_c.enhance(2.0).show()   

# saving resultant image 
im_c.enhance(2.0).save("blur1_IE_con20April2021.png")