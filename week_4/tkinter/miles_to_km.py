import tkinter

window = tkinter.Tk()
window.minsize(width=250, height=100)
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)


def convert():
    conversion = round(float(input.get()) * 1.609344)
    number.config(number.config(text=conversion))


miles = tkinter.Label(text="Miles", font=("Arial", 12))
miles.grid(column=3, row=0)

km = tkinter.Label(text="Km", font=("Arial", 12))
km.grid(column=3, row=1)

equal_to = tkinter.Label(text="is equal to", font=("Arial", 12))
equal_to.grid(column=0, row=1)

input = tkinter.Entry(width=10)
input.grid(column=1, row=0)

number = tkinter.Label(text="", font=("Arial", 12))
number.grid(column=1, row=1)

button = tkinter.Button(text="Calculate", command=convert)
button.grid(column=1, row=2)

window.mainloop()
