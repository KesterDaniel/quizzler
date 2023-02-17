from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quizbrain: QuizBrain):
        self.quiz = quizbrain
        # self.score = self.quiz.score
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(background=THEME_COLOR, padx=20, pady=20)

        self.score_label = Label(text=f"Score: 0", background=THEME_COLOR, fg="white")
        self.score_label.grid(row=0, column=2, pady=10)

        self.canvas = Canvas(width=300, height=250, highlightthickness=0)
        self.question_text = self.canvas.create_text(
            150, 125,
            text="Word on street",
            width=280,
            font=("Arial", 20, "italic")
        )
        self.canvas.grid(row=1, column=0, columnspan=3)

        true_image = PhotoImage(file="./images/true.png")
        self.true_button = Button(image=true_image, highlightthickness=0, bd=0, command=self.correct_answer)
        self.true_button.grid(row=2, column=0, pady=20)

        false_image = PhotoImage(file="./images/false.png")
        self.false_button = Button(image=false_image, highlightthickness=0, bd=0, command=self.wrong_answer)
        self.false_button.grid(row=2, column=2, pady=20)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        self.score_label.config(text=f"Score: {self.quiz.score}")
        if self.quiz.still_has_questions():
            next_question = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=next_question)
        else:
            self.canvas.itemconfig(self.question_text, text=f"Your final score:\n{self.quiz.score} out of {self.quiz.question_number}")
            self.true_button.grid_remove()
            self.false_button.grid_remove()

    def correct_answer(self):
        self.give_feedback(self.quiz.check_answer("True"))
        # self.get_next_question()

    def wrong_answer(self):
        self.give_feedback(self.quiz.check_answer("False"))
        # self.get_next_question()

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        if not is_right:
            self.canvas.config(bg="red")
        self.window.after(1000, func=self.get_next_question)
