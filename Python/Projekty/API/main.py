import requests
from tkinter import *

win = Tk()
win.minsize(300, 300)
win.resizable(False, False)
win.title("Insult")
win.config(bg="#042940")
# lang = en, fr, es, cs



def an_insult():
    user_lang = drop_down_lang.get()
    my_parameters = {
        "lang": user_lang,
        "type": "json"
    }
    response = requests.get("https://evilinsult.com/generate_insult.php", params=my_parameters)
    response.raise_for_status()
    data = response.json()
    insult = data["insult"]
    label["text"] = insult


#Roletka
drop_down_lang = StringVar(win)
drop_down_lang.set("cs")
drop_down_lang_options = OptionMenu(win, drop_down_lang, "en", "es", "fr", "cs")
drop_down_lang_options.config(bg="#005C53", fg="white", font=("Arial", 12))
drop_down_lang_options.pack(pady=(5, 5))


button = Button(text="Anotehr insult", command=an_insult, bg="#005C53", fg="white", font=("Arial", 12))
button.pack(pady=5)

label = Label(wraplength=250, bg="#042940", fg="white", font=("Arial", 14))
an_insult()
label.pack()

# response = requests.get("https://evilinsult.com/generate_insult.php?lang=en&type=json")
# response.raise_for_status()
# data = response.json()
# insult = data["insult"]


win.mainloop()
