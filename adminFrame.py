import tkinter as tk
from tkinter import font

from mainPageFrame import MainPageFrame
from moduleManagementPage import ModuleManagementPage
from adminForumPage import AdminForumPage
from login import CodeVenture


class AdminFrame(MainPageFrame):
    def __init__(self, user, master=None):
        super().__init__(user, master)

    def create_widgets(self):

        custom_font = font.Font(size=16)

        first_row_frame = tk.Frame(self)
        first_row_frame.pack(side="top")

        profile_button = tk.Button(first_row_frame, text="Profile", command= self.view_profile,width=15,height=6,font=custom_font)
        profile_button.pack(side="left", padx=10, pady=5)

        content_filter_button = tk.Button(first_row_frame, text="Content Filter",width=15,height=6,font=custom_font)
        content_filter_button.pack(side="left", padx=10, pady=5)

        manage_module_button = tk.Button(first_row_frame, text="Manage Module", command=self.manage_module,width=15,height=6,font=custom_font)
        manage_module_button.pack(side="left", padx=10, pady=5)

        second_row_frame = tk.Frame(self)
        second_row_frame.pack(side="top")

        manage_quiz_button = tk.Button(second_row_frame, text="Manage Quiz",width=15,height=6,font=custom_font)
        manage_quiz_button.pack(side="left", padx=10, pady=5)

        manage_forum_button = tk.Button(second_row_frame, text="Manage Forum", command=self.manage_forum,width=15,height=6,font=custom_font)
        manage_forum_button.pack(side="left", padx=10, pady=5)

        user_activation_button = tk.Button(second_row_frame, text="Activate/Deactivate a User", command=self.user_activation,width=15,height=6,font=custom_font)
        user_activation_button.pack(side="left", padx=10, pady=5)

    def manage_module(self):
        self.place_forget()
        module_page = ModuleManagementPage(self.master, self.user, self)
        module_page.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def manage_forum(self):
        forum_window = tk.Toplevel(self.master)
        forum_window.title("Forum")

        forum_page = AdminForumPage(forum_window, self.user)
        forum_page.pack()

    def user_activation(self):
        self.place_forget()
        