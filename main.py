from tkinter import *
import pyodbc
from PIL import ImageTk, Image
from tkinter.messagebox import *
from tkinter import ttk
from datetime import date, timedelta, datetime
import sqlite3


def connect():
    conn = (
        "Driver={SQL Server};"
        "Server=SAPKOTAFAMILY\SQLEXPRESS;"
        "Database=lib_mngmt;"
        "TRUSTED_CONNECTION=yes"
    )
    trycon = pyodbc.connect(conn)
    return trycon
#OOORRRR
def connection():
    conn = sqlite3.connect(r'C:\Users\User\Desktop\AnjalSaps\projects\pythondjangoprojects\pythontkinterfinalproject\tkinterr\lib_mngmt')
    return conn
root = Tk()
# ******************************************************LOGIN************************************************************
class login():
    def __init__(self, root1):
        self.root = root1
        self.root.title("Login To Library")
        self.root.geometry("400x200+550+250")
        self.root.iconbitmap('Images/login.ico')
        self.root.resizable(False, False)
        self.frame = Frame(self.root)
        self.frame.place(x=80, y=50)
        self.display()

    def display(self):
        lblusername = Label(self.frame, text="Username: ", font=("times new roman", 14, "bold"))
        lblusername.grid(row=0, column=0)
        lblpassword = Label(self.frame, text="Password: ", font=("times new roman", 14, "bold"))
        lblpassword.grid(row=1, column=0)
        self.txtusername = Entry(self.frame)
        self.txtusername.grid(row=0, column=1)
        self.txtpassword = Entry(self.frame, show="*")
        self.txtpassword.grid(row=1, column=1)
        btnlogin = Button(self.frame, text="login", padx=10, pady=5, bg="red",
                          command=lambda: self.displayresult(self.txtusername.get(), self.txtpassword.get()))
        btnlogin.grid(row=2, column=0, columnspan=2)

    def displayresult(self, username, password):
        if self.checklogin(username, password) == 0:
            showinfo("Cannot Log in", "Username or paswword is wrong please try again")
            self.clearfield()
        else:
            self.root.withdraw()
            z = mainpage()

    def clearfield(self):
        self.txtusername.delete(0, END)
        self.txtpassword.delete(0, END)

    def checklogin(self, username, password):
        con = connection()
        c = con.cursor()
        c.execute(f"select * from Login where username = '{username}' and password = '{password}'")
        record = c.fetchall()
        con.commit()
        con.close()
        return len(record)


# ******************************************************Mainpage************************************************************
class mainpage():
    def __init__(self):
        self.main = Toplevel()
        self.main.title("Library - Home")
        self.main.geometry("777x455+300+100")
        self.main.iconbitmap('Images/mainpage.ico')
        self.main.resizable(False, False)
        self.menu()
        self.loadimage()

    # IT LOADS THE LIBRARY IMAGE IN MAINPAGE
    def loadimage(self):
        photo = ImageTk.PhotoImage(Image.open("Images/library.jpg"))
        lblimg = Label(self.main, image=photo)
        lblimg.image = photo
        lblimg.grid(row=0, column=0)

    # CREATE MENU
    def menu(self):
        lib_menu = Menu(self.main)
        self.main.config(menu=lib_menu)

        # USER MENU
        user = Menu(lib_menu)
        lib_menu.add_cascade(label="USER", menu=user)
        user.add_command(label="CHANGE USERNAME", command=lambda: changeusernme(self.main))
        user.add_command(label="CHANGE PASSWORD", command=lambda: changepassword(self.main))

        # book
        book = Menu(lib_menu)
        lib_menu.add_cascade(label="BOOK", menu=book)
        book.add_command(label="ADD BOOK", command=lambda: addbook(self.main))
        book.add_command(label="MANAGE BOOK", command=lambda: managebook(self.main))
        book.add_command(label="SEARCH BOOK", command=lambda: searchbook(self.main))

        # Students
        student = Menu(lib_menu)
        lib_menu.add_cascade(label="STUDENT", menu=student)
        student.add_command(label="ADD STUDENT", command=lambda: addstudent(self.main))
        student.add_command(label="MANAGE STUDENT", command=lambda: managestudent(self.main))
        student.add_command(label="SEARCH STUDENT", command=lambda: searchstudent(self.main))

        # BORROW
        borrow = Menu(lib_menu)
        lib_menu.add_cascade(label="BORROW", menu=borrow)
        borrow.add_command(label="BOOK ENTRY", command=lambda: bookentry(self.main))
        borrow.add_command(label="EXTEND DATE", command=lambda: extendbookdate(self.main))
        borrow.add_command(label="RETURN BOOK", command=lambda: returnbook(self.main))

# ******************************************************USER****************************************************************
class changeusernme():
    def __init__(self, main):
        self.frame1 = LabelFrame(main, width=600, height=300)
        self.frame1.place(x=75, y=75)
        self.userdisplay()

    def userdisplay(self):
        self.frame2 = Frame(self.frame1)
        self.frame2.place(x=160, y=60)

        # labels
        lblspace = Label(self.frame2, text=" ")

        lblspace1 = Label(self.frame2, text=" ")
        lblspace1.grid(row=0, column=0)
        lblcurrentusername = Label(self.frame2, text="Current Username", font=("times new roman", 12, "bold"))
        lblcurrentusername.grid(row=1, column=0)

        lblcurrentpassword = Label(self.frame2, text=" Current Password", font=("times new roman", 12, "bold"))
        lblcurrentpassword.grid(row=2, column=0)
        lblnewusername = Label(self.frame2, text="New Username", font=("times new roman", 12, "bold"))

        lblnewusername.grid(row=3, column=0)
        lblspace.grid(row=4, column=0)

        # Texttbox
        self.txtcurrentusername = Entry(self.frame2, width=25)
        self.txtcurrentusername.grid(row=1, column=1)
        self.txtcurrentpassword = Entry(self.frame2, width=25, show="*")
        self.txtcurrentpassword.grid(row=2, column=1)
        self.txtnewusername = Entry(self.frame2, width=25)
        self.txtnewusername.grid(row=3, column=1)

        # Button
        btncngeusername = Button(self.frame2, text="Change Username",
                                 command=lambda: self.cngeusername(self.txtcurrentusername.get(),
                                                                   self.txtcurrentpassword.get(),
                                                                   self.txtnewusername.get()), bg="black",
                                 foreground="white", padx=10, pady=5, anchor=W)
        btncngeusername.grid(row=5, column=0)

        btncancel = Button(self.frame2, text="Cancel", command=self.cancel, bg="black", foreground="white", padx=55,
                           pady=6)
        btncancel.grid(row=5, column=1)

    def cancel(self):
        # self.frame2.grid_forget()
        self.frame1.place_forget()

    def cngeusername(self, cusername, cpassowrd, nusername):
        if cusername == "" or cpassowrd == "" or nusername == "":
            showinfo("Empty", "Please fill out all fields")
            self.clearfield()
        elif self.checkdata(cusername, cpassowrd) == 0:
            showerror("Invalid", "Current username and password in inorrect")
            self.clearfield()
        else:
            self.updateusername(nusername)
            showinfo("Success", "Username Changed")
            self.clearfield()

    def clearfield(self):
        self.txtcurrentusername.delete(0, END)
        self.txtcurrentpassword.delete(0, END)
        self.txtnewusername.delete(0, END)

    def checkdata(self, cuusername, cupassword):
        con = connection()
        c = con.cursor()
        c.execute(f"select * from Login where username = '{cuusername}' and password = '{cupassword}'")
        record = c.fetchall()
        con.commit()
        con.close()
        return len(record)

    def updateusername(self, username):
        con = connection()
        c = con.cursor()
        c.execute(f"""
        update Login set username = '{username}'
        """)

        con.commit()
        con.close()


