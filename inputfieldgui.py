from tkinter  import *


root = Tk()
root.title("Simple Calculatrice")


myLabel2= Label(root, text= "Calculatrice" , bg="black" , fg="white")
myLabel2.pack()


a = Entry(root, width= 16 , fg="red",bg="white" ,  borderwidth=9)
b = Entry(root, width= 16 , fg="red", bg="green", borderwidth=9)
a.pack()
b.pack()
#e.insert(0, "Enter your  favorite name : ")
def multi():
    resultofmulti= int(a.get())* int(b.get())
    myLabel2= Label(root, text=resultofmulti, bg="yellow")
    myLabel2.pack()

def add():
    resultofadd= int(a.get())+ int(b.get())
    myLabel= Label(root, text=resultofadd, bg="yellow")
    myLabel.pack()
    #myLabel= Label(root, text="hellow my  name  is  :  " + e.get(), fg="blue")
    #myLabel= Label(root, text="Look ! I clicked a Button !!")
    

#myButton = Button(root, text="Click Me! "  , command= myClick)
addButton = Button(root, text="+"  , command= add)
multiButton = Button(root, text="*"  , command= multi)
#myButton.pack()
addButton.pack()
multiButton.pack()


root.mainloop()
