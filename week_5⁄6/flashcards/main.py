import random
import tkinter

import pandas

BACKGROUND_COLOR = "#B1DDC6"

try:
    data = pandas.read_csv("./data/to_learn.csv")
except FileNotFoundError:
    df = pandas.DataFrame("./data/french_words.csv")
    df.to_csv("./data/to_learn.csv", index=False)


data = pandas.read_csv("./data/to_learn.csv")

if data.empty:
    data = pandas.read_csv("./data/french_words.csv")
    data.to_csv("./data/to_learn.csv", index=False)

words = {row.French: row.English for index, row in data.iterrows()}
wordkeys = list(words.keys())
wordvalues = list(words.values())
num = random.randint(0, len(wordkeys) - 1)


def next_card():
    global num
    num = random.randint(0, len(wordkeys) - 1)
    canvas.itemconfig(image_id, text=wordkeys[num], fill="black")
    canvas.itemconfig(canvas_image, image=card_front)
    canvas.itemconfig(lang, text="French", fill="black")
    window.after_idle(timer)


def show_back():
    canvas.itemconfig(image_id, text=wordvalues[num], fill="white")
    canvas.itemconfig(canvas_image, image=card_back)
    canvas.itemconfig(lang, text="English", fill="white")


def timer():
    window.after(3000, show_back)


def known_word():
    global words, wordkeys, wordvalues
    df = pandas.read_csv("./data/to_learn.csv")
    df = df.drop(index=num)
    if df.empty:
        print("Congratulations you learned everything.....Do it again.")
        df = pandas.read_csv("../flashcards/data/french_words.csv")
    df.to_csv("./data/to_learn.csv", index=False)
    words = {row.French: row.English for _, row in df.iterrows()}
    wordkeys = list(words.keys())
    wordvalues = list(words.values())
    next_card()


window = tkinter.Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = tkinter.Canvas(width=800, height=600, bg=BACKGROUND_COLOR)
card_front = tkinter.PhotoImage(
    file="/home/ashep/dev/python/week_5/flashcards/images/card_front.png"
)
card_back = tkinter.PhotoImage(
    file="/home/ashep/dev/python/week_5/flashcards/images/card_back.png"
)
canvas_image = canvas.create_image(400, 300, image=card_front)
canvas.grid(column=0, row=0, columnspan=2)
lang = canvas.create_text(400, 200, text="French", font=("Ariel", 40, "italic"))
image_id = canvas.create_text(400, 350, text=wordkeys[num], font=("Ariel", 60, "bold"))
red_image = tkinter.PhotoImage(
    file="/home/ashep/dev/python/week_5/flashcards/images/wrong.png"
)
red_button = tkinter.Button(image=red_image, highlightthickness=0, command=next_card)
red_button.grid(column=0, row=1)
green_image = tkinter.PhotoImage(
    file="/home/ashep/dev/python/week_5/flashcards/images/right.png"
)
green_button = tkinter.Button(
    image=green_image, highlightthickness=0, command=known_word
)
green_button.grid(column=1, row=1)

timer()

window.mainloop()
