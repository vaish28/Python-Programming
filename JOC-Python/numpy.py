# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 02:32:43 2021

@author: User
"""

import numpy as np
import random

a = np.arange(6)
print(a)
print(a.shape)

# [0 1 2 3 4 5]
# (6,)

print('\n')

a = np.arange(6).reshape(2,3)
print(a)
# [[0 1 2]
# [3 4 5]]


print(a.shape)
#and not shape() remember this 
#(2, 3) :- shape of the 2-d array
print(a.size)
# and not size() remember this 
#6 :- total number of elements
print('\n')
print(a.ndim)
# 2 #number of array dimensions

b = np.arange(12).reshape(2,2,3)
print(b)
# second digit represents the number of arrays in joint array like
# [0 1 2] and [3 4 5] are combined so how many of these
# so these two together [ [0 1 2] 
#                         [3 4 5 ] ]
# the next digit indicates how many elements in the each array 
# the first digit finally will explain how many such array inside array 


# [[[ 0  1  2]
#  [ 3  4  5]]

# [[ 6  7  8]
#  [ 9 10 11]]]


print('\n')


print(b.ndim)
# the number of array dimensions are 3 here 2,2 and 3

print(b.dtype)
#type of array


print('\n')

print(np.arange(4,40,4))# starting from 4 to 40(less than 40)  with a difference which is added of 4
# [ 4  8 12 16 20 24 28 32 36]
print(np.arange(40,4,-4)) # starting from 40(including 40) to 4(excluding 4) with difference of -4 subtracted from 40 onwards
# [40 36 32 28 24 20 16 12  8


print('\n')

c = np.random.random((3,4))
print(c)
# 3 rows and 4 columns
# [[0.78754657 0.36177683 0.25691026 0.47846747]
# [0.21255767 0.8819444  0.94483226 0.40598597]
# [0.15858898 0.64265153 0.59271233 0.02787171]]

print('sum',c.sum())
print('max ',c.max())
print('min ',c.min())

#sum 5.662347621705472 of entire 2-d array
#max  0.9322188721000596 from entire 2-d array
#min  0.17544758754519263 from entire 2-d array

print('\n')


arr= np.array([[1,2,3],[4,5,6]])
flat=arr.flatten()
print(flat) # straightens 2-d array into 1-d array