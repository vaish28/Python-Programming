# -*- coding: utf-8 -*-
"""
Created on Mon May  3 08:38:34 2021

@author: User
"""

import numpy as np
from PIL import Image

width=5
height=4

array=np.zeros([height,width,3],dtype=np.uint8)
print(array)
img= Image.fromarray(array)
img.save('test_1.png') # small rectangle with all black color, as all zero values [0,0,0]

#img.show()

array1 = np.zeros([100,200,3],dtype = np.uint8)

array1[:,:100] = [0,255,255] #cyan color left side

array1[:,100:] = [132,112,255] #right side:- light slate blue color

img1 = Image.fromarray(array1)
img1.save('test_2.png')

# 100 is the height
# 200 is the width then left and right of rectangle is equally partitioned in 0:99 and 100:199
# equal left and right sides 
# 3 is the column size 

img1.show()