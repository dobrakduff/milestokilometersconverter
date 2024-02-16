from tkinter import *

window =Tk()
window.minsize(150, 75)
def action():
    miles = float(entry.get())
    result = miles * 1.609
    label_km.config(text=result)


km = 0
entry = Entry(width=10)
entry.insert(END, string="")
print(entry.get())
entry.grid(row=0,column=1)


label = Label(text="Miles")
label.grid(row=0,column=2)


label2 = Label(text="is equal to")
label2.grid(row=1,column=0)


label_km = Label(text="0")
label_km.grid(row=1,column=1)


label3 = Label(text="km")
label3.grid(row=1,column=2)

button = Button(text="calculate", command=action)
button.grid(row=2,column=1)

window.mainloop()