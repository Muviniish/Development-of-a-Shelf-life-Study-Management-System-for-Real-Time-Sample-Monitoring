import pymysql
from tkinter import messagebox


def connect_to_database():
    global mycursor, conn
    try:
        conn = pymysql.connect(host='localhost', user='root', password='abcd1234')
        mycursor = conn.cursor()
    except:
        messagebox.showerror("Database Error", "Something went wrong while connecting to the database. Please check your connection settings.")
        return
    mycursor.execute("CREATE database IF NOT EXISTS userlogin")
    mycursor.execute("USE userlogin")
    mycursor.execute("CREATE TABLE IF NOT EXISTS user(user_id VARCHAR(20) PRIMARY KEY, name VARCHAR(50), contact VARCHAR(15), role VARCHAR(50), Gender VARCHAR(10))")

def search(option, value):
    mycursor.execute(f"SELECT * FROM user WHERE {option} = %s", value)
    result = mycursor.fetchall()
    return result

def insert(user_id, name, contact, role, gender):
    print("Inserting user data into the database...")
    mycursor.execute("INSERT INTO user VALUES (%s, %s, %s, %s, %s)", (user_id, name, contact, role, gender))
    conn.commit()
    print("User data inserted successfully.")

def update(user_id, name, contact, role, gender):
    print("Updating user data in the database...")
    mycursor.execute("UPDATE user SET name = %s, contact = %s, role = %s, gender = %s WHERE user_id = %s", (name, contact, role, gender, user_id))
    conn.commit()

def delete(user_id):
    print("Deleting user data from the database...")
    mycursor.execute("DELETE FROM user WHERE user_id = %s", (user_id,))
    conn.commit()
    print("User data deleted successfully.")

def delete_all():
    mycursor.execute("TRUNCATE TABLE user")
    conn.commit()
    print("All user data deleted successfully.")

def id_exists(user_id):
    mycursor.execute("SELECT COUNT(*) FROM user WHERE user_id = %s", (user_id,))
    result=mycursor.fetchone()
    return result[0]>0

def fetch_users():
    mycursor.execute("SELECT * FROM user")
    result = mycursor.fetchall()
    return result

connect_to_database()