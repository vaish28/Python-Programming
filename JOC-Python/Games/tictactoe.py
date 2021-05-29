# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
board = np.array([['-','-','-'],['-','-','-'],['-','-','-']]) #board 3*3 matrix
p1s = 'X' #player one symbol
p2s ='O' # player two symbol


def place(symbol):
    print(np.matrix(board))#convert it into row matrix form
    while(1):
        row =  int(input("enter row value; allowed values 1 or 2 or 3"))
        col = int(input("enter column value; allowed value 1 or 2 or 3"))
        #if already occupied or if entered wrong values
        if row>0 and row<4 and col>0 and col<4 and board[row-1][col-1] == '-':
            break
        else:
            print('Invalid input ! Please enter input again')
    board[row-1][col-1]=symbol #allow user to place at the intended postion

def check_rows(symbol):
    for i in range(3):
        count = 0
        for j in range(3):
            if(board[i][j] == symbol):
                count+=1
        if count == 3:
            print(symbol,'won')
            return True
    return False
  
def check_cols(symbol):
    for i in range(3):
        count = 0
        for j in range(3):
            if(board[j][i] == symbol):
                count+=1
        if count == 3:
            print(symbol,'won')
            return True
    return False

def check_diagonals(symbol):
    if board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[1][1] == symbol:
        return True
    if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[1][1] == symbol:
        return True
    return False
    
    
        

def won(symbol):
    return check_rows(symbol) or check_cols(symbol) or check_diagonals(symbol)
    
def play():
    #first tuen X then second O
    # since it is a 3*3 matrix 9 turns overall
    for turn in range(9):
        #even turns for X and odd turns for O
        #this is achieved using modulo operator
        
        if turn%2 == 0:
            print('X turn ')
            place(p1s)#place the symbol
            # all nine slots not occupied
            if won(p1s):#from fifth turn anyone can win
                break 
        else:
            print('O turn ')
            place(p2s)#place the symbol
            # all nine slots not occupied
            if won(p2s): #from fifth turn anyone can win
                break
            
    if not(won(p1s)) and not(won(p2s)):
        print('Draw')
        #at the end of  all nine turns hence not included while loop
        #after all turns have been exhausted
        

play()
        