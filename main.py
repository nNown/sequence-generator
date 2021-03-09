from tkinter import *
from gui import Application

if __name__ == "__main__":
    root = Tk()
    root.geometry("600x740")
    app = Application(master=root)
    app.mainloop()