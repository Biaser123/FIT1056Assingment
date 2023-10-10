import tkinter as tk


class MainPageFrame(tk.Frame):
    def __init__(self, user, master=None):
        super().__init__(master)
        self.master = master
        self.user = user
        self.pack()
        self.create_widgets()
        self.add_logout_button()

    def create_widgets(self):
        profile_button = tk.Button(self, text="Profile")
        profile_button.pack(fill=tk.X, padx=10, pady=5)

    def add_logout_button(self):
        log_out_button = tk.Button(self, text="Log Out", command=self.logout)
        log_out_button.pack(fill=tk.X, padx=10, pady=(10, 20))

    def logout(self):
        self.place_forget()
        from loginframe import LoginFrame
        student_frame = LoginFrame(self.master)
        student_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
