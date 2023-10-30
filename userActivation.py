 
import tkinter as tk
from user import User
from authenticator import Authenticator

class userActivationFrame(tk.Frame):

    def __init__(self, master, return_page):
        """
        Constructor for the userActivationFrame class.
        :param master: Tk object; the main window that the
                       user activation frame is to be contained.
        """
        super().__init__(master)
        self.master = master
        self.return_page =return_page

        activate_canvas = tk.Canvas(self, width=128, height=128)
        activate_canvas.grid(row=0, columnspan=2, sticky=tk.S, padx=10, pady=10)

        title = tk.Label(master=self,
                               text="User Activation/Deactivation ",
                               font=("Arial Bold", 25))
        title.grid(row=1, columnspan=2, padx=10, pady=10)

        user_input_label = tk.Label(self, text="User to activate/deactivate:")
        user_input_label.grid(row=2, column=0, sticky=tk.E, padx=10, pady=10)

        # Variable and entry for user to activate/deactivate
        self.user = tk.StringVar()
        self.user_entry = tk.Entry(self, textvariable=self.user)
        self.user_entry.grid(row=2, column=1, sticky=tk.W, padx=10, pady=10)
        

        # Buttons to press to either activate or deactivate
        activate_button = tk.Button(self, text="Activate",
                            command=lambda: self.activate_user(self.user_entry.get()))
        activate_button.grid(row=3, columnspan=2, padx=10, pady=10)

        deactivate_button = tk.Button(self, text="Deactivate",
                            command=lambda: self.deactivate_user(self.user_entry.get()))
        deactivate_button.grid(row=4, columnspan=2, padx=10, pady=10)

        # Message to appear once either button is clocked
        self.success_text = tk.StringVar()
        action_message = tk.Label(self, textvariable=self.success_text)
        action_message.grid(row=4, columnspan=2, padx=10, pady=10)

        # Button to return to menu
        return_to_menu_button = tk.Button(self, text="Back",
                                 command=self.return_menu)
        return_to_menu_button.grid(row=6, columnspan=2, padx=10, pady=10)

    def check_user_exists(self, user):
        """
        Logic for authenticating a login procedure
        :param user: str - username entered by admin 
        :return: [bool, user_obj]
        """
        autheticator = Authenticator()
        existing_users = autheticator.users

        for user_obj in existing_users:
            if user_obj.get_username() == user:
                return [True, user_obj, autheticator.users.index(user_obj)]
            else:
                return [False, user_obj]



    def activate_user(self, user):
        '''
        Sets user's is_active state to True

        :param:
        user: user to activate
        '''
        print(self.user_entry.get())
        validity = self.check_user_exists(user)

        if validity[0] == True:
            with open("./data/registered_users.txt", "r+") as users_f:
                users_lines = users_f.readlines()
                users_lines[validity[2]] = users_lines[validity[2]][0:-1] + "1"
                self.success_text.set(f"{validity[1].get_username()}'s account has been activated")
        else:
            self.success_text.set(f"User has not been found.")

    def deactivate_user(self, user):
        '''
        Sets user's is_active state to False

        :param:
        user: user to deactivate
        '''
        validity = self.check_user_exists(user)
        if validity[0] == True:
            with open("./data/registered_users.txt", "r+") as users_f:
                users_lines = users_f.readlines()
                users_lines[validity[2]] = users_lines[validity[2]][0:-1] + "0"
                self.success_text.set(f"{validity[1].get_username()}'s account has been deactivated")
        else:
            self.success_text.set(f"User has not been found.")

    def return_menu(self):
        """
        Function to return to admin menu if button clicked.
        """
        self.place_forget()
        self.return_page.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
