from tkinter  import *
from  PIL  import  ImageTk, Image


root= Tk()
root.title('learn how  to make  thing  programmatically')
#root.iconbitmap('c:/gui/codemy.ico')
root.geometry("400x400")

def slide(var):
    
    mylabel = Label(root, text= horizontal.get())
    mylabel.pack()
    root.geometry(str(horizontal.get()) + "x400")

vertical = Scale(root, from_=0, to=400)
vertical.pack()

horizontal = Scale(root, from_=0, to=400, orient=HORIZONTAL, command=slide)
horizontal.pack()





#btn = Button(root, text="Click me !", command=slide).pack()

root.mainloop()
