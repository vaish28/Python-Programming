# -*- coding: utf-8 -*-
"""
Regular Expression tokenizer
"""

# A RegexpTokenizer splits a string into substrings using a regular expression

from nltk.tokenize import RegexpTokenizer
text="Hey @airvistara , not #flyinghigher these days we heard? #StayingParkedStayingSafe #LetsIndiGo"
tokenizer = RegexpTokenizer('\w+')       #('\s+', gaps=true) 
tokens=tokenizer.tokenize(text)
print(tokens)