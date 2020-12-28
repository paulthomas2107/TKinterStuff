from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Frames")
root.iconbitmap('images/codemy.ico')

frame = LabelFrame(root, text="This is a Frame", padx=50,  pady=50)
frame.pack(padx=10, pady=10)

b = Button(frame, text="Don't Click")
b2 = Button(frame, text="..or here")
## b.pack()
b.grid(row=0, column=0)
b2.grid(row=1, column=1)


root.mainloop()
