from tkinter import *
THEME_COLOR = "#375362"


class QuizInterface():
    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(background=THEME_COLOR, padx=20, pady=20)

        self.score_label = Label(text="Score: 0", background=THEME_COLOR, fg="white")
        self.score_label.grid(row=0, column=2, pady=10)

        self.canvas = Canvas(width=300, height=250)
        self.question_text = self.canvas.create_text(150, 125, text="Word on street", font=("Arial", 30, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=3)

        true_image = PhotoImage(file="./images/true.png")
        self.true_button = Button(image=true_image, highlightthickness=0, bd=0)
        self.true_button.grid(row=2, column=0, pady=20)

        false_image = PhotoImage(file="./images/false.png")
        self.false_button = Button(image=false_image, highlightthickness=0, bd=0)
        self.false_button.grid(row=2, column=2, pady=20)

        self.window.mainloop()

