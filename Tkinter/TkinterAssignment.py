#import tkinter module
import tkinter as tk
#import math module
import math

#create root window
root = tk.Tk()

#create canvas
canvas_1 = tk.Canvas(root, width = 400, height = 300)
canvas_1.pack()

# Create the entry boxes to take input from user and add into canvas
entry_1 = tk.Entry (root)
canvas_1.create_window(210, 100, window=entry_1)
# Places a Tkinter widget on the canvas at  specified positional co-ordinates. 

# Create the entry boxes to take input from user and add into canvas
entry_2 = tk.Entry (root) 
canvas_1.create_window(210, 140, window=entry_2)
# Places a Tkinter widget on the canvas at  specified positional co-ordinates. 

# Create the entry boxes to take input from user and add into canvas
entry_3 = tk.Entry (root) 
canvas_1.create_window(210, 240, window=entry_3)
# Places a Tkinter widget on the canvas at  specified positional co-ordinates. 

# Create the entry boxes to take input from user and add into canvas
label_0 =tk.Label(root,text="Calculator for Basic Calculations")
canvas_1.create_window(150,40,window = label_0)
# Places a Tkinter widget on the canvas at  specified positional co-ordinates. 

# Create the entry boxes to take input from user and add into canvas
label_2 =tk.Label(root,text="Enter first number")
canvas_1.create_window(70,100,window = label_2)
# Places a Tkinter widget on the canvas at  specified positional co-ordinates. 

# Create the entry boxes to take input from user and add into canvas
label_3 =tk.Label(root,text="Enter second number")
canvas_1.create_window(75,140,window = label_3)
# Places a Tkinter widget on the canvas at  specified positional co-ordinates. 

# Create the entry boxes to take input from user and add into canvas
label_4 =tk.Label(root,text="Result of operation   =   ")
canvas_1.create_window(75,240,window = label_4)
# Places a Tkinter widget on the canvas at  specified positional co-ordinates. 


def addition(): # Addition function definition
    number_1 = float(entry_1.get()) # input from user; get returns entry’s current text as a string
    number_2 = float(entry_2.get()) # input from user; get returns entry’s current text as a string
    result = number_1+number_2 # addition of 2 numbers
    entry_3.insert(0,str(result)) # displaying result


def subtraction(): # Subtraction function definition
    number_1 = float(entry_1.get()) # input from user; get returns entry’s current text as a string
    number_2 = float(entry_2.get()) # input from user; get returns entry’s current text as a string
    result = number_1-number_2 # subtraction of 2 numbers
    entry_3.insert(0,str(result)) # displaying result

def multiplication(): # Multiplication function definition
    number_1 = float(entry_1.get()) # input from user; get returns entry’s current text as a string
    number_2 = float(entry_2.get()) # input from user; get returns entry’s current text as a string
    result = number_1*number_2 # multiplication of 2 numbers
    entry_3.insert(0,str(result)) # displaying result

def divison(): # Division function definition
    number_1 = float(entry_1.get()) # input from user; get returns entry’s current text as a string
    number_2 = float(entry_2.get()) # input from user; get returns entry’s current text as a string
    result = number_1/number_2 # divison of 2 numbers
    entry_3.insert(0,str(result)) # displaying result

def modulus(): # Modulus function definition
    number_1 = float(entry_1.get()) # input from user; get returns entry’s current text as a string
    number_2 = float(entry_2.get()) # input from user; get returns entry’s current text as a string
    result = number_1%number_2  # modulus of 2 numbers
    entry_3.insert(0,str(result)) # displaying result

def power(): #Power function definition
    number_1 = float(entry_1.get()) # input from user; get returns entry’s current text as a string
    number_2 = float(entry_2.get()) # input from user; get returns entry’s current text as a string
    result = pow(number_1,number_2) # rasing other number as a power to first number
    entry_3.insert(0,str(result)) # displaying result
     
def square_root(): # Square Root function definition
    number_1=float(entry_1.get()) # input from user; get returns entry’s current text as a string
    result = math.sqrt(number_1) # finding sqroot of a number
    entry_3.insert(0,str(result)) # displaying result



# creating button for addition selection
button_addition = tk.Button(text='+', command=addition, bg='green', fg='white', width = 4)
canvas_1.create_window(50, 190, window=button_addition)
# Places a Tkinter widget on the canvas at  specified positional co-ordinates. 

# creating button for subtraction selection
button_subtraction = tk.Button(text='-', command=subtraction, bg='green', fg='white', width = 4)
canvas_1.create_window(100, 190, window=button_subtraction)
# Places a Tkinter widget on the canvas at  specified positional co-ordinates. 

# creating button for multiplication selection
button_multiplication = tk.Button(text='*', command=multiplication, bg='green', fg='white', width = 4)
canvas_1.create_window(150, 190, window=button_multiplication)
# Places a Tkinter widget on the canvas at  specified positional co-ordinates. 

# creating button for division selection
button_divison = tk.Button(text='/', command=divison, bg='green', fg='white', width = 4)
canvas_1.create_window(200, 190, window=button_divison)
# Places a Tkinter widget on the canvas at  specified positional co-ordinates. 

# creating button for modulus selection
button_modulus = tk.Button(text='%', command=modulus, bg='green', fg='white', width = 4)
canvas_1.create_window(250, 190, window=button_modulus)
# Places a Tkinter widget on the canvas at  specified positional co-ordinates. 

# creating button for power raised to selection
button_power = tk.Button(text='^', command=power, bg='green', fg='white', width = 4)
canvas_1.create_window(300, 190, window=button_power)
# Places a Tkinter widget on the canvas at  specified positional co-ordinates. 

# creating button for sqroot of a number selection
button_sroot = tk.Button(text='/^', command=square_root, bg='green', fg='white', width = 2)
canvas_1.create_window(350, 190, window=button_sroot)
# Places a Tkinter widget on the canvas at  specified positional co-ordinates. 

root.mainloop()
# Execute mainloop 
