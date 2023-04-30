from PIL import Image
import customtkinter as ck
from tkinter import ttk
from customtkinter import CTkImage,CTkFont,CTkButton,CTkTabview,CTkEntry,CTkLabel
from datetime import date, timedelta
import tkinter as tk
import pandas as pd
import sqlite3




class App:
    def __init__(self,window):
        self.window = window
        self.window.title("LMS Database")
        self.window.geometry("1400x1200")
        self.window.iconbitmap("icons/bookshelf.ico")
        # self.window.resizable(False,False)
        self.create_into_frame()

    
    # creates the intro frame
    def create_into_frame(self):
        self.into_frame = ck.CTkFrame(master=self.window)
        self.into_frame.pack(fill='both', expand=True)

        # adds the image at the top of the frame
        lib_png = CTkImage(dark_image=Image.open("icons/bookshelf.png"),size=(650,700))
        lib_label = CTkLabel(master=self.into_frame,image=lib_png, text="")
        lib_label.pack(pady=30)

        # adds the title text under the img
        title_font = CTkFont(family='Helvetica',size=32,weight='bold')
        intro_label = CTkLabel(master=self.into_frame,text="Welcome to LMS Database",font=title_font)
        intro_label.pack(pady=30)

        # adds the button to go to next frame
        button_font = CTkFont(family='Helvetica',size=24)
        get_started = CTkButton(master=self.into_frame,text="Get Started",fg_color="#0077b6",
                                width=60,height=50,corner_radius=20,font=button_font,command = self.home_screen)
        get_started.pack(pady=30)


    def home_screen(self):
        self.into_frame.pack_forget()
        self.home_frame = ck.CTkFrame(master=self.window)
        self.home_frame.pack(fill='both', expand=True)

        self.tabview = CTkTabview(master=self.home_frame,width=1200,height=1000)
        
        self.tab_view()

        button_font = CTkFont(family='Helvetica',size=24)
        go_back_button = CTkButton(master=self.home_frame, text="Back",fg_color="#0077b6",
                                    width=60,height=50,corner_radius=20,font=button_font,command=self.go_back_into)
        go_back_button.place(x = 20, y = 1175, anchor=tk.SW)
            
    def tab_view(self):
        tab_font = CTkFont(family='Helvetica',size=32)
        self.tabview.add("Book Checkout")

        name_label = CTkLabel(master=self.tabview.tab("Book Checkout"),text="Borrower Name:",font=tab_font)
        name_label.place(relx=0.05,rely=0.05,anchor=tk.W)
        self.name_input = CTkEntry(master=self.tabview.tab("Book Checkout"),placeholder_text="Name",width=450,height=60,corner_radius=15)
        self.name_input.place(relx=0.25,rely=0.05,anchor=tk.W)

        book_label = CTkLabel(master=self.tabview.tab("Book Checkout"),text="Book Title:",font=tab_font)
        book_label.place(relx=0.12,rely=0.15,anchor=tk.W)
        self.book_input = CTkEntry(master=self.tabview.tab("Book Checkout"),placeholder_text="Title",width=450,height=60,corner_radius=15)
        self.book_input.place(relx=0.25,rely=0.15,anchor=tk.W)

        button_font = CTkFont(family='Helvetica',size=20)
        checkout_submit_button = CTkButton(master=self.tabview.tab("Book Checkout"),text="Submit",fg_color="#0077b6",
                                    width=50,height=40,corner_radius=20,font=button_font,command=self.checkout_query)
        checkout_submit_button.place(relx=0.97,rely=0.97,anchor=tk.SE)

        print_query = CTkButton(master=self.tabview.tab("Book Checkout"),text="Print",fg_color="#0077b6",
                                    width=50,height=40,corner_radius=20,font=button_font,command=self.print_query)
        print_query.place(relx=0.03,rely=0.97,anchor=tk.SW)


        self.tabview.add("Query 2")
        label2 = CTkLabel(master=self.tabview.tab("Query 2"),text="Tab2")
        label2.pack()
        self.tabview.pack()

    def checkout_query(self):
        checkout_conn = sqlite3.connect('Database_copy.db')
        checkout_cur = checkout_conn.cursor()

        # Retrieve card_no from BORROWER table based on entered name
        name = self.name_input.get()
        title = self.book_input.get()
        today = date.today()
        month = today + timedelta(days=30)
        checkout_cur.execute(f"""
                            INSERT INTO BOOK_LOANS(book_id,branch_id,card_no,date_out,due_date,Late)
                            SELECT b.book_id,bc.branch_id,bo.card_no,'{today}','{month}',0
                            FROM BORROWER bo, BOOK b, BOOK_COPIES bc
                            WHERE b.title ='{title}' AND bo.name = '{name}' AND b.book_id = bc.book_id;""")
        
        checkout_cur.execute(f"""
                            UPDATE BOOK_COPIES
                            SET no_of_copies = no_of_copies -1
                            WHERE book_id IN (
                                            SELECT book_id
                                            FROM BOOK
                                            WHERE title = '{title}');""")
        
        # df = pd.read_sql_query("SELECT DISTINCT bo.title bc.no_of_copies FROM ",checkout_conn)

        checkout_conn.commit()
        checkout_conn.close()

    def print_query(self):
        checkout_conn = sqlite3.connect('Database_copy.db')
        checkout_cur = checkout_conn.cursor()

        checkout_cur.execute("SELECT * FROM BOOK_COPIES")

        output = checkout_cur.fetchall()

        print_record = ""
        print_record += "book_id"+"\t\t"+"branch_id"+"\t\t"+"no_of_copies"+"\n\n"

        for row in output:
            print_record += str(row[0]) + "\t\t" + str(row[1]) + "\t\t" + str(row[2]) + "\n"

        print_font = CTkFont(family='Helvetica',size=18)
        print_label = CTkLabel(self.tabview.tab("Book Checkout"),text=print_record,font=print_font)
        print_label.place(relx=0.50,rely=0.50,anchor=tk.CENTER)

        # df = pd.read_sql_query("SELECT * FROM BOOK_COPIES",checkout_conn)
        # label = CTkLabel(master=self.tabview,text=df)

        # label.place(relx=0.50,rely=0.60,anchor=tk.CENTER)

        checkout_conn.commit()
        checkout_conn.close()




    def go_back_into(self):
        self.home_frame.pack_forget()
        self.create_into_frame()



    def run(self):
        self.window.mainloop()


