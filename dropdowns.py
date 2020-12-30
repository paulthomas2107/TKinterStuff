from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Dropdowns.... ")
root.iconbitmap('images/codemy.ico')
root.geometry('400x400')


def show():
    mylabel = Label(root, text=clicked.get()).pack()


options = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]

clicked = StringVar()
clicked.set(options[1]) # Monday

drop = OptionMenu(root, clicked, *options)
drop.pack()

myButton = Button(root, text='Show me', command=show).pack()
root.mainloop()
