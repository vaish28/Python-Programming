# -*- coding: utf-8 -*-
"""
@author: Vaishnavi

Image flip
"""

from PIL import Image
     
# Python Imaging Library (PIL)
# a free library for the Python programming language that adds support 
# for opening, manipulating, and saving many different image file formats. 
#It is available for Windows, Mac OS X and Linux

# use input images: original, original2 and original3


my_img = Image.open('original2.png')

#Transpose image (flip or rotate in 90 degree steps) left to right

transposed_img = my_img.transpose(Image.FLIP_LEFT_RIGHT)

transposed_img.save('flipped20Apr2021.png')

print('flipping of image done!')       

# transpose methods: https://pillow.readthedocs.io/en/stable/reference/Image.html
# top-bottom, rotate, etc.