from tkinter import *

root = Tk()

root.geometry("300x200")
v_red = IntVar()
v_green = IntVar()

root.title("Ampelsteuerung")

def red_trigger():
    print("Red_Trigger")
    if v_red.get() == 1:
        c_ampel.itemconfig(o_red, fill="#FF0000")
        c_ampel.itemconfig(o_green, fill="#555555")
        v_green.set(0)
    else:
        c_ampel.itemconfig(o_red, fill="#555555")

def green_trigger():
    print("Green_Trigger")
    if v_green.get() == 1:
        c_ampel.itemconfig(o_green, fill="#00FF00")
        c_ampel.itemconfig(o_red, fill="#555555")
        v_red.set(0)
    else:
        c_ampel.itemconfig(o_green, fill="#555555")

canvas_width = 100
canvas_height = 180

c_ampel = Canvas(root, width=canvas_width, height=canvas_height)
c_ampel.grid(row=0,column=0, rowspan=3)

c_ampel.create_rectangle(10, 10, 100, 200, fill="#000000")
o_red = c_ampel.create_oval(20, 20, 90, 90, fill="#555555")
o_green = c_ampel.create_oval(20, 100, 90, 170, fill="#555555")


Label(root, text="Ampel-ID: ").grid(row=0,column=1)

rb_red = Checkbutton(root, text="red", variable=v_red, command=red_trigger).grid(row=1,column=1)
rb_green = Checkbutton(root, text="green", variable=v_green, command=green_trigger).grid(row=2,column=1)



# sign_width = 150
# sign_heigth = 300
# ampel = Canvas(root, width=sign_width, height=sign_heigth)
# ampel.pack()
# ampel.create_text(25,75,text="Ampel")
# ampel.create_rectangle(0,25,100,150, fill="red")
# ampel.create_rectangle(0,35,20,55, fill="green")

root.mainloop()