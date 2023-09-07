from tkinter import *


gui = Tk()
gui.geometry("270x150")
from time import strftime


def my_time():
    time_string = strftime('%H:%M:%S %p')  # time format
    l1.config(text=time_string)
    l1.after(1000, my_time)  # time delay of 1000 milliseconds


my_font = ('times', 52, 'light')  # display size and style
gui.title("TIME")

l1 = Label(gui, font=my_font, bg='light green')
l1.grid(row=1, column=1, padx=5, pady=25)

my_time()
gui.mainloop()