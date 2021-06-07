from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import pymysql

con=pymysql.connect(host="localhost",user="root",passwd="Saksham@07",database="db")
cur=con.cursor()

booksTable="books"

def view():
    root=Tk()
    root.title("Library")
    root.minsize(width=40,height=40)
    root.geometry("600x500")
    Canvas1=Canvas(root)
    Canvas1.config(bg="#12a4d9")
    Canvas1.pack(expand=True, fill=BOTH)

    headingframe1=Frame(root,bg="#FFBB00",bd=5)
    headingframe1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)

    headinglabel1=Label(headingframe1,text="VIEW BOOKS",bg="black",fg="white",font=('Courier',15))
    headinglabel1.place(relx=0,rely=0,relwidth=1,relheight=1)

    labelFrame = Frame(root, bg='black')
    labelFrame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.5)

    Label(labelFrame, text="%-10s%-40s%-30s%-20s" % ('BID', 'Title', 'Author', 'Status'), bg='black', fg='white').place(
        relx=0.07, rely=0.1)
    Label(labelFrame, text="----------------------------------------------------------------------------", bg='black',
          fg='white').place(relx=0.05, rely=0.2)

    y = 0.25
    getBooks = "select * from " + booksTable
    try:
        cur.execute(getBooks)
        con.commit()
        for i in cur:
            Label(labelFrame, text="%-10s%-30s%-30s%-20s" % (i[0], i[1], i[2], i[3]), bg='black', fg='white').place(
                relx=0.07, rely=y)
            y += 0.1
    except:
        messagebox.showinfo("Failed to fetch files from database")

    quitBtn = Button(root, text="Quit", bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.4, rely=0.9, relwidth=0.18, relheight=0.08)

    root.mainloop()