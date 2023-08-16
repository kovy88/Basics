from tkinter import *

win = Tk()
win.title("Prevod men")
win.minsize(500, 500)
win.resizable(False, False)
win.iconbitmap("picture.ico")
win.config(bg="grey")


label_1 = Label(win, text="Eura", font=("Helvetica", 20), bg="grey")
# label_1.pack()
# label_1.place(x=400, y=0)
label_1.grid(row=0, column=0)

label_2 = Label(win, text="Czk", font=("Helvetica", 20), bg="grey")
# label_2.pack()
# label_2.place(x=250, y=150)
label_2.grid(row=1, column=1)

label_3 = Label(win, text="Usd", font=("Helvetiva", 20), bg="grey")
# label_3.pack()
# label_3.place(x=100, y=400)
label_3.grid(row=2, column=0)
win.mainloop()
