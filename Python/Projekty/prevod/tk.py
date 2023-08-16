from tkinter import *


#window
win = Tk()
win.geometry("500x500+0+0")
win.title('Prepocet kurzu')
win.iconbitmap("picture.ico")
win.config(bg="black")


#label
currency = Label(win, text="Eura", font=("Cambria", 20, "bold"), bg="black", fg="white", borderwidth=10, relief="sunken")
currency.pack(ipadx=20)

currency2 = Label(win, text="CZK", font=("Cambria", 20, "bold"), bg="black", fg="white")
currency2.pack()


win.mainloop()
