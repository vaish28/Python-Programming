# -*- coding: utf-8 -*-
"""
Whitespace tokenizer
"""
#Tokenizes a string on whitespace (space, tab, newline).

from nltk.tokenize import WhitespaceTokenizer

text='Totally, @airvistara! Staying home is the safe feeling! #Staying ParkedStaying Safe
tokens=WhitespaceTokenizer().tokenize(text)
print(tokens)