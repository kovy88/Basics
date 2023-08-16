from tkinter import *

win = Tk()
win.minsize(300, 100)
win.iconbitmap("picture.ico")
win.title("Prevod men")
win.config(bg="#333132")
win.resizable(False, False)


def change(event):
    final = input_1.get()
    if label_from["text"] == "CZK":
        final = round(float(final) / 23.67, 2)
    elif label_from["text"] == "EUR":
        final = round(float(final) * 23.67, 2)
    label_amount.config(text=final)
    input_1.delete(0, END)


def shift():
    label_from["text"], label_to["text"] = label_to["text"], label_from["text"]
    label_amount.config(text="0")


input_1 = Entry(win, font=("ARial", 12), width=10, bg="#333132", fg="white")
input_1.grid(row=0, column=0, pady=5, padx=(5, 0))
input_1.focus()

label_from = Label(win, text="CZK", font=("Arial", 15), bg="#333132", fg="white")
label_from.grid(row=0, column=1, padx=(20, 20))

label_to = Label(win, text="EUR", font=("Arial", 15), bg="#333132", fg="white")
label_to.grid(row=1, column=1, padx=(20, 20))

label_amount = Label(win, text="0", font=("Arial", 15), bg="#333132", fg="white")
label_amount.grid(row=1, column=0, pady=5)

button_exchange = Button(win, text="Exchange", font=("Arial", 14), bg="black", fg="white", command=change, width=10)
button_exchange.grid(row=0, column=2, padx=20)

button_shift = Button(win, text="Shift", font=("Arial", 14), bg="black", fg="white", width=10, command=shift)
button_shift.grid(row=1, column=2, padx=20)

win.bind('<Return>', change)


win.mainloop()
