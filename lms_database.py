import customtkinter as ck
import initial_window

def main():
    window = ck.CTk()
    # initial_window.setWindow(window)
    my_app = initial_window.App(window)
    my_app.run()




if __name__ == "__main__":
    main()


