from tkinter import *

win = Tk()
win.title("Prevod men")
win.minsize(500, 400)
win.resizable(False, False)
win.config(bg="grey")
win.iconbitmap("picture.ico")


label_1 = Label(text="Eura", font=("Arial", 24, "bold"), bg="grey", fg="black")
label_1.pack(pady=(10, 10))



def change():
    # if label_1["text"] == "Eura":
    #     label_1.config(text="CZK")
    #
    # else:
    #     label_1.config(text="Eura")
    # label_1.config(text=input_1.get())
    label_1.config(text=text_area.get("1.0", END))
    input_1.delete(0, END)



button_1 = Button(text="Click", command=change, width=8, height=0)
button_1.pack()


input_1 = Entry(width=10, font=("Arial", 20))
input_1.insert(0, string="AAA")
input_1.focus()
input_1.pack()
# input_1.get()


text_area = Text(width=40, height=10)
text_area.focus()
text_area.pack()


win.mainloop()
