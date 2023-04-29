from tkinter import Tk
import initial_window


def main():
    window = Tk()
    initial_window.setWindow(window)




if __name__ == "__main__":
    main()

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