class changepassword():
    def __init__(self, main):
        self.frame1 = LabelFrame(main, width=600, height=300)
        self.frame1.place(x=75, y=75)
        self.userdisplay()

    def userdisplay(self):
        self.frame2 = Frame(self.frame1)
        self.frame2.place(x=160, y=60)

        # labels
        lblspace = Label(self.frame2, text=" ")

        lblspace1 = Label(self.frame2, text=" ")
        lblspace1.grid(row=0, column=0)
        lblcurrentusername = Label(self.frame2, text="Current Username", font=("times new roman", 12, "bold"))
        lblcurrentusername.grid(row=1, column=0)

        lblcurrentpassword = Label(self.frame2, text=" Current Password", font=("times new roman", 12, "bold"))
        lblcurrentpassword.grid(row=2, column=0)
        lblnewpassword = Label(self.frame2, text="New Password", font=("times new roman", 12, "bold"))

        lblnewpassword.grid(row=3, column=0)
        lblspace.grid(row=4, column=0)

        # Texttbox
        self.txtcurrentusername = Entry(self.frame2, width=25)
        self.txtcurrentusername.grid(row=1, column=1)
        self.txtcurrentpassword = Entry(self.frame2, width=25, show="*")
        self.txtcurrentpassword.grid(row=2, column=1)
        self.txtnewpassword = Entry(self.frame2, width=25, show="*")
        self.txtnewpassword.grid(row=3, column=1)

        # Button
        btncngeusername = Button(self.frame2, text="Change Password",
                                 command=lambda: self.cngeusername(self.txtcurrentusername.get(),
                                                                   self.txtcurrentpassword.get(),
                                                                   self.txtnewpassword.get()), bg="black",
                                 foreground="white", padx=10, pady=5, anchor=W)
        btncngeusername.grid(row=5, column=0)

        btncancel = Button(self.frame2, text="Cancel", command=self.cancel, bg="black", foreground="white", padx=55,
                           pady=6)
        btncancel.grid(row=5, column=1)

    def cancel(self):
        # self.frame2.grid_forget()
        self.frame1.place_forget()

    def cngeusername(self, cusername, cpassowrd, npassword):
        if cusername == "" or cpassowrd == "" or npassword == "":
            showinfo("Empty", "Please fill out all fields")
            self.clearfield()
        elif self.checkdata(cusername, cpassowrd) == 0:
            showerror("Invalid", "Current username and password in inorrect")
            self.clearfield()
        else:
            self.updateusername(npassword)
            showinfo("Success", "Password Changed")
            self.clearfield()

    def clearfield(self):
        self.txtcurrentusername.delete(0, END)
        self.txtcurrentpassword.delete(0, END)
        self.txtnewpassword.delete(0, END)

    def checkdata(self, cuusername, cupassword):
        con = connection()
        c = con.cursor()
        c.execute(f"select * from Login where username = '{cuusername}' and password = '{cupassword}'")
        record = c.fetchall()
        con.commit()
        con.close()
        return len(record)

    def updateusername(self, password):
        con = connection()
        c = con.cursor()
        c.execute(f"""
        update Login set password = '{password}'
        """)

        con.commit()
        con.close()


# ******************************************************BOOK***************************************************************
class addbook():
    def __init__(self, main):
        self.frame1 = LabelFrame(main, width=600, height=300, text="Add Book", font=("times new roman", 16, "bold"))
        self.frame1.place(x=75, y=75)
        self.userdisplay()

    def userdisplay(self):
        self.frame2 = Frame(self.frame1)
        self.frame2.place(x=160, y=60)

        # Labels
        lblbookname = Label(self.frame2, text="Book Name: ", font=("times new roman", 12, "bold"))
        lblbookname.grid(row=0, column=0, sticky=W)
        lblauthor = Label(self.frame2, text="Author Name: ", font=("times new roman", 12, "bold"))
        lblauthor.grid(row=1, column=0, sticky=W)
        lbltype = Label(self.frame2, text="Book Type : ", font=("times new roman", 12, "bold"))
        lbltype.grid(row=2, column=0, sticky=W)
        lblquantity = Label(self.frame2, text="Book Quantity: ", font=("times new roman", 12, "bold"))
        lblquantity.grid(row=3, column=0, sticky=W)

        # textbox
        self.txtbookname = Entry(self.frame2, width=25)
        self.txtbookname.grid(row=0, column=1)
        self.txtauthor = Entry(self.frame2, width=25)
        self.txtauthor.grid(row=1, column=1)
        self.txttype = Entry(self.frame2, width=25)
        self.txttype.grid(row=2, column=1)
        self.txtquantity = Entry(self.frame2, width=25)
        self.txtquantity.grid(row=3, column=1)

        # space
        lblspace = Label(self.frame2, text=" ")
        lblspace.grid(row=4, column=0)

        # Button
        btnsave = Button(self.frame2, text="SAVE",
                         command=lambda: self.result(self.txtbookname.get(), self.txtauthor.get(), self.txttype.get(),
                                                     self.txtquantity.get()), padx=45, pady=8, bg="black",
                         foreground="white")
        btnsave.grid(row=5, column=0)

        btncancel = Button(self.frame2, text="Cancel", command=self.cancel, bg="black", foreground="white", padx=45,
                           pady=8)
        btncancel.grid(row=5, column=1)

    def cancel(self):
        self.frame1.place_forget()

    def clearfield(self):
        self.txtquantity.delete(0, END)
        self.txttype.delete(0, END)
        self.txtauthor.delete(0, END)
        self.txtbookname.delete(0, END)

    def result(self, bname, aname, type, quantity):
        if bname == "" or aname == "" or type == "" or quantity == "":
            showerror("Empty ", "Please fill out all field")
            self.clearfield()
        else:
            try:
                Q = int(quantity)
            except:
                showerror("Invalid", "Type quantity in whole number")
                self.clearfield()
                return
            try:
                self.insert(bname, aname, type, Q)
                showinfo("Success", "Book Added")
                self.clearfield()
            except:
                showerror("Invalid", "Book already exists")
                self.clearfield()

    def insert(self, bname, aname, tYpe, quantity):
        con = connection()
        c = con.cursor()
        c.execute(
            f"insert into book(bookname, author, type, quantity) values ('{bname}', '{aname}', '{tYpe}', {quantity})")
        con.commit()
        con.close()


