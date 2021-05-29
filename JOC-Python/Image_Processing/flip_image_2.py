# -*- coding: utf-8 -*-
"""
Created on Sat May  1 13:23:04 2021

@author: User
"""

from PIL import Image

my_img = Image.open('C:/Users/User/Desktop/OpenCV/resources/photos/lena.png')

transposed_img = my_img.transpose(Image.FLIP_TOP_BOTTOM)

transposed_img.save("flipped_2.png")
new_img = Image.open("flipped_2.png")
new_img.show()