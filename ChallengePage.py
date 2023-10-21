import tkinter as tk
from ChallengeSols import solutions
from module_dic import *
class ChallengePage(tk.Frame):
    def __init__(self,master, user):
        super().__init__(master)
        self.user = user
        self.master = master
        
        # Create module buttons
        challenge_label = tk.Label(self.master, text = module_1['challenge'], font = ("Arial Bold",15))
        challenge_label.grid(row =0, columnspan = 2 ,sticky= tk.E, padx =10, pady=10)

        challenge1_label = tk.Label(self.master, text = "Challenge 1 Answer Box:", font = ("Arial",12))
        challenge1_label.grid(row =1, column = 0 ,sticky= tk.E, padx =10, pady=10)

        self.challenge_var = tk.StringVar()
        self.challenge_entry = tk.Entry(self.master,textvariable= self.challenge_var)
        self.challenge_entry.grid(row=1, column= 1, sticky=tk.W, padx=10, pady=10)

        submit_button = tk.Button(self.master, text= "Submit", command= self.check_answers)
        submit_button.grid(row=2, column=1)

    def check_answers(self):
        answer = self.challenge_var.get()

        for challenge in solutions:
            if answer == solutions[challenge]:
                message = tk.Label(self.master, text = "Good work!", font= ("Arial",14))
                message.grid(row=3)

        
        with open ("saved_answers.txt","a") as file:
            file.write(f"Challenge 1's Student answers: {answer}\n")

            
        



        