class managebook():
    def __init__(self, main):
        self.frame1 = LabelFrame(main, width=600, height=300, text="Manage Book", font=("times new roman", 16, "bold"))
        self.frame1.place(x=75, y=75)
        self.userdisplay()

    def userdisplay(self):
        self.frame2 = Frame(self.frame1)
        self.frame2.place(x=160, y=0)

        self.btnframe = Frame(self.frame1)
        self.btnframe.place(x=110, y=125)





        self.tableframe = LabelFrame(self.frame1, bg="black", text="CLICK ANY ROW TO SELECT DATA", foreground="white")
        self.tableframe.place(x=5, y=170, height=100)
        self.filltable(self.tableframe)

        # Labels
        lblid = Label(self.frame2, text="ID: ", font=("times new roman", 12, "bold"))
        lblid.grid(row=0, column=0, sticky=E)
        lblbookname = Label(self.frame2, text="Book Name: ", font=("times new roman", 12, "bold"))
        lblbookname.grid(row=1, column=0, sticky=E)
        lblauthor = Label(self.frame2, text="Author Name: ", font=("times new roman", 12, "bold"))
        lblauthor.grid(row=2, column=0, sticky=E)
        lbltype = Label(self.frame2, text="Book Type : ", font=("times new roman", 12, "bold"))
        lbltype.grid(row=3, column=0, sticky=E)
        lblquantity = Label(self.frame2, text="Book Quantity: ", font=("times new roman", 12, "bold"))
        lblquantity.grid(row=4, column=0, sticky=E)

        # textbox
        self.txtid = Entry(self.frame2, width=25, state='disabled')
        self.txtid.grid(row=0, column=1)
        self.txtbookname = Entry(self.frame2, width=25)
        self.txtbookname.grid(row=1, column=1)
        self.txtauthor = Entry(self.frame2, width=25)
        self.txtauthor.grid(row=2, column=1)
        self.txttype = Entry(self.frame2, width=25)
        self.txttype.grid(row=3, column=1)
        self.txtquantity = Entry(self.frame2, width=25)
        self.txtquantity.grid(row=4, column=1)

        # Button
        btnupdate = Button(self.btnframe, text="UPDATE",
                           command=lambda: self.result(self.txtid.get(), self.txtbookname.get(), self.txtauthor.get(),
                                                       self.txttype.get(), self.txtquantity.get()), padx=45, pady=8,
                           bg="black", foreground="white")
        btnupdate.grid(row=5, column=0, sticky=W)

        btndelete = Button(self.btnframe, text="DELETE", command=lambda: self.delresult(self.txtid.get()), padx=45,
                           pady=8, bg="black", foreground="white")
        btndelete.grid(row=5, column=1)

        btncancel = Button(self.btnframe, text="Cancel", command=self.cancel, bg="black", foreground="white", padx=45,
                           pady=8)
        btncancel.grid(row=5, column=2, sticky=E)

    def cancel(self):
        self.frame1.place_forget()

    def delresult(self, id):
        if id == "":
            self.clearfield()
            showerror("Invalid", "Please select book from table below")
        else:
            try:
                self.delete(id)
                try:
                    self.tableframe.place_forget()
                except:
                    self.tableframeupdate.place_forget()
                finally:
                    self.tableframedelete = LabelFrame(self.frame1, bg="black", text="CLICK ANY ROW TO SELECT DATA",
                                                       foreground="white")
                    self.tableframedelete.place(x=5, y=170, height=100)
                self.filltable(self.tableframedelete)
                showinfo("Success", "Book successfully deleted")
                self.clearfield()
            except:
                self.clearfield()
                showerror("302 error", "Book couldn't be deleted")

    def result(self, id, bname, aname, type, quantity):
        if id == "":
            self.clearfield()
            showerror("Invalid", "Please select book from table below")
        elif bname == "" or aname == "" or type == "" or quantity == "":
            showerror("Empty", "Please fill all fields")
            self.clearfield()
        else:
            try:
                Q = int(quantity)
            except:
                showerror("Invalid", "Enter valid no in quantity")
                return
            try:
                self.update(id, bname, aname, type, Q)
                self.clearfield()
                try:
                    self.tableframe.place_forget()
                except:
                    self.tableframedelete.place_forget()
                finally:
                    self.tableframeupdate = LabelFrame(self.frame1, bg="black", text="CLICK ANY ROW TO SELECT DATA",
                                                       foreground="white")
                    self.tableframeupdate.place(x=5, y=170, height=100)
                self.filltable(self.tableframeupdate)
                showinfo("Success", "Book successfully updated")
            except:
                showerror("Exists", "Sorry book already exists")

    def clearfield(self):
        self.txtid.config(state=NORMAL)
        self.txtid.delete(0, END)
        self.txtid.config(state=DISABLED)
        self.txtbookname.delete(0, END)
        self.txtauthor.delete(0, END)
        self.txttype.delete(0, END)
        self.txtquantity.delete(0, END)

    def getdata(self):
        con = connection()
        c = con.cursor()
        c.execute("select * from book")
        record = c.fetchall()
        con.commit()
        con.close()
        return record

    def filltable(self, frame):
        self.tv = ttk.Treeview(frame, column=("column1", "column2", "column3", "column4", "column5"), show="headings")
        self.tv.pack(side='left')
        scroll = Scrollbar(frame, orient="vertical", command=self.tv.yview)
        scroll.pack(side='right', fill='y')
        self.tv.configure(yscrollcommand=scroll.set)

        self.tv.heading("#1", text="ID")
        self.tv.column("#1", minwidth=20, width=40)
        self.tv.heading("#2", text="Book Name")
        self.tv.column("#2", minwidth=100, width=150)
        self.tv.heading("#3", text="Author Name")
        self.tv.column("#3", minwidth=120, width=150)
        self.tv.heading("#4", text="Book Type")
        self.tv.column("#4", minwidth=120, width=150)
        self.tv.heading("#5", text="Quantity")
        self.tv.column("#5", minwidth=55, width=75)
        for row in self.getdata():
            self.tv.insert("", END, values=(row[0], row[1], row[2], row[3], row[4]))
        self.tv.bind('<ButtonRelease-1>', self.filltxtbox)

    def filltxtbox(self, a):
        self.clearfield()
        self.txtid.config(state=NORMAL)
        # row = self.tv.item(self.tv.selection())
        item = self.tv.selection()[0]
        self.txtid.insert(0, self.tv.item(item)['values'][0])
        self.txtid.config(state=DISABLED)
        self.txtbookname.insert(0, self.tv.item(item)['values'][1])
        self.txtauthor.insert(0, self.tv.item(item)['values'][2])
        self.txttype.insert(0, self.tv.item(item)['values'][3])
        self.txtquantity.insert(0, self.tv.item(item)['values'][4])

    def update(self, id, bookname, author, type, quantity):
        con = connection()
        c = con.cursor()
        c.execute(
            f"update book set Bookname = '{bookname}', Author = '{author}', Type = '{type}', Quantity = {quantity} where ID = {id}")
        con.commit()
        con.close()

    def delete(self, id):
        con = connection()
        c = con.cursor()
        c.execute(f"DELETE from book where id = {id}")
        con.commit()
        con.close()


