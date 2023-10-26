import tkinter as tk
from module_dic import quiz
from quizQuestionPage import quizQuestion

class QuizPage(tk.Frame):
    def __init__(self,master, user, module_frame):
        super().__init__(master)
        self.user = user
        self.master = master
        self.module_frame = module_frame


        for i in range (1,6):
            quiz_button = tk.Button(self, text = f"Quiz {i}", command= lambda m= f"Quiz {i}":self.quiz(m))
            quiz_button.grid(row =i, padx =10, pady=10)

        return_button =tk.Button(self, text="Return", command= self.module_frame_return)
        return_button.grid(row = i+1, padx=10, pady=10)

    def quiz(self, quiz_selected):
        self.place_forget()
        quiz_frame = quizQuestion(self.master, self, quiz_selected, self.user)
        quiz_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def module_frame_return(self):
        self.place_forget()
        self.module_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        
