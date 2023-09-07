from tkinter import *   
import random
root = Tk()  
  
root.geometry("500x500")  
  
#creating a simple canvas  
c = Canvas(root)  
# c.grid()
color_list = ['purple', 'cyan', 'green', 'red', 'blue', 'orange', 'black']

picked_color = StringVar()
picked_color.set("red")


def clear():
    picked_color.set("red")
    c.delete('all')
    

def change_color():
    picked_color.set(random.choice(color_list))
    print(picked_color.get())
 
def draw_circle():
    radius =  random.randint(10, 40)
    center_x = random.randint(50, 250)
    center_y = random.randint(50, 250)

    xr = center_x+int(radius/2)
    yr= center_y+int(radius/2)
    x_r = center_x-int(radius/2)
    y_r= center_y-int(radius/2)
    color = picked_color.get()
    c.create_oval(xr, yr, x_r, y_r,fill=color, width=2)#create_arc(x-r, y-r, x+r, y+r, **kwargs)

  
b1 = Button(root, 
          text='Quit', 
          command=root.quit)
b2 = Button(root, 
          text='Draw Circle', 
          command=draw_circle)

b3 = Button(root, 
          text='Change Color', 
          command=change_color)

b4 = Button(root, 
          text='Clear', 
          command=clear)

b1.pack()
b2.pack()
b3.pack()
b4.pack()

c.pack()  

root.mainloop()  
