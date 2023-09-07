from tkinter import *

root = Tk()
root.geometry("500x400")

canvas1 = Canvas(root, width=400, height=300, bg="white")
canvas1.pack(pady=20)


def my_click1():
    Circle1 = canvas1.create_oval(100, 100, 160, 160, outline="blue", width=4)


button1 = Button(root, text="blue ring", command=my_click1)
# button1.pack(pady = 2)
button1.place(x=25, y=350)


def my_click2():
    Circle2 = canvas1.create_oval(135, 135, 195, 195, outline="yellow", width=4)


button2 = Button(root, text="yellow ring", command=my_click2)
# button2.pack(pady = 2)
button2.place(x=125, y=350)


def my_click3():
    Circle3 = canvas1.create_oval(170, 100, 230, 160, outline="black", width=4)


button3 = Button(root, text="black ring", command=my_click3)
# button3.pack(pady = 2)
button3.place(x=230, y=350)


def my_click4():
    Circle4 = canvas1.create_oval(205, 135, 265, 195, outline="green", width=4)


button4 = Button(root, text="green ring", command=my_click4)
# button4.pack(pady = 2)
button4.place(x=330, y=350)


def my_click5():
    Circle5 = canvas1.create_oval(240, 100, 300, 160, outline="red", width=4)


button5 = Button(root, text="red ring", command=my_click5)
# button5.pack(pady = 2)
button5.place(x=435, y=350)

button_quit = Button(root, text="Quit", command=root.destroy)
button_quit.pack(pady=50)

canvas1.pack()

root.mainloop()