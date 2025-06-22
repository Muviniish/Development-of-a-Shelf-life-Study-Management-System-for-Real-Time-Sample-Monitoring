from customtkinter import *
import customtkinter as ctk
from tkinter import ttk

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
                         bg_color='#4a6ec0', cursor='hand2', fg_color='#4a6ec0', border_color="black", border_width=2)
    logoutBtn.place(x=950, y=25)
    Frame1 = CTkFrame(window, fg_color='#ffeae0', bg_color='#ffeae0', width=1166, height=638)
    Frame1.place(x=0, y=my_y)
    
    upperframe = CTkFrame(Frame1, fg_color='#ffeae0', bg_color='#ffeae0', width=1166, height=330)
    upperframe.place(x=0, y=0)
    label1= CTkLabel(upperframe, text="APPROVED PRODUCTS", fg_color="#ffeae0", bg_color='#ffeae0', font=('yu gothic ui', 22, 'bold'))
    label1.place(x=80, y=10)
    tree1frame = CTkFrame(upperframe, width=1000, height=40)
    tree1frame.place(x=80, y=37)
    searchOptions = ['ID', 'Username', 'Email', 'Role', 'Gender']
    searchBox= CTkComboBox(tree1frame, values=searchOptions, font=('yu gothic ui', 20), width=200, state='readonly')
    searchBox.place(x=0, y=2)
    searchBox.set('Search By')

    searchEntry = CTkEntry(tree1frame, font=('yu gothic ui', 20), width=300)
    searchEntry.place(x=220,y=2)

    searchButton = CTkButton(tree1frame, text="Search", font=('yu gothic ui', 20), width=150, cursor='hand2', text_color='black')
    searchButton.place(x=650,y=2)

    showButton = CTkButton(tree1frame, text="Show All", font=('yu gothic ui', 20), width=150, cursor='hand2', text_color='black')
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
    exportBtn = CTkButton(upperframe, text="Export to Excel File(.xlsx)", font=('yu gothic ui', 25), width=150, cursor='hand2', border_color="black", border_width=2, text_color="black")
    exportBtn.grid(row=1, column=1, padx=(220,0), pady=(10,0))

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
    scrollbar2=ttk.Scrollbar(bottomframe, orient="vertical", command=tree.yview)
    scrollbar2.grid(row=0, column=4, sticky='ns', pady=(30,0))
    tree2.configure(yscrollcommand=scrollbar2.set)
    style = ttk.Style()
    style.theme_use("clam")
    style.configure("Treeview.Heading", font=('Goudy Old Style',15,'bold'))
    style.configure("Treeview", font=('Goudy Old Style', 13, 'bold'), rowheight=15, background="gray17", foreground="white", fieldbackground="#FCD8CD")
    
    acceptBtn = CTkButton(bottomframe, text="ACCEPT", font=('yu gothic ui', 25), width=150, cursor='hand2', border_color="black", border_width=2, text_color="black")
    acceptBtn.grid(row=1, column=1, padx=(80,0))
    rejectBtn = CTkButton(bottomframe, text="REJECT", font=('yu gothic ui', 25), width=150, cursor='hand2', border_color="black", border_width=2, text_color="black")
    rejectBtn.grid(row=1, column=2)

    Frame2 = CTkFrame(window, fg_color='#FCD8CD', bg_color='#FCD8CD', width=1166, height=638)
    Frame2.place(x=0, y=80)
    label2= CTkLabel(Frame2, text="USER FORM", fg_color="#FCD8CD", bg_color='#FCD8CD', font=('yu gothic ui', 23, 'bold'))
    label2.place(x=80, y=10)
    labelLine = CTkCanvas(Frame2, width=450, height=2.0, bg="black")
    labelLine.place(x=0, y=40)
    leftFrame = CTkFrame(Frame2, fg_color="#FCD8CD", width=450, height=570)
    leftFrame.place(x=0, y=45)
    idLabel= CTkLabel(leftFrame, text="User ID     ->", fg_color="#FCD8CD", bg_color='#FCD8CD', font=('yu gothic ui', 23, 'bold'))
    idLabel.place(x=20, y=30)
    idEntry= CTkEntry(leftFrame, width=300, fg_color="#FCD8CD", bg_color='#FCD8CD', font=('yu gothic ui', 20, 'bold'))
    idEntry.place(x=150, y=30)
    nameLabel= CTkLabel(leftFrame, text="Username->", fg_color="#FCD8CD", bg_color='#FCD8CD', font=('yu gothic ui', 23, 'bold'))
    nameLabel.place(x=20, y=100)
    nameEntry= CTkEntry(leftFrame, width=300, fg_color="#FCD8CD", bg_color='#FCD8CD', font=('yu gothic ui', 20, 'bold'))
    nameEntry.place(x=150, y=100)
    passLabel= CTkLabel(leftFrame, text="Password ->", fg_color="#FCD8CD", bg_color='#FCD8CD', font=('yu gothic ui', 23, 'bold'))
    passLabel.place(x=20, y=170)
    passEntry= CTkEntry(leftFrame, width=300, fg_color="#FCD8CD", bg_color='#FCD8CD', font=('yu gothic ui', 20, 'bold'))
    passEntry.place(x=150, y=170)
    emailLabel= CTkLabel(leftFrame, text="Email        ->", fg_color="#FCD8CD", bg_color='#FCD8CD', font=('yu gothic ui', 23, 'bold'))
    emailLabel.place(x=20, y=240)
    emailEntry= CTkEntry(leftFrame, width=300, fg_color="#FCD8CD", bg_color='#FCD8CD', font=('yu gothic ui', 20, 'bold'))
    emailEntry.place(x=150, y=240)
    roleLabel= CTkLabel(leftFrame, text="Role          ->", fg_color="#FCD8CD", bg_color='#FCD8CD', font=('yu gothic ui', 23, 'bold'))
    roleLabel.place(x=20, y=310)
    roleOptions = ['Senior R&D Lab Tester','Product Developer','NPI Engineer','Global Product Launch Manager','Pharmacist','Technician']
    roleBox= CTkComboBox(leftFrame, values=roleOptions, font=('yu gothic ui', 20, 'bold'), width=300, state='readonly', fg_color="#FCD8CD", bg_color='#FCD8CD')
    roleBox.place(x=150, y=310)
    roleBox.set('')
    genderLabel= CTkLabel(leftFrame, text="Gender     ->", fg_color="#FCD8CD", bg_color='#FCD8CD', font=('yu gothic ui', 23, 'bold'))
    genderLabel.place(x=20, y=380)
    genderOptions = ['Male', 'Female']
    genderBox= CTkComboBox(leftFrame, values=genderOptions, font=('yu gothic ui', 20, 'bold'), width=300, state='readonly', fg_color="#FCD8CD", bg_color='#FCD8CD')
    genderBox.place(x=150,y=380)
    genderBox.set('')

    rightFrame = CTkFrame(Frame2, fg_color="#FCD8CD", width=700, height=500)
    rightFrame.place(x=450, y=0)
    treeviewframe = CTkFrame(rightFrame, width=680, height=45)
    treeviewframe.grid(row=0, column=0, padx=(20,0), pady=(20,0))
    searchOptions = ['ID', 'Username', 'Email', 'Role', 'Gender']
    searchBox2= CTkComboBox(treeviewframe, values=searchOptions, font=('yu gothic ui', 20), width=150, state='readonly')
    searchBox2.place(x=0, y=5)
    searchBox2.set('Search By')

    searchEntry2 = CTkEntry(treeviewframe, font=('yu gothic ui', 20), width=230)
    searchEntry2.place(x=150,y=5)

    searchButton2 = CTkButton(treeviewframe, text="Search", font=('yu gothic ui', 20), width=120, cursor='hand2', text_color='black')
    searchButton2.place(x=410,y=5)

    showButton2 = CTkButton(treeviewframe, text="Show All", font=('yu gothic ui', 20), width=120, cursor='hand2', text_color='black')
    showButton2.place(x=560,y=5)
    tree3=ttk.Treeview(rightFrame, height=10)
    tree3.grid(row=1, column=0, columnspan=4, sticky='nsew', padx=(20,0))
    tree3['columns'] = ('ID', 'Username', 'Email', 'Role', 'Gender')
    tree3.heading('ID', text='User ID', anchor=CENTER)  
    tree3.heading('Username', text='Username', anchor=CENTER)
    tree3.heading('Email', text='Email', anchor=CENTER)
    tree3.heading('Role', text='Role', anchor=CENTER)
    tree3.heading('Gender', text='Gender', anchor=CENTER)
    tree3.config(show='headings')
    tree3.column('ID', width=100, anchor=CENTER)
    tree3.column('Username', width=120)
    tree3.column('Email', width=120, anchor=CENTER)
    tree3.column('Role', width=150, anchor=CENTER)
    tree3.column('Gender', width=100, anchor=CENTER)
    scrollbar3=ttk.Scrollbar(rightFrame, orient="vertical", command=tree.yview)
    scrollbar3.grid(row=1, column=4, sticky='ns')
    tree3.configure(yscrollcommand=scrollbar3.set)
    
    bottomframe2 = CTkFrame(Frame2, fg_color="#FCD8CD", bg_color="#FCD8CD", width=600, height=330)
    bottomframe2.place(x=500, y=280)
    acceptBtn = CTkButton(bottomframe2, text="Add", font=('yu gothic ui', 25), width=150, cursor='hand2', border_color="black", border_width=2, text_color="black")
    acceptBtn.place(x=130, y=30)
    rejectBtn = CTkButton(bottomframe2, text="Delete", font=('yu gothic ui', 25), width=150, cursor='hand2', border_color="black", border_width=2, text_color="black")
    rejectBtn.place(x=330, y=30)
    acceptBtn = CTkButton(bottomframe2, text="Update", font=('yu gothic ui', 25), width=150, cursor='hand2', border_color="black", border_width=2, text_color="black")
    acceptBtn.place(x=130, y=100)
    rejectBtn = CTkButton(bottomframe2, text="Delete All", font=('yu gothic ui', 25), width=150, cursor='hand2', border_color="black", border_width=2, text_color="black")
    rejectBtn.place(x=330, y=100)
    acceptBtn = CTkButton(bottomframe2, text="Clear", font=('yu gothic ui', 25), width=150, cursor='hand2', border_color="black", border_width=2, text_color="black")
    acceptBtn.place(x=230, y=170)

    window.mainloop()

if __name__ == '__main__':
    page()