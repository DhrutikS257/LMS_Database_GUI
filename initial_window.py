from PIL import Image
import customtkinter as ck
from tkinter import ttk
from customtkinter import CTkImage,CTkFont,CTkButton,CTkTabview,CTkEntry,CTkLabel
from datetime import date, timedelta
import tkinter as tk
import pandas as pd
from prettytable import PrettyTable
from prettytable import from_db_cursor
import sqlite3




class App:
    def __init__(self,window):
        self.window = window
        self.window.title("LMS Database")
        self.window.geometry("800x600")
        self.window.iconbitmap("icons/bookshelf.ico")
        # self.window.resizable(False,False)
        self.create_into_frame()

    
    # creates the intro frame
    def create_into_frame(self):
        self.into_frame = ck.CTkFrame(master=self.window)
        self.into_frame.pack(fill='both', expand=True)

        # adds the image at the top of the frame
        lib_png = CTkImage(dark_image=Image.open("icons/bookshelf.png"),size=(250,300))
        lib_label = CTkLabel(master=self.into_frame,image=lib_png, text="")
        lib_label.pack(pady=30)

        # adds the title text under the img
        title_font = CTkFont(family='Helvetica',size=20,weight='bold')
        intro_label = CTkLabel(master=self.into_frame,text="Welcome to LMS Database",font=title_font)
        intro_label.pack(pady=30)

        # adds the button to go to next frame
        button_font = CTkFont(family='Helvetica',size=16)
        get_started = CTkButton(master=self.into_frame,text="Get Started",fg_color="#0077b6",
                                width=60,height=50,corner_radius=20,font=button_font,command = self.home_screen)
        get_started.pack(pady=30)


    def home_screen(self):
        self.into_frame.pack_forget()
        self.home_frame = ck.CTkFrame(master=self.window)
        self.home_frame.pack(fill='both', expand=True)

        self.tabview = CTkTabview(master=self.home_frame,width=600,height=500)
        
        self.tab_view()

        # back button
        button_font = CTkFont(family='Helvetica',size=24)
        go_back_button = CTkButton(master=self.home_frame, text="Back",fg_color="#0077b6",
                                    width=30,height=25,corner_radius=20,font=button_font,command=self.go_back_into)
        go_back_button.place(x = 20, y = 575, anchor=tk.SW)
            
    def tab_view(self):
        tab_font = CTkFont(family='Helvetica',size=18)
        self.tabview.add("Book Checkout")
        self.tabview.add("Add Borrower")
        self.tabview.add("New Book")
        self.tabview.add("List Book Copies")
        self.tabview.add("Late Return")
        self.tabview.add("Late Fee")
        self.tabview.add("Book Information")



        # name input for book checkout
        name_label = CTkLabel(master=self.tabview.tab("Book Checkout"),text="Borrower Name:",font=tab_font)
        name_label.place(relx=0.05,rely=0.05,anchor=tk.W)
        self.name_input = CTkEntry(master=self.tabview.tab("Book Checkout"),placeholder_text="Name",width=150,height=30,corner_radius=15)
        self.name_input.place(relx=0.26,rely=0.05,anchor=tk.W)

        # book input for book checkout
        book_label = CTkLabel(master=self.tabview.tab("Book Checkout"),text="Book Title:",font=tab_font)
        book_label.place(relx=0.12,rely=0.15,anchor=tk.W)
        self.book_input = CTkEntry(master=self.tabview.tab("Book Checkout"),placeholder_text="Title",width=150,height=30,corner_radius=15)
        self.book_input.place(relx=0.26,rely=0.15,anchor=tk.W)

        # submit button for book checkout
        button_font = CTkFont(family='Helvetica',size=16)
        checkout_submit_button = CTkButton(master=self.tabview.tab("Book Checkout"),text="Submit",fg_color="#0077b6",
                                    width=30,height=25,corner_radius=20,font=button_font,command=self.checkout_query)
        checkout_submit_button.place(relx=0.97,rely=0.97,anchor=tk.SE)

        # print book copies for book checkout
        self.print_query = CTkButton(master=self.tabview.tab("Book Checkout"),text="COPIES",fg_color="#0077b6",
                                    width=30,height=25,corner_radius=20,font=button_font,command=self.print_copies)
        self.print_query.place(relx=0.03,rely=0.97,anchor=tk.SW)

        # print book loans for book checkout
        self.print_loan_query = CTkButton(master=self.tabview.tab("Book Checkout"),text="LOANS",fg_color="#0077b6",
                                    width=30,height=25,corner_radius=20,font=button_font,command=self.print_loans)
        self.print_loan_query.place(relx=0.23,rely=0.97,anchor=tk.SW)
        

        # name input for Add Borrower
        bor_name = CTkLabel(master=self.tabview.tab("Add Borrower"),text="Borrower Name:",font=tab_font)
        bor_name.place(relx=0.05,rely=0.05,anchor=tk.W)
        self.bor_name_input = CTkEntry(master=self.tabview.tab("Add Borrower"),placeholder_text="Name",width=150,height=30,corner_radius=15)
        self.bor_name_input.place(relx=0.26,rely=0.05,anchor=tk.W)

        # address input for Add Borrower
        bor_add = CTkLabel(master=self.tabview.tab("Add Borrower"),text="Borrower Address:",font=tab_font)
        bor_add.place(relx=0.025,rely=0.15,anchor=tk.W)
        self.bor_add_input = CTkEntry(master=self.tabview.tab("Add Borrower"),placeholder_text="Address",width=150,height=30,corner_radius=15)
        self.bor_add_input.place(relx=0.26,rely=0.15,anchor=tk.W)

        # phone input for Add Borrower
        bor_phone = CTkLabel(master=self.tabview.tab("Add Borrower"),text="Borrower Phone:",font=tab_font)
        bor_phone.place(relx=0.048,rely=0.25,anchor=tk.W)
        self.bor_phone_input = CTkEntry(master=self.tabview.tab("Add Borrower"),placeholder_text="Phone",width=150,height=30,corner_radius=15)
        self.bor_phone_input.place(relx=0.26,rely=0.25,anchor=tk.W)

        # submit button for Add Borrower
        self.added = 0
        bor_submit_button = CTkButton(master=self.tabview.tab("Add Borrower"),text="Submit",fg_color="#0077b6",
                                    width=30,height=25,corner_radius=20,font=button_font,command=self.bor_query)
        bor_submit_button.place(relx=0.97,rely=0.97,anchor=tk.SE)

        # Print borrower entered button for Add Borrower
        self.print_bor_query = CTkButton(master=self.tabview.tab("Add Borrower"),text="Last_added",fg_color="#0077b6",
                                    width=30,height=25,corner_radius=20,font=button_font,command=self.print_card)
        self.print_bor_query.place(relx=0.03,rely=0.97,anchor=tk.SW)

        # Print all borrowet button for Add Borrower
        self.print_bor_all = CTkButton(master=self.tabview.tab("Add Borrower"),text="BORROWER",fg_color="#0077b6",
                                    width=30,height=25,corner_radius=20,font=button_font,command=self.print_all_card)
        self.print_bor_all.place(relx=0.23,rely=0.97,anchor=tk.SW)


        book_name = CTkLabel(master=self.tabview.tab("New Book"),text="Book Name:",font=tab_font)
        book_name.place(relx=0.1,rely=0.05,anchor=tk.W)
        self.book_nm_input = CTkEntry(master=self.tabview.tab("New Book"),placeholder_text="Book Name",width=150,height=30,corner_radius=15)
        self.book_nm_input.place(relx=0.26,rely=0.05,anchor=tk.W)


        book_author = CTkLabel(master=self.tabview.tab("New Book"),text="Author Name:",font=tab_font)
        book_author.place(relx=0.08,rely=0.15,anchor=tk.W)
        self.book_au_input = CTkEntry(master=self.tabview.tab("New Book"),placeholder_text="Author Name",width=150,height=30,corner_radius=15)
        self.book_au_input.place(relx=0.26,rely=0.15,anchor=tk.W)

        book_publisher = CTkLabel(master=self.tabview.tab("New Book"),text="Publisher Name:",font=tab_font)
        book_publisher.place(relx=0.05,rely=0.25,anchor=tk.W)
        self.book_pu_input = CTkEntry(master=self.tabview.tab("New Book"),placeholder_text="Publisher Name",width=150,height=30,corner_radius=15)
        self.book_pu_input.place(relx=0.26,rely=0.25,anchor=tk.W)

        book_submit_button = CTkButton(master=self.tabview.tab("New Book"),text="Submit",fg_color="#0077b6",
                                    width=30,height=25,corner_radius=20,font=button_font,command=self.add_new_book)
        book_submit_button.place(relx=0.97,rely=0.97,anchor=tk.SE)


        book_title = CTkLabel(master=self.tabview.tab("List Book Copies"),text="Book Name:",font=tab_font)
        book_title.place(relx=0.1,rely=0.05,anchor=tk.W)
        self.book_ti_input = CTkEntry(master=self.tabview.tab("List Book Copies"),placeholder_text="Book Name",width=150,height=30,corner_radius=15)
        self.book_ti_input.place(relx=0.26,rely=0.05,anchor=tk.W)

        title_submit_button = CTkButton(master=self.tabview.tab("List Book Copies"),text="Submit",fg_color="#0077b6",
                                    width=30,height=25,corner_radius=20,font=button_font,command=self.loan_num)
        title_submit_button.place(relx=0.97,rely=0.97,anchor=tk.SE)




        
        self.tabview.pack(pady=20)


    def loan_num(self):
        loan_conn = sqlite3.connect('Database_copy.db')
        loan_cur = loan_conn.cursor()

        button_font = CTkFont(family='Helvetica',size=16)
        print_font = CTkFont(family='Helvetica',size=18)

        title = self.book_ti_input.get()
        if title !="":
            loan_cur.execute(f"""
                            SELECT lb.branch_name AS Branch, COUNT(bl.branch_id) AS Counts
                            FROM BOOK_LOANS bl
                            JOIN BOOK b ON b.book_id = bl.book_id
                            JOIN LIBRARY_BRANCH lb ON lb.branch_id = bl.branch_id
                            WHERE lb.branch_id IN (SELECT branch_id FROM LIBRARY_BRANCH)
                            AND b.title = '{title}'
                            GROUP BY bl.branch_id;""")
            
            print_table = from_db_cursor(loan_cur)

            self.print_label = CTkLabel(self.tabview.tab("List Book Copies"),text=print_table,font=print_font)
            self.print_label.place(relx=0.50,rely=0.60,anchor=tk.CENTER)

            self.hide_query = CTkButton(master=self.tabview.tab("List Book Copies"),text="Hide list",fg_color="#0077b6",
                                        width=30,height=25,corner_radius=20,font=button_font,command=self.hide_copies)
            self.hide_query.place(relx=0.97,rely=0.97,anchor=tk.SE)

        else:

            self.print_label = CTkLabel(self.tabview.tab("List Book Copies"),text="Book Name is empty",font=print_font)
            self.print_label.place(relx=0.50,rely=0.60,anchor=tk.CENTER)


            self.hide_query = CTkButton(master=self.tabview.tab("List Book Copies"),text="Hide list",fg_color="#0077b6",
                                        width=30,height=25,corner_radius=20,font=button_font,command=self.hide_copies)
            self.hide_query.place(relx=0.97,rely=0.97,anchor=tk.SE)

        loan_conn.commit()
        loan_conn.close()




    def checkout_query(self):
        checkout_conn = sqlite3.connect('Database_copy.db')
        checkout_cur = checkout_conn.cursor()

        # Retrieve card_no from BORROWER table based on entered name
        name = self.name_input.get()
        title = self.book_input.get()
        today = date.today()
        month = today + timedelta(days=30)

        button_font = CTkFont(family='Helvetica',size=16)
        print_font = CTkFont(family='Helvetica',size=18)

        if name != "" and title != "":
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
        
        elif name == "" and title !="":
            self.print_label = CTkLabel(self.tabview.tab("Book Checkout"),text="Borrow name is required",font=print_font)
            self.print_label.place(relx=0.50,rely=0.52,anchor=tk.CENTER)
            self.hide_query = CTkButton(master=self.tabview.tab("Book Checkout"),text="  Hide  ",fg_color="#0077b6",
                                        width=40,height=30,corner_radius=20,font=button_font,command=self.hide_copies)
            self.hide_query.place(relx=0.97,rely=0.97,anchor=tk.SE)
            
        elif name != "" and title =="":
            self.print_label = CTkLabel(self.tabview.tab("Book Checkout"),text="Book title is required",font=print_font)
            self.print_label.place(relx=0.50,rely=0.52,anchor=tk.CENTER)
            self.hide_query = CTkButton(master=self.tabview.tab("Book Checkout"),text="  Hide  ",fg_color="#0077b6",
                                        width=40,height=30,corner_radius=20,font=button_font,command=self.hide_copies)
            self.hide_query.place(relx=0.97,rely=0.97,anchor=tk.SE)
        
        else:
            
            self.print_label = CTkLabel(self.tabview.tab("Book Checkout"),text="Both name and title is required",font=print_font)
            self.print_label.place(relx=0.50,rely=0.52,anchor=tk.CENTER)

            self.hide_query = CTkButton(master=self.tabview.tab("Book Checkout"),text="  Hide  ",fg_color="#0077b6",
                                        width=40,height=30,corner_radius=20,font=button_font,command=self.hide_copies)
            self.hide_query.place(relx=0.97,rely=0.97,anchor=tk.SE)

        
        checkout_conn.commit()
        checkout_conn.close()

    def print_copies(self):

        copies_conn = sqlite3.connect('Database_copy.db')
        copies_cur= copies_conn.cursor()

        copies_cur.execute("SELECT * FROM BOOK_COPIES")

        print_table = from_db_cursor(copies_cur)
        print_table.left_padding_width=10
        print_table.right_padding_width=10

        print_font = CTkFont(family='Helvetica',size=8)
        self.print_label = CTkLabel(self.tabview.tab("Book Checkout"),text=print_table,font=print_font)
        self.print_label.place(relx=0.50,rely=0.52,anchor=tk.CENTER)

        button_font = CTkFont(family='Helvetica',size=16)
        self.hide_query = CTkButton(master=self.tabview.tab("Book Checkout"),text="   Hide   ",fg_color="#0077b6",
                                    width=30,height=25,corner_radius=20,font=button_font,command=self.hide_copies)
        self.hide_query.place(relx=0.03,rely=0.97,anchor=tk.SW)
        

        copies_conn.commit()
        copies_conn.close()

    def print_loans(self):
        loan_conn = sqlite3.connect('Database_copy.db')
        loans_cur = loan_conn.cursor()

        loans_cur.execute("""SELECT * FROM BOOK_LOANS""")

        print_table = from_db_cursor(loans_cur)
        print_table.left_padding_width=5
        print_table.right_padding_width=5

        print_font = CTkFont(family='Helvetica',size=8)
        self.print_label = CTkLabel(self.tabview.tab("Book Checkout"),text=print_table,font=print_font)
        self.print_label.place(relx=0.50,rely=0.52,anchor=tk.CENTER)

        button_font = CTkFont(family='Helvetica',size=16)
        self.hide_query = CTkButton(master=self.tabview.tab("Book Checkout"),text="   Hide   ",fg_color="#0077b6",
                                    width=30,height=25,corner_radius=20,font=button_font,command=self.hide_copies)
        self.hide_query.place(relx=0.23,rely=0.97,anchor=tk.SW)
        
        loan_conn.commit()
        loan_conn.close()


    def bor_query(self):
        bor_conn = sqlite3.connect('Database_copy.db')
        bor_cur = bor_conn.cursor()

        button_font = CTkFont(family='Helvetica',size=16)
        print_font = CTkFont(family='Helvetica',size=18)


        self.name = self.bor_name_input.get()
        address = self.bor_add_input.get()
        phone = self.bor_phone_input.get()
        if self.name != "" and address !="" and phone != "":
            bor_cur.execute(f"""
                            INSERT INTO BORROWER(card_no,name,address,phone)
                            VALUES(NULL,'{self.name}','{address}','{phone}');""")
            self.added = 1

        elif self.name == "" and address != "" and phone != "":
            
            self.print_label = CTkLabel(self.tabview.tab("Add Borrower"),text="Name is required",font=print_font)
            self.print_label.place(relx=0.50,rely=0.50,anchor=tk.CENTER)

            self.hide_query = CTkButton(master=self.tabview.tab("Add Borrower"),text="  Hide  ",fg_color="#0077b6",
                                        width=30,height=25,corner_radius=20,font=button_font,command=self.hide_copies)
            self.hide_query.place(relx=0.97,rely=0.97,anchor=tk.SE)
        
        elif self.name != "" and address == "" and phone != "":
            
            self.print_label = CTkLabel(self.tabview.tab("Add Borrower"),text="Address is required",font=print_font)
            self.print_label.place(relx=0.50,rely=0.50,anchor=tk.CENTER)

            self.hide_query = CTkButton(master=self.tabview.tab("Add Borrower"),text="  Hide  ",fg_color="#0077b6",
                                        width=30,height=25,corner_radius=20,font=button_font,command=self.hide_copies)
            self.hide_query.place(relx=0.97,rely=0.97,anchor=tk.SE)
        
        elif self.name != "" and address != "" and phone == "":
            
            self.print_label = CTkLabel(self.tabview.tab("Add Borrower"),text="Phone is required",font=print_font)
            self.print_label.place(relx=0.50,rely=0.50,anchor=tk.CENTER)

            self.hide_query = CTkButton(master=self.tabview.tab("Add Borrower"),text="  Hide  ",fg_color="#0077b6",
                                        width=30,height=25,corner_radius=20,font=button_font,command=self.hide_copies)
            self.hide_query.place(relx=0.97,rely=0.97,anchor=tk.SE)

        elif self.name == "" and address == "" and phone != "":
            
            self.print_label = CTkLabel(self.tabview.tab("Add Borrower"),text="Name and address is required",font=print_font)
            self.print_label.place(relx=0.50,rely=0.50,anchor=tk.CENTER)

            self.hide_query = CTkButton(master=self.tabview.tab("Add Borrower"),text="  Hide  ",fg_color="#0077b6",
                                        width=30,height=25,corner_radius=20,font=button_font,command=self.hide_copies)
            self.hide_query.place(relx=0.97,rely=0.97,anchor=tk.SE)
        
        elif self.name == "" and address != "" and phone == "":
            
            self.print_label = CTkLabel(self.tabview.tab("Add Borrower"),text="Name and phone is required",font=print_font)
            self.print_label.place(relx=0.50,rely=0.50,anchor=tk.CENTER)

            self.hide_query = CTkButton(master=self.tabview.tab("Add Borrower"),text="  Hide  ",fg_color="#0077b6",
                                        width=30,height=25,corner_radius=20,font=button_font,command=self.hide_copies)
            self.hide_query.place(relx=0.97,rely=0.97,anchor=tk.SE)
        
        elif self.name != "" and address == "" and phone == "":
            
            self.print_label = CTkLabel(self.tabview.tab("Add Borrower"),text="Address and phone is required",font=print_font)
            self.print_label.place(relx=0.50,rely=0.50,anchor=tk.CENTER)

            self.hide_query = CTkButton(master=self.tabview.tab("Add Borrower"),text="  Hide  ",fg_color="#0077b6",
                                        width=30,height=25,corner_radius=20,font=button_font,command=self.hide_copies)
            self.hide_query.place(relx=0.97,rely=0.97,anchor=tk.SE)
        
        else:

            self.print_label = CTkLabel(self.tabview.tab("Add Borrower"),text="All fields are required",font=print_font)
            self.print_label.place(relx=0.50,rely=0.50,anchor=tk.CENTER)

            self.hide_query = CTkButton(master=self.tabview.tab("Add Borrower"),text="  Hide  ",fg_color="#0077b6",
                                        width=30,height=25,corner_radius=20,font=button_font,command=self.hide_copies)
            self.hide_query.place(relx=0.97,rely=0.97,anchor=tk.SE)    
            
        


        bor_conn.commit()
        bor_conn.close()

    def print_all_card(self):
        card_conn = sqlite3.connect('Database_copy.db')
        card_cur = card_conn.cursor()
        card_cur.execute("""SELECT card_no,name FROM BORROWER;""")

        print_table = from_db_cursor(card_cur)
        print_table.left_padding_width=5
        print_table.right_padding_width=5

        print_font = CTkFont(family='Helvetica',size=8)
        self.print_label = CTkLabel(self.tabview.tab("Add Borrower"),text=print_table,font=print_font)
        self.print_label.place(relx=0.60,rely=0.60,anchor=tk.CENTER)

        button_font = CTkFont(family='Helvetica',size=16)
        self.hide_query = CTkButton(master=self.tabview.tab("Add Borrower"),text="Hide BORROWER",fg_color="#0077b6",
                                    width=30,height=25,corner_radius=20,font=button_font,command=self.hide_copies)
        self.hide_query.place(relx=0.23,rely=0.97,anchor=tk.SW)

        card_conn.commit()
        card_conn.close()



    def print_card(self):
        card_conn = sqlite3.connect('Database_copy.db')
        card_cur = card_conn.cursor()

        print_font = CTkFont(family='Helvetica',size=20)
        button_font = CTkFont(family='Helvetica',size=16)


        if self.added == 1:
            card_cur.execute(f"""SELECT card_no, name FROM BORROWER WHERE name = '{self.name}'""")

            print_table = from_db_cursor(card_cur)
            print_table.left_padding_width=5
            print_table.right_padding_width=5
            
            self.print_label = CTkLabel(self.tabview.tab("Add Borrower"),text=print_table,font=print_font)
            self.print_label.place(relx=0.50,rely=0.60,anchor=tk.CENTER)


            self.hide_query = CTkButton(master=self.tabview.tab("Add Borrower"),text=" Hide_added ",fg_color="#0077b6",
                                        width=30,height=25,corner_radius=20,font=button_font,command=self.hide_copies)
            self.hide_query.place(relx=0.03,rely=0.97,anchor=tk.SW)
        
        else:
            self.print_label = CTkLabel(self.tabview.tab("Add Borrower"),text="Nothing added",font=print_font)
            self.print_label.place(relx=0.50,rely=0.50,anchor=tk.CENTER)


            self.hide_query = CTkButton(master=self.tabview.tab("Add Borrower"),text=" Hide_added ",fg_color="#0077b6",
                                        width=30,height=25,corner_radius=20,font=button_font,command=self.hide_copies)
            self.hide_query.place(relx=0.03,rely=0.97,anchor=tk.SW)



        card_conn.commit()
        card_conn.close()

    
    def add_new_book(self):

        self.add_book()
        self.add_author()
        self.add_copies()

    def add_book(self):
        book_conn = sqlite3.connect('Database_copy.db')
        book_cur = book_conn.cursor()

        book_name = self.book_nm_input.get()
        book_publisher = self.book_pu_input.get()

        book_cur.execute(f"""
                        INSERT INTO BOOK(book_id,title,book_publisher)
                        VALUES(NULL,'{book_name}','{book_publisher}');""")

        book_conn.commit()
        book_conn.close()

    def add_author(self):
        auth_conn = sqlite3.connect('Database_copy.db')
        auth_cur = auth_conn.cursor()

        book_author = self.book_au_input.get()
        book_name = self.book_nm_input.get()

        auth_cur.execute(f"""
                        INSERT INTO BOOK_AUTHORS(book_id,author_name)
                        SELECT DISTINCT book_id, '{book_author}'
                        FROM BOOK
                        WHERE title = '{book_name}';""")
        
        auth_conn.commit()
        auth_conn.close()

    def add_copies(self):
        copies_conn = sqlite3.connect('Database_copy.db')
        copies_cur = copies_conn.cursor()

        book_name = self.book_nm_input.get()

        copies_cur.execute(f"""INSERT INTO BOOK_COPIES(book_id,branch_id,no_of_copies)
                        SELECT b.book_id,lb.branch_id,5
                        FROM BOOK b, LIBRARY_BRANCH lb
                        WHERE lb.branch_id IN (SELECT lbr.branch_id FROM LIBRARY_BRANCH lbr) 
                        AND b.title = '{book_name}';""")
        copies_conn.commit()
        copies_conn.close()

    def hide_copies(self):
        self.print_label.place_forget()
        self.hide_query.place_forget()




    def go_back_into(self):
        self.home_frame.pack_forget()
        self.create_into_frame()



    def run(self):
        self.window.mainloop()
