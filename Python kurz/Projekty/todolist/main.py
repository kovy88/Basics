from tkinter import *
import customtkinter

win = customtkinter.CTk()
win.title("ToDoList")
win.geometry("600x355")
win.resizable(False, False)
win.iconbitmap("tdicon.ico")


#Fonts and colors
main_font = ("Arial", 12)
main_color = "#363533"
button_color = "#1b85c2"


#Functions
def add_text(event):
    text.insert(END, input_1.get())
    input_1.delete(0, END)


def remove_text():
    text.delete(ANCHOR)


def remove_all_text():
    text.delete(0, END)


def save_list():
    with open("tasks.txt", "w")as file:
        tasks = text.get(0, END)
        for i in tasks:
            if i.endswith("\n"):
                file.write(f"{i}")
            else:
                file.write(f"{i}\n")


def open_tasks():
    try:
        with open("tasks.txt", "r") as file:
            for i in file:
                text.insert(END, i)
    except:
        print("Nic")


input_frame = customtkinter.CTkFrame(win)
text_frame = customtkinter.CTkFrame(win)
button_frame = customtkinter.CTkFrame(win)
input_frame.pack(pady=5)
text_frame.pack(pady=5)
button_frame.pack()


#input frame
input_1 = customtkinter.CTkEntry(input_frame, width=400, font=main_font)
input_1.grid(row=0, column=0, padx=5, pady=5)
input_1.focus()
add_but = customtkinter.CTkButton(input_frame, text="Add", command=add_text)
add_but.grid(row=0, column=1, padx=5, pady=5)


#scroll
text_scrollbar = Scrollbar(text_frame)
text_scrollbar.grid(row=0, column=1, sticky=NS)

#text frame
text = Listbox(text_frame, width=74, height=15, borderwidth=3, font=main_font, bg="#b7bbbd", yscrollcommand=text_scrollbar.set)
text.grid(row=0, column=0)

text_scrollbar.config(command=text.yview)


# button_frame
remove_b = customtkinter.CTkButton(button_frame, text="Remove item", command=remove_text)
remove_b.grid(row=0, column=0, padx=2, pady=10)
remove_c = customtkinter.CTkButton(button_frame, text="Clear list", command=remove_all_text)
remove_c.grid(row=0, column=1, padx=2, pady=10)
remove_s = customtkinter.CTkButton(button_frame, text="Save list", command=save_list)
remove_s.grid(row=0, column=2, padx=2, pady=10)
remove_q = customtkinter.CTkButton(button_frame, text="Quit", command=win.destroy)
remove_q.grid(row=0, column=3, padx=2, pady=10)




win.bind('<Return>', add_text)

# test_but = Label(button_frame, text="LOLOLO")
# test_but.grid(row=1, column=0, sticky=W+E)

# try:
#     print(x)
# except:
#     print("x nenalezeno")

open_tasks()

win.mainloop()
