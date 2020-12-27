from tkinter import *

root = Tk()

e = Entry(root, width=50, bg="blue", fg="white", borderwidth=5)
e.pack()
e.insert(0, "Enter your name: ")


def myClick():
    hello = "Hello " + e.get()
    my_label = Label(root, text=hello)
    my_label.pack()


myButton = Button(root, text="Enter name", padx=50, pady=50, command=myClick, fg="green", bg="#eeeeee")
myButton.pack()

root.mainloop()
