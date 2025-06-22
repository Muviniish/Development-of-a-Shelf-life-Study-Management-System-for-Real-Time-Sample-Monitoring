import customtkinter
import tkinter
import mysql.connector
import messagebox

db = mysql.connector.connect(host='localhost',
                                     user='root',
                                     password='abcd1234',
                                     db='adminlogin') 

cursor = db.cursor()


customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.title("Admin Login")
app.geometry(f"{app.winfo_screenwidth()}x{app.winfo_screenheight()}-8+0")

bottomframe = tkinter.Frame(app)
bottomframe.pack(expand=True)

def button_function():
    
    cursor.execute("SELECT * FROM admin WHERE username=%s AND password=%s", (user_name.get(), password.get()))
    result = cursor.fetchone()
    if result:
        label.configure(text="Login Successful", text_color="green")
        messagebox.showinfo("Login", "Login Successful")
        app.destroy()
        import admin_dashboard
    else:
        label.configure(text="Login Failed", text_color="red")

user_name = customtkinter.CTkEntry(master = bottomframe,
                                   placeholder_text="Username",
                                   font=('Helvetica', 28),
                                   width=800,
                                   height=100,
                                   border_width=2,
                                   corner_radius=30)
user_name.pack()

password = customtkinter.CTkEntry(master = bottomframe,
                                   placeholder_text="Password",
                                   font=('Helvetica', 28),
                                   show="*",
                                   width=800,
                                   height=100,
                                   border_width=2,
                                   corner_radius=30)
password.pack()

button = customtkinter.CTkButton(master = bottomframe,
                                 text="Log In",
                                 font=('Helvetica', 28),
                                 width=500,
                                 height=100,
                                 text_color="black",
                                 border_width=0,
                                 corner_radius=8,
                                 command= button_function)
button.pack()

label = customtkinter.CTkLabel(master = bottomframe,
                               text = "",
                               text_color = "black",
                               font=('Helvetica', 28),
                               width=200,
                               height=100,
                               fg_color="white",
                               corner_radius=8)
label.pack()


app.mainloop()