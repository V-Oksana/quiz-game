from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")
FONT2 = ("Arial", 12, "normal")

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Oksana's Quiz Game")
        self.window.config(bg=THEME_COLOR, pady=20, padx=20)
        self.score = 0

        self.score_lbl = Label(text=f"Score: {self.score}", font=FONT2, fg="white", bg=THEME_COLOR, highlightthickness=0, padx=20, pady=20)
        self.score_lbl.grid(column=1, row=0)

        self.canvas = Canvas(height=250, width=300, bg="white")
        self.question_text = self.canvas.create_text(150,
                                              125,
                                              text="Placeholder",
                                              font=FONT,
                                              fill="black",
                                              anchor="center", width=280)

        self.canvas.grid(column=0, row=1, columnspan=2)

        check_img = PhotoImage(file="images/true.png")
        cross_img = PhotoImage(file="images/false.png")

        self.right_btn = Button(highlightthickness=0, command=self.true_pressed)
        self.right_btn.config(image=check_img)
        self.right_btn.grid(column=0, row=2, pady=50)

        self.wrong_btn = Button(highlightthickness=0, command=self.false_pressed)
        self.wrong_btn.config(image=cross_img)
        self.wrong_btn.grid(column=1, row=2, padx=20, pady=20)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_lbl.config(text=f"Score: {self.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz!")
            self.right_btn.config(state="disabled")
            self.wrong_btn.config(state="disabled")

    def true_pressed(self):
        is_correct = self.quiz.check_answer("True")
        self.give_feedback(is_correct)

    def false_pressed(self):
        is_correct = self.quiz.check_answer("False")
        self.give_feedback(is_correct)

    def give_feedback(self, is_guessed_correctly):
        if is_guessed_correctly:
            self.score += 1
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.get_next_question)