class searchbook():
    def __init__(self, main):
        self.frame1 = LabelFrame(main, width=600, height=300, text="Search Book", font=("times new roman", 16, "bold"))
        self.frame1.place(x=75, y=75)
        self.userdisplay()
        self.filltable(self.tableframe, "select * from book")

    def userdisplay(self):
        self.frame2 = Frame(self.frame1)
        self.frame2.place(x=70, y=0)

        self.tableframe = Frame(self.frame1)
        self.tableframe.place(x=5, y=75, height=193)
        # Label
        self.lblsearch = Label(self.frame2, text="Search By ID: ")
        self.lblsearch.grid(row=0, column=0, sticky=W, padx=10)
        lblsearch = Label(self.frame2, text="Search By ")
        lblsearch.grid(row=0, column=2, sticky=W, padx=10, pady=10)

        # Textbox
        txtsearch = Entry(self.frame2, width=25)
        txtsearch.grid(row=0, column=1)

        # combobox
        self.combo = ttk.Combobox(self.frame2, width=15)
        self.combo['values'] = ("ID", "BookName", "Author", "Type")
        self.combo.current(0)
        self.combo.bind("<<ComboboxSelected>>", self.changetext)
        self.combo.grid(row=0, column=3)

        # BUTTON
        btnsearch = Button(self.frame2, text="SEARCH", padx=10, pady=2, bg="black", foreground="white",
                           command=lambda: self.result(txtsearch.get(), self.combo.get()))
        btnsearch.grid(row=1, column=0, padx=10, columnspan=2, sticky=E)

        btncancel = Button(self.frame2, text="CANCEL", padx=10, pady=2, bg="black", foreground="white",
                           command=self.cancel)
        btncancel.grid(row=1, column=2, padx=10, columnspan=2, sticky=W)

    def result(self, name, combo):
        if combo == "" or name == "":
            showerror("Empty", "Choose from combobox and fill textbox")
            return
        elif combo == "ID":
            try:
                id = int(name)
                sql = f"select * from book where id = {id}"
            except:
                showerror("Invalid", "Enter valid id")
                return
        elif combo == "BookName":
            sql = f"select * from book where BookName like '{name}%'"
        elif combo == "Author":
            sql = f"select * from book where author like '{name}%'"
        elif combo == "Type":
            sql = f"select * from book where Type like '{name}%'"
        else:
            showerror("Invalid", "Invalid search by item")
            return
        self.tableframe.place_forget()
        self.tableframe = Frame(self.frame1)
        self.tableframe.place(x=5, y=75, height=193)
        self.filltable(self.tableframe, sql)

    def cancel(self):
        self.frame1.place_forget()

    def changetext(self, a):
        self.lblsearch.configure(text="Search By " + self.combo.get())

    def filltable(self, frame, query):
        self.tv = ttk.Treeview(frame, column=("column1", "column2", "column3", "column4", "column5"), show="headings")
        self.tv.pack(side='left')
        scroll = Scrollbar(frame, orient="vertical", command=self.tv.yview)
        scroll.pack(side='right', fill='y')
        self.tv.configure(yscrollcommand=scroll.set)

        self.tv.heading("#1", text="ID")
        self.tv.column("#1", minwidth=20, width=40)
        self.tv.heading("#2", text="Book Name")
        self.tv.column("#2", minwidth=100, width=150)
        self.tv.heading("#3", text="Author Name")
        self.tv.column("#3", minwidth=120, width=150)
        self.tv.heading("#4", text="Book Type")
        self.tv.column("#4", minwidth=120, width=150)
        self.tv.heading("#5", text="Quantity")
        self.tv.column("#5", minwidth=55, width=75)
        for row in (self.getdata(query)):
            self.tv.insert("", END, values=(row[0], row[1], row[2], row[3], row[4]))

    def getdata(self, query):
        con = connection()
        c = con.cursor()
        c.execute(query)
        record = c.fetchall()
        con.commit()
        con.close()
        return record


# ******************************************************STUDENT************************************************************
class addstudent():
    def __init__(self, main):
        self.frame1 = LabelFrame(main, width=600, height=300, text="Add Student", font=("times new roman", 16, "bold"))
        self.frame1.place(x=75, y=75)
        self.userdisplay()

    def userdisplay(self):
        self.frame2 = Frame(self.frame1)
        self.frame2.place(x=160, y=60)

        # Labels
        lblstudentname = Label(self.frame2, text="Student Name: ", font=("times new roman", 12, "bold"))
        lblstudentname.grid(row=0, column=0, sticky=E)
        lblphoneno = Label(self.frame2, text="Phone N0: ", font=("times new roman", 12, "bold"))
        lblphoneno.grid(row=1, column=0, sticky=E)
        lblclass = Label(self.frame2, text="Class : ", font=("times new roman", 12, "bold"))
        lblclass.grid(row=2, column=0, sticky=E)
        lblgender = Label(self.frame2, text="Gender: ", font=("times new roman", 12, "bold"))
        lblgender.grid(row=3, column=0, sticky=E)

        # radiobutton
        self.gender = StringVar()
        self.gender.set("M")
        Radiobutton(self.frame2, text="Male", variable=self.gender, value="M").grid(row=3, column=1, sticky=W)
        Radiobutton(self.frame2, text="Female", variable=self.gender, value="F").grid(row=3, column=1, sticky=E)

        # textbox
        self.txtstudentname = Entry(self.frame2, width=25)
        self.txtstudentname.grid(row=0, column=1)
        self.txtphone = Entry(self.frame2, width=25)
        self.txtphone.grid(row=1, column=1)
        self.txtclass = Entry(self.frame2, width=25)
        self.txtclass.grid(row=2, column=1)

        # space
        lblspace = Label(self.frame2, text=" ")
        lblspace.grid(row=4, column=0)

        # Button
        btnsave = Button(self.frame2, text="SAVE",
                         command=lambda: self.result(self.txtstudentname.get(), self.txtphone.get(),
                                                     self.txtclass.get(), self.gender.get()), padx=45, pady=8,
                         bg="black", foreground="white")
        btnsave.grid(row=5, column=0)

        btncancel = Button(self.frame2, text="Cancel", command=self.cancel, bg="black", foreground="white", padx=45,
                           pady=8)
        btncancel.grid(row=5, column=1)

    def cancel(self):
        self.frame1.place_forget()

    def clearfield(self):
        self.txtstudentname.delete(0, END)
        self.txtphone.delete(0, END)
        self.txtclass.delete(0, END)
        self.gender.set("M")

    def result(self, sname, no, classs, gender):
        if sname == "" or no == "" or classs == "" or gender == "":
            showerror("Empty ", "Please fill out all field")
            self.clearfield()
        elif len(no) != 10:
            showerror("Invalid", "Type valid phone number")
        else:
            try:
                self.insert(sname, no, classs, gender)
                showinfo("Success", "Student Added")
                self.clearfield()
            except:
                showerror("Invalid", "203 error")
                self.clearfield()

    def insert(self, sname, num, grade, gen):
        con = connection()
        c = con.cursor()
        c.execute(
            f"insert into student(studentname, phoneno, class, gender) values ('{sname}', '{num}', '{grade}', '{gen}')")
        con.commit()
        con.close()


