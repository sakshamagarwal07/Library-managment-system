from tkinter import *
from PIL import ImageTk,Image
import pymysql
from add_book1 import *
from issuebook1 import *
from deletebook1 import *
from return_book1 import *
from viewbooks1 import *


# connnecting with sql server
con=pymysql.connect(host="localhost",user="root",passwd="Saksham@07",database="db")
cur=con.cursor()

#creating a window
root=Tk()
root.title("Library")
root.minsize(width=400,height=400)
root.geometry("600x500")

#adding image in background
same=TRUE
n=0.25
background_image = Image.open("lib.jpg")
[imageSizeWidth, imageSizeHeight] = background_image.size

newImageSizeWidth = int(imageSizeWidth * n)
if same:
    newImageSizeHeight = int(imageSizeHeight * n)
else:
    newImageSizeHeight = int(imageSizeHeight / n)

background_image = background_image.resize((newImageSizeWidth,newImageSizeHeight),Image.ANTIALIAS)
img = ImageTk.PhotoImage(background_image)
Canvas1 = Canvas(root)
Canvas1.create_image(300,340,image = img)
Canvas1.config(bg="white",width = newImageSizeWidth, height = newImageSizeHeight)
Canvas1.pack(expand=True,fill=BOTH)

#Creating heading

heading_frame1=Frame(root,bg="#FFBB00",bd=5)
heading_frame1.place(relwidth=0.6,relheight=0.16,relx=0.2,rely=0.1,)

heading_label=Label(heading_frame1,text="WELCOME TO LIBRARY ",fg="white",bg="black",font=('Courier',20))
heading_label.place(relx=0,rely=0,relwidth=1,relheight=1)


#creating buttons




btn1=Button(root,text="ADD BOOK DETAILS",bg="black",fg="white",command=addBook)
btn1.place(relwidth=.4,relheight=.1,relx=0.3,rely=0.4)

btn2=Button(root,text="DELETE BOOK",bg="black",fg="white",command=delete)
btn2.place(relwidth=.4,relheight=.1,relx=0.3,rely=0.5)

btn3=Button(root,text="VIEW BOOK LIST",bg="black",fg="white",command=view)
btn3.place(relwidth=.4,relheight=.1,relx=0.3,rely=0.6)

btn4=Button(root,text="ISSUE BOOK TO STUDENT",bg="black",fg="white",command=issuebook)
btn4.place(relwidth=.4,relheight=.1,relx=0.3,rely=0.7)

btn5=Button(root,text="RETURN BOOK",bg="black",fg="white",command=return_book)
btn5.place(relwidth=.4,relheight=.1,relx=0.3,rely=0.8)


root.mainloop()


