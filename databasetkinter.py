from tkinter import *
from PIL  import ImageTk, Image
import  sqlite3


root = Tk()
root.title('my database...')
#window  size
root.geometry("400x400")
#window color
#root.configure(bg='#856ff8')
root.configure(bg='blue')
#Databases

#create  a  database  or connect   to  one 
conn = sqlite3.connect('book_kdp.db')

#sent  a cursor  to a database to do a work
c = conn.cursor()



###create table
##c.execute("""CREATE TABLE  addresses(
##        first_name text,
##        last_name  text,
##        address   text,
##        city      text,
##        state  text,
##        zipcode  integer
##        )""")

#create  submit  function for  database
def  submit():
    #create  a  database  or connect   to  one 
    conn = sqlite3.connect('book_kdp.db')
    #sent  a cursor  to a database to do a work
    c = conn.cursor()
    #insert into Table
    c.execute("INSERT INTO addresses VALUES(:f_name,:l_name,:address,:city,:state,:zipcode)",
              {
                'f_name':f_name.get(),
                'l_name':l_name.get(),
                'address':address.get(),
                'city':city.get(),
                'state':state.get(),
                'zipcode':zipcode.get(),
               })
    
    #commit  any  change
    conn.commit()
    #close  connection
    conn.close()

    #clear  the Text  Boxes
    f_name.delete(0,END)
    l_name.delete(0,END)
    address.delete(0,END)
    city.delete(0,END)
    state.delete(0,END)
    zipcode.delete(0,END)
    
#create  query  function
def  query():
    #create  a  database  or connect   to  one 
    conn = sqlite3.connect('book_kdp.db')
    #sent  a cursor  to a database to do a work
    c = conn.cursor()
    #Query  the  database
    c.execute("SELECT*,oid FROM addresses")
    records = c.fetchall()
    #print(records)

    #loop through  results
    print_records = ""
    #for record in  records :  #all tuples of list in  once  
    for record in  records[0] : #records[0]list take index 0 because it has one tuple
        print_records += str(record) + "\n"
    query_label = Label(root, text=print_records, bg="blue", fg="white")
    query_label.grid(row=12, column=0)
    
    #commit  any  change
    conn.commit()
    #close  connection
    conn.close()

    return
# create  text Boxes
f_name = Entry(root, width=30)
f_name.grid(row=1, column=1, padx=20)

l_name = Entry(root, width=30)
l_name.grid(row=2, column=1)

address = Entry(root, width=30)
address.grid(row=3, column=1)

city = Entry(root, width=30)
city.grid(row=4, column=1)

state = Entry(root, width=30)
state.grid(row=5, column=1)

zipcode = Entry(root, width=30)
zipcode.grid(row=6, column=1)

#create  text box  labels
f_name_label = Label(root, text=" ", bg="blue", fg="white")
f_name_label.grid(row=0, column=0)

f_name_label = Label(root, text="First Name", bg="blue", fg="white")
f_name_label.grid(row=1, column=0)

l_name_label = Label(root, text="Last Name", bg="blue", fg="white")
l_name_label.grid(row=2, column=0)

address_label = Label(root, text="Address", bg="blue", fg="white")
address_label.grid(row=3, column=0)

city_label = Label(root, text="city", bg="blue", fg="white")
city_label.grid(row=4, column=0)

state_label = Label(root, text="State", bg="blue", fg="white")
state_label.grid(row=5, column=0)

zipcode_label = Label(root, text="Zipcode", bg="blue", fg="white")
zipcode_label.grid(row=6, column=0)

#Create  Submit  Button
submit_btn = Button(root, text="Add  Record  To    Darabase...", command=submit)
submit_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

#create  a  query  Button
query_btn = Button(root, text="Show Records", command=query)
query_btn.grid(row=8, column=0, columnspan=2, pady=10, padx=10, ipadx=137)
#add  label  with  image
image = Image.open("fish.jpg")
image = image.resize((150, 150), Image.ANTIALIAS)
lyimage= ImageTk.PhotoImage(image)
labelimage=Label(root, image=lyimage, bg="blue")
labelimage.grid(row=12, column=1)

#commit  any  change
conn.commit()

#close  connection
conn.close()


root.mainloop()