class managestudent():
    def __init__(self, main):
        self.frame1 = LabelFrame(main, width=600, height=300, text="Manage Book", font=("times new roman", 16, "bold"))
        self.frame1.place(x=75, y=75)
        self.userdisplay()

    def userdisplay(self):
        self.frame2 = Frame(self.frame1)
        self.frame2.place(x=160, y=0)

        self.btnframe = Frame(self.frame1)
        self.btnframe.place(x=110, y=125)

        self.tableframe = LabelFrame(self.frame1, bg="black", text="CLICK ANY ROW TO SELECT DATA", foreground="white")
        self.tableframe.place(x=5, y=170, height=100)
        self.filltable(self.tableframe)

        # Labels
        lblid = Label(self.frame2, text="ID: ", font=("times new roman", 12, "bold"))
        lblid.grid(row=0, column=0, sticky=E)
        lblstudentname = Label(self.frame2, text="Student Name: ", font=("times new roman", 12, "bold"))
        lblstudentname.grid(row=1, column=0, sticky=E)
        lblphoneno = Label(self.frame2, text="Phone NO: ", font=("times new roman", 12, "bold"))
        lblphoneno.grid(row=2, column=0, sticky=E)
        lblclass = Label(self.frame2, text="Class : ", font=("times new roman", 12, "bold"))
        lblclass.grid(row=3, column=0, sticky=E)
        lblgender = Label(self.frame2, text="Gender: ", font=("times new roman", 12, "bold"))
        lblgender.grid(row=4, column=0, sticky=E)

        # textbox
        self.txtid = Entry(self.frame2, width=25, state='disabled')
        self.txtid.grid(row=0, column=1)
        self.txtstudentname = Entry(self.frame2, width=25)
        self.txtstudentname.grid(row=1, column=1)
        self.txtphoneno = Entry(self.frame2, width=25)
        self.txtphoneno.grid(row=2, column=1)
        self.txtclass = Entry(self.frame2, width=25)
        self.txtclass.grid(row=3, column=1)

        # Radio Button
        self.gender = StringVar()
        self.gender.set("M")
        Radiobutton(self.frame2, text="Male", variable=self.gender, value="M").grid(row=4, column=1, sticky=W)
        Radiobutton(self.frame2, text="Female", variable=self.gender, value="F").grid(row=4, column=1, sticky=E)

        # Button
        btnupdate = Button(self.btnframe, text="UPDATE",
                           command=lambda: self.result(self.txtid.get(), self.txtstudentname.get(),
                                                       self.txtphoneno.get(), self.txtclass.get(), self.gender.get()),
                           padx=45, pady=8, bg="black", foreground="white")
        btnupdate.grid(row=5, column=0, sticky=W)

        btndelete = Button(self.btnframe, text="DELETE", command=lambda: self.delresult(self.txtid.get()), padx=45,
                           pady=8, bg="black", foreground="white")
        btndelete.grid(row=5, column=1)

        btncancel = Button(self.btnframe, text="Cancel", command=self.cancel, bg="black", foreground="white", padx=45,
                           pady=8)
        btncancel.grid(row=5, column=2, sticky=E)

    def cancel(self):
        self.frame1.place_forget()

    def delresult(self, id):
        if id == "":
            self.clearfield()
            showerror("Invalid", "Please select book from table below")
        else:
            try:
                self.delete(id)
                try:
                    self.tableframe.place_forget()
                except:
                    self.tableframeupdate.place_forget()
                finally:
                    self.tableframedelete = LabelFrame(self.frame1, bg="black", text="CLICK ANY ROW TO SELECT DATA",
                                                       foreground="white")
                    self.tableframedelete.place(x=5, y=170, height=100)
                self.filltable(self.tableframedelete)
                showinfo("Success", "Student successfully deleted")
                self.clearfield()
            except:
                self.clearfield()
                showerror("302 error", "Student couldn't be deleted")

    def result(self, id, sname, phone, classs, gen):
        if id == "":
            self.clearfield()
            showerror("Invalid", "Please select book from table below")
        elif sname == "" or phone == "" or classs == "" or gen == "":
            showerror("Empty", "Please fill all fields")
            self.clearfield()
        elif len(phone) != 10:
            showerror("Invalid", "Type valid phone number")
        else:
            # try:
            self.update(id, sname, phone, classs, gen)
            self.clearfield()
            try:
                self.tableframe.place_forget()
            except:
                self.tableframedelete.place_forget()
            finally:
                self.tableframeupdate = LabelFrame(self.frame1, bg="black", text="CLICK ANY ROW TO SELECT DATA",
                                                   foreground="white")
                self.tableframeupdate.place(x=5, y=170, height=100)
                self.filltable(self.tableframeupdate)
                showinfo("Success", "Student successfully updated")
            '''except:
                showerror("Exists", "201 error")'''

    def clearfield(self):
        self.txtid.config(state=NORMAL)
        self.txtid.delete(0, END)
        self.txtid.config(state=DISABLED)
        self.txtstudentname.delete(0, END)
        self.txtphoneno.delete(0, END)
        self.txtclass.delete(0, END)
        self.gender.set("M")

    def getdata(self):
        con = connection()
        c = con.cursor()
        c.execute("select * from student")
        record = c.fetchall()
        con.commit()
        con.close()
        return record

    def filltable(self, frame):
        self.tv = ttk.Treeview(frame, column=("column1", "column2", "column3", "column4", "column5"), show="headings")
        self.tv.pack(side='left')
        scroll = Scrollbar(frame, orient="vertical", command=self.tv.yview)
        scroll.pack(side='right', fill='y')
        self.tv.configure(yscrollcommand=scroll.set)

        self.tv.heading("#1", text="ID")
        self.tv.column("#1", minwidth=20, width=40)
        self.tv.heading("#2", text="Student Name")
        self.tv.column("#2", minwidth=100, width=150)
        self.tv.heading("#3", text="Phone NO")
        self.tv.column("#3", minwidth=120, width=150)
        self.tv.heading("#4", text="Class")
        self.tv.column("#4", minwidth=120, width=150)
        self.tv.heading("#5", text="Gender")
        self.tv.column("#5", minwidth=55, width=75)
        for row in self.getdata():
            self.tv.insert("", END, values=(row[0], row[1], row[2], row[3], row[4]))
        self.tv.bind('<ButtonRelease-1>', self.filltxtbox)

    def filltxtbox(self, a):
        self.clearfield()
        self.txtid.config(state=NORMAL)
        item = self.tv.selection()[0]
        self.txtid.insert(0, self.tv.item(item)['values'][0])
        self.txtid.config(state=DISABLED)
        self.txtstudentname.insert(0, self.tv.item(item)['values'][1])
        self.txtphoneno.insert(0, self.tv.item(item)['values'][2])
        self.txtclass.insert(0, self.tv.item(item)['values'][3])
        self.gender.set(self.tv.item(item)['values'][4])

    def update(self, id, stname, phone, grade, gen):
        con = connection()
        c = con.cursor()
        c.execute(
            f"update student set studentname = '{stname}', phoneno = '{phone}', class = '{grade}', gender = '{gen}' where ID = {id}")
        con.commit()
        con.close()

    def delete(self, id):
        con = connection()
        c = con.cursor()
        c.execute(f"DELETE from student where id = {id}")
        con.commit()
        con.close()


class searchstudent():
    def __init__(self, main):
        self.frame1 = LabelFrame(main, width=600, height=300, text="Search Student",
                                 font=("times new roman", 16, "bold"))
        self.frame1.place(x=75, y=75)
        self.userdisplay()
        self.filltable(self.tableframe, "select * from student")

    def userdisplay(self):
        self.frame2 = Frame(self.frame1)
        self.frame2.place(x=70, y=0)

        self.tableframe = Frame(self.frame1)
        self.tableframe.place(x=5, y=75, height=193)
        # Label
        self.lblsearch = Label(self.frame2, text="Search By ID: ")
        self.lblsearch.grid(row=0, column=0, sticky=W, padx=10)
        lblsearch = Label(self.frame2, text="Search By ")
        lblsearch.grid(row=0, column=2, sticky=W, padx=10, pady=10)

        # Textbox
        txtsearch = Entry(self.frame2, width=25)
        txtsearch.grid(row=0, column=1)

        # combobox
        self.combo = ttk.Combobox(self.frame2, width=15)
        self.combo['values'] = ("ID", "StudentName", "Class")
        self.combo.current(0)
        self.combo.bind("<<ComboboxSelected>>", self.changetext)
        self.combo.grid(row=0, column=3)

        # BUTTON
        btnsearch = Button(self.frame2, text="SEARCH", padx=10, pady=2, bg="black", foreground="white",
                           command=lambda: self.result(txtsearch.get(), self.combo.get()))
        btnsearch.grid(row=1, column=0, padx=10, columnspan=2, sticky=E)

        btncancel = Button(self.frame2, text="CANCEL", padx=10, pady=2, bg="black", foreground="white",
                           command=self.cancel)
        btncancel.grid(row=1, column=2, padx=10, columnspan=2, sticky=W)

    def result(self, name, combo):
        if combo == "" or name == "":
            showerror("Empty", "Choose from combobox and fill textbox")
            return
        elif combo == "ID":
            try:
                id = int(name)
                sql = f"select * from student where id = {id}"
            except:
                showerror("Invalid", "Enter valid id")
                return
        elif combo == "StudentName":
            sql = f"select * from student where StudentName like '{name}%'"
        elif combo == "Class":
            sql = f"select * from student where class like '{name}%'"

        else:
            showerror("Invalid", "Invalid search by item")
            return
        self.tableframe.place_forget()
        self.tableframe = Frame(self.frame1)
        self.tableframe.place(x=5, y=75, height=193)
        self.filltable(self.tableframe, sql)

    def cancel(self):
        self.frame1.place_forget()

    def changetext(self, a):
        self.lblsearch.configure(text="Search By " + self.combo.get())

    def filltable(self, frame, query):
        self.tv = ttk.Treeview(frame, column=("column1", "column2", "column3", "column4", "column5"), show="headings")
        self.tv.pack(side='left')
        scroll = Scrollbar(frame, orient="vertical", command=self.tv.yview)
        scroll.pack(side='right', fill='y')
        self.tv.configure(yscrollcommand=scroll.set)

        self.tv.heading("#1", text="ID")
        self.tv.column("#1", minwidth=20, width=40)
        self.tv.heading("#2", text="Student Name")
        self.tv.column("#2", minwidth=100, width=150)
        self.tv.heading("#3", text="Phone NO.")
        self.tv.column("#3", minwidth=120, width=150)
        self.tv.heading("#4", text="Class")
        self.tv.column("#4", minwidth=120, width=150)
        self.tv.heading("#5", text="Gender")
        self.tv.column("#5", minwidth=55, width=75)
        for row in (self.getdata(query)):
            self.tv.insert("", END, values=(row[0], row[1], row[2], row[3], row[4]))


    def getdata(self, query):
        con = connection()
        c = con.cursor()
        c.execute(query)
        record = c.fetchall()
        con.commit()
        con.close()
        return record


