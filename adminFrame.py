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

        custom_font = font.Font(size=15)

        first_row_frame = tk.Frame(self)
        first_row_frame.pack(side="top")

        self.profile_image = tk.PhotoImage(file="images/pngegg.png")
        self.profile_image = self.profile_image.subsample(11) 
        button = tk.Button(first_row_frame, text="Profile",command=self.view_profile, image=self.profile_image, compound=tk.TOP, width=140, height = 130, font=custom_font)
        button.pack(side="left", padx=10, pady=5)

        self.filter_image = tk.PhotoImage(file="images/filter.png")
        self.filter_image = self.filter_image.subsample(11) 
        content_filter_button = tk.Button(first_row_frame, text="Content Filter",image=self.filter_image, compound=tk.TOP, width=140, height = 130, font=custom_font)
        content_filter_button.pack(side="left", padx=10, pady=5)

        self.module_image = tk.PhotoImage(file="images/module.png")
        self.module_image = self.module_image.subsample(13) 
        manage_module_button = tk.Button(first_row_frame, text="Manage Module", command=self.manage_module,image=self.module_image, compound=tk.TOP, width=140, height = 130,font=custom_font)
        manage_module_button.pack(side="left", padx=10, pady=5)

        second_row_frame = tk.Frame(self)
        second_row_frame.pack(side="top")

        self.challenge_image = tk.PhotoImage(file="images/challenge.png")
        self.challenge_image = self.challenge_image.subsample(11) 
        manage_quiz_button = tk.Button(second_row_frame, text="Manage Quiz",image=self.challenge_image, compound=tk.TOP, width=140, height = 130, font=custom_font)
        manage_quiz_button.pack(side="left", padx=10, pady=5)

        self.forum_image = tk.PhotoImage(file="images/forum.png")
        self.forum_image = self.forum_image.subsample(17) 
        manage_forum_button = tk.Button(second_row_frame, text="Manage Forum", command=self.manage_forum,image=self.forum_image, compound=tk.TOP, width=140, height = 130, font=custom_font)
        manage_forum_button.pack(side="left", padx=10, pady=5)

        self.usermanage_image = tk.PhotoImage(file="images/management.png")
        self.usermanage_image = self.usermanage_image.subsample(10) 
        user_activation_button = tk.Button(second_row_frame, text="User management", command=self.user_activation,image=self.usermanage_image, compound=tk.TOP, width=140, height = 130, font=font.Font(size=13))
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
        # activation_page =  
        activation_page.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
