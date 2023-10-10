import tkinter as tk

from mainPageFrame import MainPageFrame


class StudentFrame(MainPageFrame):
    def create_widgets(self):
        super().create_widgets()
        take_quiz_button = tk.Button(self, text="Take Quiz")
        take_quiz_button.pack(fill=tk.X, padx=10, pady=5)

        forum_button = tk.Button(self, text="View Forum")
        forum_button.pack(fill=tk.X, padx=10, pady=5)

        if __name__ == "__main__":
            # Feel free to amend this block while working or testing,
            # but any amendments here should be reverted upon submission.
            # You will not be assessed for any work here, but if any code
            # written here causes an error when running week10_interface.py,
            # then marks will be deducted.
            pass
