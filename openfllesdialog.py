from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

root = Tk()
root.title("Open Files Dialog")
root.iconbitmap('images/codemy.ico')


def open_file():
    global my_image
    root.filename = \
        filedialog.askopenfilename(initialdir=".", title="Get file", filetypes=(('png', '*.png'), ('All', '*')))
    my_label = Label(root, text=root.filename).pack()
    my_image = ImageTk.PhotoImage(Image.open(root.filename))
    my_image_label = Label(image=my_image).pack()


my_button = Button(root, text="Open me", command=open_file).pack()
root.mainloop()
