

from tkinter import *
root= Tk()

root.title("My First Window")
root.geometry("100x100")
btn = Button(root,text = "Hi I am a button",fg="purple",command=root.destroy) #kills the button after it is pressed
btn.pack()
root.mainloop()