# import tkinter as tk
# from ctk import CTk, CTkLabel, CTkEntry, CTkButton, CTKTreeview
# import sqlite3
# import pandas as pd

# class Library(CTk):
#     def __init__(self):
#         super().__init__()

#         self.tabview = self.add_tab('Checkout')

#         self.name_label = CTkLabel(master=self.tabview,text='Name')
#         self.name_label.place(relx=0.15,rely=0.15,anchor=tk.W)
#         self.name_input = CTkEntry(master=self.tabview)
#         self.name_input.place(relx=0.25,rely=0.15,anchor=tk.W)

#         self.book_label = CTkLabel(master=self.tabview,text='Book Title')
#         self.book_label.place(relx=0.15,rely=0.25,anchor=tk.W)
#         self.book_input = CTkEntry(master=self.tabview)
#         self.book_input.place(relx=0.25,rely=0.25,anchor=tk.W)

#         self.checkout_button = CTkButton(master=self.tabview,text='Checkout',command=self.checkout_query)
#         self.checkout_button.place(relx=0.15,rely=0.3,anchor=tk.W)

#         self.treeview = CTKTreeview(master=self.tabview, columns=('ID', 'Book ID', 'Card No', 'Date Out', 'Due Date', 'Late'))
#         self.treeview.place(relx=0.1, rely=0.4, anchor=tk.W)

#     def checkout_query(self):
#         checkout_conn = sqlite3.connect('Database_copy.db')
#         checkout_cur = checkout_conn.cursor()

#         # Retrieve card_no from BORROWER table based on entered name
#         name = self.name_input.get()
#         title = self.book_input.get()
#         today = date.today()
#         week = today + timedelta(days=7)
#         checkout_cur.execute(f"""
#                             INSERT INTO BOOK_LOANS(book_id,card_no,date_out,due_date,Late)
#                             SELECT b.book_id,bo.card_no,'{today}','{week}',0
#                             FROM BORROWER bo, BOOK b
#                             WHERE b.title ='{title}' AND bo.name = '{name}';""")
        
#         checkout_cur.execute(f"""
#                             UPDATE BOOK_COPIES
#                             SET no_of_copies = no_of_copies -1
#                             WHERE book_id IN (
#                                             SELECT book_id
#                                             FROM BOOK
#                                             WHERE title = '{title}');""")
        
#         checkout_conn.commit()

#         # Retrieve BOOK_LOANS table from database
#         df = pd.read_sql_query("SELECT * FROM BOOK_LOANS", checkout_conn)

#         # Update treeview with BOOK_LOANS data
#         self.treeview.delete(*self.treeview.get_children())
#         for index, row in df.iterrows():
#             self.treeview.insert('', tk.END, values=row)

#         checkout_conn.close()

# app = Library()
# app.mainloop()
