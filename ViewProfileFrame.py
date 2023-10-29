import tkinter as tk
from authenticator import Authenticator
import os
from tkinter import messagebox


class ViewProfileFrame(tk.Frame):
    def __init__(self, master, user, student_page):
        super().__init__(master)
        self.show_password = None
        self.master = master
        self.user = user
        self.student_page = student_page

        font_format = ("Arial", 12)

        self.firstname_label = tk.Label(self, text="First Name:", font=font_format)
        self.firstname_label.pack()

        self.lastname_label = tk.Label(self, text="Last Name:", font=font_format)
        self.lastname_label.pack()

        self.email_label = tk.Label(self, text="Email:", font=font_format)
        self.email_label.pack()

        self.email_entry = tk.Entry(self)
        self.email_entry.pack()

        self.role_label = tk.Label(self, text="Role:", font=font_format)
        self.role_label.pack()

        self.username_label = tk.Label(self, text="UserName:", font=font_format)
        self.username_label.pack()

        self.password_label = tk.Label(self, text="Password:", font=font_format)
        self.password_label.pack()

        self.password_entry = tk.Entry(self, show="*")
        self.password_entry.pack()

        self.show_password = tk.Button(self, text="Show Password", command=self.toggle_password_visibility)
        self.show_password.pack()

        view_profile_button = tk.Button(self, text="View Personal Information", command=self.view_info)
        view_profile_button.pack()

        update_profile_button = tk.Button(self, text="Update Personal Details", command=self.update_profile)
        update_profile_button.pack()

        return_button = tk.Button(self, text="Return", command=self.student_page_return)
        return_button.pack()

        self.user_data = self.load_user_data(self.user.get_username())

    def view_info(self):
        self.username_label.config(text=f"Username: {self.user.get_username()}")
        self.firstname_label.config(text=f"Username: {self.user.get_first_name()}")
        self.lastname_label.config(text=f"Username: {self.user.get_last_name()}")
        self.email_entry.delete(0, tk.END)
        self.email_entry.insert(0, self.user.get_email())
        self.role_label.config(text=f"Role: {self.user.get_role()}")
        self.password_entry.delete(0, tk.END)
        self.password_entry.insert(0, self.user.get_password())

    def toggle_password_visibility(self):
        if self.password_entry["show"] == "":
            self.password_entry.config(show="*")
            self.show_password.config(text="Show Password")
        else:
            self.password_entry.config(show="")
            self.show_password.config(text="Hide Password")

    def load_user_data(self, username_to_find):
        self.user_data = {}
        with open("data/registered_users.txt", "r") as file:
            for line in file:
                data = line.strip().split(',')
                username = data[0]
                if username == username_to_find:
                    self.user_data["username"] = username
                    self.user_data['password'] = data[1]
                    self.user_data['firstname'] = data[2]
                    self.user_data['lastname'] = data[3]
                    self.user_data['email'] = data[4]
                    self.user_data['role'] = data[5]
                    self.user_data['active_status'] = data[6]
        return self.user_data

    def update_user_data(self, updated_user_data):
        with open("data/registered_users.txt", "r") as file:
            lines = file.readlines()

        with open("data/registered_users.txt", "w") as file:
            for line in lines:
                data = line.strip().split(',')
                username = data[0]
                if username == updated_user_data["username"]:
                    line = f"{updated_user_data['username']},{updated_user_data['password']},{updated_user_data['firstname']},{updated_user_data['lastname']},{updated_user_data['email']},{updated_user_data['role']},{updated_user_data['active_status']}\n"
                file.write(line)

    def update_profile(self):
        self.user_data["email"] = self.email_entry.get()
        self.user_data["password"] = self.password_entry.get()
        self.update_user_data(self.user_data)
        messagebox.showinfo("Success", "Profile updated successfully!")

    def student_page_return(self):
        self.place_forget()
        self.student_page.place(relx=.5, rely=.5, anchor=tk.CENTER)
