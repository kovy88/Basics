import requests
from tkinter import *

win = Tk()
win.minsize(700, 400)
win.resizable(False, False)
win.title("ISS")

#Funkce
def iss_cor():
    response = requests.get("http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    longitude = data["iss_position"]["longitude"]
    latitude = data["iss_position"]["latitude"]
    latitude_label.config(text=f"Zemepisna sirka je: {latitude}")
    longitude_label.config(text=f"Zemepisna delka je: {longitude}")



canvas = Canvas(win, width=500, height=280, bg="grey")
canvas.pack()
iss_img = PhotoImage(file="giphy.gif")
canvas.create_image(0, 0, image=iss_img, anchor="nw")

#Frame

but_frame = Frame(win)
but_frame.pack()

rec_but = Button(but_frame, text="ISS souradnice", command=iss_cor)
rec_but.pack()

latitude_label = Label()
latitude_label.pack()

longitude_label = Label()
longitude_label.pack()


#

#
# print(f"Soucasna pozice ISS je {latitude} : {longitude} ")
win.mainloop()
