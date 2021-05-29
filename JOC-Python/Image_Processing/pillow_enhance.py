# -*- coding: utf-8 -*-
"""
Created on Tue Apr 20 12:26:09 2021

@author: User
"""

# histogram equalisation ; adapative  histogram equalization
# improve the contrast of the picture using a clahe object

from PIL import Image,ImageEnhance
img = Image.open('C:/Users/User/Desktop/OpenCV/resources/photos/blur1.png')
im_c = ImageEnhance.Contrast(img)
im_c.enhance(3.0).save("blur_enhanced.png")
img1 = Image.open("blur_enhanced.png")
img1.show()