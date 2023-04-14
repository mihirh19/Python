from tkinter import *


if __name__ == '__main__':

    root = Tk()
    root.title("GUI")
    root.geometry("544x444")

    # label option
    # text -- add text
    # bd  -- background
    # fg --fore ground
    # font -- set font
    # padx  --- x padding
    # pady --- y padding
    # relief --- border styling --- SUNKEN, RAISED, GROOVE RIDGE

    title_labal = Label(text="Mihir\nHadavani", background="blue", foreground="white", font=("Cascadia Code", 19, "bold"), pady=56, padx=26, borderwidth=3, relief=SUNKEN)


# important pack option
#     anchor  = nw    north - west
#     sw = south -east
# side = top bottom

    # title_labal.pack(anchor="ne", side=BOTTOM)
    title_labal.pack(fill=Y, side=LEFT)
    root.mainloop()