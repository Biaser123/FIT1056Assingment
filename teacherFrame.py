import tkinter as tk

from ForumPage import ForumPage
from mainPageFrame import MainPageFrame
from moduleManagementPage import ModuleManagementPage
from feedbackPage import FeedbackFrame

class TeacherFrame(MainPageFrame):
    def __init__(self, user, master=None):
        super().__init__(user, master)

    def create_widgets(self):
        super().create_widgets()
        manage_module_button = tk.Button(self, text="Manage Module", command=self.manage_module)
        manage_module_button.pack(fill=tk.X, padx=10, pady=5)

        manage_quiz_button = tk.Button(self, text="Manage Quiz")
        manage_quiz_button.pack(fill=tk.X, padx=10, pady=5)

        forum_button = tk.Button(self, text="View Forum", command=self.view_forum)
        forum_button.pack(fill=tk.X, padx=10, pady=5)
        
        feedback_button = tk.Button(self, text="Feedback",command= self.feedback_page)
        feedback_button.pack(fill = tk.X, padx=10, pady=5)

    def view_forum(self):
        forum_window = tk.Toplevel(self.master)
        forum_window.title("Forum")

        forum_page = ForumPage(forum_window, user=self.user)
        forum_page.pack()

    def manage_module(self):
        self.place_forget()
        module_page = ModuleManagementPage(self.master, self.user, self)
        module_page.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def feedback_page(self):
        self.place_forget()
        feedback_page= FeedbackFrame(self.master,self.user, self)
        feedback_page.place(relx=.5, rely=.5, anchor= tk.CENTER)
