import tkinter as tk
from tkinter import *
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="123456",
  database="stccoimabtore"
  
)

name = mydb.cursor()

def close():
   r.destroy()

def submit_it():
    query = "INSERT INTO student (f_name, s_name, contact, password, conf_password) VALUES(%s, %s, %s, %s, %s)"
    my_data = (f_name.get(),s_name.get(), contact.get(), password.get(), conf_password.get())
    name.execute(query,my_data)
    mydb.commit()


    r = tk.Tk()
    r.geometry("300x300")
    r.title("Sql_New")
        
r = tk.Tk()
r.geometry("300x300")
r.title("Sql_New")

da = tk.Label(r, text="f_name")
da.place(x=50, y=20)

f_name = tk.Entry(r, width=35)
f_name.place(x=150, y=20, width=100)

av = tk.Label(r, text="s_name")
av.place(x=50, y=50)

s_name = tk.Entry(r, width=35)
s_name.place(x=150, y=50, width=100)

cv = tk.Label(r, text="contact")
cv.place(x=50, y=80)

contact = tk.Entry(r, width=35)
contact.place(x=150, y=80, width=100)

ar= tk.Label(r, text="password")
ar.place(x=50, y=110)

password = tk.Entry(r, width=35)
password.place(x=150, y=110, width=100)

we = tk.Label(r, text="conf_password")
we.place(x=50, y=140)

conf_password = tk.Entry(r, width=35)
conf_password.place(x=150, y=140, width=100)


cw= tk.Button(r, text ="Register", bg='blue', command=submit_it)
cw.place(x=150, y=180, width=55)

cd = tk.Button(r,text ="Quit",bg ='blue', command=close)
cd.place(x=80, y=180, width=55)

r.mainloop()
