from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        # Window
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # Question
        self.canvas = Canvas(width=300, height=250, bg='white', highlightthickness=0)
        self.question_card_text = self.canvas.create_text(
            150,
            120,
            text="This is a question",
            font=('Arial', 20, 'italic'),
            fill='black',
            width=280
        )

        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        # Label
        self.label = Label(text="Score: 0", font=('Arial', 12), bg=THEME_COLOR)
        self.label.grid(column=1, row=0)

        # Buttons
        self.true_image = PhotoImage(file="./images/true.png")
        self.true_button = Button(
            image=self.true_image,
            highlightbackground=THEME_COLOR,
            highlightthickness=0,
            command=self.select_true
        )
        self.true_button.grid(column=0, row=2)

        self.false_image = PhotoImage(file='./images/false.png')
        self.false_button = Button(
            image=self.false_image,
            highlightbackground=THEME_COLOR,
            highlightthickness=0,
            command=self.select_false
        )
        self.false_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            self.label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_card_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_card_text, text="You have reached the end of the quiz")
            self.true_button.config(state='disabled')
            self.false_button.config(state='disabled')


    def select_true(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def select_false(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right: bool):
        if is_right:
            self.canvas.config(background='green')
        elif not is_right:
            self.canvas.configure(background='red')
        self.canvas.update()
        self.window.after(1000, self.get_next_question)
