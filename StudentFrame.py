import tkinter as tk
from tkinter import messagebox
from tkinter import font

from ForumPage import ForumPage
from mainPageFrame import MainPageFrame
from LearningModuleFrame import LearningModulePage
from ChallengePage import ChallengePage
from updateProgressFrame import updateProgressFrame
from feedbackPage import FeedbackFrame



class StudentFrame(MainPageFrame):
    def __init__(self, user, master):
        super().__init__(master)
        self.master = master
        self.user = user

    def create_widgets(self):

        custom_font = font.Font(size=16)

        first_row_frame = tk.Frame(self)
        first_row_frame.pack(side="top")

        profile_button = tk.Button(first_row_frame, text="Profile", command= self.view_profile,width=15,height=6,font=custom_font)
        profile_button.pack(side="left", padx=10, pady=5)

        module_button = tk.Button(first_row_frame, text="Learning Module", command=self.learning_module,width=15,height=6,font=custom_font)
        module_button.pack(side="left", padx=10, pady=5)

        take_quiz_button = tk.Button(first_row_frame, text="Take Challenge", command=self.take_challenge,width=15,height=6,font=custom_font)
        take_quiz_button.pack(side="left", padx=10, pady=5)

        second_row_frame = tk.Frame(self)
        second_row_frame.pack(side="top")

        forum_button = tk.Button(second_row_frame, text="View Forum", command=self.view_forum,width=15,height=6,font=custom_font)
        forum_button.pack(side="left", padx=10, pady=5)

        feedback_button = tk.Button(second_row_frame, text="Feedback",command= self.feedback_page,width=15,height=6,font=custom_font)
        feedback_button.pack(side="left", padx=10, pady=20)

        update_progress = tk.Button(second_row_frame, text="Update Progress", command =self.update_progress,width=15,height=6,font=custom_font)
        update_progress.pack(side="left", padx=10, pady=5)

    def view_forum(self):
        forum_window = tk.Toplevel(self.master)
        forum_window.title("Forum")

        forum_page = ForumPage(forum_window, user=self.user)
        forum_page.pack()

        # self.place_forget()

    def learning_module(self):
        # module_window = tk.Toplevel(self.master)
        # module_window.title("Learning Module")
        self.place_forget()
        module_page = LearningModulePage(self.master, self.user, self)
        module_page.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        # self.place_forget()

    def take_challenge(self):
        challenge_window = tk.Toplevel(self.master)
        challenge_window.title("Challenge")

        challenge_page = ChallengePage(challenge_window, user=self.user)
        challenge_page.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        # self.place_forget()

    def feedback_page(self):
        self.place_forget()
        feedback_page= FeedbackFrame(self.master,self.user, self)
        feedback_page.place(relx=.5, rely=.5, anchor= tk.CENTER)

    def update_progress(self):
        self.place_forget()
        update_page = updateProgressFrame(self.master, self.user, self)
        # update_page.place(relx=.5, rely=.5, anchor= tk.CENTER)
        update_page.pack(padx=10,pady=10)
