from tkinter import *

root = Tk()
root.geometry("444x415")   ## default size
root.minsize(300, 100)  #min size

name = Label(text = "hello mihir")   ## text
name.pack()
root.mainloop()