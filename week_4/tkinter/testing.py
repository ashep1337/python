import tkinter

window = tkinter.Tk()
window.title("Hello World")
window.minsize(width=500, height=300)
window.config(padx=200, pady=200)

label = tkinter.Label(text="This is a label.", font=("Arial", 24, "bold"))
label.grid(column=1, row=1)

label["text"] = "New Text"
label.config(text="New Text", padx=100, pady=100)


def button_clicked():
    label.config(label.config(text=input.get()))


button = tkinter.Button(text="Click me", command=button_clicked)
button.grid(column=3, row=1)

button = tkinter.Button(text="Click me", command=button_clicked)
button.grid(column=2, row=2)

input = tkinter.Entry(width=10)
input.grid(column=4, row=3)
input.get()

window.mainloop()
