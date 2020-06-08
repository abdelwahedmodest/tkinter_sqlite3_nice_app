from  tkinter  import *
from PIL  import  ImageTk, Image


root = Tk()
root.title('coding  is not  aboout  staning')
root.iconbitmap('')
root.geometry("400x400")

#drop  down  boxes
def  show():
    mylabel = Label(root, text=clicked.get(), bg="yellow").pack()

list = [
         "Monday",
         "Tuesday",
         "Wednesday",
         "Thursday",
         "Friday"
 ]


clicked= StringVar()
clicked.set(list[0])

drop = OptionMenu(root, clicked,*list)
drop.pack()

mybutton = Button(root, text="Show Selection", command=show).pack()
root.mainloop()
