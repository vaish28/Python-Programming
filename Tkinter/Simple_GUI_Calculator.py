

import tkinter as tk
import math
root = tk.Tk()

canvas_1 = tk.Canvas(root, width = 400, height = 300)
canvas_1.pack()

entry_1 = tk.Entry (root)
canvas_1.create_window(210, 100, window=entry_1)

entry_2 = tk.Entry (root) 
canvas_1.create_window(210, 140, window=entry_2)


entry_3 = tk.Entry (root) 
canvas_1.create_window(210, 240, window=entry_3)

label_0 =tk.Label(root,text="Calculator for Basic Calculations")
canvas_1.create_window(150,40,window = label_0)

label_2 =tk.Label(root,text="Enter first number")
canvas_1.create_window(70,100,window = label_2)

label_3 =tk.Label(root,text="Enter second number")
canvas_1.create_window(75,140,window = label_3)

label_4 =tk.Label(root,text="Result of operation   =   ")
canvas_1.create_window(75,240,window = label_4)

def addition():
    number_1 = float(entry_1.get())
    number_2 = float(entry_2.get())
    result = number_1+number_2
    entry_3.insert(0,str(result))


def subtraction():
    number_1 = float(entry_1.get())
    number_2 = float(entry_2.get())
    result = number_1-number_2
    entry_3.insert(0,str(result))

def multiplication():
    number_1 = float(entry_1.get())
    number_2 = float(entry_2.get())
    result = number_1*number_2
    entry_3.insert(0,str(result))

def divison():
    number_1 = float(entry_1.get())
    number_2 = float(entry_2.get())
    result = number_1/number_2
    entry_3.insert(0,str(result))

def modulus():
    number_1 = float(entry_1.get())
    number_2 = float(entry_2.get())
    result = number_1%number_2
    entry_3.insert(0,str(result))

def power():
    number_1 = float(entry_1.get())
    number_2 = float(entry_2.get())
    result = pow(number_1,number_2)
    entry_3.insert(0,str(result))

def square_root():
    number_1=float(entry_1.get())
    result = math.sqrt(number_1)
    entry_3.insert(0,str(result))

button_addition = tk.Button(text='+', command=addition, bg='green', fg='white', width = 4)
canvas_1.create_window(50, 190, window=button_addition)

button_subtraction = tk.Button(text='-', command=subtraction, bg='green', fg='white', width = 4)
canvas_1.create_window(100, 190, window=button_subtraction)

button_multiplication = tk.Button(text='*', command=multiplication, bg='green', fg='white', width = 4)
canvas_1.create_window(150, 190, window=button_multiplication)

button_divison = tk.Button(text='/', command=divison, bg='green', fg='white', width = 4)
canvas_1.create_window(200, 190, window=button_divison)

button_modulus = tk.Button(text='%', command=modulus, bg='green', fg='white', width = 4)
canvas_1.create_window(250, 190, window=button_modulus)

button_power = tk.Button(text='^', command=power, bg='green', fg='white', width = 4)
canvas_1.create_window(300, 190, window=button_power)

button_sroot = tk.Button(text='/^', command=square_root, bg='green', fg='white', width = 2)
canvas_1.create_window(350, 190, window=button_sroot)


root.mainloop()

