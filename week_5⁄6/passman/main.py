import json
import random
import string
import tkinter
from tkinter import messagebox

pass_string = None


def generate_pass():
    global pass_string
    password_entry.delete(0, tkinter.END)
    sym_string = [
        random.choice(string.punctuation) for _ in range(random.randint(2, 5))
    ]
    letters = [
        random.choice(string.ascii_letters) for _ in range(random.randint(8, 12))
    ]
    num_list = list(str(random.randint(100, 9999)))
    final_string = letters + sym_string + num_list

    random.shuffle(final_string)
    pass_string = "".join(final_string)
    window.clipboard_append(pass_string)
    password_entry.insert(0, pass_string)


def add():
    webdata = website_entry.get()
    userdata = username_entry.get()
    passdata = password_entry.get()
    json_data = {
        webdata: {
            "email": userdata,
            "password": passdata,
        }
    }
    if webdata == "" or userdata == "" or passdata == "":
        messagebox.showinfo(
            title="info", message="Please fill out all fields before saving."
        )
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
                data.update(json_data)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(json_data, data_file, indent=4)
        else:
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, tkinter.END)
            password_entry.delete(0, tkinter.END)


def find_password():
    webdata = website_entry.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(
            title="Info",
            message="No data present. Please add an entry before searching.",
        )
    else:
        if webdata in data:
            messagebox.showinfo(
                title="Info",
                message=f"Email: {data[webdata]['email']}\nPassword: {
                    data[webdata]['password']
                }",
            )
        else:
            messagebox.showinfo(
                title="Info", message="Ivalid Entry. Please enter a valid domain."
            )


window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = tkinter.Canvas(width=200, height=200)
logo = tkinter.PhotoImage(file="/home/ashep/dev/python/week_5/passman/logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

website = tkinter.Label(text="Website:")
website_entry = tkinter.Entry(width=25)
website.grid(column=0, row=1)
website_entry.grid(column=1, row=1)
website_entry.focus()

username = tkinter.Label(text="Email/Username:")
username_entry = tkinter.Entry(width=45)
username.grid(column=0, row=2)
username_entry.grid(column=1, row=2, columnspan=2)
username_entry.insert(0, "ashep50624@gmail.com")

password = tkinter.Label(text="Password")
password.grid(column=0, row=3)

password_entry = tkinter.Entry(width=25)
password_entry.grid(column=1, row=3)

password_button = tkinter.Button(text="Generate Password", command=generate_pass)
password_button.grid(column=2, row=3)
password_entry.grid(column=1, row=3)


add_button = tkinter.Button(text="Add", width=36, command=add)
add_button.grid(column=1, row=4, columnspan=2)
add_button.bind("<Return>", lambda event: add_button.invoke())

search_button = tkinter.Button(text="Search", command=find_password)
search_button.grid(column=2, row=1)

window.mainloop()
