from PIL import Image
import customtkinter as ck
from tkinter import ttk
from customtkinter import CTkImage,CTkFont,CTkButton,CTkTabview,CTkEntry,CTkLabel,CTkScrollbar
from datetime import date, timedelta
import tkinter as tk
import pandas as pd
import sqlite3




class App:
    def __init__(self,window):
        self.window = window
        self.window.title("LMS Database")
        self.window.geometry("800x600")
        self.window.resizable(False,False)
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
        
        bor_submit_button = CTkButton(master=self.tabview.tab("Add Borrower"),text="Submit",fg_color="#0077b6",
                                    width=30,height=25,corner_radius=20,font=button_font,command=self.bor_query)
        bor_submit_button.place(relx=0.97,rely=0.97,anchor=tk.SE)

        # Print borrower entered button for Add Borrower
        
        print_bor_query = CTkButton(master=self.tabview.tab("Add Borrower"),text="BORROWER",fg_color="#0077b6",
                                    width=30,height=25,corner_radius=20,font=button_font,command=self.print_all_card)
        print_bor_query.place(relx=0.03,rely=0.97,anchor=tk.SW)


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

        print_book_query = CTkButton(master=self.tabview.tab("New Book"),text="BOOK",fg_color="#0077b6",
                                    width=30,height=25,corner_radius=20,font=button_font,command=self.print_book)
        print_book_query.place(relx=0.03,rely=0.97,anchor=tk.SW)

        print_author_query = CTkButton(master=self.tabview.tab("New Book"),text="AUTHOR",fg_color="#0077b6",
                                    width=30,height=25,corner_radius=20,font=button_font,command=self.print_authors)
        print_author_query.place(relx=0.16,rely=0.97,anchor=tk.SW)

        print_pub_query = CTkButton(master=self.tabview.tab("New Book"),text="PUBLISHER",fg_color="#0077b6",
                                    width=30,height=25,corner_radius=20,font=button_font,command=self.print_publisher)
        print_pub_query.place(relx=0.315,rely=0.97,anchor=tk.SW)


        book_title = CTkLabel(master=self.tabview.tab("List Book Copies"),text="Book Name:",font=tab_font)
        book_title.place(relx=0.1,rely=0.05,anchor=tk.W)
        self.book_title_input = CTkEntry(master=self.tabview.tab("List Book Copies"),placeholder_text="Book Name",width=150,height=30,corner_radius=15)
        self.book_title_input.place(relx=0.26,rely=0.05,anchor=tk.W)

        title_submit_button = CTkButton(master=self.tabview.tab("List Book Copies"),text="Submit",fg_color="#0077b6",
                                    width=30,height=25,corner_radius=20,font=button_font,command=self.loan_num)
        title_submit_button.place(relx=0.97,rely=0.97,anchor=tk.SE)

        start_date = CTkLabel(master=self.tabview.tab("Late Return"),text="Start Date:",font=tab_font)
        start_date.place(relx=0.12,rely=0.05,anchor=tk.W)
        self.start_da_input = CTkEntry(master=self.tabview.tab("Late Return"),placeholder_text="Start Date",width=150,height=30,corner_radius=15)
        self.start_da_input.place(relx=0.26,rely=0.05,anchor=tk.W)

        end_date = CTkLabel(master=self.tabview.tab("Late Return"),text="End Date:",font=tab_font)
        end_date.place(relx=0.13,rely=0.15,anchor=tk.W)
        self.end_da_input = CTkEntry(master=self.tabview.tab("Late Return"),placeholder_text="End Date",width=150,height=30,corner_radius=15)
        self.end_da_input.place(relx=0.26,rely=0.15,anchor=tk.W)

        date_submit_button = CTkButton(master=self.tabview.tab("Late Return"),text="Submit",fg_color="#0077b6",
                                    width=30,height=25,corner_radius=20,font=button_font,command=self.date_query)
        date_submit_button.place(relx=0.97,rely=0.97,anchor=tk.SE)

        bor_id = CTkLabel(master=self.tabview.tab("Late Fee"),text="Borrower ID:",font=tab_font)
        bor_id.place(relx=0.097,rely=0.05,anchor=tk.W)
        self.bor_id_input = CTkEntry(master=self.tabview.tab("Late Fee"),placeholder_text="ID",width=150,height=30,corner_radius=15)
        self.bor_id_input.place(relx=0.26,rely=0.05,anchor=tk.W)

        bor_nm = CTkLabel(master=self.tabview.tab("Late Fee"),text="Borrower Name:",font=tab_font)
        bor_nm.place(relx=0.05,rely=0.15,anchor=tk.W)
        self.bor_nm_input = CTkEntry(master=self.tabview.tab("Late Fee"),placeholder_text="Name",width=150,height=30,corner_radius=15)
        self.bor_nm_input.place(relx=0.26,rely=0.15,anchor=tk.W)

        latefee_submit_button = CTkButton(master=self.tabview.tab("Late Fee"),text="Submit",fg_color="#0077b6",
                                    width=30,height=25,corner_radius=20,font=button_font,command=self.late_fee_check)
        latefee_submit_button.place(relx=0.97,rely=0.97,anchor=tk.SE)

        book_id = CTkLabel(master=self.tabview.tab("Book Information"),text="Book ID:",font=tab_font)
        book_id.place(relx=0.145,rely=0.05,anchor=tk.W)
        self.book_id_input = CTkEntry(master=self.tabview.tab("Book Information"),placeholder_text="ID",width=150,height=30,corner_radius=15)
        self.book_id_input.place(relx=0.26,rely=0.05,anchor=tk.W)

        book_ti = CTkLabel(master=self.tabview.tab("Book Information"),text="Book Title:",font=tab_font) 
        book_ti.place(relx=0.12,rely=0.15,anchor=tk.W)
        self.book_ti_input = CTkEntry(master=self.tabview.tab("Book Information"),placeholder_text="Title",width=150,height=30,corner_radius=15)
        self.book_ti_input.place(relx=0.26,rely=0.15,anchor=tk.W)

        book_info_button = CTkButton(master=self.tabview.tab("Book Information"),text="Submit",fg_color="#0077b6",
                                    width=30,height=25,corner_radius=20,font=button_font,command=self.book_info_query)
        book_info_button.place(relx=0.97,rely=0.97,anchor=tk.SE)
        
        self.tabview.pack(pady=20)




    # Query 1
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
            self.name_input.delete('0',ck.END)
            self.book_input.delete('0',ck.END)
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
                                        width=30,height=25,corner_radius=20,font=button_font,command=self.hide_copies)
            self.hide_query.place(relx=0.97,rely=0.97,anchor=tk.SE)
            
        elif name != "" and title =="":
            self.print_label = CTkLabel(self.tabview.tab("Book Checkout"),text="Book title is required",font=print_font)
            self.print_label.place(relx=0.50,rely=0.52,anchor=tk.CENTER)
            self.hide_query = CTkButton(master=self.tabview.tab("Book Checkout"),text="  Hide  ",fg_color="#0077b6",
                                        width=30,height=25,corner_radius=20,font=button_font,command=self.hide_copies)
            self.hide_query.place(relx=0.97,rely=0.97,anchor=tk.SE)
        
        else:
            
            self.print_label = CTkLabel(self.tabview.tab("Book Checkout"),text="Both name and title is required",font=print_font)
            self.print_label.place(relx=0.50,rely=0.52,anchor=tk.CENTER)

            self.hide_query = CTkButton(master=self.tabview.tab("Book Checkout"),text="  Hide  ",fg_color="#0077b6",
                                        width=30,height=25,corner_radius=20,font=button_font,command=self.hide_copies)
            self.hide_query.place(relx=0.97,rely=0.97,anchor=tk.SE)

        
        checkout_conn.commit()
        checkout_conn.close()

    # Query 1
    def print_copies(self):

        copies_conn = sqlite3.connect('Database_copy.db')

        print_table = pd.read_sql('SELECT * FROM BOOK_COPIES',copies_conn,)
        print_font = CTkFont(family='Helvetica',size=12)

        self.print_label = tk.Text(self.tabview.tab("Book Checkout"),font=print_font,width=50,height=20)
        scroll_bar = CTkScrollbar(self.tabview.tab("Book Checkout"),command=self.print_label.yview)

        self.print_label.configure(yscrollcommand=scroll_bar.set)
        self.print_label.place(relx=0.50,rely=0.52,anchor=tk.CENTER)

        columns = "\t\t".join(print_table.columns)
        self.print_label.insert(tk.END,columns)


        for index,row in print_table.iterrows():
            self.print_label.insert(tk.END,f"\n{row[0]}\t\t{row[1]}\t\t{row[2]}")


        self.print_label.configure(state="disabled")

        button_font = CTkFont(family='Helvetica',size=16)
        self.hide_query = CTkButton(master=self.tabview.tab("Book Checkout"),text="    Hide    ",fg_color="#0077b6",
                                    width=30,height=25,corner_radius=20,font=button_font,command=self.hide_copies)
        self.hide_query.place(relx=0.03,rely=0.97,anchor=tk.SW)
        

        copies_conn.commit()
        copies_conn.close()

    # Query 1
    def print_loans(self):
        loan_conn = sqlite3.connect('Database_copy.db')

        print_table = pd.read_sql('SELECT book_id,branch_id,card_no,date_out,due_date FROM BOOK_LOANS',loan_conn)
        print_font = CTkFont(family='Helvetica',size=12)

        self.print_label = tk.Text(self.tabview.tab("Book Checkout"),font=print_font,width=80,height=20)
        yscroll_bar = CTkScrollbar(self.tabview.tab("Book Checkout"),command=self.print_label.yview)

        self.print_label.configure(yscrollcommand=yscroll_bar.set)
        self.print_label.place(relx=0.50,rely=0.52,anchor=tk.CENTER)

        columns = "\t\t".join(print_table.columns)
        self.print_label.insert(tk.END,columns)

        for index,row in print_table.iterrows():
            self.print_label.insert(tk.END,f"\n{row[0]}\t\t{row[1]}\t\t{row[2]}\t\t{row[3]}\t\t{row[4]}")


        self.print_label.configure(state="disabled")

        

        button_font = CTkFont(family='Helvetica',size=16)
        self.hide_query = CTkButton(master=self.tabview.tab("Book Checkout"),text="   Hide   ",fg_color="#0077b6",
                                    width=30,height=25,corner_radius=20,font=button_font,command=self.hide_copies)
        self.hide_query.place(relx=0.23,rely=0.97,anchor=tk.SW)
        
        loan_conn.commit()
        loan_conn.close()


    # Query 2
    def bor_query(self):
        bor_conn = sqlite3.connect('Database_copy.db')
        bor_cur = bor_conn.cursor()

        button_font = CTkFont(family='Helvetica',size=16)
        print_font = CTkFont(family='Helvetica',size=18)


        name = self.bor_name_input.get()
        address = self.bor_add_input.get()
        phone = self.bor_phone_input.get()
        if name != "" and address !="" and phone != "":
            self.bor_name_input.delete('0',ck.END)
            self.bor_add_input.delete('0',ck.END)
            self.bor_phone_input.delete('0',ck.END)

            bor_cur.execute(f"""
                            INSERT INTO BORROWER(card_no,name,address,phone)
                            VALUES(NULL,'{name}','{address}','{phone}');""")
            
            print_table = pd.read_sql(f"""SELECT card_no, name 
                            FROM BORROWER
                            WHERE name = '{name}' AND address = '{address}' AND phone = '{phone}';""",bor_conn)


            self.print_label = tk.Text(self.tabview.tab("Add Borrower"),font=print_font,width=25,height=5)
            scroll_bar = CTkScrollbar(self.tabview.tab("Add Borrower"),command=self.print_label.yview)

            self.print_label.configure(yscrollcommand=scroll_bar.set)
            self.print_label.place(relx=0.50,rely=0.60,anchor=tk.CENTER)

            columns = "\t\t".join(print_table.columns)
            self.print_label.insert(tk.END,columns)


            for index,row in print_table.iterrows():
                self.print_label.insert(tk.END,f"\n{row[0]}\t\t{row[1]}")


            self.print_label.configure(state="disabled")

            self.hide_query = CTkButton(master=self.tabview.tab("Add Borrower"),text="  Hide  ",fg_color="#0077b6",
                                        width=30,height=25,corner_radius=20,font=button_font,command=self.hide_copies)
            self.hide_query.place(relx=0.97,rely=0.97,anchor=tk.SE)
            

        elif name == "" and address != "" and phone != "":
            self.bor_phone_input.delete('0',ck.END)
            self.bor_add_input.delete('0',ck.END)
            
            self.print_label = CTkLabel(self.tabview.tab("Add Borrower"),text="Name is required",font=print_font)
            self.print_label.place(relx=0.50,rely=0.50,anchor=tk.CENTER)

            self.hide_query = CTkButton(master=self.tabview.tab("Add Borrower"),text="  Hide  ",fg_color="#0077b6",
                                        width=30,height=25,corner_radius=20,font=button_font,command=self.hide_copies)
            self.hide_query.place(relx=0.97,rely=0.97,anchor=tk.SE)
        
        elif name != "" and address == "" and phone != "":
            self.bor_name_input.delete('0',ck.END)
            self.bor_phone_input.delete('0',ck.END)

            self.print_label = CTkLabel(self.tabview.tab("Add Borrower"),text="Address is required",font=print_font)
            self.print_label.place(relx=0.50,rely=0.50,anchor=tk.CENTER)

            self.hide_query = CTkButton(master=self.tabview.tab("Add Borrower"),text="  Hide  ",fg_color="#0077b6",
                                        width=30,height=25,corner_radius=20,font=button_font,command=self.hide_copies)
            self.hide_query.place(relx=0.97,rely=0.97,anchor=tk.SE)
        
        elif name != "" and address != "" and phone == "":
            self.bor_add_input.delete('0',ck.END)
            self.bor_name_input.delete('0',ck.END)
            
            self.print_label = CTkLabel(self.tabview.tab("Add Borrower"),text="Phone is required",font=print_font)
            self.print_label.place(relx=0.50,rely=0.50,anchor=tk.CENTER)

            self.hide_query = CTkButton(master=self.tabview.tab("Add Borrower"),text="  Hide  ",fg_color="#0077b6",
                                        width=30,height=25,corner_radius=20,font=button_font,command=self.hide_copies)
            self.hide_query.place(relx=0.97,rely=0.97,anchor=tk.SE)

        elif name == "" and address == "" and phone != "":
            self.bor_phone_input.delete('0',ck.END)

            self.print_label = CTkLabel(self.tabview.tab("Add Borrower"),text="Name and address is required",font=print_font)
            self.print_label.place(relx=0.50,rely=0.50,anchor=tk.CENTER)

            self.hide_query = CTkButton(master=self.tabview.tab("Add Borrower"),text="  Hide  ",fg_color="#0077b6",
                                        width=30,height=25,corner_radius=20,font=button_font,command=self.hide_copies)
            self.hide_query.place(relx=0.97,rely=0.97,anchor=tk.SE)
        
        elif name == "" and address != "" and phone == "":
            self.bor_add_input.delete('0',ck.END)

            self.print_label = CTkLabel(self.tabview.tab("Add Borrower"),text="Name and phone is required",font=print_font)
            self.print_label.place(relx=0.50,rely=0.50,anchor=tk.CENTER)

            self.hide_query = CTkButton(master=self.tabview.tab("Add Borrower"),text="  Hide  ",fg_color="#0077b6",
                                        width=30,height=25,corner_radius=20,font=button_font,command=self.hide_copies)
            self.hide_query.place(relx=0.97,rely=0.97,anchor=tk.SE)
        
        elif name != "" and address == "" and phone == "":
            self.bor_name_input.delete('0',ck.END)
            

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

    # Query 2
    # change the print_table and delete entry
    def print_all_card(self):
        card_conn = sqlite3.connect('Database_copy.db')

        button_font = CTkFont(family='Helvetica',size=16)
        print_font = CTkFont(family='Helvetica',size=18)
        
        # card_cur = card_conn.cursor()
        print_table = pd.read_sql(f"""SELECT card_no,name 
                                FROM BORROWER;""",card_conn)


        self.print_label = tk.Text(self.tabview.tab("Add Borrower"),font=print_font,width=25,height=7)
        scroll_bar = CTkScrollbar(self.tabview.tab("Add Borrower"),command=self.print_label.yview)

        self.print_label.configure(yscrollcommand=scroll_bar.set)
        self.print_label.place(relx=0.50,rely=0.60,anchor=tk.CENTER)

        columns = "\t".join(print_table.columns)
        self.print_label.insert(tk.END,columns)


        for index,row in print_table.iterrows():
            self.print_label.insert(tk.END,f"\n{row[0]}\t{row[1]}")


        self.print_label.configure(state="disabled")

        self.hide_query = CTkButton(master=self.tabview.tab("Add Borrower"),text="       Hide         ",fg_color="#0077b6",
                                    width=30,height=25,corner_radius=20,font=button_font,command=self.hide_copies)
        self.hide_query.place(relx=0.03,rely=0.97,anchor=tk.SW)

        card_conn.commit()
        card_conn.close()


    
    # Query 3
    def add_new_book(self):
        book_name = self.book_nm_input.get()
        book_publisher = self.book_pu_input.get()
        book_author = self.book_au_input.get()


        print_font = CTkFont(family='Helvetica',size=20)
        button_font = CTkFont(family='Helvetica',size=16)

        if book_name != "" and book_publisher != "" and book_author != "":
            self.book_nm_input.delete('0',ck.END)
            self.book_pu_input.delete('0',ck.END)
            self.book_au_input.delete('0',ck.END)

            self.add_book(book_name,book_publisher)
            self.add_author(book_name,book_author)
            self.add_copies(book_name)

        elif book_name == "" and book_publisher != "" and book_author != "":
            self.book_pu_input.delete('0',ck.END)
            self.book_au_input.delete('0',ck.END)

            self.print_label = CTkLabel(self.tabview.tab("New Book"),text="Book Name is required",font=print_font)
            self.print_label.place(relx=0.50,rely=0.50,anchor=tk.CENTER)

            self.hide_query = CTkButton(master=self.tabview.tab("New Book"),text="  Hide  ",fg_color="#0077b6",
                                        width=30,height=25,corner_radius=20,font=button_font,command=self.hide_copies)
            self.hide_query.place(relx=0.97,rely=0.97,anchor=tk.SE)
        
        elif book_name != "" and book_publisher == "" and book_author != "":
            self.book_nm_input.delete('0',ck.END)
            self.book_au_input.delete('0',ck.END)

            self.print_label = CTkLabel(self.tabview.tab("New Book"),text="Book Publisher is required",font=print_font)
            self.print_label.place(relx=0.50,rely=0.50,anchor=tk.CENTER)

            self.hide_query = CTkButton(master=self.tabview.tab("New Book"),text="  Hide  ",fg_color="#0077b6",
                                        width=30,height=25,corner_radius=20,font=button_font,command=self.hide_copies)
            self.hide_query.place(relx=0.97,rely=0.97,anchor=tk.SE)
        
        elif book_name != "" and book_publisher != "" and book_author == "":
            self.book_nm_input.delete('0',ck.END)
            self.book_pu_input.delete('0',ck.END)
            
            self.print_label = CTkLabel(self.tabview.tab("New Book"),text="Book Author is required",font=print_font)
            self.print_label.place(relx=0.50,rely=0.50,anchor=tk.CENTER)

            self.hide_query = CTkButton(master=self.tabview.tab("New Book"),text="  Hide  ",fg_color="#0077b6",
                                        width=30,height=25,corner_radius=20,font=button_font,command=self.hide_copies)
            self.hide_query.place(relx=0.97,rely=0.97,anchor=tk.SE)

        elif book_name != "" and book_publisher == "" and book_author == "":
            self.book_nm_input.delete('0',ck.END)

            self.print_label = CTkLabel(self.tabview.tab("New Book"),text="Book Publisher and Author are required",font=print_font)
            self.print_label.place(relx=0.50,rely=0.50,anchor=tk.CENTER)

            self.hide_query = CTkButton(master=self.tabview.tab("New Book"),text="  Hide  ",fg_color="#0077b6",
                                        width=30,height=25,corner_radius=20,font=button_font,command=self.hide_copies)
            self.hide_query.place(relx=0.97,rely=0.97,anchor=tk.SE)

        elif book_name == "" and book_publisher != "" and book_author == "":
            self.book_pu_input.delete('0',ck.END)

            self.print_label = CTkLabel(self.tabview.tab("New Book"),text="Book Name and Author are required",font=print_font)
            self.print_label.place(relx=0.50,rely=0.50,anchor=tk.CENTER)

            self.hide_query = CTkButton(master=self.tabview.tab("New Book"),text="  Hide  ",fg_color="#0077b6",
                                        width=30,height=25,corner_radius=20,font=button_font,command=self.hide_copies)
            self.hide_query.place(relx=0.97,rely=0.97,anchor=tk.SE)
        
        elif book_name == "" and book_publisher == "" and book_author != "":
            self.book_au_input.delete('0',ck.END)

            self.print_label = CTkLabel(self.tabview.tab("New Book"),text="Book Name and Publisher are required",font=print_font)
            self.print_label.place(relx=0.50,rely=0.50,anchor=tk.CENTER)

            self.hide_query = CTkButton(master=self.tabview.tab("New Book"),text="  Hide  ",fg_color="#0077b6",
                                        width=30,height=25,corner_radius=20,font=button_font,command=self.hide_copies)
            self.hide_query.place(relx=0.97,rely=0.97,anchor=tk.SE)
        
        else:
            self.print_label = CTkLabel(self.tabview.tab("New Book"),text="All fields are required",font=print_font)
            self.print_label.place(relx=0.50,rely=0.50,anchor=tk.CENTER)

            self.hide_query = CTkButton(master=self.tabview.tab("New Book"),text="  Hide  ",fg_color="#0077b6",
                                        width=30,height=25,corner_radius=20,font=button_font,command=self.hide_copies)
            self.hide_query.place(relx=0.97,rely=0.97,anchor=tk.SE)

    # Query 3
    def add_book(self,book_name,book_publisher):
        book_conn = sqlite3.connect('Database_copy.db')
        book_cur = book_conn.cursor()

        book_cur.execute(f"""
                        INSERT INTO BOOK(book_id,title,book_publisher)
                        VALUES(NULL,'{book_name}',
                        (SELECT publisher_name 
                        FROM PUBLISHER 
                        WHERE publisher_name = '{book_publisher}'));""")

        book_conn.commit()
        book_conn.close()

    # Query 3
    def add_author(self,book_name,book_author):
        auth_conn = sqlite3.connect('Database_copy.db')
        auth_cur = auth_conn.cursor()

        

        auth_cur.execute(f"""
                        INSERT INTO BOOK_AUTHORS(book_id,author_name)
                        SELECT DISTINCT book_id, '{book_author}'
                        FROM BOOK
                        WHERE title = '{book_name}';""")
        
        auth_conn.commit()
        auth_conn.close()

    # Query 3
    def add_copies(self,book_name):
        copies_conn = sqlite3.connect('Database_copy.db')
        copies_cur = copies_conn.cursor()

        copies_cur.execute(f"""INSERT INTO BOOK_COPIES(book_id,branch_id,no_of_copies)
                        SELECT b.book_id,lb.branch_id,5
                        FROM BOOK b, LIBRARY_BRANCH lb
                        WHERE lb.branch_id IN (SELECT lbr.branch_id FROM LIBRARY_BRANCH lbr) 
                        AND b.title = '{book_name}';""")
        
        copies_conn.commit()
        copies_conn.close()

    # Query 3
    def print_publisher(self):
        book_conn = sqlite3.connect('Database_copy.db')

        button_font = CTkFont(family='Helvetica',size=16)
        print_font = CTkFont(family='Helvetica',size=18)
        
        
        print_table = pd.read_sql(f"""SELECT publisher_name
                                FROM PUBLISHER;""",book_conn)


        self.print_label = tk.Text(self.tabview.tab("New Book"),font=print_font,width=30,height=10)
        scroll_bar = CTkScrollbar(self.tabview.tab("New Book"),command=self.print_label.yview)

        self.print_label.configure(yscrollcommand=scroll_bar.set)
        self.print_label.place(relx=0.50,rely=0.60,anchor=tk.CENTER)

        columns = "\t\t".join(print_table.columns)
        self.print_label.insert(tk.END,columns)


        for index,row in print_table.iterrows():
            self.print_label.insert(tk.END,f"\n{row[0]}")


        self.print_label.configure(state="disabled")

        self.hide_query = CTkButton(master=self.tabview.tab("New Book"),text="       Hide       ",fg_color="#0077b6",
                                    width=30,height=25,corner_radius=20,font=button_font,command=self.hide_copies)
        self.hide_query.place(relx=0.315,rely=0.97,anchor=tk.SW)

        book_conn.commit()
        book_conn.close()

    # Query 3
    def print_authors(self):
        book_conn = sqlite3.connect('Database_copy.db')

        button_font = CTkFont(family='Helvetica',size=16)
        print_font = CTkFont(family='Helvetica',size=18)
        
        
        print_table = pd.read_sql(f"""SELECT *
                                FROM BOOK_AUTHORS;""",book_conn)


        self.print_label = tk.Text(self.tabview.tab("New Book"),font=print_font,width=40,height=10)
        scroll_bar = CTkScrollbar(self.tabview.tab("New Book"),command=self.print_label.yview)

        self.print_label.configure(yscrollcommand=scroll_bar.set)
        self.print_label.place(relx=0.50,rely=0.60,anchor=tk.CENTER)

        columns = "\t\t".join(print_table.columns)
        self.print_label.insert(tk.END,columns)


        for index,row in print_table.iterrows():
            self.print_label.insert(tk.END,f"\n{row[0]}\t\t{row[1]}")


        self.print_label.configure(state="disabled")

        self.hide_query = CTkButton(master=self.tabview.tab("New Book"),text="    Hide    ",fg_color="#0077b6",
                                    width=30,height=25,corner_radius=20,font=button_font,command=self.hide_copies)
        self.hide_query.place(relx=0.16,rely=0.97,anchor=tk.SW)

        book_conn.commit()
        book_conn.close()

    # Query 3
    def print_book(self):
        book_conn = sqlite3.connect('Database_copy.db')

        button_font = CTkFont(family='Helvetica',size=16)
        print_font = CTkFont(family='Helvetica',size=18)
        
        # card_cur = card_conn.cursor()
        print_table = pd.read_sql(f"""SELECT title, book_publisher
                                FROM BOOK
                                ORDER BY book_id ASC;""",book_conn)


        self.print_label = tk.Text(self.tabview.tab("New Book"),font=print_font,width=60,height=10)
        scroll_bar = CTkScrollbar(self.tabview.tab("New Book"),command=self.print_label.yview)

        self.print_label.configure(yscrollcommand=scroll_bar.set)
        self.print_label.place(relx=0.50,rely=0.60,anchor=tk.CENTER)

        columns = "\t\t\t\t".join(print_table.columns)
        self.print_label.insert(tk.END,columns)


        for index,row in print_table.iterrows():
            self.print_label.insert(tk.END,f"\n{row[0]}\t\t\t\t{row[1]}")


        self.print_label.configure(state="disabled")

        self.hide_query = CTkButton(master=self.tabview.tab("New Book"),text="  Hide  ",fg_color="#0077b6",
                                    width=30,height=25,corner_radius=20,font=button_font,command=self.hide_copies)
        self.hide_query.place(relx=0.03,rely=0.97,anchor=tk.SW)

        book_conn.commit()
        book_conn.close()


    # Query 4
    def loan_num(self):
        loan_conn = sqlite3.connect('Database_copy.db')

        button_font = CTkFont(family='Helvetica',size=16)
        print_font = CTkFont(family='Helvetica',size=18)

        title = self.book_title_input.get()

        if title != "":
            self.book_title_input.delete('0',ck.END)
            print_table = pd.read_sql(f"""
                            SELECT lb.branch_name AS Branch, COUNT(bl.branch_id) AS Counts
                            FROM BOOK_LOANS bl
                            JOIN BOOK b ON b.book_id = bl.book_id
                            JOIN LIBRARY_BRANCH lb ON lb.branch_id = bl.branch_id
                            WHERE lb.branch_id IN (SELECT branch_id FROM LIBRARY_BRANCH)
                            AND b.title = '{title}'
                            GROUP BY bl.branch_id;""",loan_conn)


            self.print_label = tk.Text(self.tabview.tab("List Book Copies"),font=print_font,width=25,height=5)
            scroll_bar = CTkScrollbar(self.tabview.tab("List Book Copies"),command=self.print_label.yview)

            self.print_label.configure(yscrollcommand=scroll_bar.set)
            self.print_label.place(relx=0.50,rely=0.52,anchor=tk.CENTER)

            columns = "\t\t".join(print_table.columns)
            self.print_label.insert(tk.END,columns)


            for index,row in print_table.iterrows():
                self.print_label.insert(tk.END,f"\n{row[0]}\t\t{row[1]}")


            self.print_label.configure(state="disabled")

            self.hide_query = CTkButton(master=self.tabview.tab("List Book Copies"),text="  Hide  ",fg_color="#0077b6",
                                        width=30,height=25,corner_radius=20,font=button_font,command=self.hide_copies)
            self.hide_query.place(relx=0.97,rely=0.97,anchor=tk.SE)



        else:
            self.print_label = CTkLabel(self.tabview.tab("List Book Copies"),text="Book Name is empty",font=print_font)
            self.print_label.place(relx=0.50,rely=0.60,anchor=tk.CENTER)


            self.hide_query = CTkButton(master=self.tabview.tab("List Book Copies"),text="  Hide  ",fg_color="#0077b6",
                                        width=30,height=25,corner_radius=20,font=button_font,command=self.hide_copies)
            self.hide_query.place(relx=0.97,rely=0.97,anchor=tk.SE)

        loan_conn.commit()
        loan_conn.close()

    # Query 5
    def date_query(self):
        date_conn = sqlite3.connect('Database_copy.db')

        button_font = CTkFont(family='Helvetica',size=16)
        print_font = CTkFont(family='Helvetica',size=18)

        start_date = self.start_da_input.get()
        end_date = self.end_da_input.get()

        if start_date != "" and end_date != "":
            self.end_da_input.delete('0',ck.END)
            self.start_da_input.delete('0',ck.END)
            print_table = pd.read_sql(f"""SELECT bl.card_no,b.title, 
                                    julianday(bl.returned_date) - julianday(bl.due_date) Late_Day 
                                    FROM BOOK_LOANS bl 
                                    NATURAL JOIN BOOK b 
                                    WHERE (bl.due_date BETWEEN '{start_date}' AND '{end_date}') 
                                    And bl.Late = 1;""",date_conn)


            self.print_label = tk.Text(self.tabview.tab("Late Return"),font=print_font,width=60,height=10)
            scroll_bar = CTkScrollbar(self.tabview.tab("Late Return"),command=self.print_label.yview)

            self.print_label.configure(yscrollcommand=scroll_bar.set)
            self.print_label.place(relx=0.50,rely=0.52,anchor=tk.CENTER)

            columns = "\t\t\t".join(print_table.columns)
            self.print_label.insert(tk.END,columns)


            for index,row in print_table.iterrows():
                self.print_label.insert(tk.END,f"\n{row[0]}\t\t{row[1]}\t\t\t\t{row[2]}")


            self.print_label.configure(state="disabled")

            self.hide_query = CTkButton(master=self.tabview.tab("Late Return"),text="  Hide  ",fg_color="#0077b6",
                                        width=30,height=25,corner_radius=20,font=button_font,command=self.hide_copies)
            self.hide_query.place(relx=0.97,rely=0.97,anchor=tk.SE)
            
        elif start_date == "" and end_date != "":

            self.print_label = CTkLabel(self.tabview.tab("Late Return"),text="Start Date is required",font=print_font)
            self.print_label.place(relx=0.50,rely=0.52,anchor=tk.CENTER)
            self.hide_query = CTkButton(master=self.tabview.tab("Late Return"),text="  Hide  ",fg_color="#0077b6",
                                        width=30,height=25,corner_radius=20,font=button_font,command=self.hide_copies)
            self.hide_query.place(relx=0.97,rely=0.97,anchor=tk.SE)

        elif start_date != "" and end_date == "":

            self.print_label = CTkLabel(self.tabview.tab("Late Return"),text="End Date is required",font=print_font)
            self.print_label.place(relx=0.50,rely=0.52,anchor=tk.CENTER)
            self.hide_query = CTkButton(master=self.tabview.tab("Late Return"),text="  Hide  ",fg_color="#0077b6",
                                        width=30,height=25,corner_radius=20,font=button_font,command=self.hide_copies)
            self.hide_query.place(relx=0.97,rely=0.97,anchor=tk.SE)

        else:
            self.print_label = CTkLabel(self.tabview.tab("Late Return"),text="Start and End Date is required",font=print_font)
            self.print_label.place(relx=0.50,rely=0.52,anchor=tk.CENTER)
            self.hide_query = CTkButton(master=self.tabview.tab("Late Return"),text="  Hide  ",fg_color="#0077b6",
                                        width=30,height=25,corner_radius=20,font=button_font,command=self.hide_copies)
            self.hide_query.place(relx=0.97,rely=0.97,anchor=tk.SE)

        date_conn.commit()
        date_conn.close()

    # Query 6a
    def late_fee_check(self):
        late_fee_conn = sqlite3.connect('Database_copy.db')

        button_font = CTkFont(family='Helvetica',size=16)
        print_font = CTkFont(family='Helvetica',size=18)

        id = self.bor_id_input.get()
        name = self.bor_nm_input.get()

        if id != "" and name == "":
            self.bor_id_input.delete('0',ck.END)
            
            print_table = pd.read_sql(f"""SELECT card_no,name, 
                                    CASE WHEN LateFeeBalance > 0 THEN '$'||LateFeeBalance ELSE '$0.00' END Late_Balance 
                                    FROM vBookLoanInfo 
                                    WHERE card_no = '{id}' 
                                    ORDER BY card_no DESC;""",late_fee_conn)

            self.print_label = tk.Text(self.tabview.tab("Late Fee"),font=print_font,width=45,height=7)
            scroll_bar = CTkScrollbar(self.tabview.tab("Late Fee"),command=self.print_label.yview)

            self.print_label.configure(yscrollcommand=scroll_bar.set)
            self.print_label.place(relx=0.50,rely=0.52,anchor=tk.CENTER)

            columns = "\t\t".join(print_table.columns)
            self.print_label.insert(tk.END,columns)


            for index,row in print_table.iterrows():
                self.print_label.insert(tk.END,f"\n{row[0]}\t\t{row[1]}\t\t{row[2]}")


            self.print_label.configure(state="disabled")

            self.hide_query = CTkButton(master=self.tabview.tab("Late Fee"),text="  Hide  ",fg_color="#0077b6",
                                        width=30,height=25,corner_radius=20,font=button_font,command=self.hide_copies)
            self.hide_query.place(relx=0.97,rely=0.97,anchor=tk.SE)
        
        elif name!= "" and id == "":
            self.bor_nm_input.delete('0',ck.END)

            print_table = pd.read_sql(f"""SELECT card_no,name,
                                    CASE WHEN LateFeeBalance > 0 THEN '$'||LateFeeBalance ELSE '$0.00' END Late_Balance 
                                    FROM vBookLoanInfo 
                                    WHERE name LIKE '%{name}%' 
                                    ORDER BY card_no DESC;""",late_fee_conn)
            
            self.print_label = tk.Text(self.tabview.tab("Late Fee"),font=print_font,width=45,height=7)
            scroll_bar = CTkScrollbar(self.tabview.tab("Late Fee"),command=self.print_label.yview)

            self.print_label.configure(yscrollcommand=scroll_bar.set)
            self.print_label.place(relx=0.50,rely=0.52,anchor=tk.CENTER)

            columns = "\t\t".join(print_table.columns)
            self.print_label.insert(tk.END,columns)


            for index,row in print_table.iterrows():
                self.print_label.insert(tk.END,f"\n{row[0]}\t\t{row[1]}\t\t{row[2]}")


            self.print_label.configure(state="disabled")

            self.hide_query = CTkButton(master=self.tabview.tab("Late Fee"),text="  Hide  ",fg_color="#0077b6",
                                        width=30,height=25,corner_radius=20,font=button_font,command=self.hide_copies)
            self.hide_query.place(relx=0.97,rely=0.97,anchor=tk.SE)
        
        elif name == "" and id == "":
            
            print_table = pd.read_sql(f"""SELECT card_no,name,
                                    CASE WHEN LateFeeBalance > 0 THEN '$'||LateFeeBalance ELSE '$0.00' END Late_Balance 
                                    FROM vBookLoanInfo 
                                    ORDER BY LateFeeBalance DESC;""",late_fee_conn)

            self.print_label = tk.Text(self.tabview.tab("Late Fee"),font=print_font,width=45,height=7)
            scroll_bar = CTkScrollbar(self.tabview.tab("Late Fee"),command=self.print_label.yview)

            self.print_label.configure(yscrollcommand=scroll_bar.set)
            self.print_label.place(relx=0.50,rely=0.52,anchor=tk.CENTER)

            columns = "\t\t".join(print_table.columns)
            self.print_label.insert(tk.END,columns)


            for index,row in print_table.iterrows():
                self.print_label.insert(tk.END,f"\n{row[0]}\t\t{row[1]}\t\t{row[2]}")


            self.print_label.configure(state="disabled")

            self.hide_query = CTkButton(master=self.tabview.tab("Late Fee"),text="  Hide  ",fg_color="#0077b6",
                                        width=30,height=25,corner_radius=20,font=button_font,command=self.hide_copies)
            self.hide_query.place(relx=0.97,rely=0.97,anchor=tk.SE)

        late_fee_conn.commit()
        late_fee_conn.close()
    
        # Query 6b
    def book_info_query(self):
        info_conn = sqlite3.connect('Database_copy.db')

        button_font = CTkFont(family='Helvetica',size=16)
        print_font = CTkFont(family='Helvetica',size=18)

        id = self.book_id_input.get()
        title = self.book_ti_input.get()

        if id != "" and title == "":
            self.book_id_input.delete('0',ck.END)

            print_table = pd.read_sql(f"SELECT title,CASE WHEN LateFeeBalance > 0 THEN (CASE When LateFeeBalance LIKE '%.__' THEN '$'||LateFeeBalance ELSE '$'||LateFeeBalance||'0' END) ELSE 'N/A' END Late_Fee FROM vBookLoanInfo NATURAL JOIN BOOK b WHERE b.book_id = '{id}' ORDER BY LateFeeBalance DESC;",info_conn)

            self.print_label = tk.Text(self.tabview.tab("Book Information"),font=print_font,width=42,height=10)
            scroll_bar = CTkScrollbar(self.tabview.tab("Book Information"),command=self.print_label.yview)

            self.print_label.configure(yscrollcommand=scroll_bar.set)
            self.print_label.place(relx=0.50,rely=0.52,anchor=tk.CENTER)

            columns = "\t\t\t\t".join(print_table.columns)
            self.print_label.insert(tk.END,columns)


            for index,row in print_table.iterrows():
                self.print_label.insert(tk.END,f"\n{row[0]}\t\t\t\t{row[1]}")


            self.print_label.configure(state="disabled")

            self.hide_query = CTkButton(master=self.tabview.tab("Book Information"),text="  Hide  ",fg_color="#0077b6",
                                        width=30,height=25,corner_radius=20,font=button_font,command=self.hide_copies)
            self.hide_query.place(relx=0.97,rely=0.97,anchor=tk.SE)
        
        elif id == "" and title != "":
            self.book_ti_input.delete('0',ck.END)

            print_table = pd.read_sql(f"SELECT title,CASE WHEN LateFeeBalance > 0 THEN (CASE When LateFeeBalance LIKE '%.__' THEN '$'||LateFeeBalance ELSE '$'||LateFeeBalance||'0' END) ELSE 'N/A' END Late_Fee FROM vBookLoanInfo WHERE title LIKE '%{title}%' ORDER BY LateFeeBalance DESC;",info_conn)

            self.print_label = tk.Text(self.tabview.tab("Book Information"),font=print_font,width=42,height=10)
            scroll_bar = CTkScrollbar(self.tabview.tab("Book Information"),command=self.print_label.yview)

            self.print_label.configure(yscrollcommand=scroll_bar.set)
            self.print_label.place(relx=0.50,rely=0.52,anchor=tk.CENTER)

            columns = "\t\t\t\t".join(print_table.columns)
            self.print_label.insert(tk.END,columns)


            for index,row in print_table.iterrows():
                self.print_label.insert(tk.END,f"\n{row[0]}\t\t\t\t{row[1]}")


            self.print_label.configure(state="disabled")

            self.hide_query = CTkButton(master=self.tabview.tab("Book Information"),text="  Hide  ",fg_color="#0077b6",
                                        width=30,height=25,corner_radius=20,font=button_font,command=self.hide_copies)
            self.hide_query.place(relx=0.97,rely=0.97,anchor=tk.SE)


        elif id == "" and title == "":
            
            print_table = pd.read_sql(f"SELECT title,CASE WHEN LateFeeBalance > 0 THEN (CASE When LateFeeBalance LIKE '%.__' THEN '$'||LateFeeBalance ELSE '$'||LateFeeBalance||'0' END) ELSE 'N/A' END Late_Fee FROM vBookLoanInfo ORDER BY LateFeeBalance DESC;",info_conn)

            self.print_label = tk.Text(self.tabview.tab("Book Information"),font=print_font,width=42,height=10)
            scroll_bar = CTkScrollbar(self.tabview.tab("Book Information"),command=self.print_label.yview)

            self.print_label.configure(yscrollcommand=scroll_bar.set)
            self.print_label.place(relx=0.50,rely=0.52,anchor=tk.CENTER)

            columns = "\t\t\t\t".join(print_table.columns)
            self.print_label.insert(tk.END,columns)


            for index,row in print_table.iterrows():
                self.print_label.insert(tk.END,f"\n{row[0]}\t\t\t\t{row[1]}")


            self.print_label.configure(state="disabled")

            self.hide_query = CTkButton(master=self.tabview.tab("Book Information"),text="  Hide  ",fg_color="#0077b6",
                                        width=30,height=25,corner_radius=20,font=button_font,command=self.hide_copies)
            self.hide_query.place(relx=0.97,rely=0.97,anchor=tk.SE)




        info_conn.commit()
        info_conn.close()

    def hide_copies(self):
        self.print_label.place_forget()
        self.hide_query.place_forget()


    def go_back_into(self):
        self.home_frame.pack_forget()
        self.create_into_frame()



    def run(self):
        self.window.mainloop()
