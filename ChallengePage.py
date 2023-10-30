import tkinter as tk
from ChallengeFrame import ChallengeFrame
from module_dic import *
class ChallengePage(tk.Frame):
    def __init__(self,master, user, student_page):
        super().__init__(master)
        self.user = user
        self.master = master
        self.student_page = student_page

        row_frame = tk.Frame(self)
        row_frame.pack(side="top")

        for challenge in range(1,len(challenges)+1):
            challenge_button = tk.Button(row_frame, text =f"Challenge {challenge}", command= lambda m= f"Challenge {challenge}":self.open_challenge(m),font=(13),width=17,height=7,bg="lightyellow")
            challenge_button.pack(side="left",padx=15)

        return_button = tk.Button(self, text="Return", command=self.return_page, width=10,height=3, bg= "lightgray")
        return_button.pack(pady=20)

    def open_challenge(self, challenge_selected):
        print(challenge_selected)
        self.place_forget()
        challenge_frame = ChallengeFrame(self.master, self.user, challenge_selected,self)
        challenge_frame.place(relx =.5, rely= .5, anchor=tk.CENTER)

    def return_page(self):
        self.place_forget()
        self.student_page.place(relx =.5, rely=.5, anchor =tk.CENTER)
        
  
                


        
        

            
        



        

