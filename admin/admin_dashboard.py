from customtkinter import *
from PIL import Image
from tkinter import ttk, messagebox
import user_database

def search_user():
    if searchBox.get() == "Search By":
        messagebox.showerror("Error", "Please select a search option")
    elif searchEntry.get() == "":
        messagebox.showerror("Error", "Please enter a search term")
    else:
        searched_users = user_database.search(searchBox.get(), searchEntry.get())
        tree.delete(*tree.get_children())
        for user in searched_users:
            tree.insert('', END, values=user)

def showall():
    treeview_data()
    searchEntry.delete(0, END)
    searchBox.set('Search By')

def treeview_data():
    users = user_database.fetch_users()
    tree.delete(*tree.get_children())
    for user in users:
        tree.insert('', END, values=user)

def selection(event):
    selected_item = tree.selection()
    if selected_item:
        item = tree.item(selected_item)
        clear()
        idEntry.insert(0, item['values'][0])
        nameEntry.insert(0, item['values'][1])
        contactEntry.insert(0, item['values'][2])
        roleBox.set(item['values'][3])
        genderBox.set(item['values'][4])

def clear(value=False):
    if value:
        tree.selection_remove(tree.focus())
    idEntry.delete(0, END)
    nameEntry.delete(0, END)
    contactEntry.delete(0, END)
    roleBox.set('')
    genderBox.set('')

def add_user():
    if idEntry.get() == "" or nameEntry.get() == "" or contactEntry.get() == "" or roleBox.get() == "" or genderBox.get() == "":
        messagebox.showerror("Error", "All fields are required")
    elif user_database.id_exists(idEntry.get()):
        messagebox.showerror("Error", "User ID already exists")
    else:
        id = idEntry.get()
        if not id.startswith("USER"):
            if id.isdigit():
                id = "USER" + idEntry.get()
                user_database.insert(id, nameEntry.get(), contactEntry.get(), roleBox.get(), genderBox.get())
                treeview_data()
                clear()
                messagebox.showinfo("Success", "User added successfully")
            else:
                messagebox.showerror("Error", "User ID must start with 'USER' followed by digits")
        else:
            user_database.insert(id, nameEntry.get(), contactEntry.get(), roleBox.get(), genderBox.get())
            treeview_data()
            clear()
            messagebox.showinfo("Success", "User added successfully")

def update_user():
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showerror("Error", "Select data to update")
    else:
        user_database.update(idEntry.get(), nameEntry.get(), contactEntry.get(), roleBox.get(), genderBox.get())
        treeview_data()
        clear()
        messagebox.showinfo("Success", "User updated successfully")

def delete_user():
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showerror("Error", "Select data to delete")
    else:
        user_database.delete(idEntry.get())
        treeview_data()
        clear()
        messagebox.showinfo("Success", "User deleted successfully")

def deleteall():
    result = messagebox.askyesno('Confirm','Do you really want to delete all users?', icon='warning')
    if result:
        user_database.delete_all()
    else:
        pass
    treeview_data()

def logout():
    result = messagebox.askyesno('Confirm','Do you really want to log out?', icon='warning')
    if result:
        app.destroy()
        import admin_loginpage
    else:
        pass

app = CTk()
app.title("Admin Dashboard")
app.geometry(f"{app.winfo_screenwidth()}x{app.winfo_screenheight()}-8+0")
app.configure(fg_color="indianred4")

imgFrame= CTkFrame(app, width=app.winfo_screenwidth(), height=app.winfo_screenheight()/3, fg_color="indianred4")
imgFrame.grid(row=0, column=0, padx=20, pady=20, columnspan=2)
image = CTkImage(Image.open("Images/admin_dashboard.png"), size=(app.winfo_screenwidth()/1.5, app.winfo_screenheight()/3))
imgLabel = CTkLabel(imgFrame, image=image, text="")
imgLabel.place(relx=0.5, rely=0.5, anchor=CENTER)


leftFrame = CTkFrame(app, fg_color="indianred4")
leftFrame.grid(row=1, column=0)

idLabel = CTkLabel(leftFrame, text="User ID", font=('Helvetica', 25, 'bold'),text_color="white")
idLabel.grid(row=0, column=0, padx=40, pady=20, sticky='w')

idEntry = CTkEntry(leftFrame, font=('Helvetica', 20), width=360)
idEntry.grid(row=0, column=1, padx=20, pady=20)

nameLabel = CTkLabel(leftFrame, text="Name", font=('Helvetica', 25, 'bold'),text_color="white")
nameLabel.grid(row=1, column=0, padx=40, pady=20, sticky='w')

nameEntry = CTkEntry(leftFrame, font=('Helvetica', 20), width=360)
nameEntry.grid(row=1, column=1, padx=20, pady=20)

contactLabel = CTkLabel(leftFrame, text="Contact", font=('Helvetica', 25, 'bold'),text_color="white")
contactLabel.grid(row=2, column=0, padx=40, pady=20, sticky='w')

contactEntry = CTkEntry(leftFrame, font=('Helvetica', 20), width=360)
contactEntry.grid(row=2, column=1, padx=20, pady=20)

