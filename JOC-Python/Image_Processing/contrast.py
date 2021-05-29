# -*- coding: utf-8 -*-
"""
Created on Mon May  3 07:14:37 2021

@author: User
"""
'''
from PIL import Image,ImageEnhance

img = Image.open('path/blur1.png')

img_contrast = ImageEnhance.Contrast(img)

img_contrast.enhance(2.0).save("contast_blur.png")
'''


from PIL import Image
from PIL import ImageEnhance

image = Image.open("path/blur1.png")
image.show()
enhancer = ImageEnhance.Contrast(image)
new_image = enhancer.enhance(1.5)

new_image.save("newImage.png")
new_image.show()
