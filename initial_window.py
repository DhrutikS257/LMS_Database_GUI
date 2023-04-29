from PIL import Image,ImageTk
from tkinter import Tk,Menu,font, Label, ttk, Button, Frame,Grid

Bg = '#242526'
Dg = '#18191A'
Fg = '#ffffff'



def setWindow(window):
    
    style = ttk.Style()
    style.theme_use('clam')

    window.title("LMS Database")
    window.geometry("600x450")
    window.configure(bg = Dg)
    window.resizable(False,False)
    window.iconbitmap("icons/bookshelf.ico")

    frame1 = Frame(window, bg= Dg)
    frame1.pack(fill='both', expand=True)
    image = Image.open("icons/bookshelf.png")
    image = image.resize((150,200),Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(image)
    image_label = Label(frame1,image=photo,bg = Dg)
    image_label.pack()

    title_font = font.Font(family='Helvetica', size=16, weight='bold')
    title_label = Label(frame1, text="Welcome to LMS Database", font=title_font,bg = Dg, fg = Fg, pady= 40)
    title_label.pack(pady=20)

    

    get_started = Button(frame1,text="Get Started", fg = Fg, bg = Bg, width= 15, height= 2, 
                        borderwidth=0, relief="ridge", activebackground="#ffffff")
    get_started.pack()

    
    window.mainloop()
