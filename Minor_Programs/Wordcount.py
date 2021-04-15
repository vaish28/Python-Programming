print("Welcome to sub-list of list of strings")
print("The original list is")
this_list=["apple","mango","pappaya","babbon"];
print(this_list)
l3=[]
for word in this_list:
    ch=word[0]
    if(word.count(ch)>2):
        l3.append(word)
        
print("The later list is")
print(l3)






'''OUTPUT

Welcome to sub-list of list of strings
The original list is
['apple', 'mango', 'pappaya', 'babbon']
The later list is
['pappaya', 'babbon']


'''
