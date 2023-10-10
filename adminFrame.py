import tkinter as tk

from mainPageFrame import MainPageFrame


class AdminFrame(MainPageFrame):
    def __init__(self, user, master=None):
        super().__init__(user, master)

    def create_widgets(self):
        super().create_widgets()
        content_filter_button = tk.Button(self, text="Content Filter")
        content_filter_button.pack(fill=tk.X, padx=10, pady=5)

        manage_module_button = tk.Button(self, text="Manage Module")
        manage_module_button.pack(fill=tk.X, padx=10, pady=5)

        manage_quiz_button = tk.Button(self, text="Manage Quiz")
        manage_quiz_button.pack(fill=tk.X, padx=10, pady=5)

        manage_forum_button = tk.Button(self, text="Manage Forum")
        manage_forum_button.pack(fill=tk.X, padx=10, pady=5)