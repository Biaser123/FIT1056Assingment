import tkinter as tk

# Local application imports
from authenticator import Authenticator


class LoginFrame(tk.Frame):
    """
    The class definition for the LoginFrame class.
    """

    def __init__(self, master):
        """
        Constructor for the LoginFrame class.
        :param master: Tk object; the main window that the
                       login frame is to be contained.
        """
        super().__init__(master=master)

        # Logo UI for the login page
        login_canvas = tk.Canvas(master=self, width=128, height=128)
        login_canvas.grid(row=0, columnspan=2, sticky=tk.S, padx=10, pady=10)

        # Image obtained from:
        # https://www.veryicon.com/icons/healthcate-medical/medical-icon-two-color-icon/ico-health-clinic.html
        # image_path = "./images/week09_image.png"
        # self.login_logo = tk.PhotoImage(file=image_path)
        # login_canvas.create_image(0, 0,
        #                           anchor=tk.NW,
        #                           image=self.login_logo)

        # Label containing the welcome heading
        login_title = tk.Label(master=self,
                               text="Welcome to CodeVenture",
                               font=("Arial Bold", 25))
        login_title.grid(row=1, columnspan=2, padx=10, pady=10)

        # Label to ask user for Username
        username_label = tk.Label(master=self, text="Username:")
        username_label.grid(row=2, column=0, sticky=tk.E, padx=10, pady=10)

        # Variable and input widget for username
        self.username = tk.StringVar()
        username_entry = tk.Entry(master=self, textvariable=self.username)
        username_entry.grid(row=2, column=1, padx=10, pady=10, sticky=tk.W)

        # Label to ask user for Password
        password_label = tk.Label(master=self, text="Password:")
        password_label.grid(row=3, column=0, sticky=tk.E, padx=10, pady=10)

        # Variable and input widget for password
        self.password = tk.StringVar()
        password_entry = tk.Entry(master=self, textvariable=self.password, show="●")
        password_entry.grid(row=3, column=1, padx=10, pady=10, sticky=tk.W)

        # Button to login
        login_button = tk.Button(master=self, text="Login",
                                 command=self.authenticate_login)
        login_button.grid(row=4, column=0, columnspan=2,padx=10, pady=10)

        # Button to register
        login_button = tk.Button(master=self, text="Register",
                                 command=self.authenticate_login)
        login_button.grid(row=4, column=1, padx=10, pady=10)

        # Variable and label to inform user of login outcome
        self.login_text = tk.StringVar()
        login_text_label = tk.Label(master=self, textvariable=self.login_text)
        login_text_label.grid(row=5, columnspan=2, padx=10, pady=10)

    def authenticate_login(self):
        """
        Frontend function for the authentication procedure.
        This is invoked when the login button is clicked.
        :return: None
        """
        authenticator = Authenticator()
        if authenticator.authenticate(self.username.get(),
                                      self.password.get()):
            self.login_text.set("Login successfully!")
        else:
            self.login_text.set("Failed to login")


if __name__ == "__main__":
    # Feel free to amend this block while working or testing,
    # but any amendments here should be reverted upon submission.
    # You will not be assessed for any work here, but if any code
    # written here causes an error when running week09_interface.py,
    # then marks will be deducted.
    pass
