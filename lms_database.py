from tkinter import *
import set_theme
import navbar
import sqlite3

def main():
    window = set_theme.setTheme()

    window_w_navbar = navbar.navBar(window)

    window_w_navbar.mainloop()




if __name__ == "__main__":
    main()