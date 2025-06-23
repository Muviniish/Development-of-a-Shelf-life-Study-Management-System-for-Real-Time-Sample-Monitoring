import pymysql
from tkinter import messagebox


def connect_to_database():
    global mycursor, conn
    try:
        conn = pymysql.connect(host='localhost', user='root', password='abcd1234', database="userlogin")
        mycursor = conn.cursor()
    except:
        messagebox.showerror("Database Error", "Something went wrong while connecting to the database. Please check your connection settings.")
        return

def connection(user_name,password):
    mycursor.execute("SELECT * FROM user WHERE username=%s AND password=%s", (user_name, password))
    result = mycursor.fetchone()
    return result

def search(option, value):
    mycursor.execute(f"SELECT * FROM user WHERE {option} = %s", value)
    result = mycursor.fetchall()
    return result

def insert(user_id, name, password, email, role, gender):
    print("Inserting user data into the database...")
    mycursor.execute("INSERT INTO user VALUES (%s, %s, %s, %s, %s, %s)", (user_id, name, password, email, role, gender))
    conn.commit()
    print("User data inserted successfully.")

def update(user_id, name, password, email, role, gender):
    print("Updating user data in the database...")
    mycursor.execute("UPDATE user SET Username = %s, Password = %s, Email = %s, Role = %s, Gender = %s WHERE ID = %s", (name, password, email, role, gender, user_id))
    conn.commit()

def delete(user_id):
    print("Deleting user data from the database...")
    mycursor.execute("DELETE FROM user WHERE ID = %s", (user_id))
    conn.commit()
    print("User data deleted successfully.")

def delete_all():
    mycursor.execute("TRUNCATE TABLE user")
    conn.commit()
    print("All user data deleted successfully.")

def id_exists(user_id):
    mycursor.execute("SELECT COUNT(*) FROM user WHERE ID = %s", (user_id))
    result=mycursor.fetchone()
    return result[0]>0

def fetch_users():
    mycursor.execute("SELECT * FROM user")
    result = mycursor.fetchall()
    return result

connect_to_database()