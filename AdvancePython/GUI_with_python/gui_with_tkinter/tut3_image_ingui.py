from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("GUI")
root.geometry("1080x1920")
# photo = PhotoImage(file="3790078.png")   #jpg not support for jpg install pillow module

# for jpg
im = Image.open("3790078.png")
photo = ImageTk.PhotoImage(im)

pic_la = Label(image=photo)
pic_la.pack()

root.mainloop()
