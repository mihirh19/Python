from tkinter import *

root = Tk()
root.geometry("644x566")

f1 = Frame(root, bg="red", borderwidth=6, )
la = Label(f1,text="Project")
f1.pack(fill="y")
la.pack()


f2 = Frame(root, borderwidth=8, background="grey", relief=SUNKEN)
f2.pack(side=TOP)

root.mainloop()