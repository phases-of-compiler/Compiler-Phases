from tkinter import *
from PIL import Image, ImageTk
from tkintertable import TableCanvas

root = Tk()
root.title("3 Address Code")


def val():
    d = e1.get()
    panel.pack(side="right", fill="both", expand="yes")
    mtable.show()
    table1.show()
    table2.show()
    table3.show()


topframe = Frame(root)
topframe.pack(side=TOP, padx=30)
middleframe = Frame(root, bg="blue")
middleframe.pack(fill=X, padx=30)
bottomframe = Frame(root)
bottomframe.pack(side=BOTTOM, fill=X, padx=30)

l1 = Label(topframe, text="Expression :- ", font=30).pack(side=LEFT)

e1 = Entry(topframe)
e1.pack(side=LEFT)

b1 = Button(topframe, text="Submit", command=val, font=30, padx=20, anchor=W)
b2 = Button(bottomframe, text="Quit", command=root.quit, font=30, padx=20)
b1.pack(side=LEFT)
b2.pack(side=BOTTOM)

path = "cr7.jpeg"
im = Image.open(path)
im = im.resize((286, 347), Image.ANTIALIAS)
imager = ImageTk.PhotoImage(im)
panel = Label(middleframe, image=imager, pady=20, text='Syntax Tree')


syt = {'5': (5, 'LT', '5'), 'd': (3, 'ID', 'd')}

syt_val = list(syt.values())

data = {}

for i in range(len(syt.keys())):
    data['rec'+str(i)] = {'Index': syt_val[i][0], 'Label': syt_val[i][1], 'Value': syt_val[i][2]}


mframe = Frame(middleframe)
mframe.pack(side=LEFT)
mtable = TableCanvas(mframe, data=data, editable=False, cellwidth=100)

bframe1 = Frame(bottomframe)
bframe2 = Frame(bottomframe)
bframe3 = Frame(bottomframe)

bframe1.pack(side=LEFT)
table1 = TableCanvas(bframe1, data=data, editable=False, cellwidth=100)
bframe2.pack(side=LEFT)
table2 = TableCanvas(bframe2, data=data, editable=False, cellwidth=100)
bframe3.pack(side=LEFT)
table3 = TableCanvas(bframe3, data=data, editable=False, cellwidth=53)

root.mainloop()
