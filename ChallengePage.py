import tkinter as tk
from ChallengeFrame import ChallengeFrame
from module_dic import *
class ChallengePage(tk.Frame):
    def __init__(self,master, user, student_page):
        super().__init__(master)
        self.user = user
        self.master = master
        self.student_page = student_page

        for challenge in range(1,len(challenges)+1):
            challenge_button = tk.Button(self, text =f"Challenge {challenge}", command= lambda m= f"Challenge {challenge}":self.open_challenge(m))
            challenge_button.pack()

        return_button = tk.Button(self, text="Return", command=self.return_page)
        return_button.pack()

    def open_challenge(self, challenge_selected):
        print(challenge_selected)
        self.place_forget()
        challenge_frame = ChallengeFrame(self.master, self.user, challenge_selected,self)
        challenge_frame.place(relx =.5, rely= .5, anchor=tk.CENTER)

    def return_page(self):
        self.place_forget()
        self.student_page.place(relx =.5, rely=.5, anchor =tk.CENTER)
        
  
                


        
        

            
        



        

