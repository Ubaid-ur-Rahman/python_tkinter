# import all functions from the tkinter            
from tkinter import *

# import messagebox class from tkinter             
from tkinter import messagebox


# Function for clearing the contents of all text entry boxes                 
def clearAll():
    # deleting the content from the entry box      
    nameField.delete(0, END)
    f_nameField.delete(0, END)
    dob_DayField.delete(0, END)
    dob_MonthField.delete(0, END)
    dob_YearField.delete(0, END)
    disp_dob_yearField.delete(0, END)
    disp_dob_monthField.delete(0, END)
    disp_nameField.delete(0, END)
    disp_f_nameField.delete(0, END)
    disp_dob_DayField.delete(0, END)



# function for checking error
def checkError():
    # if any of the entry field is empty
    # then show an error message and clear
    # all the entries
    if (nameField.get() == "" or f_nameField.get() == ""
            or dob_DayField.get() == "" or dob_MonthField.get() == ""
            or dob_YearField.get() == ""):
        # show the error message
        messagebox.showerror("Input Error")

        # clearAll function calling
        clearAll()

        return -1


def var():
    value = checkError()

    if value == -1:
        return ()
    else:
        name = str(nameField.get())
        f_name = str(f_nameField.get())
        dob_day = int(dob_DayField.get())
        dob_month = int(dob_MonthField.get())
        dob_year = int(dob_YearField.get())

        disp_nameField.insert(10, str(name))
        disp_f_nameField.insert(10, str(f_name))
        disp_dob_DayField.insert(10, str(dob_day))
        disp_dob_monthField.insert(10, str(dob_month))
        disp_dob_yearField.insert(10, str(dob_year))


if __name__ == "__main__":
    gui = Tk()

    gui.configure(background="light green")

    gui.title("Question 1")

    gui.geometry("560x150")

    details = Label(gui, text="Details", bg="light green")

    out = Label(gui, text="OUTPUT", bg='Light green')

    name = Label(gui, text="First Name", bg="light green")

    f_name = Label(gui, text="Last Name", bg="light green")

    day = Label(gui, text="Day", bg="light green")

    month = Label(gui, text="Month", bg="light green")

    year = Label(gui, text="Year", bg="light green")

    disp = Button(gui, text="Display", fg="Black", bg="Red", command=var)

    disp_name = Label(gui, text="Your Last name is:", bg="light green")
    disp_fname = Label(gui, text="Your First name is:", bg="light green")

    disp_dob_Year = Label(gui, text="Years", bg="light green")

    # Create a Months : label
    disp_dob_Month = Label(gui, text="Months", bg="light green")

    # Create a Days : label
    disp_dob_Day = Label(gui, text="Days", bg="light green")

    clearAllEntry = Button(gui, text="Clear All", fg="Black", bg="Red", command=clearAll)

    nameField = Entry(gui)
    f_nameField = Entry(gui)
    dob_DayField = Entry(gui)
    dob_MonthField = Entry(gui)
    dob_YearField = Entry(gui)

    disp_nameField = Entry(gui)
    disp_f_nameField = Entry(gui)
    disp_dob_DayField = Entry(gui)
    disp_dob_monthField = Entry(gui)
    disp_dob_yearField = Entry(gui)

    details.grid(row=0, column=1)

    # USER INPUTS
    name.grid(row=1, column=0)
    nameField.grid(row=1, column=1)

    f_name.grid(row=2, column=0)
    f_nameField.grid(row=2, column=1)

    day.grid(row=3, column=0)
    dob_DayField.grid(row=3, column=1)

    day.grid(row=3, column=0)
    dob_DayField.grid(row=3, column=1)

    month.grid(row=4, column=0)
    dob_MonthField.grid(row=4, column=1)

    year.grid(row=5, column=0)
    dob_YearField.grid(row=5, column=1)


    #OUTPUTS
    out.grid(row=0, column=3)
    disp.grid(row=3, column=2)
    disp_fname.grid(row=1, column=3)
    disp_f_nameField.grid(row=1, column=4)

    disp_name.grid(row=2, column=3)
    disp_nameField.grid(row=2, column=4)

    disp_dob_Day.grid(row=3, column=3)
    disp_dob_DayField.grid(row=3, column=4)

    disp_dob_Month.grid(row=4, column=3)
    disp_dob_monthField.grid(row=4, column=4)

    disp_dob_Year.grid(row=5, column=3)
    disp_dob_yearField.grid(row=5, column=4)

    clearAllEntry.grid(row=12, column=2)

    gui.mainloop()
