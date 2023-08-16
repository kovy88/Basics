import tkinter

window = tkinter.Tk()
window.title("Moje prvni okno")
window.minsize(500, 400)
window.resizable(False, False)
window.iconbitmap("picture.ico")
window.config(bg="grey")


window2 = tkinter.Tk()
window2.title("XXXX")
window2.geometry("600x400+800+100")
window2.resizable(False, False)
window2.iconbitmap("picture.ico")
window2.config(bg="cyan")
window2


#Label

label = tkinter.Label(window, text="X", bg="grey", fg="white", font=("Arial", 24, "bold"))
label.pack(side="top")



window.mainloop()
