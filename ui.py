from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        # self.question1 = self.question.next_question
        # self.question2 = self.question1.q_text
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(background=THEME_COLOR)
        self.Canvas = Canvas()
        self.Canvas.config(width=300, height=250, bg="white", highlightthickness=0)
        self.question_text = self.Canvas.create_text(
            150,
            125,
            width=280,
            text=f"some text",
            font=("Ariel", 20, "italic"), fill=THEME_COLOR)
        self.Canvas.grid(column=0, row=1, columnspan=2, padx=20, pady=20)

        self.score_label = Label(text="Score: 0", background=THEME_COLOR, foreground="white")
        self.score_label.grid(row=0, column=1)

        image_tick = PhotoImage(file="images/true.png")
        self.tick_button = Button(image=image_tick,
                                  highlightthickness=0,
                                  command=self.check_answer_is_correct)
        self.tick_button.grid(row=2, column=0, pady=20, padx=20)

        image_wrong = PhotoImage(file="images/false.png")
        self.wrong_button = Button(image=image_wrong,
                                   highlightthickness=0,
                                   command=self.check_answer_is_wrong)
        self.wrong_button.grid(row=2, column=1, pady=20, padx=20)

        self.get_next_question()


        self.window.mainloop()

    def get_next_question(self):
        self.Canvas.config(background="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.Canvas.itemconfig(self.question_text, text= q_text)
        else:
            self.Canvas.itemconfig(self.question_text, text="You have reached the end of game")
            self.wrong_button.config(state="disabled")
            self.tick_button.config(state="disabled")

    def check_answer_is_correct(self):
        self.give_feedback(self.quiz.check_answer("True"))


    def check_answer_is_wrong(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.Canvas.config(background="green")
        else:
            self.Canvas.config(background="red")
        self.window.after(1000, self.get_next_question)








