from customtkinter import *
from tkinter import ttk, messagebox
import sys, re, os
sys.path.append('.')
from admin import pendingproduct_database
import login
from tester import tester_database
from  datetime import datetime

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

class LoginForm:
    def __init__(self, window):
        self.window = window
        self.window.geometry('1166x718')
        self.window.state('zoomed')
        self.window.resizable(0, 0)

def has_run_today(log_file='log/last_run.txt'):
    today = datetime.now().strftime('%Y-%m-%d')
    if os.path.exists(log_file):
        with open(log_file, 'r') as file:
            last_run = file.read().strip()
            return last_run == today
    return False

def mark_as_run(log_file='log/last_run.txt'):
    today = datetime.now().strftime('%Y-%m-%d')
    os.makedirs(os.path.dirname(log_file), exist_ok=True)
    with open(log_file, 'w') as file:
        file.write(today)

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
        searched_emails = pendingproduct_database.search2()
        tree.delete(*tree.get_children())
        for product in searched_emails:
            tree.insert('', END, values=product)

    def treeview_data2():
        searched_emails = tester_database.search()
        tree2.delete(*tree2.get_children())
        for product in searched_emails:
            tree2.insert('', END, values=product)

    window = CTk()
    LoginForm(window)
    Frame = CTkFrame(window, fg_color='#4abdc0', bg_color='#4abdc0', width=1166, height=80)
    Frame.place(x=0, y=0)
    logoutBtn = CTkButton(Frame, text="Log Out", text_color="black",  font=('yu gothic ui', 20, 'bold'), width=150,
                         bg_color='#4a6ec0', cursor='hand2', fg_color='#4a6ec0', border_color="black", border_width=2, command=logout)
    logoutBtn.place(x=950, y=25)
    Frame2 = CTkFrame(window, fg_color='#FCD8CD', bg_color='#FCD8CD', width=1166, height=638)
    Frame2.place(x=0, y=80)
    label2= CTkLabel(Frame2, text="TESTER FORM", fg_color="#FCD8CD", bg_color='#FCD8CD', font=('yu gothic ui', 23, 'bold'))
    label2.place(x=80, y=285)
    labelLine = CTkCanvas(Frame2, width=570, height=2.0, bg='black')
    labelLine.place(x=0, y=320)
    bottomFrame = CTkFrame(Frame2, fg_color="#FCD8CD", width=570, height=300)
    bottomFrame.place(x=0, y=330)
    idLabel= CTkLabel(bottomFrame, text="Product ID       ->", fg_color="#FCD8CD", bg_color='#FCD8CD', font=('yu gothic ui', 23, 'bold'))
    idLabel.place(x=80, y=10)
    idEntry= CTkEntry(bottomFrame, width=300, fg_color="#FCD8CD", bg_color='#FCD8CD', font=('yu gothic ui', 20, 'bold'))
    idEntry.place(x=260, y=10)
    startLabel= CTkLabel(bottomFrame, text="Test Start         ->", fg_color="#FCD8CD", bg_color='#FCD8CD', font=('yu gothic ui', 23, 'bold'))
    startLabel.place(x=80, y=80)
    startEntry= CTkEntry(bottomFrame, width=300, fg_color="#FCD8CD", bg_color='#FCD8CD', font=('yu gothic ui', 20, 'bold'))
    startEntry.place(x=260, y=80)
    endLabel= CTkLabel(bottomFrame, text="Test End           ->", fg_color="#FCD8CD", bg_color='#FCD8CD', font=('yu gothic ui', 23, 'bold'))
    endLabel.place(x=80, y=150)
    endEntry= CTkEntry(bottomFrame, width=300, fg_color="#FCD8CD", bg_color='#FCD8CD', font=('yu gothic ui', 20, 'bold'))
    endEntry.place(x=260, y=150)
    statusLabel= CTkLabel(bottomFrame, text="Status       ->", fg_color="#FCD8CD", bg_color='#FCD8CD', font=('yu gothic ui', 23, 'bold'))
    statusLabel.place(x=80, y=220)
    statusOptions = ['Complete', 'Incomplete']
    statusBox= CTkComboBox(bottomFrame, values=statusOptions, font=('yu gothic ui', 20, 'bold'), width=300, state='readonly', fg_color="#FCD8CD", bg_color='#ffeae0')
    statusBox.place(x=260,y=220)
    statusBox.set('')

    def search_user():
        if searchBox2.get() == "Search By":
            messagebox.showerror("Error", "Please select a search option")
        elif searchEntry2.get() == "":
            messagebox.showerror("Error", "Please enter a search term")
        else:

            searched_users = tester_database.search3(searchBox2.get(), searchEntry2.get())
            tree2.delete(*tree2.get_children())
            for user in searched_users:
                tree2.insert('', END, values=user)

    def showall2():
        treeview_data2()
        searchEntry2.delete(0, END)
        searchBox2.set('Search By')

    smalFrame = CTkFrame(Frame2, fg_color="#FCD8CD", width=700, height=400)
    smalFrame.place(x=570, y=312)
    treeviewframe = CTkFrame(smalFrame, width=580, height=35)
    treeviewframe.grid(row=0, column=0)

    searchOptions2 = ['ID', 'Tester_Email']
    searchBox2= CTkComboBox(treeviewframe, values=searchOptions2, font=('yu gothic ui', 15), width=120, state='readonly')
    searchBox2.place(x=8, y=4)
    searchBox2.set('Search By')

    searchEntry2 = CTkEntry(treeviewframe, font=('yu gothic ui', 15), width=180)
    searchEntry2.place(x=130,y=4)

    searchButton2 = CTkButton(treeviewframe, text="Search", font=('yu gothic ui', 15), width=100, cursor='hand2', text_color='black', command= search_user)
    searchButton2.place(x=350,y=4)

    showButton2 = CTkButton(treeviewframe, text="Show All", font=('yu gothic ui', 15), width=100, cursor='hand2', text_color='black', command= showall2)
    showButton2.place(x=470,y=4)

    tree2=ttk.Treeview(smalFrame, height=10)
    tree2.grid(row=1, column=0, columnspan=4, sticky='nsew')
    tree2['columns'] = ('ID', 'Start', 'End', 'Status', 'tester_Email', 'owner_Email')
    tree2.heading('ID', text='Product ID', anchor=CENTER)  
    tree2.heading('Start', text='Start Date', anchor=CENTER)
    tree2.heading('End', text='End Date', anchor=CENTER)
    tree2.heading('Status', text='Status', anchor=CENTER)
    tree2.heading('tester_Email', text='Tester Email', anchor=CENTER)
    tree2.heading('owner_Email', text='Owner Email', anchor=CENTER)
    tree2.config(show='headings')
    tree2.column('ID', width=90, anchor=CENTER)
    tree2.column('Start', width=98)
    tree2.column('End', width=98, anchor=CENTER)
    tree2.column('Status', width=80, anchor=CENTER)
    tree2.column('tester_Email', width=102, anchor=CENTER)
    tree2.column('owner_Email', width=102, anchor=CENTER)
    scrollbar2=ttk.Scrollbar(smalFrame, orient="vertical", command=tree2.yview)
    scrollbar2.grid(row=1, column=4, sticky='ns')
    tree2.configure(yscrollcommand=scrollbar2.set)

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
    style.configure("Treeview.Heading", font=('Goudy Old Style',12,'bold'))
    style.configure("Treeview", font=('Goudy Old Style', 9, 'bold'), rowheight=15, background="gray17", foreground="white", fieldbackground="#FCD8CD")

    def add():
        selected_item = tree.selection()
        if not selected_item:
            messagebox.showerror("Error", "Select a product to add")
        else:
            item = tree.item(selected_item)
            id=item['values'][0]
            start=item['values'][5]
            owner=item['values'][4]
            status="Incomplete"
            email= emailEntry.get()
            if email == "":
                messagebox.showerror("Error", "Please enter tester email to assign")
            elif tester_database.id_exists(id):
                messagebox.showerror("Error", "Product ID already exists")
            else:
                if not validate_email(email):
                    messagebox.showerror("Error", "Invalid email format")
                else:
                    tester_database.insert(id, start, status, email, owner)
                    treeview_data2()
                    clear()
                    messagebox.showinfo("Success", "Product added successfully")

    def clear(value=False):
        if value:
            tree.selection_remove(tree.focus())
            tree2.selection_remove(tree2.focus())
        emailEntry.delete(0, END)
        idEntry.delete(0, END)
        startEntry.delete(0, END)
        endEntry.delete(0, END)
        statusBox.set('')

    def update():
        selected_item = tree2.selection()
        if not selected_item:
            messagebox.showerror("Error", "Select data to update")
        else:
            tester_database.update(idEntry.get(), emailEntry.get(), startEntry.get(), endEntry.get(),statusBox.get())
            messagebox.showinfo("Success", "Product updated successfully")
            treeview_data2()
            clear()
        
    def selection(event):
        selected_item = tree2.selection()
        if selected_item:
            item = tree2.item(selected_item)
            clear()
            emailEntry.insert(0, item['values'][4])
            idEntry.insert(0, item['values'][0])
            startEntry.insert(0, item['values'][1])
            endEntry.insert(0, item['values'][2])
            statusBox.set(item['values'][3])
    
    bottomFrame2 = CTkFrame(Frame2, fg_color="#FCD8CD", bg_color="#FCD8CD", width=1100, height=80)
    bottomFrame2.place(x=30, y=195)
    emailLabel= CTkLabel(bottomFrame2, text="Tester Email     ->", fg_color="#FCD8CD", bg_color='#FCD8CD', font=('yu gothic ui', 23, 'bold'))
    emailLabel.place(x=50, y=25)
    emailEntry= CTkEntry(bottomFrame2, width=300, fg_color="#FCD8CD", bg_color='#FCD8CD', font=('yu gothic ui', 20, 'bold'))
    emailEntry.place(x=230, y=25)
    addBtn = CTkButton(bottomFrame2, text="Assign", font=('yu gothic ui', 25), width=150, cursor='hand2', border_color="black", border_width=2, text_color="black", command=add)
    addBtn.place(x=740, y=20)
    clearBtn = CTkButton(Frame2, text="Clear", font=('yu gothic ui', 25), width=150, cursor='hand2', border_color="black", border_width=2, text_color="black", command=lambda:clear(True))
    clearBtn.place(x=880, y=550)
    updateBtn = CTkButton(Frame2, text="Update", font=('yu gothic ui', 25), width=150, cursor='hand2', border_color="black", border_width=2, text_color="black", command=update)
    updateBtn.place(x=680, y=550)

    

    treeview_data()
    treeview_data2()
    tree2.bind('<ButtonRelease-1>', selection)

    window.mainloop()

if __name__ == '__main__':
    if not has_run_today():
        tester_database.search2()
        mark_as_run()
    page()