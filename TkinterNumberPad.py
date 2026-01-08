from tkinter import *

window = Tk()
window.title("Number Pad")
window.geometry("250x300")

nums = [['9', '8', '7'],
        ['6', '5', '4'],   
        ['3', '2', '1'],
        ['0', '.', 'C']]

for r in range(4):
    window.columnconfigure(r, weight=1, minsize=75)
    window.rowconfigure(r, weight=1, minsize=50)
    for j in range(0,3):
        frame = Frame(master=window, relief=SUNKEN, borderwidth=1, bg="lightgray")
        frame.grid(row=r, column=j)
        label = Button(master=frame, text=nums[r][j], bg="gray")
        label.pack(padx=1, pady=1)

window.mainloop()