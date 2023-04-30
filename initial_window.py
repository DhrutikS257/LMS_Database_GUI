from PIL import Image,ImageTk
import customtkinter as ck
from customtkinter import CTkImage
from customtkinter import CTkFont
from customtkinter import CTkButton
import tkinter as tk




class App:
    def __init__(self,window):
        self.window = window
        self.window.title("LMS Database")
        self.window.geometry("1400x1200")
        self.window.iconbitmap("icons/bookshelf.ico")
        # self.window.resizable(False,False)
        self.create_into_frame()

    

    def create_into_frame(self):
        self.into_frame = ck.CTkFrame(master=self.window)
        self.into_frame.pack(fill='both', expand=True)

        lib_png = CTkImage(dark_image=Image.open("icons/bookshelf.png"),size=(650,700))
        lib_label = ck.CTkLabel(master=self.into_frame,image=lib_png, text="")
        lib_label.pack(pady=30)

        title_font = CTkFont(family='Helvetica',size=32,weight='bold')
        intro_label = ck.CTkLabel(master=self.into_frame,text="Welcome to LMS Database",font=title_font)
        intro_label.pack(pady=30)

        button_font = CTkFont(family='Helvetica',size=18)
        get_started = CTkButton(master=self.into_frame,text="Get Started",fg_color="#0077b6",
                                width=60,height=50,corner_radius=20,font=button_font,command = self.home_screen)
        get_started.pack(pady=30)


    def home_screen(self):
        self.into_frame.pack_forget()
        self.home_frame = ck.CTkFrame(master=self.window)
        self.home_frame.pack(fill='both', expand=True)

        button_font = CTkFont(family='Helvetica',size=24)
        go_back_button = CTkButton(master=self.home_frame, text="Back",fg_color="#0077b6",
                                    width=60,height=50,corner_radius=20,font=button_font,command=self.go_back_into)
        go_back_button.place(x = 20, y = 1175, anchor=tk.SW)

    def go_back_into(self):
        self.home_frame.pack_forget()
        self.create_into_frame()



    def run(self):
        self.window.mainloop()

# import tkinter as tk

# class App(tk.Frame):
#     def __init__(self, master=None):
#         super().__init__(master)
#         self.pack()
#         self.create_widgets()

#     def create_widgets(self):
#         # Create the first screen
#         self.screen1 = tk.Frame(self)
#         self.screen1.pack()

#         self.label1 = tk.Label(self.screen1, text="Screen 1")
#         self.label1.pack()

#         self.button1 = tk.Button(self.screen1, text="Next", command=self.show_screen2)
#         self.button1.pack()

#         # Create the second screen
#         self.screen2 = tk.Frame(self)
#         self.screen2.pack()

#         self.label2 = tk.Label(self.screen2, text="Screen 2")
#         self.label2.pack()

#         self.button2 = tk.Button(self.screen2, text="Back", command=self.show_screen1)
#         self.button2.pack()

#         # Hide the second screen initially
#         self.screen2.pack_forget()

#     def show_screen1(self):
#         # Hide the second screen and show the first screen
#         self.screen2.pack_forget()
#         self.screen1.pack()

#     def show_screen2(self):
#         # Hide the first screen and show the second screen
#         self.screen1.pack_forget()
#         self.screen2.pack()

# app = App()
# app.mainloop()

# def setWindow(window):
    
#     style = ttk.Style()
#     style.theme_use('clam')

#     window.title("LMS Database")
#     window.geometry("600x450")
#     window.configure(bg = Dg)
#     window.resizable(False,False)
#     window.iconbitmap("icons/bookshelf.ico")

#     frame1 = Frame(window, bg= Dg)
#     frame1.pack(fill='both', expand=True)
#     image = Image.open("icons/bookshelf.png")
#     image = image.resize((150,200),Image.ANTIALIAS)
#     photo = ImageTk.PhotoImage(image)
#     image_label = Label(frame1,image=photo,bg = Dg)
#     image_label.pack()

#     title_font = font.Font(family='Helvetica', size=16, weight='bold')
#     title_label = Label(frame1, text="Welcome to LMS Database", font=title_font,bg = Dg, fg = Fg, pady= 40)
#     title_label.pack(pady=20)
    
#     get_started = Button(frame1,text="Get Started", fg = Fg, bg = Bg, width= 15, height= 2, 
#                         borderwidth=0, relief="ridge", activebackground="#ffffff")
#     get_started.pack()

    
#     window.mainloop()
