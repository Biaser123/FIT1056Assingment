import tkinter as tk
from module_dic import quiz


class quizQuestion(tk.Frame):
    def __init__(self, master, quiz_page, quiz_selected, user):
        super().__init__(master)
        self.master = master
        self.quiz_page =quiz_page
        self.quiz_selected = quiz_selected
        self.user =user
        self.score = 0
        self.current_question = 0
        self.selected_answers ={}

        timemessage=tk.Label(self, text= "You have 30 minutes to complete this Quiz", font= ("Arial bold",13))
        timemessage.pack()
        timeduration = 5
        self.end_time = datetime.now()+timedelta(seconds= timeduration)
        self.time_label = tk.Label(self, text="", font= ('Arial',20))
        self.time_label.pack()
        self.update_timer()
        
        for i in range (1,6):
            if quiz_selected == f"Quiz {i}":
                self.questions = quiz[i-1]
                self.question_label = tk.Label(self, text='', font=("Arial", 12))
                self.question_label.pack(pady=10)
                self.user_answer = tk.IntVar()
                self.user_answer.set(-1)

                

                self.radio_buttons = []
                for i in range(4):
                    radio_button = tk.Radiobutton(self, text='', variable=self.user_answer, value= i )
                    radio_button.pack()
                    self.radio_buttons.append(radio_button)

                self.submit_button = tk.Button(self, text="Save First! Then click Next or Previous", command=self.check_answer)
                self.submit_button.pack(pady=10)
                self.prev_button = tk.Button (self, text = "Previous", command = self.previous_question)
                self.prev_button.pack(side = "left",pady= 10)
                self.next_button = tk.Button(self, text = "Next", command = self.next_question)    
                self.next_button.pack(side = "right", pady=10)   
                self.return_button = tk.Button(self,text = "Quit Quiz", command =self.quiz_return)
                self.return_button.pack(side= "bottom", pady=10)

                self.load_questions()

    def load_questions(self):
        question_data = self.questions[self.current_question]
        self.question_label.config(text = question_data['question'])
        for i in range(4):
            rb= self.radio_buttons[i]
            print(rb)
            rb.config(text = question_data['options'][i])

    def previous_question(self):
        if self.current_question > 0:
            self.current_question -= 1
            self.load_questions()
            self.user_answer.set(self.selected_answers.get(self.current_question,-1))

    def next_question(self):
        if self.current_question < len(self.questions)-1:
            self.current_question += 1
            self.load_questions()
            self.user_answer.set(self.selected_answers.get(self.current_question,-1))
        else:
            self.save_score()

    def check_answer(self):
        selected_option = self.user_answer.get()
        correct_option= self.questions[self.current_question]["correct option"]
        self.selected_answers[self.current_question] = selected_option
        if selected_option== correct_option:
            self.score += 1
        

    def save_score(self):
        with open("data/quiz_score.txt", "w") as file:
            file.write(f"{self.user.get_username()}: {self.score}/{len(self.questions)}")
        
        self.question_label.config(text=f"Quiz completed! Your score: {self.score}/{len(self.questions)}")
        for radio_button in self.radio_buttons:
            radio_button.config(state="disabled")
        self.submit_button.config(state="disabled")

    def quiz_return(self):
        self.place_forget()
        self.quiz_page.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def update_timer(self):
        current_time =datetime.now()
        time_left = self.end_time -current_time
        if time_left.total_seconds()<=0:
            self.time_label.config(text = f"Time's up! Your score: {self.score}/{len(self.questions)}")
            self.save_score()
            self.after(1000, self.quiz_return)
        else:
            self.time_label.config(text=str(time_left).split(".")[0])
            self.after(1000, self.update_timer)

