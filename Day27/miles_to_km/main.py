from tkinter import *
FONT = ("Arial", 10, "normal")


def button_click():
    mile = int(inp.get())
    km = mile * 1.609344
    count_label.config(text=km)


window = Tk()
window.title("Mile to Km converter")
window.minsize(width=200, height=100)
window.config(padx=15, pady=15)


inp = Entry(width=10)
inp.grid(column=1, row=0)


miles_label = Label(text="Miles", font=FONT)
miles_label.grid(column=2, row=0)
miles_label.config(pady=10, padx=5)


equal_label = Label(text="is equal to", font=FONT)
equal_label.grid(column=0, row=1)


count_label = Label(text="0", font=FONT)
count_label.grid(column=1, row=1)
count_label.config(padx=5, pady=5)


km_label = Label(text="Km", font=FONT)
km_label.grid(column=2, row=1)


calc_button = Button(text="Calculate", command=button_click)
calc_button.grid(column=1, row=2)
window.mainloop()
