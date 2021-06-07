from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import pymysql
def bookRegister():
    bid = bookInfo1.get()
    title = bookInfo2.get()
    author = bookInfo3.get()
    status = bookInfo4.get()
    status = status.lower()

    insertBooks = "insert into " + bookTable + " values('" + bid + "','" + title + "','" + author + "','" + status + "')"
    try:
        cur.execute(insertBooks)
        con.commit()
        messagebox.showinfo('Success', "Book added successfully")
    except:
        messagebox.showinfo("Error", "Can't add data into Database")

    print(bid)
    print(title)
    print(author)
    print(status)

    root.destroy()


def addBook():

    global bookInfo1,bookInfo2,bookInfo3,bookInfo4,canvas1,con,cur,bookTable,root

    root=Tk()
    root.title("Library")
    root.minsize(width=40,height=40)
    root.geometry("600x500")

    con=pymysql.connect(host="localhost",user="root",passwd="Saksham@07",database="db")
    cur=con.cursor()

    bookTable="Books"

    canvas1=Canvas(root)
    canvas1.config(bg="#ff6e40")
    canvas1.pack(expand=True, fill=BOTH)
    headingFrame1 = Frame(root, bg="#FFBB00", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)
    headinglabel1=Label(headingFrame1,text="ADD BOOK",bg='black', fg='white', font=('Courier',15))
    headinglabel1.place(relx=0,rely=0,relwidth=1,relheight=1)

    labelframe=Frame(root,bg="black")
    labelframe.place(relheight=0.4,relwidth=0.8,relx=0.1,rely=0.4)
    #1
    lb1=Label(labelframe,text="BOOK ID:",bg="black",fg="white")
    lb1.place(relx=0.05,rely=0.2, relheight=0.08)

    bookInfo1=Entry(labelframe)
    bookInfo1.place(relx=0.3,rely=0.2, relwidth=0.62, relheight=0.08)
    #2
    lb2 = Label(labelframe, text="TITLE:", bg="black", fg="white")
    lb2.place(relx=0.05, rely=0.35, relheight=0.08)

    bookInfo2 = Entry(labelframe)
    bookInfo2.place(relx=0.3, rely=0.35, relwidth=0.62, relheight=0.08)
   #3
    lb3 = Label(labelframe, text="AUTHOR:", bg="black", fg="white")
    lb3.place(relx=0.05, rely=0.5, relheight=0.08)

    bookInfo3 = Entry(labelframe)
    bookInfo3.place(relx=0.3, rely=0.5, relwidth=0.62, relheight=0.08)

#4
    lb4 = Label(labelframe, text="STATUS:", bg="black", fg="white")
    lb4.place(relx=0.05, rely=0.65, relheight=0.08)

    bookInfo4 = Entry(labelframe)
    bookInfo4.place(relx=0.3, rely=0.65, relwidth=0.62, relheight=0.08)

    # Submit Button
    SubmitBtn = Button(root, text="SUBMIT", bg='#d1ccc0', fg='black', command=bookRegister)
    SubmitBtn.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)

    quitBtn = Button(root, text="Quit", bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)

    root.mainloop()
