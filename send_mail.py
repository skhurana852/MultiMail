from tkinter import *
import smtplib
from tkinter import messagebox
import sqlite3
from Insert import AddMail

def getData():
    conn = sqlite3.connect('data.db')
    print('connected succesfully')

    cursor= conn.execute("SELECT * FROM COMPANY");
    return cursor



def mail():
    def goToMailList():
        AddMail()

    def sendmail():
        sender = Email.get()
        passcred=Password.get()
        receivers = getData()
        SUBJECT = Subject.get()
        TEXT = Message.get("1.0",END)
        message = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)


        try:
            smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
            smtpObj.ehlo()
            smtpObj.starttls()
            smtpObj.login(sender, passcred)
            for row in receivers:
                smtpObj.sendmail(sender, row[0], message)
                messagebox.showinfo("Success", "Mail Sent Successfull")
                print("Successfully sent email")
        except smtplib.SMTPException:
            messagebox.showerror("Error", "Error in sending mail")
            print("Error: unable to send email")

    top = Tk()
    top.geometry("400x400")

    email1 = StringVar()
    password = StringVar()
    regemail = StringVar()
    regpassword = StringVar()

    Welcome = Label(top, text="Welcome to Multimail").place(x=100, y=10)

    Email = Label(top, text="Email").place(x=30, y=50)
    Email = Entry(top)
    Email.place(x=95, y=50)

    Password = Label(top, text="Password").place(x=30, y=80)
    Password = Entry(top)
    Password.place(x=95, y=80)


    Subject = Label(top, text="Subject").place(x=30, y=110)
    Subject = Entry(top)
    Subject.place(x=95, y=110)

    Message = Label(top, text="Message").place(x=30, y=170)
    Message = Text(top,height=6, width=30)
    Message.place(x=95, y=170)

    login = Button(top, text="Send Mail", bg="grey", command=sendmail)
    login.place(x=30, y=280)

    insert = Button(top, text="Add To Mailing List", bg="grey",command=goToMailList)
    insert.place(x=120, y=280)
    top.mainloop()



mail()


