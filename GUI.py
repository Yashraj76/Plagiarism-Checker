from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import sqlite3
import os
import os.path
import shutil
 

window = Tk()
window.title("Plagiarism Checker")
label = Label(window, text="PLagiarism Checker", font=('arial',20,'bold'),bg="black",fg="white")
label.pack(side=TOP,fill=X)
label = Label(window,text="",font=('arial',15,'bold'),bg="black",fg="white")
label.pack(side=BOTTOM,fill=X)

save_path = os.getcwd()+"\Datasets"
print(save_path)

def open():
    global txtfile
    window.filename = filedialog.askopenfilename(initialdir=save_path, title="Select a file", filetypes=(("txt files", "txt"),("all files", ".*")))
    my_label = Label(window, text=window.filename)
    my_label.place(x=260,y=140)
    txtfile = os.path.basename(window.filename)
    print(window.filename)
    complete_name = os.path.join(save_path, os.path.basename(window.filename))
    print(complete_name)
    shutil.copy(window.filename, complete_name)

def create():
    conn=sqlite3.connect('database.db')
    c=conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS users(id integer primary key autoincrement, name TEXT, txtfile TEXT, sqltime TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL)")
    conn.commit()
    conn.close()

create()

label = Label(window,text="Name",font=('arial',13,'bold'))
label.place(x=30,y=60)

name_entry=StringVar()
name_entry=ttk.Entry(window, textvariable=name_entry)
name_entry.place(x=170,y=60)
name_entry.focus()


label = Label(window,text="File upload:",font=('arial',13,'bold'))
label.place(x=30,y=140)

def savedata():
    conn=sqlite3.connect('database.db')
    c=conn.cursor()
    c.execute('INSERT INTO users(name,txtfile) VALUES (?,?)',(name_entry.get(),txtfile))
    conn.commit()
    print("saved")


btn = ttk.Button(window,text='Save Data', command=savedata)
btn.place(x=170,y=220, width=125, height=30)

my_btn = ttk.Button(window, text="Open file", command=open)
my_btn.place(x=170,y=140, width=80, height=25)

window.geometry('640x350')
window.resizable(False,False)
window.mainloop()