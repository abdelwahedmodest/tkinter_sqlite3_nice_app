from tkinter import *
#from urllib.request import  urlopen
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException

root =  Tk()

def openwebsite():
    driver = webdriver.Chrome("C:\chromewebdriver\chromedriver.exe")
    driver.maximize_window()
    driver.get("https://www.google.com/")

    
def content():
    response = requests.get("https://www.google.com/")
    r = response.text
    #print(r)
    myLabel= Label(root, text=r , fg="green")
    myLabel.pack()

def myClick():
    myLabel= Label(root, text="Look ! clicked a Button !! " )
    myLabel.pack()

def myClick2():
    myButton = Button(root, text="Click Me ! " , fg="green" , bg="red",padx=10, pady=10 )
    myButton.pack()

myButton3 = Button(root, text="give me text ! " , command=content )
#myButton4 = Button(root, text="give me text ! " , command=openwebsite)
myButton2 = Button(root, text="Click Me ! " , padx=50, pady=50, command=myClick)
myButton = Button(root, text="Click Me ! " ,bg="blue", padx=50, pady=50, command=myClick2 )
myButton.pack()
myButton2.pack()
myButton3.pack()
#myButton4.pack()


root.mainloop()
