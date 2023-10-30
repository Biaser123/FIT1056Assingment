import tkinter as tk
from ViewProfileFrame import ViewProfileFrame
from authenticator import Authenticator
from settingFrame import settingFrame



class MainPageFrame(tk.Frame):

    def __init__(self, user, master=None):
        super().__init__(master)
        self.master = master
        self.user = user
        self.pack()
        self.create_widgets()
        self.add_logout_button()
        self.add_settings_button()

    def add_logout_button(self):
        log_out_button = tk.Button(self, text="Log Out", command=self.logout, width=10)
        log_out_button.pack(side="bottom", padx=10, pady=(10, 20))

    def add_settings_button(self):
        self.settings_image = tk.PhotoImage(file="images/settings.png")
        self.settings_image = self.settings_image.subsample(17) 
        settings_button = tk.Button(self, command =self.settings,image=self.settings_image, compound=tk.TOP, width=45, height = 33)
        settings_button.pack(side="top", padx=10, pady=5)

    def settings(self):
        self.place_forget()
        settings_page = settingFrame(self.master,self.user,self)
        settings_page.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def logout(self):
        self.place_forget()
        from loginframe import LoginFrame
        student_frame = LoginFrame(self.master)
        student_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def view_profile(self):
        self.place_forget()
        view_profile_page = ViewProfileFrame(self.master, self.user,self,)
        view_profile_page.place(relx=.5, rely =.5, anchor= tk.CENTER)
