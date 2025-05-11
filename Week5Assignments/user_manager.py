from database import create_connection
import sqlite3

def add_user(name, email):
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", (name, email))
        conn.commit()
        print(" User added successfully.")
    except sqlite3.IntegrityError:
        print(" Email must be unique.")
    conn.close()

def view_users():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
    conn.close()
    return rows

def search_user(name):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE name LIKE ?", ('%' + name + '%',))
    rows = cursor.fetchall()
    conn.close()
    return rows

def delete_user(user_id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
    conn.commit()
    conn.close()
    print("🗑️ User deleted.")

#Add one more option (No.6) to do the advanced search based on ID and name
#f"%{name}% as in formatted string with wildcard
def advanced_search(user_id=None, name=None):
    conn = create_connection()
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE id = ? AND name LIKE ?"
    values = [user_id, f"%{name}%"]
    cursor.execute(query, values)
    rows = cursor.fetchall()
    conn.close()
    return rows

#Add one more Table "course" (name, ID and unit columns ) with two functionality insert and search based on course_ID and user namedef enroll_user_to_course(user_id, course_id):
def add_course(name, unit):   
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO course (name, unit) VALUES (?, ?)", (name, unit))
    conn.commit()
    print("Course added successfully.")
    
    print("Course name must be unique.")
    conn.close()

def enrollcourse(user_id, course_id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO studentcourse (userid, courseid) VALUES (?, ?)", (user_id, course_id))
    conn.commit()
    print("User enrolled in course.")
    conn.close()

def view_course():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM course")
    rows = cursor.fetchall()
    conn.close()
    return rows

def searchcoursenuser(course_id, user_name):
    conn = create_connection()
    cursor = conn.cursor()
    #Get all required values from users and course tables and lists it. Have to take it from studentcourse while joining the users and course table with the foreign key
    #since the inputs are course.id and users.name have to add it for where conditon
    cursor.execute( '''
    SELECT users.id, users.name, users.email, course.id ,course.name , course.unit 
    FROM studentcourse
    JOIN users ON studentcourse.userid = users.id
    JOIN course ON studentcourse.courseid = course.id
    WHERE course.id = ?
    AND
    users.name LIKE ?
    ''',(course_id, f"%{user_name}%"))
    rows = cursor.fetchall()
    conn.close()
    return rows

'''def check_tables():
    conn = create_connection()
    cursor = conn.cursor()
    
    # Check users table
    print("\n--- Users Table ---")
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    for user in users:
        print(user)
    
    # Check course table
    print("\n--- Course Table ---")
    cursor.execute("SELECT * FROM course")
    courses = cursor.fetchall()
    for course in courses:
        print(course)
    
    # Check studentcourse table
    print("\n--- StudentCourse Table ---")
    cursor.execute("SELECT * FROM studentcourse")
    studentcourses = cursor.fetchall()
    for studentcourse in studentcourses:
        print(studentcourse)

    conn.close()
'''

