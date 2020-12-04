

from tkinter import * 
from tkinter import messagebox 
  
root = Tk() 
root.geometry("500x500")


label=Label(root,text="Enter roll number").pack(side=TOP)
entry_input = Entry(root,bd=7).pack(side=TOP)

def thankyou():
     messagebox.showinfo("showinfo", "Information")

btn = Button(root,text = "Submit roll number",fg="purple",command=thankyou) #prints respond Thank you!
btn.pack(side=BOTTOM)


root.mainloop()
