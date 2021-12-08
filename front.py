from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.messagebox import showinfo
import back


def update():
    def get_selected_row(event):
        global selected_row
        index = list.curselection()[0]
        selected_row = list.get(index)
        e1.delete(0, END)
        e1.insert(END, selected_row[1])
        e2.delete(0, END)
        e2.insert(END, selected_row[2])
        e3.delete(0, END)
        e3.insert(END, selected_row[3])
        e4.delete(0, END)
        e4.insert(END, selected_row[4])
        e5.delete(0, END)
        e5.insert(END, selected_row[5])
        e6.delete(0, END)
        e6.insert(END, selected_row[6])

    def deletelist():
        back.delete(selected_row[0])

    def viewList():
        list.delete(0, END)
        for datas in back.view():
            list.insert(END, datas)

    def searchlist():
        list.delete(0, END)
        for i in back.search(date_text.get(), Earnings_text.get(), exercise_text.get(), study_text.get(), diet_text.get(), python_text.get()):
            list.insert(END, i)

    def addlist():
        back.insert(date_text.get(), Earnings_text.get(), exercise_text.get(
        ), study_text.get(), diet_text.get(), python_text.get())

        list.delete(0, END)
        list.insert(END, (date_text.get(), Earnings_text.get(), exercise_text.get(
        ), study_text.get(), diet_text.get(), python_text.get()))

    views = Toplevel(win)
    views.title("LIST OF STUDENTS")
    l1 = Label(views, text="Date")
    l1.grid(row=0, column=0)
    l2 = Label(views, text="Earnings")
    l2.grid(row=0, column=2)
    l3 = Label(views, text="Exercise")
    l3.grid(row=1, column=0)
    l4 = Label(views, text="Study")
    l4.grid(row=1, column=2)
    l5 = Label(views, text="Diet")
    l5.grid(row=2, column=0)
    l6 = Label(views, text="Python")
    l6.grid(row=2, column=2)

    date_text = StringVar()
    e1 = Entry(views, textvariable=date_text)
    e1.grid(row=0, column=1)

    Earnings_text = StringVar()
    e2 = Entry(views, textvariable=Earnings_text)
    e2.grid(row=0, column=3)

    exercise_text = StringVar()
    e3 = Entry(views, textvariable=exercise_text)
    e3.grid(row=1, column=1)

    study_text = StringVar()
    e4 = Entry(views, textvariable=study_text)
    e4.grid(row=1, column=3)

    diet_text = StringVar()
    e5 = Entry(views, textvariable=diet_text)
    e5.grid(row=2, column=1)

    python_text = StringVar()
    e6 = Entry(views, textvariable=python_text)
    e6.grid(row=2, column=3)

    list = Listbox(views, height=8, width=35)
    list.grid(row=3, column=0, rowspan=9, columnspan=2)

    sb = Scrollbar(views)
    sb.grid(row=3, column=2, rowspan=9)

    list.bind('<<ListboxSelect>>', get_selected_row)

    b2 = Button(views, text='Search', width=10, pady=10, command=searchlist)
    b2.grid(row=3, column=3)

    b3 = Button(views, text='Delete', width=10, pady=10, command=deletelist)
    b3.grid(row=4, column=3)

    b4 = Button(views, text='View all', width=10, pady=10, command=viewList)
    b4.grid(row=5, column=3)

    b5 = Button(views, text='Close', width=10, pady=10, command=views.destroy)
    b5.grid(row=7, column=3)


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
    win.geometry("500x250")

    enrollbtn = Button(win, text="ENROLL A STUDENT", font=(
        'Arial 12 bold'), command=enroll_window)
    enrollbtn.place(relx=0.5, rely=0.3, anchor=CENTER)

    viewbtn = Button(win, text="List Of Students",
                     font=('Arial 12 bold'), command=show)
    viewbtn.place(relx=0.5, rely=0.5, anchor=CENTER)

    updatebtn = Button(win, text="UPDATE STUDENT INFO",
                       font=('Arial 12 bold'), command=update)
    updatebtn.place(relx=0.5, rely=0.7, anchor=CENTER)

    win.mainloop()
