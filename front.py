from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.messagebox import showinfo
import back


def show():
    views = Toplevel(win)
    views.title("LIST OF STUDENTS")

    tree = ttk.Treeview(views, column=(
        "c1", "c2", "c3", "c4", "c5", "c6", "c7", "c8"), show='headings')

    for row in back.view():
        tree.insert("", END, values=row)

    tree.column("#1", anchor=CENTER)
    tree.heading("#1", text="No.")
    tree.column("#2", anchor=CENTER)
    tree.heading("#2", text="Last Name")
    tree.column("#3", anchor=CENTER)
    tree.heading("#3", text="Sure name")
    tree.column("#4", anchor=CENTER)
    tree.heading("#4", text="M. name")
    tree.column("#5", anchor=CENTER)
    tree.heading("#5", text="Birth date")
    tree.column("#6", anchor=CENTER)
    tree.heading("#6", text="Sex")
    tree.column("#7", anchor=CENTER)
    tree.heading("#7", text="Address")
    tree.column("#8", anchor=CENTER)
    tree.heading("#8", text="Contact")
    tree.pack()


def enroll_window():
    def enroll():
        try:
            back.insert(Lname.get(), Sname.get(), Mname.get(), Bday.get(),
                        sex.get(), age.get(), loc.get(), contact.get())
            e1.delete(0, END)
            e2.delete(0, END)
            e3.delete(0, END)
            e4.delete(0, END)
            e5.delete(0, END)
            e6.delete(0, END)
            e7.delete(0, END)
            e8.delete(0, END)
            return messagebox.showinfo("showinfo", "SUCCESSFUL")
        except Exception as e:
            raise messagebox.showerror("showerror", "Error")

    top = Toplevel(win)
    top.title("ENROLLMENT FORM")
    l1 = Label(top, text="Last Name")
    l1.grid(row=0, column=0)
    l2 = Label(top, text="Sure name")
    l2.grid(row=0, column=2)
    l3 = Label(top, text="M. name")
    l3.grid(row=0, column=4)
    l4 = Label(top, text="Birth date")
    l4.grid(row=1, column=0)
    l5 = Label(top, text="Sex")
    l5.grid(row=1, column=2)
    l6 = Label(top, text="Age")
    l6.grid(row=1, column=4)
    l7 = Label(top, text="Address")
    l7.grid(row=2, column=0)
    l8 = Label(top, text="Contact")
    l8.grid(row=2, column=4)

    Lname = StringVar()
    e1 = Entry(top, textvariable=Lname)
    e1.grid(row=0, column=1)

    Sname = StringVar()
    e2 = Entry(top, textvariable=Sname)
    e2.grid(row=0, column=3)

    Mname = StringVar()
    e3 = Entry(top, textvariable=Mname)
    e3.grid(row=0, column=5)

    Bday = StringVar()
    e4 = Entry(top, textvariable=Bday)
    e4.grid(row=1, column=1)

    sex = StringVar()
    e5 = Entry(top, textvariable=sex)
    e5.grid(row=1, column=3)

    age = StringVar()
    e6 = Entry(top, textvariable=age)
    e6.grid(row=1, column=5)

    loc = StringVar()
    e7 = Entry(top, textvariable=loc)
    e7.grid(row=2, column=1, columnspan=3, ipadx="80")

    contact = StringVar()
    e8 = Entry(top, textvariable=contact)
    e8.grid(row=2, column=5)

    b1 = Button(top, text='ENROLL', font=('Arial 10 bold'), command=enroll)
    b1.grid(row=3, column=0, columnspan=2)


if __name__ == "__main__":
    win = Tk()
    win.geometry("300x150")

    enrollbtn = Button(win, text="ENROLL A STUDENT", font=(
        'Arial 12 bold'), command=enroll_window)
    enrollbtn.place(relx=0.5, rely=0.4, anchor=CENTER)

    viewbtn = Button(win, text="List Of Students",
                     font=('Arial 12 bold'), command=show)
    viewbtn.place(relx=0.5, rely=0.7, anchor=CENTER)

    win.mainloop()
