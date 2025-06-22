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
    mycursor.execute("CREATE database IF NOT EXISTS adminlogin")
    mycursor.execute("CREATE database IF NOT EXISTS userlogin")
    mycursor.execute("CREATE database IF NOT EXISTS testerlogin")
    mycursor.execute("CREATE database IF NOT EXISTS pendingProducts")
    mycursor.execute("CREATE database IF NOT EXISTS approvedProducts")
    mycursor.execute("USE adminlogin")
    mycursor.execute("CREATE TABLE IF NOT EXISTS admin(ID VARCHAR(20) PRIMARY KEY, username VARCHAR(20), password VARCHAR(20))")
    mycursor.execute("USE userlogin")
    mycursor.execute("CREATE TABLE IF NOT EXISTS user(ID VARCHAR(20) PRIMARY KEY, username VARCHAR(50), password VARCHAR(50), email VARCHAR(50), role VARCHAR(50), gender VARCHAR(20))")
    mycursor.execute("USE testerlogin")
    mycursor.execute("CREATE TABLE IF NOT EXISTS tester(ID VARCHAR(20) PRIMARY KEY, username VARCHAR(20), password VARCHAR(20))")
    mycursor.execute("USE pendingProducts")
    mycursor.execute("CREATE TABLE IF NOT EXISTS product(ID VARCHAR(20) PRIMARY KEY, name VARCHAR(20), description VARCHAR(50), quantity INT, email VARCHAR(50), test_date DATE, status VARCHAR(20))")
    mycursor.execute("USE approvedProducts")
    mycursor.execute("CREATE TABLE IF NOT EXISTS products(ID VARCHAR(20) PRIMARY KEY, name VARCHAR(20), description VARCHAR(50), quantity INT, email VARCHAR(50), test_date DATE, approved_date DATE)")

def connection1(user_name,password):
    mycursor.execute("USE adminlogin")
    mycursor.execute("SELECT * FROM admin WHERE username=%s AND password=%s", (user_name, password))
    result = mycursor.fetchone()
    if result:
        return result
def connection2(user_name,password):
    mycursor.execute("USE userlogin")
    mycursor.execute("SELECT * FROM user WHERE username=%s AND password=%s", (user_name, password))
    result = mycursor.fetchone()
    if result:
        return result
def connection3(user_name,password):
    mycursor.execute("USE testerlogin")
    mycursor.execute("SELECT * FROM tester WHERE username=%s AND password=%s", (user_name, password))
    result = mycursor.fetchone()
    if result:
        return result

connect_to_database()