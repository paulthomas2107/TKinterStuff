from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Checkboxes.... ")
root.iconbitmap('images/codemy.ico')
root.geometry('400x400')


def show():
    my_label = Label(root, text=var.get()).pack()


var = StringVar()

c = Checkbutton(root, text='Check me', variable=var, onvalue="ON", offvalue="OFF")
c.deselect()
c.pack()

my_button = Button(root, text='Show me', command=show).pack()

root.mainloop()
