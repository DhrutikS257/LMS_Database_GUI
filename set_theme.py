from ttkthemes import ThemedTk
from ttkthemes import ThemedStyle

def setTheme():
    window = ThemedTk(theme="Equilux")
    style = ThemedStyle(window)
    style.set_theme("black")
    window.title("LMS Database")
    window.geometry("600x450")
    window.iconbitmap("icons/database_logo.ico")
    return window