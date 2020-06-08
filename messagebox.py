from tkinter import *
from PIL  import  ImageTk, Image
from tkinter import messagebox

root = Tk()
root.title('learn to code')
#root.iconbitmap(r'C:\Users\jannat\Desktop\newone\phone.ico')
root.iconbitmap('hand.png')

# showinfo, showwarning, showerror, askquestion, askokcancel, askyesno

def popup():
    #messagebox.showinfo("showinfo ", "hellow world ")
    #messagebox.showwarning("showwarning ", "hellow world ")
    #messagebox.showerror("showerror ", "hellow world ")
    #messagebox.askquestion("askquestion ", "hellow world ")
    #messagebox.askokcancel("askokcancel ", "hellow world ")
    messagebox.askyesno("askyesno ", "hellow world ")

Button(root, text="Popup", command=popup).pack()

##for i  in range(1,5):
##    top = Toplevel()
##    Button(top, text= i , bg="white", fg="red", command=quit).pack()
    



root.mainloop()
