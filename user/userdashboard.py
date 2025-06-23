from customtkinter import *
from tkinter import ttk, messagebox, simpledialog
import sys, re
sys.path.append('.')
from admin import pendingproduct_database
import login
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

class LoginForm:
    def __init__(self, window):
        self.window = window
        self.window.geometry('1166x718')
        self.window.state('zoomed')
        self.window.resizable(0, 0)


def page():
    def logout():
        result = messagebox.askyesno('Confirm','Do you really want to log out?', icon='warning')
        if result:
            window.destroy()
            login.page()
        else:
            pass

    def validate_email(email):
        if re.fullmatch(regex, email):
            return True
        else:
            return False
        
    def treeview_data():
        searched_emails = pendingproduct_database.search(email)
        tree.delete(*tree.get_children())
        for product in searched_emails:
            tree.insert('', END, values=product)

    def pop():
        global email
        email = simpledialog.askstring("Input Required", "Enter your email:")
        
        if email:
            if not validate_email(email):
                messagebox.showerror("Error", "Invalid email format")
                pop()
            else:
                treeview_data()
        else:
            messagebox.showwarning("No Input", "Please retry.")
            window.destroy()
    window = CTk()
    LoginForm(window)
    window.after(100,pop)
    Frame = CTkFrame(window, fg_color='#4abdc0', bg_color='#4abdc0', width=1166, height=80)
    Frame.place(x=0, y=0)
    logoutBtn = CTkButton(Frame, text="Log Out", text_color="black",  font=('yu gothic ui', 20, 'bold'), width=150,
                         bg_color='#4a6ec0', cursor='hand2', fg_color='#4a6ec0', border_color="black", border_width=2, command=logout)
    logoutBtn.place(x=950, y=25)
    
    Frame2 = CTkFrame(window, fg_color='#FCD8CD', bg_color='#FCD8CD', width=1166, height=638)
    Frame2.place(x=0, y=80)
    label2= CTkLabel(Frame2, text="PRODUCT FORM", fg_color="#FCD8CD", bg_color='#FCD8CD', font=('yu gothic ui', 23, 'bold'))
    label2.place(x=80, y=290)
    labelLine = CTkCanvas(Frame2, width=1166, height=2.0, bg='black')
    labelLine.place(x=0, y=330)
    bottomFrame = CTkFrame(Frame2, fg_color="#FCD8CD", width=1166, height=250)
    bottomFrame.place(x=0, y=350)
    idLabel= CTkLabel(bottomFrame, text="Product ID       ->", fg_color="#FCD8CD", bg_color='#FCD8CD', font=('yu gothic ui', 23, 'bold'))
    idLabel.place(x=80, y=30)
    idEntry= CTkEntry(bottomFrame, width=300, fg_color="#FCD8CD", bg_color='#FCD8CD', font=('yu gothic ui', 20, 'bold'))
    idEntry.place(x=260, y=30)
    nameLabel= CTkLabel(bottomFrame, text="Product Name ->", fg_color="#FCD8CD", bg_color='#FCD8CD', font=('yu gothic ui', 23, 'bold'))
    nameLabel.place(x=80, y=100)
    nameEntry= CTkEntry(bottomFrame, width=300, fg_color="#FCD8CD", bg_color='#FCD8CD', font=('yu gothic ui', 20, 'bold'))
    nameEntry.place(x=260, y=100)
    descLabel= CTkLabel(bottomFrame, text="Description      ->", fg_color="#FCD8CD", bg_color='#FCD8CD', font=('yu gothic ui', 23, 'bold'))
    descLabel.place(x=80, y=170)
    descEntry= CTkEntry(bottomFrame, width=300, fg_color="#FCD8CD", bg_color='#FCD8CD', font=('yu gothic ui', 20, 'bold'))
    descEntry.place(x=260, y=170)
    quanLabel= CTkLabel(bottomFrame, text="Quantity   ->", fg_color="#FCD8CD", bg_color='#FCD8CD', font=('yu gothic ui', 23, 'bold'))
    quanLabel.place(x=650, y=65)
    quanEntry= CTkEntry(bottomFrame, width=300, fg_color="#FCD8CD", bg_color='#FCD8CD', font=('yu gothic ui', 20, 'bold'))
    quanEntry.place(x=780, y=65)
    testLabel= CTkLabel(bottomFrame, text="Test Date  ->", fg_color="#FCD8CD", bg_color='#FCD8CD', font=('yu gothic ui', 23, 'bold'))
    testLabel.place(x=650, y=135)
    testEntry= CTkEntry(bottomFrame, width=300, fg_color="#FCD8CD", bg_color='#FCD8CD', font=('yu gothic ui', 20, 'bold'))
    testEntry.place(x=780, y=135)

    topFrame = CTkFrame(Frame2, fg_color="#FCD8CD", width=700, height=400)
    topFrame.place(x=60, y=0)
    tree=ttk.Treeview(topFrame, height=10)
    tree.grid(row=1, column=0, columnspan=4, sticky='nsew')
    tree['columns'] = ('ID', 'Name', 'Description', 'Quantity', 'Email', 'Date','Status')
    tree.heading('ID', text='Product ID', anchor=CENTER)  
    tree.heading('Name', text='Product Name', anchor=CENTER)
    tree.heading('Description', text='Description', anchor=CENTER)
    tree.heading('Quantity', text='Quantity', anchor=CENTER)
    tree.heading('Email', text='Email', anchor=CENTER)
    tree.heading('Date', text='Test Date', anchor=CENTER)
    tree.heading('Status', text='Approval Status', anchor=CENTER)
    tree.config(show='headings')
    tree.column('ID', width=130, anchor=CENTER)
    tree.column('Name', width=150)
    tree.column('Description', width=150, anchor=CENTER)
    tree.column('Quantity', width=100, anchor=CENTER)
    tree.column('Email', width=150, anchor=CENTER)
    tree.column('Date', width=145, anchor=CENTER)
    tree.column('Status', width=170, anchor=CENTER)
    scrollbar=ttk.Scrollbar(topFrame, orient="vertical", command=tree.yview)
    scrollbar.grid(row=1, column=4, sticky='ns')
    tree.configure(yscrollcommand=scrollbar.set)
    style = ttk.Style()
    style.theme_use("clam")
    style.configure("Treeview.Heading", font=('Goudy Old Style',15,'bold'))
    style.configure("Treeview", font=('Goudy Old Style', 9, 'bold'), rowheight=15, background="gray17", foreground="white", fieldbackground="#FCD8CD")

    def add():
        if idEntry.get() == "" or nameEntry.get() == "" or descEntry.get() == "" or quanEntry.get() == "" or testEntry.get() == "":
            messagebox.showerror("Error", "All fields are required")
        elif pendingproduct_database.id_exists(idEntry.get()):
            messagebox.showerror("Error", "Product ID already exists")
        else:
            id = idEntry.get()
            pendingproduct_database.insert(id, nameEntry.get(), descEntry.get(), quanEntry.get(), email, testEntry.get(), "Pending")
            treeview_data()
            clear()
            messagebox.showinfo("Success", "Product added successfully")
                
    def delete():
        selected_item = tree.selection()
        if not selected_item:
            messagebox.showerror("Error", "Select data to delete")
        else:
            item = tree.item(selected_item)
            if item['values'][6]=="Approved":
                messagebox.showerror("Error", "Unable to delete approved product.")
            else:
                pendingproduct_database.delete(idEntry.get(), email)
                messagebox.showinfo("Success", "Product deleted successfully")
            treeview_data()
            clear()

    def update():
        selected_item = tree.selection()
        if not selected_item:
            messagebox.showerror("Error", "Select data to update")
        else:
            item = tree.item(selected_item)
            status= item['values'][6]
            if status=="Pending":
                pendingproduct_database.update(idEntry.get(), nameEntry.get(), descEntry.get(), quanEntry.get(), email, testEntry.get(), status)
                messagebox.showinfo("Success", "Product updated successfully")
            else:
                messagebox.showerror("Error", "Unable to update approved or rejected product. Please add the product again.")
            treeview_data()
            clear()

    def deleteAll():
        result = messagebox.askyesno('Confirm','Do you really want to delete all products?', icon='warning')
        if result:
            pendingproduct_database.delete_all(email)
        else:
            pass
        treeview_data()
        clear()

    def clear(value=False):
        if value:
            tree.selection_remove(tree.focus())
        idEntry.delete(0, END)
        nameEntry.delete(0, END)
        descEntry.delete(0, END)
        quanEntry.delete(0, END)
        testEntry.delete(0, END)

    def selection(event):
        selected_item = tree.selection()
        if selected_item:
            item = tree.item(selected_item)
            clear()
            idEntry.insert(0, item['values'][0])
            nameEntry.insert(0, item['values'][1])
            descEntry.insert(0, item['values'][2])
            quanEntry.insert(0, item['values'][3])
            testEntry.insert(0, item['values'][5])
    
    bottomFrame = CTkFrame(Frame2, fg_color="#FCD8CD", bg_color="#FCD8CD", width=1100, height=80)
    bottomFrame.place(x=30, y=195)
    addBtn = CTkButton(bottomFrame, text="Add", font=('yu gothic ui', 25), width=150, cursor='hand2', border_color="black", border_width=2, text_color="black", command=add)
    addBtn.place(x=65, y=20)
    deleteBtn = CTkButton(bottomFrame, text="Delete", font=('yu gothic ui', 25), width=150, cursor='hand2', border_color="black", border_width=2, text_color="black", command=delete)
    deleteBtn.place(x=265, y=20)
    updateBtn = CTkButton(bottomFrame, text="Update", font=('yu gothic ui', 25), width=150, cursor='hand2', border_color="black", border_width=2, text_color="black", command=update)
    updateBtn.place(x=465, y=20)
    deleteallBtn = CTkButton(bottomFrame, text="Delete All", font=('yu gothic ui', 25), width=150, cursor='hand2', border_color="black", border_width=2, text_color="black",command=deleteAll)
    deleteallBtn.place(x=665, y=20)
    clearBtn = CTkButton(bottomFrame, text="Clear", font=('yu gothic ui', 25), width=150, cursor='hand2', border_color="black", border_width=2, text_color="black", command=lambda:clear(True))
    clearBtn.place(x=865, y=20)

    treeview_data
    tree.bind('<ButtonRelease-1>', selection)

    window.mainloop()

if __name__ == '__main__':
    page()