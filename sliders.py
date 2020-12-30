from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Sliders.... ")
root.iconbitmap('images/codemy.ico')


def slide():
    my_label = Label(root, text=horizontal.get()).pack()
    my_label_2 = Label(root, text=vertical.get()).pack()
    root.geometry(str(horizontal.get()), + 'x' + str(vertical.get()))


root.geometry('400x400')

vertical = Scale(root, from_=0, to=200)
vertical.pack()

horizontal = Scale(root, from_=0, to=200, orient=HORIZONTAL)
horizontal.pack()

my_label = Label(root, text=horizontal.get()).pack()
my_button = Button(root, text='Click me', command=slide).pack()

root.mainloop()


