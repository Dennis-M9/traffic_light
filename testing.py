from tkinter import *

root = Tk()

canvas_width = 50
canvas_height = 25
color = ["#FF0000", "#00FF00"]
i = 0

def change():
    global i
    if i == 1:
        i = 0
    elif i == 0:
        i = 1
    else:
        i = 0
    c.itemconfig(r, fill=color[i])

c = Canvas(root, width=canvas_width, height=canvas_height)
c.pack()
r = c.create_rectangle(0,0,50,25,fill=color[0])



b = Button(root, text="CHANGE", command=change)
b.pack()

root.mainloop()