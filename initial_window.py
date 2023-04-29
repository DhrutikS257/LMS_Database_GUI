from PIL import Image,ImageTk
import customtkinter as ck
from customtkinter import CTkImage
from customtkinter import CTkFont
from customtkinter import CTkButton
# import tkinter as tk

Bg = '#242526'
Dg = '#18191A'
Fg = '#ffffff'

class App:
    def __init__(self,window):
        self.window = window
        self.window.title("LMS Database")
        self.window.geometry("600x450")
        self.window.iconbitmap("icons/bookshelf.ico")

        into_frame = ck.CTkFrame(master=self.window)
        into_frame.pack(fill='both', expand=True)

        lib_png = CTkImage(dark_image=Image.open("icons/bookshelf.png"),size=(150,200))
        lib_label = ck.CTkLabel(master=into_frame,image=lib_png, text="")
        lib_label.pack()

        title_font = CTkFont(family='Helvetica',size=16,weight='bold')
        intro_label = ck.CTkLabel(master=into_frame,text="Welcome to LMS Database",font=title_font,pady=40)
        intro_label.pack()

        button_font = CTkFont(family='Helvetica',size=12)
        get_started = CTkButton(master=into_frame,text="Get Started",fg_color="#0077b6",width=40,height=30,corner_radius=10,font=button_font)
        get_started.pack()
        



    def run(self):
        self.window.mainloop()



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
