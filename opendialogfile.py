from  tkinter  import *
from PIL  import  ImageTk,Image
from tkinter  import  filedialog


root = Tk()
root.title('Codemy.com Image Viewer')
#root.iconbitmap('')

root.filename = filedialog.askopenfilename(initialdir="C:/Users/jannat/Desktop ",title="Select AFile", filetypes=(("pdf files", "*.pdf"),("all files","*.*")))
mylabel = Label(root, text=root.filename).pack()

root.mainloop()
