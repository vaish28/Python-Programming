# -*- coding: utf-8 -*-
"""
Created on Mon May  3 07:18:11 2021

@author: User
"""
'''
List slicing
'''

import numpy as np
array = np.zeros([2,4,3],dtype=np.uint8) 
print('Original array is: \n ',array, '\n')

array[:,:2] = [5,5,5] 
print('After filling array by 5 array is : \n ',array,'\n')

array[:,2:] = [1,1,1]
print('After filling array by 1 array is : \n ',array,'\n')

