import tkinter as tk

from mainPageFrame import MainPageFrame
from moduleManagementPage import ModuleManagementPage
from adminForumPage import AdminForumPage


class AdminFrame(MainPageFrame):
    def __init__(self, user, master=None):
        super().__init__(user, master)

    def create_widgets(self):
        super().create_widgets()
        content_filter_button = tk.Button(self, text="Content Filter")
        content_filter_button.pack(fill=tk.X, padx=10, pady=5)

        manage_module_button = tk.Button(self, text="Manage Module", command=self.manage_module)
        manage_module_button.pack(fill=tk.X, padx=10, pady=5)

        manage_quiz_button = tk.Button(self, text="Manage Quiz")
        manage_quiz_button.pack(fill=tk.X, padx=10, pady=5)

        manage_forum_button = tk.Button(self, text="Manage Forum", command=self.manage_forum)
        manage_forum_button.pack(fill=tk.X, padx=10, pady=5)

    def manage_module(self):
        self.place_forget()
        module_page = ModuleManagementPage(self.master, self.user, self)
        module_page.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def manage_forum(self):
        forum_window = tk.Toplevel(self.master)
        forum_window.title("Forum")

        forum_page = AdminForumPage(forum_window, self.user)
        forum_page.pack()
