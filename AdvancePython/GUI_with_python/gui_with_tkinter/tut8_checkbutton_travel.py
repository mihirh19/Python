from tkinter import *

def getval():
    pass



if __name__ == '__main__':

    root = Tk()
    root.geometry("644x355")
    Label(root, text="Hello mihir", font=("cascadia code", 16, "bold"), pady=15).grid(row=0, column=3)
    name = Label(root, text="name")
    gender = Label(root, text="gender")
    name.grid(row=1, column=2)
    gender.grid(row=2, column=2)


    nameval = StringVar()
    genderval = StringVar()
    checkval = IntVar()

    nameval = Entry(root, textvariable=nameval).grid(row=1, column=3)
    genderval = Entry(root, textvariable=genderval).grid(row=2, column=3)

    # checkbox
    check = Checkbutton(text="Pre-book", variable=checkval)
    check.grid(row=3, column=3)


    # button
    Button(text="Submit", command=getval).grid(row=7, column=3)

    root.mainloop()