import tkinter as tk


class QuizPage(tk.Frame):
    def __init__(self,master, user):
        super().__init__(master)
        self.user = user
        self.master = master

        quiz1_button = tk.Button(self.master, text = "Quiz 1", command= self.quiz_1)
        quiz1_button.grid(row =0, column = 0 , padx =10, pady=10)

        quiz2_button = tk.Button(self.master, text = "Quiz 2")
        quiz2_button.grid(row =1, column = 0 , padx =10, pady=10)

        quiz3_button = tk.Button(self.master, text = "Quiz 3")
        quiz3_button.grid(row =2, column = 0 , padx =10, pady=10)

    def quiz_1(self):
        self.place_forget()
        quiz1_frame = tk.Toplevel(self.master)
        quiz1_frame.title("Quiz 1")

        self.score = 0
        self.current_question = 0

        self.questions = [
            {
                "question": "What is Python?",
                "options": ["Programming Language", "An animal", "A function", "A module"],
                "correct_option": 0
            },
            {
                "question": "What can Python do?",
                "options": ["Python can supply power to the computer", "Python can create solid parts for 3D printing", "Python can be used for rapid prototyping, or for production-ready software development.", "Python can be used to chat with friends."],
                "correct_option": 2
            },
            {
                "question": "What will show on the cosole with this line of code (print('Hello, World!'))",
                "options": ["Hello World", "Hello, World!", "print('Hello, World!)", "Print('Hello, World!)"],
                "correct_option": 1
            }
        ]

        self.question_label = tk.Label(quiz1_frame, text="", font=("Arial", 12))
        self.question_label.pack(pady=10)

        self.radio_var = tk.IntVar()

        self.radio_buttons = []
        for i in range(4):
            radio_button = tk.Radiobutton(quiz1_frame, text="", variable=self.radio_var, value=i)
            radio_button.pack()
            self.radio_buttons.append(radio_button)

        self.submit_button = tk.Button(quiz1_frame, text="Submit", command=self.check_answer)
        self.submit_button.pack(pady=10)

        self.next_question()

    def next_question(self):
        if self.current_question < len(self.questions):
            question_data = self.questions[self.current_question]
            self.question_label.config(text=question_data["question"])

            for i in range(4):
                self.radio_buttons[i].config(text=question_data["options"][i])

            self.radio_var.set(-1)
        else:
            self.save_score()

    def check_answer(self):
        selected_option = self.radio_var.get()
        correct_option = self.questions[self.current_question]["correct_option"]

        if selected_option == correct_option:
            self.score += 1

        self.current_question += 1
        self.next_question()

    def save_score(self):
        with open("quiz_score.txt", "w") as file:
            file.write(f"{self.user.get_username()}: {self.score}/{len(self.questions)}")
        
        self.question_label.config(text=f"Quiz completed! Your score: {self.score}/{len(self.questions)}")
        for radio_button in self.radio_buttons:
            radio_button.config(state="disabled")
        self.submit_button.config(state="disabled")



