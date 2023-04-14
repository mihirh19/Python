from tkinter import *

def hello():
    print("hello")

if __name__ == '__main__':

    root = Tk()
    root.geometry("444x350")
    f1 = Frame(root, borderwidth=6, bg="grey", relief=SUNKEN)
    f1.pack(side=LEFT, anchor="nw")
    b1 = Button(f1, fg="red", text="print now", command =hello)
    b1.pack(side=LEFT)
    b2 = Button(f1, fg="red", text="print now")
    b2.pack(side=LEFT)
    b3 = Button(f1, fg="red", text="print now")
    b3.pack(side=LEFT)
    b4 = Button(f1, fg="red", text="print now")
    b4.pack(side=LEFT)


    root.mainloop()