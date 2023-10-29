# Local and Thirt Party Imports
import tkinter as tk 
from module_dic import challenges
from ChallengeCodeEditor import ChallengeCodeEditor


class ChallengeFrame(tk.Frame):
    """
    Class definition for the ChallengeFrame class
    """
    def __init__(self, master, user, challenge_selected,return_page):
        super().__init__(master)
        self.master=  master
        self.user = user
        self.challenge_selected = challenge_selected
        self.return_page =return_page

        canvas = tk.Canvas(self, width = 970, height= 540)
        canvas.pack(fill = tk.BOTH, expand=1)
        scroll_bar_y = tk.Scrollbar(self, orient='vertical', command=canvas.yview)
        scroll_bar_y.pack(side = tk.RIGHT, fill=tk.Y)
        scroll_bar_x = tk.Scrollbar(self, orient='horizontal', command=canvas.xview)
        scroll_bar_x.pack(side= tk.BOTTOM, fill = tk.X)
        canvas.config(yscrollcommand=scroll_bar_y.set, xscrollcommand=scroll_bar_x.set)
        second_frame = tk.Frame(canvas)
        canvas.create_window((0, 0), window=second_frame, anchor='nw')

        for challenge in range(1,len(challenges)+1):
            if challenge_selected == f"Challenge {challenge}":
                module_heading = tk.Label(second_frame, text=challenges[challenge - 1]['heading'], font=("Arial Bold", 25))
                module_heading.grid(row=0)
                module_content = tk.Label(second_frame, text=challenges[challenge - 1]['content'], font=("Arial", 12))
                module_content.grid(row=1)

        challenge_button = tk.Button(second_frame, text="Take Challenge", command=lambda m= f"{challenge_selected}":self.challenge(m))
        challenge_button.grid(row=2)

        return_button = tk.Button(second_frame, text="Return", command=self.challenge_return)
        return_button.grid(row=3)

        second_frame.update_idletasks()
        canvas.config(scrollregion=canvas.bbox("all"))


    def challenge(self, challenge_selected):
        print(challenge_selected)
        self.place_forget()
        code_editor = ChallengeCodeEditor(self.master, challenge_selected, self.user, self)
        code_editor.place(relx= .5, rely=.5, anchor= tk.CENTER)
        
    def challenge_return(self):
        self.place_forget()
        self.return_page.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

