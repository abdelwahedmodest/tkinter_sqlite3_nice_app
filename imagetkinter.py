from tkinter  import *
from PIL import  ImageTk,Image


root= Tk()
root.title('Learn to Code  at  Codeacademy.com')


frame = LabelFrame(root, text="this is my  Frame...", padx=2, pady=2, bg="red")
frame.pack(padx=3, pady=3)
#frame.pack()
#root.iconbitmap('c:/gui/codemy.ico')
button_quit = Button(frame, text="Exit Program", command=root.quit)
button_quit.grid(row=1,column=0)

my_img = ImageTk.PhotoImage(Image.open("taha.jpg"))
label3 = Label(frame,image=my_img)
label3.grid(row=0,column=0)

#frame2 = LabelFrame(root, text="this is my  Frame...", padx=2, pady=2, bg="yellow")
#frame2.pack(padx=3, pady=3)
#button2 = Button(frame2, text="Exit Program")
#button2.grid(row=4,column=0)
root.mainloop()
