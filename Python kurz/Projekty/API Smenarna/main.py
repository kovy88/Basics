from tkinter import *
import requests

app = Tk()
app.minsize(350, 100)
app.resizable(False, False)
app.title("Prevod men")
app.iconbitmap("picture.ico")
app.config(bg="#333132")


def exchange():
    try:
        label_error["text"] = ""
        cur_from = choice_from.get()
        cur_to = choice_to.get()
        amount = int(price_input.get())

        url = f"https://api.apilayer.com/exchangerates_data/convert?to={cur_to}&from={cur_from}&amount={amount}"

        payload = {}
        headers = {
            "apikey": "mz3Ui8wXHIA54AcO14BTaLM9EhkfOKj1"
        }

        response = requests.request("GET", url, headers=headers, data=payload)

        response.raise_for_status()
        data = response.json()

        label_amount["text"] = round(data["result"], 2)
        price_input.delete(0, END)

    except:
        label_error["text"] = "Zadejte prosim castku"
        label_amount["text"] = 0
        price_input.delete(0, END)


price_input = Entry(app, font=("Arial", 12), width=15, bg="#333132", fg="white", justify=CENTER)
# price_input.insert(0, "0")
price_input.grid(padx=10, pady=10)
price_input.focus()

label_amount = Label(app, text=0, bg="#333132", fg="white", font=("Arial", 12))
label_amount.grid(row=1, column=0)

label_error = Label(app, bg="#333132", fg="white", font=("Arial", 12))
label_error.grid(row=2, column=0, padx=5, pady=(0, 3))

choice_from = StringVar(app)
choice_from.set("CZK")
choice_from_op = OptionMenu(app, choice_from, "CZK", "EUR", "USD", )
choice_from_op.config(bg="#333132", fg="white")
choice_from_op.grid(row=0, column=1)

choice_to = StringVar(app)
choice_to.set("EUR")
choice_to_op = OptionMenu(app, choice_to, "CZK", "EUR", "USD", )
choice_to_op.config(bg="#333132", fg="white")
choice_to_op.grid(row=1, column=1)

button_ex = Button(app, text="Exchange", font=("Arial", 14), bg="black", fg="white", width=10, command=exchange)
button_ex.grid(column=2, row=1, padx=10)

# button_sw = Button(app, text="Switch", font=("Arial", 14), bg="black", fg="white", width=10, command=switch)
# button_sw.grid(column=2, row=1, padx=10)


app.mainloop()
