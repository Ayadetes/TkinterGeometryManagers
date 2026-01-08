from tkinter import *

window = Tk()
window.title("Login Form")
window.geometry("500x500")

frame = Frame(master=window, height=200, width=360, bg="lightblue")

lbl1 = Label(master=frame, text="Username:", bg="lightblue")
lbl2 = Label(master=frame, text="Password:", bg="lightblue")
lbl3 = Label(master=frame, text="Email", bg="lightblue")

name = Entry(master=frame, width=30)
password = Entry(master=frame, width=30, show="*")
email = Entry(master=frame, width=30)

def display():
    name_value = name.get()
    greet = "Hello, " + name_value + "!"
    message = "\nCongratulations! You have successfully logged in."
    textbox.insert(END, greet)
    textbox.insert(END, message)

textbox = Text(master=frame, bg="#BEBEBE", fg="black")

btn = Button(master=frame, text="Login", command=display(), bg="red")

frame.place(x=20, y=0)
lbl1.place(x=20, y=20)
name.place(x=150, y=20)
lbl2.place(x=20, y=80)
password.place(x=150, y=80)
lbl3.place(x=20, y=140)
email.place(x=150, y=140)
btn.place(x=130, y=210)
textbox.place(y=250)
window.mainloop()