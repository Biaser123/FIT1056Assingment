import tkinter as tk
from tkinter import font

from ForumPage import ForumPage
from mainPageFrame import MainPageFrame
from moduleManagementPage import ModuleManagementPage
from feedbackPage import FeedbackFrame

class TeacherFrame(MainPageFrame):
    def __init__(self, user, master=None):
        super().__init__(user, master)

    def create_widgets(self):
        
        custom_font = font.Font(size=16)

        first_row_frame = tk.Frame(self)
        first_row_frame.pack(side="top")

        profile_button = tk.Button(first_row_frame, text="Profile", command= self.view_profile,width=15,height=6,font=custom_font)
        profile_button.pack(side="left", padx=10, pady=5)

        manage_module_button = tk.Button(first_row_frame, text="Manage Module", command=self.manage_module,width=15,height=6,font=custom_font)
        manage_module_button.pack(side="left", padx=10, pady=5)

        manage_quiz_button = tk.Button(first_row_frame, text="Manage Quiz",width=15,height=6,font=custom_font)
        manage_quiz_button.pack(side="left", padx=10, pady=5)

        second_row_frame = tk.Frame(self)
        second_row_frame.pack(side="top")

        forum_button = tk.Button(second_row_frame, text="View Forum", command=self.view_forum,width=15,height=6,font=custom_font)
        forum_button.pack(side="left", padx=10, pady=5)
        
        feedback_button = tk.Button(second_row_frame, text="Feedback",command= self.feedback_page,width=15,height=6,font=custom_font)
        feedback_button.pack(side="left", padx=10, pady=5)


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
