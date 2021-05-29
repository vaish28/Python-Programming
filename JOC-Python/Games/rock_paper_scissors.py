# -*- coding: utf-8 -*-
"""
Created on Wed Apr 21 07:29:03 2021

@author: User
"""

def rock_paper_scissor(num1,num2,bit1,bit2):
    p1=int(num1[bit1])%3   # to get position value. %3 because we have 3 values, 0,1,2
    print(p1)
    p2=int(num2[bit2])%3
    # rock, paper and scissors so %3
    print(p2)
    print(ply_1[p1])
    print(ply_2[p2])
    
    if(ply_1[p1]==ply_2[p2]):
        print("draw")
    elif(ply_1[p1]=='Rock' and ply_2[p2]=='Scissors'):
        print("player 1 wins")
    elif(ply_1[p1]=='Rock' and ply_2[p2]=='Paper'):
        print("player 2 wins") 
    elif(ply_1[p1]=='Paper' and ply_2[p2]=='Scissors'):
        print("player 2 wins")
    elif(ply_1[p1]=='Paper' and ply_2[p2]=='Rock'):
        print("player 1 wins")    
    elif(ply_1[p1]=='Scissors' and ply_2[p2]=='Paper'):
        print("player 1 wins")
    elif(ply_1[p1]=='Scissors' and ply_2[p2]=='Rock'):
        print("player 2 wins")
    
 
ply_1={0:'Rock', 1:'Paper', 2:'Scissors'}
ply_2={0:'Paper', 1:'Rock', 2:'Scissors'}

while(1):
    print('Welcome to Rock Scissors and Paper Game!')
    num1=input("Player 1, enter your choice (give 5 digit number which also contains your choice): ")
    num2=input("Player 2, enter your choice: ")
    ch_bit1=int(input("player 1, enter your secret bit position (from 0 to last minus 1): "))
    ch_bit2=int(input("player 2, enter your secret bit position: "))
    rock_paper_scissor(num1,num2,ch_bit1,ch_bit2)
    ch=input("do you want to continue (y/n): ")
    if ch=='n':
        break

