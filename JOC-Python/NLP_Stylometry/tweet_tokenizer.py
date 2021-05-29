# -*- coding: utf-8 -*-
"""
Tweet tokenizer
"""

#Tokenizer for tweets

from nltk.tokenize import TweetTokenizer
text="Hey @airvistara , not #flyinghigher these days we heard? #StayingParkedStayingSafe #LetsIndiGo laugh/cry"
tk = TweetTokenizer()
tokens=tk.tokenize(text)
print(tokens)
'''
['Hey', '@airvistara', ',', 'not', '#flyinghigher', 'these', 'days', 
 'we', 'heard', '?', '#StayingParkedStayingSafe', '#LetsIndiGo', 'laugh', '/', 'cry']

'''
