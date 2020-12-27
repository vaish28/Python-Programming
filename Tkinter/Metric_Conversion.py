'''
@author Vaishnavi Madhekar
A simple metric converter using Tkinter
'''

#import tkinter module
import tkinter as tk
#import math module
import math

#create root window
root = tk.Tk()
#create canvas
canvas_1 = tk.Canvas(root, width = 500, height = 500)
canvas_1.pack()


# Create the entry boxes to take input from user and add into canvas
entry_1 = tk.Entry (root)
canvas_1.create_window(350, 100, window=entry_1)
# Places a Tkinter widget on the canvas at  specified positional co-ordinates. 

# Create the entry boxes to take input from user and add into canvas
entry_2 = tk.Entry (root) 
canvas_1.create_window(350, 170, window=entry_2)
# Places a Tkinter widget on the canvas at  specified positional co-ordinates. 

# create the label boxes for displaying text
label_0 =tk.Label(root,text="Metric Converter",font=("Pristina", 35))
canvas_1.create_window(225,40,window = label_0)
# Places a Tkinter widget on the canvas at  specified positional co-ordinates. 

# create the label boxes for displaying text
label_2 =tk.Label(root,text="Enter Value to be converted",fg='purple',font=("Forte", 14))
canvas_1.create_window(150,100,window = label_2)
# Places a Tkinter widget on the canvas at  specified positional co-ordinates. 

# create the label boxes for displaying text
label_4 =tk.Label(root,text="Result of the operation   =   ",fg='purple',font=("Forte", 15))
canvas_1.create_window(150,170,window = label_4)
# Places a Tkinter widget on the canvas at  specified positional co-ordinates. 


def celsius_to_fahrenheit(): # function to convert celsius temperature to fahrenheit temperature
    number_1 = float(entry_1.get()) #input from user; get returns entry’s current text as a string
    result = (number_1*1.8)+32.0
    entry_2.insert(0,str(result)) #displaying results

def fahrenheit_to_celsius():  # function to convert fahrenheit temperature to celsius temperature  
     number_1 = float(entry_1.get()) #input from user; get returns entry’s current text as a string
     result = (number_1-32)/1.8
     entry_2.insert(0,str(result))  #displaying result

def height_in_cm(): # function to convert measurement of height in inches to centimeter
     number_1 = float(entry_1.get()) #input from user; get returns entry’s current text as a string
     result = (number_1*2.54)
     entry_2.insert(0,str(result))  #displaying result

def weight_in_gr(): # function to convert measurement of weight in kg to grams
    number_1 = float(entry_1.get()) #input from user; get returns entry’s current text as a string
    result = (number_1*1000)
    entry_2.insert(0,str(result))  #displaying result

def weight_in_lbs(): # function to convert measurement of weight in kg to lbs
    number_1 = float(entry_1.get()) #input from user; get returns entry’s current text as a string
    result = (number_1*2.2046226)
    entry_2.insert(0,str(result))  #displaying result

def rupee_to_dollarus(): # function to convert rupees to us dollars
    number_1 = float(entry_1.get()) #input from user; get returns entry’s current text as a string
    result = (number_1*0.014)
    entry_2.insert(0,str(result))  #displaying result
     
def dollarus_to_rupee(): # function to convert us dollars to rupees
    number_1 = float(entry_1.get()) #input from user; get returns entry’s current text as a string
    result = (number_1*73.80)
    entry_2.insert(0,str(result))  #displaying result


#creating button from conversion selection
button_celsius_to_fahren = tk.Button(text='Fahrenheit', command=celsius_to_fahrenheit, bg='blue', fg='white', width = 15,font=("Franklin Gothic Demi", 12))
canvas_1.create_window(150, 250, window=button_celsius_to_fahren)
# Places a Tkinter widget on the canvas at  specified positional co-ordinates. 

#creating button from conversion selection
button_fahren_to_celsius = tk.Button(text='Celsius', command=fahrenheit_to_celsius, bg='blue', fg='white', width = 15,font=("Franklin Gothic Demi", 12))
canvas_1.create_window(350, 250, window=button_fahren_to_celsius)
# Places a Tkinter widget on the canvas at  specified positional co-ordinates. 

#creating button from conversion selection
button_height = tk.Button(text='Height in cm', command= height_in_cm, bg='red', fg='white',width = 15,font=("Franklin Gothic Demi", 12))
canvas_1.create_window(150, 300, window=button_height)
# Places a Tkinter widget on the canvas at  specified positional co-ordinates. 

#creating button from conversion selection
button_weight = tk.Button(text='Weight in gram', command=weight_in_gr, bg='red', fg='white', width = 15,font=("Franklin Gothic Demi", 12))
canvas_1.create_window(350, 300, window=button_weight)
# Places a Tkinter widget on the canvas at  specified positional co-ordinates. 

#creating button from conversion selection
button_weight_lbs = tk.Button(text='Weight in lbs', command=weight_in_lbs, bg='green', fg='white',  width = 15,font=("Franklin Gothic Demi", 12))
canvas_1.create_window(150, 350, window=button_weight_lbs)
# Places a Tkinter widget on the canvas at  specified positional co-ordinates. 

#creating button from conversion selection
button_rupee_to_dollar = tk.Button(text='Amount in us dollar', command=rupee_to_dollarus, bg='green', fg='white',  width = 15,font=("Franklin Gothic Demi", 12))
canvas_1.create_window(350, 350, window=button_rupee_to_dollar)
# Places a Tkinter widget on the canvas at  specified positional co-ordinates. 

#creating button from conversion selection
button_dollar_to_rupee = tk.Button(text=' Amount in rupees ', command=dollarus_to_rupee, bg='purple', fg='white',  width = 15,font=("Franklin Gothic Demi", 12))
canvas_1.create_window(250, 400, window=button_dollar_to_rupee)
# Places a Tkinter widget on the canvas at  specified positional co-ordinates. 



#Execute mainloop 
root.mainloop()
