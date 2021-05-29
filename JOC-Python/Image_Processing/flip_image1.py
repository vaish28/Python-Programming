# -*- coding: utf-8 -*-
"""
Created on Sat May  1 13:16:49 2021

@author: User
"""

'''
from PIL import Image

my_img = Image.open('C:/Users/User/Desktop/OpenCV/resources/photos/lena.png')

transposed_img = my_img.transpose(Image.FLIP_LEFT_RIGHT)

transposed_img.save("flipped_1.png")

'''

from PIL import Image
my_img_1 = Image.open('C:/Users/User/Desktop/OpenCV/resources/photos/original2.png')

transposed_img_hand = my_img_1.transpose(Image.FLIP_LEFT_RIGHT)
transposed_img_hand.save("flipped_3.png")