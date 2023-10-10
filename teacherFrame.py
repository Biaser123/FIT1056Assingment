import tkinter as tk

from mainPageFrame import MainPageFrame


class TeacherFrame(MainPageFrame):
    def create_widgets(self):
        super().create_widgets()
        manage_module_button = tk.Button(self, text="Manage Module")
        manage_module_button.pack(fill=tk.X, padx=10, pady=5)

        manage_quiz_button = tk.Button(self, text="Manage Quiz")
        manage_quiz_button.pack(fill=tk.X, padx=10, pady=5)

        forum_button = tk.Button(self, text="View Forum")
        forum_button.pack(fill=tk.X, padx=10, pady=5)