# ******************************************************BORROW************************************************************
class bookentry():
    def __init__(self, main):
        self.frame1 = LabelFrame(main, width=600, height=300, text="Borrow Book", font=("times new roman", 16, "bold"))
        self.frame1.place(x=75, y=75)
        self.userdisplay()

        self.studtableframe = LabelFrame(self.frame1, text='Students', font=("times new roman", 10, "bold"))
        self.studtableframe.place(x=0, y=160, height=115)

        self.booktableframe = LabelFrame(self.frame1, text='Book', font=("times new roman", 10, "bold"))
        self.booktableframe.place(x=290, y=160, height=115)

        self.filltablestudent(self.studtableframe)
        self.filltablebook(self.booktableframe)

    def userdisplay(self):
        self.frame2 = Frame(self.frame1)
        self.frame2.place(x=150, y=0)

        # Label
        lblbookname = Label(self.frame2, text="Book Name:", font=("times new roman", 12, "bold"))
        lblbookname.grid(row=0, column=0, sticky=E, padx=5)

        lblstudentname = Label(self.frame2, text="Student Name:", font=("times new roman", 12, "bold"))
        lblstudentname.grid(row=1, column=0, sticky=E, padx=5)
        lbltakendate = Label(self.frame2, text="Taken Date(Y-M-D):", font=("times new roman", 12, "bold"))
        lbltakendate.grid(row=2, column=0, sticky=E, padx=0)
        lbldeadline = Label(self.frame2, text="Deadline(Y-M-D):", font=("times new roman", 12, "bold"))
        lbldeadline.grid(row=3, column=0, sticky=E, padx=5)

        # TEXTBOX
        self.txtbookname = Entry(self.frame2, width=25, state=DISABLED)
        self.txtbookname.grid(row=0, column=1)
        self.studentid = 0
        self.bookid = 0
        self.txtstudentname = Entry(self.frame2, width=25, state=DISABLED)
        self.txtstudentname.grid(row=1, column=1)
        self.txttakendate = Entry(self.frame2, width=25)
        self.txttakendate.grid(row=2, column=1)

        self.txttakendate.insert(0, date.today())
        self.txtdeadline = Entry(self.frame2, width=25)
        self.txtdeadline.grid(row=3, column=1)
        self.txtdeadline.insert(0, date.today() + timedelta(days=15))

        # space
        lblspace = Label(self.frame2, text=" ")
        lblspace.grid(row=4, column=0)

        # Button
        btnconfirm = Button(self.frame2, text="CONFIRM", padx=45, pady=8, bg="black", foreground="white",
                            command=lambda: self.result(self.bookid, self.studentid, self.txttakendate.get(),
                                                        self.txtdeadline.get()))
        btnconfirm.grid(row=5, column=0)

        btncancel = Button(self.frame2, text="Cancel", bg="black", foreground="white", padx=45, pady=8,
                           command=self.frame1.place_forget)
        btncancel.grid(row=5, column=1, sticky=E)

    def result(self, bid, sid, tdate, deadline):
        if bid == 0 or sid == 0:
            showerror("Invalid", "Please select book and student from below table")
            self.clearfield()
        elif tdate == "" or deadline == "":
            showerror("Empty", "Please fill takendate and return date")
            self.clearfield()
        else:
            try:
                self.insert(int(bid), int(sid), tdate, deadline)
                self.clearfield()
                self.updatequantity(int(bid))
                self.booktableframe.place_forget()
                self.booktableframe = LabelFrame(self.frame1, text='Book', font=("times new roman", 10, "bold"))
                self.booktableframe.place(x=290, y=160)
                self.filltablebook(self.booktableframe)
                showinfo("Success", "Book taken from library")
            except:
                showerror("Error", "Please enter valid date")
                self.clearfield()

    def filltablestudent(self, frame):
        self.tv = ttk.Treeview(frame, column=("column1", "column2", "column3"),
                               show="headings")
        self.tv.pack(side='left')
        scroll = Scrollbar(frame, orient="vertical", command=self.tv.yview)
        scroll.pack(side='right', fill='y')
        self.tv.configure(yscrollcommand=scroll.set)

        self.tv.heading("#1", text="ID")
        self.tv.column("#1", minwidth=20, width=40)
        self.tv.heading("#2", text="Student Name")
        self.tv.column("#2", minwidth=100, width=130)
        self.tv.heading("#3", text="Class")
        self.tv.column("#3", minwidth=120, width=90)

        for row in (self.getdata('select id, studentname,class from student')):
            self.tv.insert("", END, values=(row[0], row[1], row[2]))
        self.tv.bind('<ButtonRelease-1>', self.filltxtboxstudent)

    def filltablebook(self, frame):
        self.tvv = ttk.Treeview(frame, column=("column1", "column2", "column3"), show="headings")
        self.tvv.pack(side='left')
        scroll = Scrollbar(frame, orient="vertical", command=self.tvv.yview)
        scroll.pack(side='right', fill='y')
        self.tvv.configure(yscrollcommand=scroll.set)

        self.tvv.heading("#1", text="ID")
        self.tvv.column("#1", minwidth=20, width=40)
        self.tvv.heading("#2", text="Book Name")
        self.tvv.column("#2", minwidth=100, width=150)
        self.tvv.heading("#3", text="Author Name")
        self.tvv.column("#3", minwidth=120, width=90)

        for row in (self.getdata('select id, bookname,author from book where quantity > 0')):
            self.tvv.insert("", END, values=(row[0], row[1], row[2]))
        self.tvv.bind('<ButtonRelease-1>', self.filltxtboxbook)

    def filltxtboxstudent(self, a):
        item = self.tv.selection()[0]
        self.studentid = int(self.tv.item(item)['values'][0])
        self.txtstudentname.config(state=NORMAL)
        self.txtstudentname.delete(0, END)
        self.txtstudentname.insert(0, self.tv.item(item)['values'][1])
        self.txtstudentname.config(state=DISABLED)

    def filltxtboxbook(self, a):
        item = self.tvv.selection()[0]
        self.bookid = int(self.tvv.item(item)['values'][0])
        self.txtbookname.config(state=NORMAL)
        self.txtbookname.delete(0, END)
        self.txtbookname.insert(0, self.tvv.item(item)['values'][1])
        self.txtbookname.config(state=DISABLED)

    def clearfield(self):
        self.txtstudentname.config(state=NORMAL)
        self.txtstudentname.delete(0, END)
        self.txtstudentname.config(state=DISABLED)

        self.txtbookname.config(state=NORMAL)
        self.txtbookname.delete(0, END)
        self.txtbookname.config(state=DISABLED)
        self.txtdeadline.delete(0, END)
        self.txttakendate.delete(0, END)
        self.txtdeadline.insert(0, date.today() + timedelta(days=15))
        self.txttakendate.insert(0, date.today())

        self.studentid = 0
        self.bookid = 0

    def getdata(self, query):
        con = connection()
        c = con.cursor()
        c.execute(query)
        record = c.fetchall()
        con.commit()
        con.close()
        return record

    def updatequantity(self, id):
        con = connection()
        c = con.cursor()
        c.execute(f"update book set Quantity = Quantity - 1 where id = {id}")
        con.commit()
        con.close()

    def insert(self, bookid, studentid, takendate, deadline):
        con = connection()
        c = con.cursor()
        c.execute(
            f"insert into borrow(bookid,studentid,takendate,deadline) values({bookid},{studentid},'{takendate}','{deadline}')")
        con.commit()
        con.close()


