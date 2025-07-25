class QuizBrain:
    def __init__(self, q_list):
        self.q_number = 0
        self.q_list = q_list
        self.score = 0

    def still_has_questions(self):
        return len(self.q_list) > self.q_number

    def next_question(self):
        current_question = self.q_list[self.q_number]
        self.q_number += 1
        user_answer = input(
            f"Q{self.q_number + 1}: {current_question.question} "
        ).capitalize()
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer:
            self.score += 1
            print("You guessed correctly!")
            print(f"Your score is: {self.score}/{self.q_number}")
        else:
            print("You guessed incorrectly!")
            print(f"Your score is: {self.score}/{self.q_number}")
        print("\n")
