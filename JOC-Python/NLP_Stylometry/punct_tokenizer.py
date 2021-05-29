# -*- coding: utf-8 -*-
"""
Punctuation tokenizer
"""
#Tokenizes a text into a sequence of alphabetic and non-alphabetic characters. 
#splits all punctuations into separate tokens

from nltk.tokenize import WordPunctTokenizer
text="Hey @airvistara , not #flyinghigher these days we heard? #StayingParkedStayingSafe #LetsIndiGo laugh/cry"
tokens=WordPunctTokenizer().tokenize(text)
print(tokens)