from tkinter import *


def getval():
    print(uservalue.get())

root = Tk()
root.geometry("655x256")
user = Label(root, text="Username")
passw =Label(root, text="password")
user.grid()
passw.grid(row=1)

## variable class in tkinter
# boolen, double, int , str,

uservalue = StringVar()
passvalue = StringVar()

userentry = Entry(root, textvariable=uservalue)
passentry = Entry(root, textvariable=passvalue)
userentry.grid(row=0, column=1)
passentry.grid(row=1, column=1)

Button(text="Submit", command=getval).grid()

root.mainloop()