from tkinter import *

root = Tk()


def myClick():
    my_label = Label(root, text="I clicked a button")
    my_label.pack()


myButton = Button(root, text="Click Me", padx=50, pady=50, command=myClick, fg="green", bg="#eeeeee")
myButton.pack()

root.mainloop()