roleLabel = CTkLabel(leftFrame, text="Role", font=('Helvetica', 25, 'bold'),text_color="white")
roleLabel.grid(row=3, column=0, padx=40, pady=20, sticky='w')
roleOptions = ['Research Scientist','Regulatory Affairs Specialist','Clinical Research Associate','Pharmaceutical Sales Representative','Pharmacist','Quality Control Specialist']
roleBox= CTkComboBox(leftFrame, values=roleOptions, font=('Helvetica', 20), width=360, state='readonly')
roleBox.grid(row=3, column=1, padx=20, pady=20)
roleBox.set('')

genderLabel = CTkLabel(leftFrame, text="Gender", font=('Helvetica', 25, 'bold'),text_color="white")
genderLabel.grid(row=4, column=0, padx=40, pady=20, sticky='w')
genderOptions = ['Male', 'Female']
genderBox= CTkComboBox(leftFrame, values=genderOptions, font=('Helvetica', 20), width=360, state='readonly')
genderBox.grid(row=4, column=1, padx=20, pady=20)
genderBox.set('')

rightFrame = CTkFrame(app)
rightFrame.grid(row=1, column=1, padx=20, pady=20)

searchOptions = ['ID', 'Name', 'Contact Number', 'Role', 'Gender']
searchBox= CTkComboBox(rightFrame, values=searchOptions, font=('Helvetica', 25), width=250, state='readonly')
searchBox.grid(row=0, column=0, pady=10)
searchBox.set('Search By')

searchEntry = CTkEntry(rightFrame, font=('Helvetica', 25), width=360)
searchEntry.grid(row=0, column=1, pady=10)

searchButton = CTkButton(rightFrame, text="Search", font=('Helvetica', 25), width=200, command=search_user)
searchButton.grid(row=0, column=2, pady=10)

showButton = CTkButton(rightFrame, text="Show All", font=('Helvetica', 25), width=200, command=showall)
showButton.grid(row=0, column=3, pady=10)

tree=ttk.Treeview(rightFrame, height=10)
tree.grid(row=1, column=0, columnspan=4)
tree['columns'] = ('ID', 'Name', 'Contact Number', 'Role', 'Gender')

tree.heading('ID', text='User ID', anchor=CENTER)
tree.heading('Name', text='Name', anchor=CENTER)
tree.heading('Contact Number', text='Contact Number', anchor=CENTER)
tree.heading('Role', text='Role', anchor=CENTER)
tree.heading('Gender', text='Gender', anchor=CENTER)
tree.config(show='headings')
tree.column('ID', width=150, anchor=CENTER)
tree.column('Name', width=300)
tree.column('Contact Number', width=250, anchor=CENTER)
tree.column('Role', width=400, anchor=CENTER)
tree.column('Gender', width=130, anchor=CENTER)

style = ttk.Style()
style.theme_use("clam")
style.configure("Treeview.Heading", font=('Goudy Old Style',18,'bold'))
style.configure("Treeview", font=('Goudy Old Style', 15, 'bold'), rowheight=30, background="gray17", foreground="white", fieldbackground="indianred4")

scrollbar=ttk.Scrollbar(rightFrame, orient="vertical", command=tree.yview)
scrollbar.grid(row=1, column=4, sticky='ns')

tree.configure(yscrollcommand=scrollbar.set)

buttonFrame = CTkFrame(app, fg_color="indianred4")
buttonFrame.grid(row=2, column=0, columnspan=2)

addButton = CTkButton(buttonFrame, text="Add User", font=('Helvetica', 25,'bold'), width=200, corner_radius=15, command=add_user)
addButton.grid(row=0, column=0, padx=30, pady=30)

deleteButton = CTkButton(buttonFrame, text="Delete User", font=('Helvetica', 25,'bold'), width=200, corner_radius=15, command=delete_user)
deleteButton.grid(row=0, column=1, padx=30, pady=30)

updateButton = CTkButton(buttonFrame, text="Update User", font=('Helvetica', 25,'bold'), width=200, corner_radius=15, command=update_user)
updateButton.grid(row=0, column=2, padx=30, pady=30)

deleteallButton = CTkButton(buttonFrame, text="Delete All User", font=('Helvetica', 25,'bold'), width=200, corner_radius=15, command=deleteall)
deleteallButton.grid(row=0, column=3, padx=30, pady=30)

clearButton = CTkButton(buttonFrame, text="Clear", font=('Helvetica', 25,'bold'), width=200, corner_radius=15, command=lambda: clear(True))
clearButton.grid(row=0, column=4, padx=30, pady=30)

logoutFrame = CTkFrame(app, fg_color="indianred4")
logoutFrame.grid(row=3, column=1, sticky="e", padx=80)

logoutButton = CTkButton(logoutFrame, text="Log Out", font=('Helvetica', 25,'bold'), width=200, corner_radius=15, command=logout)
logoutButton.grid(row=0, column=0)

treeview_data()

tree.bind('<ButtonRelease-1>', selection)

app.mainloop()