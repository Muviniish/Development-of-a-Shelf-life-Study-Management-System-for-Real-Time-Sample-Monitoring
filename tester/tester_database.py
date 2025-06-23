import pymysql
from tkinter import messagebox
import gmail

def connect_to_database():
    global mycursor, conn
    try:
        conn = pymysql.connect(host='localhost', user='root', password='abcd1234',database='testerDb')
        mycursor = conn.cursor()
    except:
        messagebox.showerror("Database Error", "Something went wrong while connecting to the database. Please check your connection settings.")
        return
    
def search():
    mycursor.execute(f"SELECT * FROM db")
    result = mycursor.fetchall()
    return result

def search2():
    mycursor.execute(f"SELECT * FROM db WHERE DATEDIFF(start, CURDATE()) <=3 AND start >= CURDATE()")
    results = mycursor.fetchall()
    for result in results:
        gmail.main(result[4],result[1])
        gmail.main(result[5],result[1])

def search3(option, value):
    mycursor.execute(f"SELECT * FROM db WHERE {option} = %s", value)
    result = mycursor.fetchall()
    return result

def update(id, tester, start, end, status):
    print("Updating user data in the database...")
    mycursor.execute("UPDATE db SET start = %s, end = %s, status = %s, tester_email = %s WHERE ID = %s", (start, end, status, tester, id))
    conn.commit()

def id_exists(user_id):
    mycursor.execute("SELECT COUNT(*) FROM db WHERE ID = %s", (user_id,))
    result=mycursor.fetchone()
    return result[0]>0

def insert(id, start, status, testeremail, owneremail):
    print("Inserting user data into the database...")
    mycursor.execute("INSERT INTO db VALUES (%s, %s, %s, %s, %s, %s)", (id, start, None, status, testeremail, owneremail))
    conn.commit()
    print("User data inserted successfully.")

def fetch_users():
    mycursor.execute("SELECT * FROM db")
    result = mycursor.fetchall()
    return result

connect_to_database()