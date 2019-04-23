from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("3 Address Code")

p = [(21, 2), (37, 98), (8, 898)]
q = [(21, 2), (37, 98), (8, 898)]


def val():
    sy = ""
    ty = ""
    d = e1.get()
    print(d)
    for i in p:
        sy += "( "
        ty += "( "
        for x in i:
            sy += str(x)+" "
            ty += str(x)+" "
        sy += ")\n"
        ty += ")\n"

    l2 = Label(middleframe, text="Symbol Table\n"+sy, font=30, padx=150, pady=20)
    l3 = Label(middleframe, text="Literal Table\n"+sy, font=30, padx=150, pady=20)
    l2.pack(side=LEFT)
    l3.pack(side=LEFT)
    panel.pack(side="right", fill="both", expand="yes")
    l4 = Label(bottomframe, text="Symbol Table\n"+sy, font=30, padx=150)
    l5 = Label(bottomframe, text="Symbol Table\n"+sy, font=30, padx=150)
    l6 = Label(bottomframe, text="Symbol Table\n"+sy, font=30, padx=150)
    l4.pack(side=LEFT)
    l5.pack(side=LEFT)
    l6.pack(side=LEFT)


topframe = Frame(root)
topframe.pack(side=TOP, padx=30)
middleframe = Frame(root, bg="blue")
middleframe.pack(fill=X, padx=30)
bottomframe = Frame(root)
bottomframe.pack(side=BOTTOM, fill=X, padx=30)

l1 = Label(topframe, text="Expression :- ", font=30).grid(row=0, column=5)

e1 = Entry(topframe)
e1.grid(row=0, column=8)

b1 = Button(topframe, text="Submit", command=val, font=30, padx=20, anchor=W)
b2 = Button(bottomframe, text="Quit", command=root.quit, font=30, padx=20)
b1.grid(row=0, column=10)
b2.pack(side=BOTTOM)

path = "cr7.jpeg"
im = Image.open(path)
im = im.resize((250, 250), Image.ANTIALIAS)
imager = ImageTk.PhotoImage(im)
panel = Label(middleframe, image=imager, pady=20, text='Syntax Tree')

root.mainloop()
