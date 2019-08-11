from tkinter import *
from tkinter import messagebox
import sqlite3
def AddMail():
    def insertData():
        data=Email.get()

        conn = sqlite3.connect('data.db')
        conn.execute("INSERT INTO COMPANY(EMAIL) \
                     VALUES("+"'"+data+"'"+")");
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Inserted Successfull")
        print('Data Inserted successfully')


    top = Tk()
    top.geometry("400x250")


    Head = Label(top, text="Add To Mailing list").place(x=30, y=90)

    Email = Label(top, text="Enter Email").place(x=30, y=130)
    Email = Entry(top)
    Email.place(x=95, y=130)


    insert = Button(top, text="Add To Mailing List", bg="grey", command=insertData)
    insert.place(x=30, y=210)
    top.mainloop()

