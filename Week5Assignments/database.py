import sqlite3

def create_connection():
    conn = sqlite3.connect("users.db")
    return conn
    

def create_table():
    conn = create_connection()
    cursor = conn.cursor()
    #cursor.execute("DELETE FROM users")
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE
        )
    ''')

    # Add one more Table "course" (name, ID and unit columns )
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS course (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            unit INTEGER NOT NULL
        )
    ''')
    #cursor.execute("DELETE FROM studentcourse")

    # Creating another table named studentcourse with two ID's user_id and course_id
    # where user_id has a matching entry in users table id column and course_id in course table id column
    # references to primary key from studentcourse table are added below as FOREIGN KEYs
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS studentcourse (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            userid INTEGER,
            courseid INTEGER,
            FOREIGN KEY(userid) REFERENCES users(id), 
            FOREIGN KEY(courseid) REFERENCES course(id) 
        )
    ''')

    conn.commit()
    conn.close()
