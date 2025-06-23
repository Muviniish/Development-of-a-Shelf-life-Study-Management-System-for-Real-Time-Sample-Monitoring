from customtkinter import *
from tkinter import ttk, messagebox
import re
from datetime import datetime
import sys
sys.path.append('.')
import login, barcodegenerator
from admin import product_database, pendingproduct_database
from user import user_database
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
class LoginForm:
    def __init__(self, window):
        self.window = window
        self.window.geometry('1166x718')
        self.window.state('zoomed')
        self.window.resizable(0, 0)

def page():
    global my_y
    my_y=720
    def user():
        global my_y
        my_y -=20
        if my_y >=80:
            Frame2.place(x=0, y=my_y)
            window.after(20,user)

    def product():
        global my_y
        my_y +=20
        if my_y <=780:
            Frame2.place(x=0, y=my_y)
            window.after(20, product)
    
    def logout():
        result = messagebox.askyesno('Confirm','Do you really want to log out?', icon='warning')
        if result:
            window.destroy()
            login.page()
        else:
            pass
    
    def treeview1_data():
        products = product_database.fetch_users()
        tree.delete(*tree.get_children())
        for product in products:
            tree.insert('', END, values=product)
    
    def treeview2_data():
        products = pendingproduct_database.search2()
        tree2.delete(*tree2.get_children())
        for product in products:
            tree2.insert('', END, values=product)

    def treeview3_data():
        users = user_database.fetch_users()
        tree3.delete(*tree3.get_children())
        for user in users:
            tree3.insert('', END, values=user)    
    
    window = CTk()
    LoginForm(window)
    Frame = CTkFrame(window, fg_color='#4abdc0', bg_color='#4abdc0', width=1166, height=80)
    Frame.place(x=0, y=0)
    productBtn = CTkButton(Frame, text="PRODUCT DASHBOARD", text_color="black",  font=('yu gothic ui', 20, 'bold'), width=300,
                         bg_color='#4a6ec0', cursor='hand2', fg_color='#4a6ec0', command=product, border_color="black", border_width=2)
    productBtn.place(x=50, y=25)
    userBtn = CTkButton(Frame, text="USER DASHBOARD",  font=('yu gothic ui', 20, 'bold'), width=300,
                         bg_color='#4a6ec0', cursor='hand2', fg_color='#4a6ec0', command=user, border_color="black", border_width=2, text_color="black")
    userBtn.place(x=400, y=25)
    logoutBtn = CTkButton(Frame, text="Log Out", text_color="black",  font=('yu gothic ui', 20, 'bold'), width=150,
                         bg_color='#4a6ec0', cursor='hand2', fg_color='#4a6ec0', border_color="black", border_width=2, command=logout)
    logoutBtn.place(x=950, y=25)
    

    def showall():
        treeview1_data()
        searchEntry.delete(0, END)
        searchBox.set('Search By')

    def search_product():
        if searchBox.get() == "Search By":
            messagebox.showerror("Error", "Please select a search option")
        elif searchEntry.get() == "":
            messagebox.showerror("Error", "Please enter a search term")
        else:
            searched_products = product_database.search(searchBox.get(), searchEntry.get())
            tree.delete(*tree.get_children())
            for product in searched_products:
                tree.insert('', END, values=product)

    def generate_barcode():
        selected_item = tree.selection()
        if not selected_item:
            messagebox.showerror("Error", "Select a product")
        else:
            item = tree.item(selected_item)
            id=item['values'][0]
            barcodegenerator.generator(id, window)

    Frame1 = CTkFrame(window, fg_color='#ffeae0', bg_color='#ffeae0', width=1166, height=638)
    Frame1.place(x=0, y=80)
    upperframe = CTkFrame(Frame1, fg_color='#ffeae0', bg_color='#ffeae0', width=1166, height=330)
    upperframe.place(x=0, y=0)
    label1= CTkLabel(upperframe, text="APPROVED PRODUCTS", fg_color="#ffeae0", bg_color='#ffeae0', font=('yu gothic ui', 22, 'bold'))
    label1.place(x=80, y=10)
    tree1frame = CTkFrame(upperframe, width=1000, height=40)
    tree1frame.place(x=80, y=37)
    searchOptions = ['ID', 'Name', 'Description', 'Email', 'Test_Date','Approved_Date']
    searchBox= CTkComboBox(tree1frame, values=searchOptions, font=('yu gothic ui', 20), width=200, state='readonly')
    searchBox.place(x=0, y=2)
    searchBox.set('Search By')

    searchEntry = CTkEntry(tree1frame, font=('yu gothic ui', 20), width=300)
    searchEntry.place(x=220,y=2)
    searchButton = CTkButton(tree1frame, text="Search", font=('yu gothic ui', 20), width=150, cursor='hand2', text_color='black', command=search_product)
    searchButton.place(x=650,y=2)

    showButton = CTkButton(tree1frame, text="Show All", font=('yu gothic ui', 20), width=150, cursor='hand2', text_color='black', command=showall)
    showButton.place(x=850,y=2)
    tree=ttk.Treeview(upperframe, height=10)
    tree.grid(row=0, column=0, columnspan=4, sticky='nsew', padx=(80,0), pady=(78,0))
    tree['columns'] = ('ID', 'Name', 'Description', 'Quantity', 'Email', 'Date', 'Approved')
    tree.heading('ID', text='Product ID', anchor=CENTER)  
    tree.heading('Name', text='Product Name', anchor=CENTER)
    tree.heading('Description', text='Description', anchor=CENTER)
    tree.heading('Quantity', text='Quantity', anchor=CENTER)
    tree.heading('Email', text='Email', anchor=CENTER)
    tree.heading('Date', text='Test Date', anchor=CENTER)
    tree.heading('Approved', text='Approved Date', anchor=CENTER)
    tree.config(show='headings')
    tree.column('ID', width=130, anchor=CENTER)
    tree.column('Name', width=150)
    tree.column('Description', width=150, anchor=CENTER)
    tree.column('Quantity', width=100, anchor=CENTER)
    tree.column('Email', width=150, anchor=CENTER)
    tree.column('Date', width=145, anchor=CENTER)
    tree.column('Approved', width=170, anchor=CENTER)
    scrollbar=ttk.Scrollbar(upperframe, orient="vertical", command=tree.yview)
    scrollbar.grid(row=0, column=4, sticky='ns', pady=(78,0))
    tree.configure(yscrollcommand=scrollbar.set)
    barcodeBtn = CTkButton(upperframe, text="Print Barcode", font=('yu gothic ui', 25), width=150, cursor='hand2', border_color="black", border_width=2, text_color="black", command=generate_barcode)
    barcodeBtn.grid(row=1, column=1, padx=(220,0), pady=(10,0))


    def addProduct():
        selected_item = tree2.selection()
        if not selected_item:
            messagebox.showerror("Error", "Select product to approve")
        else:
            item = tree2.item(selected_item)
            id=item['values'][0]
            name=item['values'][1]
            desc=item['values'][2]
            qtn=item['values'][3]
            email=item['values'][4]
            test_date=item['values'][5]
            approved=datetime.now().strftime("%Y-%m-%d")
            if product_database.id_exists(id):
                messagebox.showerror("Error", "Product ID already exists")
            else:
                print(id)
                product_database.insert(id, name, desc, qtn, email, test_date, approved)
                pendingproduct_database.updateapprove(id)
                treeview1_data()
                treeview2_data()
                messagebox.showinfo("Success", "Product approved")
                barcodegenerator.generator(id, window)
                
                
                

    def deleteProduct():
        selected_item = tree2.selection()
        if not selected_item:
            messagebox.showerror("Error", "Select product to reject")
        else:
            item = tree2.item(selected_item)
            id=item['values'][0]
            pendingproduct_database.updatereject(id)
            treeview2_data()
            messagebox.showinfo("Success", "Product rejected")
   
    bottomframe = CTkFrame(Frame1, fg_color='#ffeae0', bg_color='#ffeae0', width=1166, height=280)
    bottomframe.place(x=0, y=330)
    label2= CTkLabel(bottomframe, text="PENDING APPROVALS", fg_color="#ffeae0", bg_color='#ffeae0', font=('yu gothic ui', 22, 'bold'))
    label2.place(x=80, y=0)
    tree2=ttk.Treeview(bottomframe, height=10)
    tree2.grid(row=0, column=0, columnspan=4, sticky='nsew', padx=(80,0), pady=(30,0))
    tree2['columns'] = ('ID', 'Name', 'Description', 'Quantity', 'Email', 'Date','Status')
    tree2.heading('ID', text='Product ID', anchor=CENTER)  
    tree2.heading('Name', text='Product Name', anchor=CENTER)
    tree2.heading('Description', text='Description', anchor=CENTER)
    tree2.heading('Quantity', text='Quantity', anchor=CENTER)
    tree2.heading('Email', text='Email', anchor=CENTER)
    tree2.heading('Date', text='Test Date', anchor=CENTER)
    tree2.heading('Status', text='Approval Status', anchor=CENTER)
    tree2.config(show='headings')
    tree2.column('ID', width=130, anchor=CENTER)
    tree2.column('Name', width=150)
    tree2.column('Description', width=150, anchor=CENTER)
    tree2.column('Quantity', width=100, anchor=CENTER)
    tree2.column('Email', width=150, anchor=CENTER)
    tree2.column('Date', width=145, anchor=CENTER)
    tree2.column('Status', width=170, anchor=CENTER)
    scrollbar2=ttk.Scrollbar(bottomframe, orient="vertical", command=tree2.yview)
    scrollbar2.grid(row=0, column=4, sticky='ns', pady=(30,0))
    tree2.configure(yscrollcommand=scrollbar2.set)
    style = ttk.Style()
    style.theme_use("clam")
    style.configure("Treeview.Heading", font=('Goudy Old Style',15,'bold'))
    style.configure("Treeview", font=('Goudy Old Style', 9, 'bold'), rowheight=15, background="gray17", foreground="white", fieldbackground="#FCD8CD")
    
    acceptBtn = CTkButton(bottomframe, text="ACCEPT", font=('yu gothic ui', 25), width=150, cursor='hand2', border_color="black", border_width=2, text_color="black", command=addProduct)
    acceptBtn.grid(row=1, column=1, padx=(80,0), pady=(10,0))
    rejectBtn = CTkButton(bottomframe, text="REJECT", font=('yu gothic ui', 25), width=150, cursor='hand2', border_color="black", border_width=2, text_color="black", command = deleteProduct)
    rejectBtn.grid(row=1, column=2, pady=(10,0))


    def addUser():
        if idEntry.get() == "" or nameEntry.get() == "" or passEntry.get() == "" or emailEntry.get() == "" or roleBox.get() == "" or genderBox.get() == "":
            messagebox.showerror("Error", "All fields are required")
        elif user_database.id_exists(idEntry.get()):
            messagebox.showerror("Error", "User ID already exists")
        elif not validate_email(emailEntry.get()):
            messagebox.showerror("Error", "Invalid email format")
        else:
            id = idEntry.get()
            user_database.insert(id, nameEntry.get(), passEntry.get(), emailEntry.get(), roleBox.get(), genderBox.get())
            treeview3_data()
            clear()
            messagebox.showinfo("Success", "User added successfully")

    def validate_email(email):
        if re.fullmatch(regex, email):
            return True
        else:
            return False
                
    def deleteUser():
        selected_item = tree3.selection()
        if not selected_item:
            messagebox.showerror("Error", "Select data to delete")
        else:
            user_database.delete(idEntry.get())
            treeview3_data()
            clear()
            messagebox.showinfo("Success", "User deleted successfully")

    def updateUser():
        selected_item = tree3.selection()
        if not selected_item:
            messagebox.showerror("Error", "Select data to update")
        else:
            user_database.update(idEntry.get(), nameEntry.get(), passEntry.get(), emailEntry.get(), roleBox.get(), genderBox.get())
            treeview3_data()
            clear()
            messagebox.showinfo("Success", "User updated successfully")

    def deleteAll():
        result = messagebox.askyesno('Confirm','Do you really want to delete all users?', icon='warning')
        if result:
            user_database.delete_all()
        else:
            pass
        treeview3_data()

    def clear(value=False):
        if value:
            tree3.selection_remove(tree3.focus())
        idEntry.delete(0, END)
        nameEntry.delete(0, END)
        passEntry.delete(0, END)
        emailEntry.delete(0, END)
        roleBox.set('')
        genderBox.set('')

    def selection(event):
        selected_item = tree3.selection()
        if selected_item:
            item = tree3.item(selected_item)
            clear()
            idEntry.insert(0, item['values'][0])
            nameEntry.insert(0, item['values'][1])
            passEntry.insert(0, item['values'][2])
            emailEntry.insert(0, item['values'][3])
            roleBox.set(item['values'][4])
            genderBox.set(item['values'][5])

    def search_user():
        if searchBox2.get() == "Search By":
            messagebox.showerror("Error", "Please select a search option")
        elif searchEntry2.get() == "":
            messagebox.showerror("Error", "Please enter a search term")
        else:
            searched_users = user_database.search(searchBox2.get(), searchEntry2.get())
            tree3.delete(*tree3.get_children())
            for user in searched_users:
                tree3.insert('', END, values=user)

    def showall2():
        treeview3_data()
        searchEntry2.delete(0, END)
        searchBox2.set('Search By')

    Frame2 = CTkFrame(window, fg_color='#ffeae0', bg_color='#ffeae0', width=1166, height=638)
    Frame2.place(x=0, y=my_y)
    label2= CTkLabel(Frame2, text="USER FORM", fg_color="#ffeae0", bg_color='#ffeae0', font=('yu gothic ui', 23, 'bold'))
    label2.place(x=80, y=10)
    labelLine = CTkCanvas(Frame2, width=450, height=2.0, bg="black")
    labelLine.place(x=0, y=40)
    leftFrame = CTkFrame(Frame2, fg_color="#ffeae0", width=450, height=570)
    leftFrame.place(x=0, y=45)
    idLabel= CTkLabel(leftFrame, text="User ID     ->", fg_color="#ffeae0", bg_color='#ffeae0', font=('yu gothic ui', 23, 'bold'))
    idLabel.place(x=20, y=30)
    idEntry= CTkEntry(leftFrame, width=300, fg_color="#ffeae0", bg_color='#ffeae0', font=('yu gothic ui', 20, 'bold'))
    idEntry.place(x=150, y=30)
    nameLabel= CTkLabel(leftFrame, text="Username->", fg_color="#ffeae0", bg_color='#ffeae0', font=('yu gothic ui', 23, 'bold'))
    nameLabel.place(x=20, y=100)
    nameEntry= CTkEntry(leftFrame, width=300, fg_color="#ffeae0", bg_color='#ffeae0', font=('yu gothic ui', 20, 'bold'))
    nameEntry.place(x=150, y=100)
    passLabel= CTkLabel(leftFrame, text="Password ->", fg_color="#ffeae0", bg_color='#ffeae0', font=('yu gothic ui', 23, 'bold'))
    passLabel.place(x=20, y=170)
    passEntry= CTkEntry(leftFrame, width=300, fg_color="#ffeae0", bg_color='#ffeae0', font=('yu gothic ui', 20, 'bold'))
    passEntry.place(x=150, y=170)
    emailLabel= CTkLabel(leftFrame, text="Email        ->", fg_color="#ffeae0", bg_color='#ffeae0', font=('yu gothic ui', 23, 'bold'))
    emailLabel.place(x=20, y=240)
    emailEntry= CTkEntry(leftFrame, width=300, fg_color="#ffeae0", bg_color='#ffeae0', font=('yu gothic ui', 20, 'bold'))
    emailEntry.place(x=150, y=240)
    roleLabel= CTkLabel(leftFrame, text="Role          ->", fg_color="#ffeae0", bg_color='#ffeae0', font=('yu gothic ui', 23, 'bold'))
    roleLabel.place(x=20, y=310)
    roleOptions = ['Senior R&D Lab Tester','Product Developer','NPI Engineer','Global Product Launch Manager','Pharmacist','Technician']
    roleBox= CTkComboBox(leftFrame, values=roleOptions, font=('yu gothic ui', 20, 'bold'), width=300, state='readonly', fg_color="#ffeae0", bg_color='#ffeae0')
    roleBox.place(x=150, y=310)
    roleBox.set('')
    genderLabel= CTkLabel(leftFrame, text="Gender     ->", fg_color="#ffeae0", bg_color='#ffeae0', font=('yu gothic ui', 23, 'bold'))
    genderLabel.place(x=20, y=380)
    genderOptions = ['Male', 'Female']
    genderBox= CTkComboBox(leftFrame, values=genderOptions, font=('yu gothic ui', 20, 'bold'), width=300, state='readonly', fg_color="#ffeae0", bg_color='#ffeae0')
    genderBox.place(x=150,y=380)
    genderBox.set('')

    rightFrame = CTkFrame(Frame2, fg_color="#ffeae0", width=700, height=500)
    rightFrame.place(x=450, y=0)
    treeviewframe = CTkFrame(rightFrame, width=680, height=45)
    treeviewframe.grid(row=0, column=0, padx=(20,0), pady=(20,0))
    searchOptions2 = ['ID', 'Username', 'Email', 'Role', 'Gender']
    searchBox2= CTkComboBox(treeviewframe, values=searchOptions2, font=('yu gothic ui', 20), width=150, state='readonly')
    searchBox2.place(x=0, y=5)
    searchBox2.set('Search By')

    searchEntry2 = CTkEntry(treeviewframe, font=('yu gothic ui', 20), width=230)
    searchEntry2.place(x=150,y=5)

    searchButton2 = CTkButton(treeviewframe, text="Search", font=('yu gothic ui', 20), width=120, cursor='hand2', text_color='black', command= search_user)
    searchButton2.place(x=410,y=5)

    showButton2 = CTkButton(treeviewframe, text="Show All", font=('yu gothic ui', 20), width=120, cursor='hand2', text_color='black', command= showall2)
    showButton2.place(x=560,y=5)
    tree3=ttk.Treeview(rightFrame, height=10)
    tree3.grid(row=1, column=0, columnspan=4, sticky='nsew', padx=(20,0))
    tree3['columns'] = ('ID', 'Username', 'Password', 'Email', 'Role', 'Gender')
    tree3.heading('ID', text='User ID', anchor=CENTER)  
    tree3.heading('Username', text='Username', anchor=CENTER)
    tree3.heading('Password', text='Password', anchor=CENTER)
    tree3.heading('Email', text='Email', anchor=CENTER)
    tree3.heading('Role', text='Role', anchor=CENTER)
    tree3.heading('Gender', text='Gender', anchor=CENTER)
    tree3.config(show='headings')
    tree3.column('ID', width=100, anchor=CENTER)
    tree3.column('Username', width=100)
    tree3.column('Password', width=100)
    tree3.column('Email', width=100, anchor=CENTER)
    tree3.column('Role', width=150, anchor=CENTER)
    tree3.column('Gender', width=100, anchor=CENTER)
    scrollbar3=ttk.Scrollbar(rightFrame, orient="vertical", command=tree3.yview)
    scrollbar3.grid(row=1, column=4, sticky='ns')
    tree3.configure(yscrollcommand=scrollbar3.set)
    
    bottomframe2 = CTkFrame(Frame2, fg_color="#ffeae0", bg_color="#ffeae0", width=600, height=330)
    bottomframe2.place(x=500, y=280)
    addUserBtn = CTkButton(bottomframe2, text="Add", font=('yu gothic ui', 25), width=150, cursor='hand2', border_color="black", border_width=2, text_color="black", command=addUser)
    addUserBtn.place(x=130, y=30)
    deleteUserBtn = CTkButton(bottomframe2, text="Delete", font=('yu gothic ui', 25), width=150, cursor='hand2', border_color="black", border_width=2, text_color="black", command=deleteUser)
    deleteUserBtn.place(x=330, y=30)
    updateUserBtn = CTkButton(bottomframe2, text="Update", font=('yu gothic ui', 25), width=150, cursor='hand2', border_color="black", border_width=2, text_color="black", command=updateUser)
    updateUserBtn.place(x=130, y=100)
    deleteAllBtn = CTkButton(bottomframe2, text="Delete All", font=('yu gothic ui', 25), width=150, cursor='hand2', border_color="black", border_width=2, text_color="black", command=deleteAll)
    deleteAllBtn.place(x=330, y=100)
    clearBtn = CTkButton(bottomframe2, text="Clear", font=('yu gothic ui', 25), width=150, cursor='hand2', border_color="black", border_width=2, text_color="black", command= lambda: clear(True))
    clearBtn.place(x=230, y=170)

    treeview1_data()
    treeview2_data()
    treeview3_data()

    tree3.bind('<ButtonRelease-1>', selection)

    window.mainloop()

if __name__ == '__main__':
    page()