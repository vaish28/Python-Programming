

from tkinter import *
root= Tk()

root.title("My First Window")
root.geometry("500x500")


label=Label(root,text="Enter roll number").pack(side=TOP)

entry_input = Entry(root,bd=7).pack(side=TOP)

def thankyou():
    print("Thank you!") #thankyou function before the button


btn = Button(root,text = "Submit roll number",fg="purple",command=thankyou) #prints respond Thank you!
btn.pack(side=BOTTOM)


root.mainloop()
