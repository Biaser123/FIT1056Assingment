import tkinter as tk


class StudentFrame(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        # Profile button
        view_profile_button = tk.Button(self, text="Profile")
        view_profile_button.pack(fill=tk.X, padx=10, pady=5)

        # Take Quiz
        calculate_bmi_button = tk.Button(self, text="Take Quiz")
        calculate_bmi_button.pack(fill=tk.X, padx=10, pady=5)

        # forum
        view_appointments_button = tk.Button(self, text="View Forum")
        view_appointments_button.pack(fill=tk.X, padx=10, pady=5)

        # Log Out button
        log_out_button = tk.Button(self, text="Log Out")
        log_out_button.pack(fill=tk.X, padx=10, pady=5)

        if __name__ == "__main__":
            # Feel free to amend this block while working or testing,
            # but any amendments here should be reverted upon submission.
            # You will not be assessed for any work here, but if any code
            # written here causes an error when running week10_interface.py,
            # then marks will be deducted.
            pass
