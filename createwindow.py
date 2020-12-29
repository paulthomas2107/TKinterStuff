from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

root = Tk()
root.title("Create Windows")
root.iconbitmap('images/codemy.ico')


def open_window():
    global my_image
    top = Toplevel()
    top.title("Windows :)")
    top.iconbitmap('images/codemy.ico')
    my_image = ImageTk.PhotoImage(Image.open("images/aspen.png"))
    my_label = Label(top, image=my_image).pack()
    btn2 = Button(top, text="Close window", command=top.destroy).pack()


btn = Button(root, text="Open 2nd window", command=open_window).pack()


root.mainloop()
