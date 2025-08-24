import tkinter

from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = tkinter.Tk()
        self.window.title("Quizzlet")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score = tkinter.Label(
            text=f"Score: {self.quiz.score}", bg=THEME_COLOR, fg="White"
        )
        self.score.grid(row=0, column=1)

        self.canvas = tkinter.Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150, 125, text="Test Text", font=("Arial", 20, "italic"), width=280
        )

        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        red_image = tkinter.PhotoImage(file="./images/false.png")
        self.red_button = tkinter.Button(
            image=red_image, highlightthickness=0, command=self.check_false
        )
        self.red_button.grid(row=3, column=0)

        green_image = tkinter.PhotoImage(file="./images/true.png")
        self.green_button = tkinter.Button(
            image=green_image, highlightthickness=0, command=self.check_true
        )
        self.green_button.grid(row=3, column=1)

        self.get_question()

        self.window.mainloop()

    def get_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(
                self.question_text,
                text=f"You've reached the end of the quiz. {self.quiz.score}/10",
            )
            self.red_button.config(state="disabled")
            self.green_button.config(state="disabled")

    def check_true(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def check_false(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_question)
