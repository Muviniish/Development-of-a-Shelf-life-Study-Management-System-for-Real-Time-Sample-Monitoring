import pymysql
from tkinter import messagebox

def connect_to_database():
    global mycursor, conn
    try:
        conn = pymysql.connect(host='localhost', user='root', password='abcd1234',database='pendingProducts')
        mycursor = conn.cursor()
    except:
        messagebox.showerror("Database Error", "Something went wrong while connecting to the database. Please check your connection settings.")
        return
    
def fetch_users():
    mycursor.execute("SELECT * FROM product")
    result = mycursor.fetchall()
    return result

def delete_all(email):
    mycursor.execute("DELETE FROM product WHERE email= %s AND Status= %s", (email, "Pending"))
    conn.commit()


def insert(id, name, desc, quan, email, testdate, status):
    print("Inserting user data into the database...")
    mycursor.execute("INSERT INTO product VALUES (%s, %s, %s, %s, %s, %s, %s)", (id, name, desc, quan, email, testdate, status))
    conn.commit()
    print("User data inserted successfully.")

def id_exists(user_id):
    mycursor.execute("SELECT COUNT(*) FROM product WHERE ID = %s", (user_id,))
    result=mycursor.fetchone()
    return result[0]>0

def updateapprove(id):
    print("Updating user data in the database...")
    mycursor.execute("UPDATE product SET status = %s WHERE ID = %s", ("Approved", id))
    conn.commit()
    
def updatereject(id):
    print("Updating user data in the database...")
    mycursor.execute("UPDATE product SET status = %s WHERE ID = %s", ("Rejected", id))
    conn.commit()

def update(id, name, desc, quan, email, testdate, status):
    print("Updating user data in the database...")
    mycursor.execute("UPDATE product SET name = %s, description = %s, quantity = %s, test_date = %s, status = %s WHERE ID = %s AND email = %s", (name, desc, quan, testdate, status, id, email))
    conn.commit()

def delete(id, email):
    print("Deleting product data from the database...")
    mycursor.execute("DELETE FROM product WHERE ID = %s AND email = %s AND status = %s", (id, email, "Pending"))
    conn.commit()
    print("Product data deleted successfully.")

def search(value):
    mycursor.execute(f"SELECT * FROM product WHERE email = %s", value)
    result = mycursor.fetchall()
    return result

def search2():
    mycursor.execute(f"SELECT * FROM product WHERE status = %s", "Pending")
    result = mycursor.fetchall()
    return result

connect_to_database()