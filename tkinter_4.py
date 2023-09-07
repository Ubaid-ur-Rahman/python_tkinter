import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from calendar import month_name

root = tk.Tk()

# config the root window
root.geometry('400x100')
root.resizable(False, False)
root.title('Combobox Widget')


# label
#label = ttk.Label(text="Please select a month:")
#label.pack(fill=tk.X, padx=5, pady=5)

# create a combobox
selected_month = tk.StringVar()
month_cb = ttk.Combobox(root, textvariable=selected_month)

# get first 3 letters of every month name
month_cb['values'] = ['purple', 'cyan', 'green', 'red', 'blue', 'orange', 'black']

# prevent typing a value
month_cb['state'] = 'readonly'

# place the widget
month_cb.pack(fill=tk.X, padx=5, pady=5)


# bind the selected value changes
def month_changed(event):
    """ handle the month changed event """
    color = selected_month.get()
    root.configure(bg=color)
    root.update()


month_cb.bind('<<ComboboxSelected>>', month_changed)



root.mainloop()