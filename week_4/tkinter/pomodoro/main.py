import math
import os
import tkinter

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK = 1500
SHORT = 300
LONG = 1200
reps = 0
after_id = None


def reset_timer():
    global reps
    reps = 0
    text_checkmark.config(text="")
    text_timer.config(text="Timer")
    window.after_cancel(after_id)
    canvas.itemconfig(timer, text="00:00")


def start_timer():
    global reps
    reps += 1

    if reps % 8 == 0:
        timer_counter(LONG)
        text_timer.config(text="Break", fg=RED)
        os.system('notify-send "Time for a LONG break" "Break for 20 minutes"')

    elif reps % 2 == 0:
        timer_counter(SHORT)
        text_timer.config(text="Break", fg=PINK)
        os.system('notify-send "Time for a SHORT break" "Break for 5 minutes"')

    else:
        timer_counter(WORK)
        text_timer.config(text="Work", fg=GREEN)
        os.system('notify-send "Time to work" "Working for 25 minutes"')


def timer_counter(count):
    global after_id
    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer, text=f"{count_min}:{count_sec}")
    if count > 0:
        after_id = window.after(1000, timer_counter, count - 1)
    else:
        if reps == 8:
            text_checkmark.config(text="")
            text_timer.config(text="Reset")
        else:
            start_timer()
            current = text_checkmark.cget("text")
            if reps % 2:
                text_checkmark.config(text=current + "✔")


window = tkinter.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)
text_timer = tkinter.Label(
    text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold")
)
text_timer.grid(column=1, row=0)

text_checkmark = tkinter.Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 24, "bold"))

text_checkmark.grid(column=1, row=3)

start = tkinter.Button(text="Start", command=start_timer)
start.grid(column=0, row=2)

reset = tkinter.Button(text="Reset", command=reset_timer)
reset.grid(column=2, row=2)

canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = tkinter.PhotoImage(
    file="/home/ashep/dev/python/week_4/tkinter/pomodoro/tomato.png"
)
canvas.create_image(101, 112, image=tomato_img)
timer = canvas.create_text(
    101, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold")
)
canvas.grid(column=1, row=1)


window.mainloop()
