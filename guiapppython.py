from tkinter import *


root = Tk()

#creating a label widget
myLabel = Label(root, text="hello world")
myLabel2 = Label(root, text="My NAME  IS ABDO ")

#positioning label
myLabel.grid(row=0,column=0)
myLabel2.grid(row=1,column=0)
#shoving it onto the screen
#myLabel.pack()

root.mainloop()

