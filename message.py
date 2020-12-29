from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Message Box")
root.iconbitmap('images/codemy.ico')


def popup():
    # messagebox.showinfo("This is a popup", "Hello Paul")
    # messagebox.showwarning("This is a popup", "Hello Paul")
    # messagebox.showerror("This is a popup", "Hello Paul")
    # messagebox.askquestion("This is a popup", "Hello Paul")
    # messagebox.askokcancel("This is a popup", "Hello Paul")
    # Label(root, text=response).pack()

    response = messagebox.askyesno("This is a popup", "Hello Paul")
    msg = "You clicked "
    answer = "Yes"

    if response == 0:
        answer = "No"

    Label(root, text=msg + answer).pack()


Button(root, text="Popup", command=popup).pack()


root.mainloop()
