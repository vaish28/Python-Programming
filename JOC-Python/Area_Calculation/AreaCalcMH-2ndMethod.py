# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 18:13:29 2020

@author: Supriya
2nd method Area Calculation
"""
 
'''
scipy.misc.imread(*args, **kwds)
imread is deprecated! imread is deprecated in SciPy 1.0.0, and will be removed in 1.2.0. Use imageio.imread instead.

Read an image from a file as an array.
This function is only available if Python Imaging Library (PIL) is installed.

Parameters:	
name : str or file object
The file name or file object to be read.

flatten : bool, optional
If True, flattens the color layers into a single gray-scale layer.

mode : str, optional
Mode to convert image to, e.g. 'RGB'. See the Notes for more details.

Returns:	
imread : ndarray
The array obtained by reading the image.
'''

import scipy.misc 
import random
img = scipy.misc.imread('Map_India_with_MH.png') # returns array
count_mh=0
count_rest=0
cnt=0
while(cnt<=80000):
    #image dimention is(x,y) => length X width. But in python it is taken reverse
    x=random.randint(0,449)   #width   
    y=random.randint(0,449)   #length
    z=0 #scipy needs z dimention but our image is 2D so z=0
    if(img[x][y][z]==237):
        count_rest=count_rest+1
        cnt=cnt+1
    else:
        if(img[x][y][z]==238):
            count_mh=count_mh+1
            cnt=cnt+1
area_mh=(count_mh/count_rest)*3287263   #Area of India=3.287 million km²
print(area_mh)       #Area of Maharashtra= 307,713 km2 


        
        
        