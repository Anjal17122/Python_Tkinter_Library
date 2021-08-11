import sqlite3
username = 'admin'
password = 'admin'
PATH = r'C:\Users\User\Desktop\AnjalSaps\projects\pythondjangoprojects\pythontkinterfinalproject\tkinterr\lib_mngmt'
def connect():
    conn = sqlite3.connect(PATH)

    return conn
def create_table_book():
    conn=connect()
    c=conn.cursor()
    c.execute('''create table book(
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                BookName TEXT not null unique,
                Author TEXT,
                Type TEXT,
                Quantity INTEGER
                )''')
    conn.commit()
    conn.close()

def create_table_student():
    conn=connect()
    c=conn.cursor()
    c.execute('''create table student(
                ID integer primary key AUTOINCREMENT,
                StudentName TEXT,
                Phoneno TEXT,
                Class TEXT,
                Gender TEXT
                )''')
    conn.commit()
    conn.close()

def create_table_login():
    conn=connect()
    c=conn.cursor()
    c.execute('''create table Login(
                ID integer primary key AUTOINCREMENT,
                username TEXT,
                password TEXT
                )''')
    conn.commit()
    conn.close()

def create_table_borrow():
    conn=connect()
    c=conn.cursor()
    c.execute('''create table borrow(
                ID integer primary key AUTOINCREMENT,
                bookid INTEGER,
                studentid INTEGER,
                takendate TEXT,
                deadline TEXT,
                returndate TEXT
                )''')
    conn.commit()
    conn.close()

def insert_table_login():
    conn = connect()
    c=conn.cursor()
    c.execute(f"insert into LOGIN(USERNAME,PASSWORD) values('{username}', '{password}')")
    conn.commit()
    conn.close()
    print(f"Your username is {username} and password is {password}")
def getdata():
    conn = connect()
    c = conn.cursor()
    c.execute('''
    select bo.id,b.bookname,b.type,s.studentname,
s.class,bo.takendate,bo.deadline from borrow bo
inner join book b on  bo.bookid = b.id
inner join student s on bo.studentid = s.ID where bo.returndate is Null
    ''')
    rows = c.fetchall()
    print(rows)
    conn.commit()
    conn.close()


create_table_student()
create_table_book()
create_table_borrow()
create_table_login()
insert_table_login()