class extendbookdate():
    def __init__(self, main):
        self.frame1 = LabelFrame(main, width=600, height=300, text="Extend Book Date",
                                 font=("times new roman", 16, "bold"))
        self.frame1.place(x=75, y=75)

        self.tableframe = LabelFrame(self.frame1, text='Borrow', font=("times new roman", 10, "bold"), width=600)
        self.tableframe.place(x=5, y=147, height=130)
        self.filltable(self.tableframe)
        self.userdisplay()

    def userdisplay(self):
        self.frame2 = Frame(self.frame1)
        self.frame2.place(x=150, y=0)
        # Label
        lblbookname = Label(self.frame2, text="Book Name:", font=("times new roman", 12, "bold"))
        lblbookname.grid(row=0, column=0, sticky=E, padx=5)
        lblstudentname = Label(self.frame2, text="Student Name:", font=("times new roman", 12, "bold"))
        lblstudentname.grid(row=1, column=0, sticky=E, padx=5)
        lbldeadline = Label(self.frame2, text="Deadline(Y-M-D):", font=("times new roman", 12, "bold"))
        lbldeadline.grid(row=2, column=0, sticky=E, padx=0)
        lbladddays = Label(self.frame2, text="Add Days:", font=("times new roman", 12, "bold"))
        lbladddays.grid(row=3, column=0, sticky=E, padx=5)

        # Text Boxes
        self.txtbookname = Entry(self.frame2, width=25, state=DISABLED)
        self.txtbookname.grid(row=0, column=1)
        self.ID = 0
        self.txtstudentname = Entry(self.frame2, width=25, state=DISABLED)
        self.txtstudentname.grid(row=1, column=1)

        self.txtdeadline = Entry(self.frame2, width=25, state=DISABLED)
        self.txtdeadline.grid(row=2, column=1)

        self.txtadddays = Entry(self.frame2, width=25)
        self.txtadddays.grid(row=3, column=1, pady=5)

        # space
        # lblspace = Label(self.frame2, text=" ")
        # lblspace.grid(row=4, column=0)

        # Button
        btnconfirm = Button(self.frame2, text="CONFIRM", padx=45, pady=8, bg="black", foreground="white",
                            command=lambda: self.result(self.ID, self.txtadddays.get()))
        btnconfirm.grid(row=5, column=0, sticky=W)

        btncancel = Button(self.frame2, text="Cancel", bg="black", foreground="white", padx=45, pady=8,
                           command=self.frame1.place_forget)
        btncancel.grid(row=5, column=1, sticky=E)

    def result(self, id, days):
        if id == 0 or days == "":
            showerror("Error", "Field Empty")
            self.clearfield()
        else:
            try:
                convert = int(days)
                self.update(id, convert)
                self.tableframe = LabelFrame(self.frame1, text='Borrow', font=("times new roman", 10, "bold"),
                                             width=600)
                self.tableframe.place(x=5, y=147, height=130)
                self.filltable(self.tableframe)
                self.clearfield()
                showinfo("Success", "Date succesfully extended")
            except:
                showerror("Error", "Enter valid day")
                self.clearfield()
                return

    def filltable(self, frame):

        self.tvv = ttk.Treeview(frame, column=("column1", "column2", "column3", "column4", "column5", "column6"),
                                show="headings")
        self.tvv.pack(side='left', fill='x')
        scroll = Scrollbar(frame, orient="vertical", command=self.tvv.yview)
        scroll.pack(side='right', fill='y')
        self.tvv.configure(yscrollcommand=scroll.set)

        self.tvv.heading("#1", text="ID")
        self.tvv.column("#1", minwidth=40, width=40)
        self.tvv.heading("#2", text="Book Name")
        self.tvv.column("#2", minwidth=150, width=150)
        self.tvv.heading("#3", text="Student Name")
        self.tvv.column("#3", minwidth=90, width=90)
        self.tvv.heading("#4", text="Class")
        self.tvv.column("#4", minwidth=60, width=60)
        self.tvv.heading("#5", text="Taken Date")
        self.tvv.column("#5", minwidth=120, width=120)
        self.tvv.heading("#6", text="Dedline")
        self.tvv.column("#6", minwidth=120, width=100)

        for row in (self.getdata()):
            self.tvv.insert("", END, values=(row[0], row[1], row[2], row[3], row[4], row[5]))
        self.tvv.bind('<ButtonRelease-1>', self.filltxtbox)

    def filltxtbox(self, a):
        self.clearfield()
        item = self.tvv.selection()[0]
        self.ID = int(self.tvv.item(item)['values'][0])
        self.txtbookname.config(state=NORMAL)
        self.txtbookname.insert(0, self.tvv.item(item)['values'][1])
        self.txtbookname.config(state=DISABLED)

        self.txtstudentname.config(state=NORMAL)
        self.txtstudentname.insert(0, self.tvv.item(item)['values'][2])
        self.txtstudentname.config(state=DISABLED)

        self.txtdeadline.config(state=NORMAL)
        self.txtdeadline.insert(0, self.tvv.item(item)['values'][5])
        self.txtdeadline.config(state=DISABLED)

    def clearfield(self):
        self.ID = 0

        self.txtbookname.config(state=NORMAL)
        self.txtbookname.delete(0, END)
        self.txtbookname.config(state=DISABLED)

        self.txtstudentname.config(state=NORMAL)
        self.txtstudentname.delete(0, END)
        self.txtstudentname.config(state=DISABLED)

        self.txtdeadline.config(state=NORMAL)
        self.txtdeadline.delete(0, END)
        self.txtdeadline.config(state=DISABLED)

        self.txtadddays.delete(0, END)

    def update(self, id, days):
        con = connection()
        c = con.cursor()
        c.execute(f"update borrow set deadline = Dateadd(DAY,{days},deadline) where id = {id}")
        con.commit()
        con.close()

    def getdata(self):
        con = connection()
        c = con.cursor()
        c.execute("""
        select bo.id,b.bookname,s.studentname,
        s.class,bo.takendate,bo.deadline from borrow bo
        inner join book b on  bo.bookid = b.id
        inner join student s on bo.studentid = s.ID where 
        bo.returndate is Null

        """)
        record = c.fetchall()
        con.commit()
        con.close()
        return record


