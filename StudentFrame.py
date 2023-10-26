import tkinter as tk
from tkinter import messagebox

from ForumPage import ForumPage
from mainPageFrame import MainPageFrame
from LearningModuleFrame import LearningModulePage
from ChallengePage import ChallengePage


class StudentFrame(MainPageFrame):
    def __init__(self, user, master):
        super().__init__(master)
        self.master = master
        self.user = user

    def create_widgets(self):
        super().create_widgets()

        module_button = tk.Button(self, text="Learning Module", command=self.learning_module)
        module_button.pack(fill=tk.X, padx=10, pady=5)

        take_quiz_button = tk.Button(self, text="Take Challenge", command=self.take_challenge)
        take_quiz_button.pack(fill=tk.X, padx=10, pady=5)

        forum_button = tk.Button(self, text="View Forum", command=self.view_forum)
        forum_button.pack(fill=tk.X, padx=10, pady=5)

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
