# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 08:29:54 2021

@author: User
"""

from PIL import Image,ImageEnhance
img = Image.open('C:/Users/User/Desktop/OpenCV/resources/photos/blur1.png')
im_s = ImageEnhance.Sharpness(img)
im_s.enhance(2.0).save("blur_sharp_image.png")
img1= Image.open('blur_sharp_image.png')
img1.show()