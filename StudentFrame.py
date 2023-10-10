import tkinter as tk

from ForumPage import ForumPage
from mainPageFrame import MainPageFrame


class StudentFrame(MainPageFrame):
    def __init__(self, user, master=None):
        super().__init__(user, master)

    def create_widgets(self):
        super().create_widgets()
        take_quiz_button = tk.Button(self, text="Take Quiz")
        take_quiz_button.pack(fill=tk.X, padx=10, pady=5)

        forum_button = tk.Button(self, text="View Forum", command=self.view_forum)
        forum_button.pack(fill=tk.X, padx=10, pady=5)

    def view_forum(self):
        forum_window = tk.Toplevel(self.master)
        forum_window.title("Forum")

        forum_page = ForumPage(forum_window, user=self.user)
        forum_page.pack()
