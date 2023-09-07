from cmath import sqrt
from math import dist
import tkinter as tk
from tkinter import ttk

root = tk.Tk()

# set the variables
width, height = 610, 410

# canvas width height
c_width, c_height = width - 10, height - 65

d = str(width) + "x" + str(height)
root.geometry("610x500")
# root.geometry(d)
c1 = tk.Canvas(root, width=c_width, height=c_height, bg='cyan')
c1.grid(row=0, column=0, padx=5, pady=5, columnspan=3)
ttk.Label(root, text=f"Mass of star 1: 4.5 x 10^30 kg. Mass of star 2: 3 x 10^30 kg").grid(column=1, row=7)


def create_circle(x, y, r, color, tag):  # center coordinates, radius
    # global object_id
    x0 = x - r
    y0 = y - r
    x1 = x + r
    y1 = y + r
    c1.create_oval(x0, y0, x1, y1, width=2, outline=color, fill=color, tags=tag)


step = 10  # Jump in each movement, change this value
x1, y1, r1, color1 = 300, 200, 35, 'blue'
x2, y2, r2, color2 = 300, 200, 20, 'red'
star_1 = create_circle(x1, y1, r1, color1, 'star1')
star_2 = create_circle(x2, y2, r2, color2, 'star2')


def right1(event):
    global x1, y1, star_1, distance, force
    x1 = x1 + step  # increase the horizontal coordinates
    c1.delete('star1')  # delete the circle
    star_1 = create_circle(x1, y1, r1, color1, 'star1')
    distance = sqrt(pow((x2 - x1), 2) + pow((y2 - y1), 2))
    force = 9.0045 * (pow(distance,
                          -2))  # 9.0045 sale de multiplicar la constante de gravitación G (6.67X10^11) por las dos masas consideradas (4.5 y 3 x10^30) dividido (10^6)^2 (ya que las distancias que estan en el denominador son del orden de 10^6 y se encuentran elevadas al cuadrado)
    # El resultado de force hay que multiplicarlo x10^60 para que de el resultado final
    ttk.Label(root, text=f"Distance: {distance} x10^6 m").grid(column=1, row=5)
    ttk.Label(root, text=f"Force: {force} x10^60 N").grid(column=1, row=6)


def left1(event):
    global x1, y1, star_1, distance
    x1 = x1 - step  # increase the horizontal coordinates
    c1.delete('star1')  # delete the circle
    star_1 = create_circle(x1, y1, r1, color1, 'star1')
    distance = sqrt(pow((x2 - x1), 2) + pow((y2 - y1), 2))
    force = 9.0045 * (pow(distance, -2))
    ttk.Label(root, text=f"Distance: {distance} x10^6 m").grid(column=1, row=5)
    ttk.Label(root, text=f"Force: {force} x10^60 N").grid(column=1, row=6)


def up1(event):
    global x1, y1, star_1, distance
    y1 = y1 - step  # decrease the vertical coordinates
    c1.delete('star1')  # delete the circle
    star_1 = create_circle(x1, y1, r1, color1, 'star1')
    distance = sqrt(pow((x2 - x1), 2) + pow((y2 - y1), 2))
    force = 9.0045 * (pow(distance, -2))
    ttk.Label(root, text=f"Distance: {distance} x10^6 m").grid(column=1, row=5)
    ttk.Label(root, text=f"Force: {force} x10^60 N").grid(column=1, row=6)


def down1(event):
    global x1, y1, star_1, distance
    y1 = y1 + step  # increase the vertical coordinates
    c1.delete('star1')  # delete the circle
    star_1 = create_circle(x1, y1, r1, color1, 'star1')
    distance = sqrt(pow((x2 - x1), 2) + pow((y2 - y1), 2))
    force = 9.0045 * (pow(distance, -2))
    ttk.Label(root, text=f"Distance: {distance} x10^6 m").grid(column=1, row=5)
    ttk.Label(root, text=f"Force: {force} x10^60 N").grid(column=1, row=6)


def right2(event):
    global x2, y2, star_2, distance
    x2 = x2 + step  # increase the horizontal coordinates
    c1.delete('star2')  # delete the circle
    star_2 = create_circle(x2, y2, r2, color2, 'star2')
    distance = sqrt(pow((x2 - x1), 2) + pow((y2 - y1), 2))
    force = 9.0045 * (pow(distance, -2))
    ttk.Label(root, text=f"Distance: {distance} x10^6 m").grid(column=1, row=5)
    ttk.Label(root, text=f"Force: {force} x10^60 N").grid(column=1, row=6)


def left2(event):
    global x2, y2, star_2, distance
    x2 = x2 - step  # increase the horizontal coordinates
    c1.delete('star2')  # delete the circle
    star_2 = create_circle(x2, y2, r2, color2, 'star2')
    distance = sqrt(pow((x2 - x1), 2) + pow((y2 - y1), 2))
    force = 9.0045 * (pow(distance, -2))
    ttk.Label(root, text=f"Distance: {distance} x10^6 m").grid(column=1, row=5)
    ttk.Label(root, text=f"Force: {force} x10^60 N").grid(column=1, row=6)


def up2(event):
    global x2, y2, star_2, distance
    y2 = y2 - step  # decrease the vertical coordinates
    c1.delete('star2')  # delete the circle
    star_2 = create_circle(x2, y2, r2, color2, 'star2')
    distance = sqrt(pow((x2 - x1), 2) + pow((y2 - y1), 2))
    force = 9.0045 * (pow(distance, -2))
    ttk.Label(root, text=f"Distance: {distance} x10^6 m").grid(column=1, row=5)
    ttk.Label(root, text=f"Force: {force} x10^60 N").grid(column=1, row=6)


def down2(event):
    global x2, y2, star_2, distance
    y2 = y2 + step  # increase the vertical coordinates
    c1.delete('star2')  # delete the circle
    star_2 = create_circle(x2, y2, r2, color2, 'star2')
    distance = sqrt(pow((x2 - x1), 2) + pow((y2 - y1), 2))
    force = 9.0045 * (pow(distance, -2))
    ttk.Label(root, text=f"Distance: {distance} x10^6 m").grid(column=1, row=5)
    ttk.Label(root, text=f"Force: {force} x10^60 N").grid(column=1, row=6)


b1 = tk.Button(root, text='Big Left', command=lambda: left1('x'))
b1.grid(row=1, column=0, rowspan=2, sticky='E')
b2 = tk.Button(root, text='Big Up', command=lambda: up1('x'))
b2.grid(row=1, column=1)
b3 = tk.Button(root, text='Big Right', command=lambda: right1('x'))
b3.grid(row=1, column=2, rowspan=2, sticky='W')
b4 = tk.Button(root, text='Big Down', command=lambda: down1('x'))
b4.grid(row=2, column=1)

b5 = tk.Button(root, text='Small Left', command=lambda: left2('x'))
b5.grid(row=3, column=0, rowspan=2, sticky='E')
b6 = tk.Button(root, text='Small Up', command=lambda: up2('x'))
b6.grid(row=3, column=1)
b7 = tk.Button(root, text='Small Right', command=lambda: right2('x'))
b7.grid(row=3, column=2, rowspan=2, sticky='W')
b8 = tk.Button(root, text='Small Down', command=lambda: down2('x'))
b8.grid(row=4, column=1)

root.mainloop()