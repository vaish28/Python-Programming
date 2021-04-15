print("Welcome to sub-list operations")
L=[]
L1=[]
L2=[]
size=int(input('Enter the size of the list'))

for i in range(size): 
    num=int(input("Enter a number"))
    L.append(num)
for j in range(size):
    if(L[j]%2==0):
        L1.append(L[j])
    else:
        L2.append(L[j])
print(L1)
print(L2)

print("Sum of elements in given list is :", sum(L1))
print("Sum of elements in given list is :", sum(L2))

'''OUTPUT
Welcome to sub-list operations
Enter the size of the list5
Enter a number5
Enter a number6
Enter a number3
Enter a number8
Enter a number12
[6, 8, 12]
[5, 3]
('Sum of elements in given list is :', 26)
('Sum of elements in given list is :', 8)
'''
