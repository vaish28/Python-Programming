# -*- coding: utf-8 -*-
"""
Word tokenizer
"""
#used to find the words and punctuation in a string. Separates words using spaces and punctuations.

#import nltk     # use any one of import statements if this statement is used then, tokens=nltk.word_tokenize(text)   to be used
from nltk import word_tokenize
text = "Hey @airvistara , not #flyinghigher these days we heard? #StayingParkedStayingSafe #LetsIndiGo laugh/cry"
tokens=word_tokenize(text)
print(tokens)