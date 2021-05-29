# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 16:00:50 2020

@author: Supriya
"""
#import nltk     # use any one of import statements if this statement is used then, tokens=nltk.word_tokenize(text)   to be used
from nltk import word_tokenize
text = "Hey @airvistara , not #flyinghigher these days we heard? #StayingParkedStayingSafe #LetsIndiGo"
tokens=word_tokenize(text)
print(tokens)