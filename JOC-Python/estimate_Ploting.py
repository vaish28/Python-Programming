# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 06:56:09 2018

@author: Supriya
feedback: asked to guess a number about a jar containing colored stones
actual number of stones is 50
"""

import matplotlib.pyplot as grph
from statistics import mean, median
from scipy import stats

feedback = [10,15,25,18,58,45,20,30,100,60,75,70,80,85,65,90,55,66,88,68,40,95,35]
feedback.sort()
print ("After sorting feedback list...",feedback, "\n")
print ("Length of feedback list:",len(feedback), "\n")

# using scipy module mean calculation can be as simple as this:
meantrim = stats.trim_mean(feedback,0.1)
print("Mean using scipy.stats: ", meantrim, "\n")

# for using statistics module for mean and median calculation...pre-work  
trim10 = int(0.1*len(feedback))
print ("trim value: ", trim10, "\n")

feedback = feedback[trim10:]
print ("feedback list after trimming on LHS of list  ", feedback, "\n\n")
feedback = feedback[:(len(feedback)-trim10)]
print ("feedback list after trimming on RHS of list  ", feedback, "\n\n")

# Using statistics module for mean and median calculation
mn=mean(feedback)
meen=[]
meen.append(mn)

med = median(feedback)
medi=[]
medi.append(med)

print ("Mean value of the feedback list:", mean(feedback), "\n\n")

print ("Median value of the feedback list:", median(feedback), "\n\n")

# Ploting the list, mean and median and actual number of colored stones
y=[]
for i in range(len(feedback)):
    y.append(10)
grph.plot(feedback,y, "r--")  # red dash
grph.plot([mean(feedback)],[10],'bs')
grph.plot(medi,[10],'g^')
grph.plot([50],[10],'ro')    # actual no of stones





    
    