class returnbook():
    def __init__(self, main):
        self.frame1 = LabelFrame(main, width=600, height=300, text="Return Book",
                                 font=("times new roman", 16, "bold"))
        self.frame1.place(x=75, y=75)

        self.tableframe = LabelFrame(self.frame1, text='Borrow', font=("times new roman", 10, "bold"), width=600)
        self.tableframe.place(x=5, y=147, height=130)
        self.filltable(self.tableframe)
        self.userdisplay()

    def userdisplay(self):
        self.frame2 = Frame(self.frame1)
        self.frame2.place(x=150, y=0)
        # Label
        lblbookname = Label(self.frame2, text="Book Name:", font=("times new roman", 12, "bold"))
        lblbookname.grid(row=0, column=0, sticky=E, padx=5)
        lblstudentname = Label(self.frame2, text="Student Name:", font=("times new roman", 12, "bold"))
        lblstudentname.grid(row=1, column=0, sticky=E, padx=5)
        lblreturn = Label(self.frame2, text="Return Date(Y-M-D):", font=("times new roman", 12, "bold"))
        lblreturn.grid(row=2, column=0, sticky=E, padx=0)
        btnfine = Button(self.frame2, text="Calculate Fine", font=("times new roman", 10, "bold"),
                         command=lambda: self.calculatefine(self.deadline, self.txtreturn.get()))
        btnfine.grid(row=3, column=0, sticky=E, padx=5)

        # Text Boxes
        self.txtbookname = Entry(self.frame2, width=25, state=DISABLED)
        self.txtbookname.grid(row=0, column=1)

        self.ID = 0
        self.bookid = 0
        self.deadline = ""

        self.txtstudentname = Entry(self.frame2, width=25, state=DISABLED)
        self.txtstudentname.grid(row=1, column=1)

        self.txtreturn = Entry(self.frame2, width=25)
        self.txtreturn.grid(row=2, column=1)
        self.txtreturn.insert(0, date.today())

        self.txtfine = Entry(self.frame2, width=25)
        self.txtfine.grid(row=3, column=1, pady=5)

        # Button
        btnconfirm = Button(self.frame2, text="CONFIRM", padx=45, pady=8, bg="black", foreground="white",
                            command=lambda: self.result(self.ID, self.txtreturn.get(), self.bookid))
        btnconfirm.grid(row=5, column=0, sticky=W)

        btncancel = Button(self.frame2, text="Cancel", bg="black", foreground="white", padx=45, pady=8,
                           command=self.frame1.place_forget)
        btncancel.grid(row=5, column=1, sticky=E)

    def calculatefine(self, deadline, returndate):
        try:
            date1 = datetime.strptime(deadline, "%Y-%m-%d")
            date2 = datetime.strptime(returndate, "%Y-%m-%d")
            totaldays = abs((date2 - date1).days)
            if date2 > date1:
                self.txtfine.delete(0, END)
                self.txtfine.insert(0, str(int(totaldays) * 30))
            else:
                self.txtfine.delete(0, END)
                self.txtfine.insert(0, "0")
        except:
            showerror("Invalid", "Enter valid date")
            self.clearfield()

    def result(self, id, returndate, bookid):
        if id == 0 or returndate == "":
            showerror("Error", "Please fill all fields")
            self.clearfield()
        else:
            try:
                self.update(id, returndate)
                self.updatequantity(bookid)
                self.clearfield()
                self.tableframe.place_forget()
                self.tableframe = LabelFrame(self.frame1, text='Borrow', font=("times new roman", 10, "bold"),
                                             width=600)
                self.tableframe.place(x=5, y=147, height=130)
                self.filltable(self.tableframe)
                showinfo("Success", "Book Successfully returned")
            except:
                showerror("Invalid", "Invalid returnd date")
                self.clearfield()

    def updatequantity(self, id):
        con = connection()
        c = con.cursor()
        c.execute(f"update book set quantity = quantity + 1 where id = {id}")
        con.commit()
        con.close()

    def update(self, id, date):
        con = connection()
        c = con.cursor()
        c.execute(f"update borrow set returndate = '{date}' where id = {id}")
        con.commit()
        con.close()

    def filltable(self, frame):
        self.tvv = ttk.Treeview(frame,
                                column=("column1", "column2", "column3", "column4", "column5", "column6", "column7"),
                                show="headings")
        self.tvv.pack(side='left', fill='x')
        scroll = Scrollbar(frame, orient="vertical", command=self.tvv.yview)
        scroll.pack(side='right', fill='y')
        self.tvv.configure(yscrollcommand=scroll.set)

        self.tvv.heading("#1", text="ID")
        self.tvv.column("#1", minwidth=40, width=40)
        self.tvv.heading("#2", text="Book Name")
        self.tvv.column("#2", minwidth=120, width=130)
        self.tvv.heading("#3", text="Student Name")
        self.tvv.column("#3", minwidth=90, width=90)
        self.tvv.heading("#4", text="Class")
        self.tvv.column("#4", minwidth=60, width=60)
        self.tvv.heading("#5", text="Taken Date")
        self.tvv.column("#5", minwidth=120, width=120)
        self.tvv.heading("#6", text="Dedline")
        self.tvv.column("#6", minwidth=100, width=100)
        self.tvv.heading("#7", text="Bookid")
        self.tvv.column("#7", minwidth=20, width=20)
        for row in (self.getdata()):
            self.tvv.insert("", END, values=(row[0], row[1], row[2], row[3], row[4], row[5], row[6]))
        self.tvv.bind('<ButtonRelease-1>', self.filltxtbox)

    def clearfield(self):
        self.ID = 0
        self.txtbookname.config(state=NORMAL)
        self.txtbookname.delete(0, END)
        self.txtbookname.config(state=DISABLED)

        self.txtstudentname.config(state=NORMAL)
        self.txtstudentname.delete(0, END)
        self.txtstudentname.config(state=DISABLED)
        self.txtreturn.delete(0, END)
        self.txtreturn.insert(0, date.today())

        self.deadline = ""
        self.bookid = 0

    def filltxtbox(self, a):
        self.clearfield()
        item = self.tvv.selection()[0]
        self.ID = int(self.tvv.item(item)['values'][0])
        self.txtbookname.config(state=NORMAL)
        self.txtbookname.insert(0, self.tvv.item(item)['values'][1])
        self.txtbookname.config(state=DISABLED)

        self.txtstudentname.config(state=NORMAL)
        self.txtstudentname.insert(0, self.tvv.item(item)['values'][2])
        self.txtstudentname.config(state=DISABLED)

        self.deadline = self.tvv.item(item)['values'][5]

        self.bookid = self.tvv.item(item)['values'][6]

    def getdata(self):
        con = connection()
        c = con.cursor()
        c.execute("""
        select bo.id,b.bookname,s.studentname,
        s.class,bo.takendate,bo.deadline,b.id from borrow bo
        inner join book b on  bo.bookid = b.id
        inner join student s on bo.studentid = s.ID where 
        bo.returndate is Null

        """)
        record = c.fetchall()
        con.commit()
        con.close()
        return record


displaylogin = login(root)
# abcd = mainpage()
root.mainloop()