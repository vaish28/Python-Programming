# -*- coding: utf-8 -*-
"""
Created on Sat May  1 13:30:08 2021

@author: User
"""

from PIL import Image

my_img = Image.open('C:/Users/User/Desktop/OpenCV/resources/photos/download.png')

transposed_img = my_img.transpose(Image.FLIP_TOP_BOTTOM)

transposed_img.save("flipped_3.png")

