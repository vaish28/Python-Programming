


from tkinter import *
root= Tk()

root.title("My First Window")
root.geometry("500x500")


label=Label(root,text="Enter roll number").pack(side=TOP)

entry_input = Entry(root,bd=7).pack(side=TOP)

btn = Button(root,text = "Submit roll number",fg="purple",command=root.destroy) #kills the button after it is pressed
btn.pack(side=BOTTOM)

root.mainloop()


