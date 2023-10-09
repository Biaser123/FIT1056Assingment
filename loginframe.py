# Third party imports
import tkinter as tk
from tkinter import messagebox
import time

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

        # Logo image for the login page
        login_canvas = tk.Canvas(master=self, width=128, height=128)
        login_canvas.grid(row=0, columnspan=2, sticky=tk.S, padx=10, pady=10)

        # Image obtained from:
        # https://www.veryicon.com/icons/healthcate-medical/medical-icon-two-color-icon/ico-health-clinic.html
        image_path = "./images/python-5-128.png"
        self.login_logo = tk.PhotoImage(file=image_path)
        login_canvas.create_image(0, 0,
                                  anchor=tk.NW,
                                  image=self.login_logo)

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
        self.username = tk.Entry(master=self,textvariable= self.username)
        self.username.grid(row=2, column=1,sticky=tk.W, padx=10, pady=10)

        # Label to ask user for Password
        password_label = tk.Label(master=self, text="Password:")
        password_label.grid(row=3, column=0, sticky=tk.E, padx=10, pady=10)

        # Variable and input widget for password
        self.password = tk.StringVar()
        self.password = tk.Entry(master=self, textvariable= self.password, show=".")
        self.password.grid(row = 3, column= 1,sticky=tk.W, padx=10, pady=10)


        # Button to login
        login_button = tk.Button(master=self, text="Login",
                                 command=self.authenticate_login)
        login_button.grid(row=4, columnspan=2, padx=10, pady=10)

        # Variable and label to inform user of login outcome
        self.login_text = tk.StringVar()
        # TODO: est. 2 lines
        label = tk.Label(master=self, textvariable= self.login_text, relief= tk.FLAT)
        label.grid(row =6 ,columnspan= 10, padx= 10, pady= 10)

        interface = self.master
        self.registration_window = tk.Toplevel(interface)
        self.registration_window.title("Registation Page")
        self.registration_window.withdraw()
        
        
        #Title of Registration page
        registration_title = tk.Label(self.registration_window,text="Registration Page", font=("Arial Bold",25))
        registration_title.grid(row = 0 , column=1)
        registration_title.grid_rowconfigure(1,weight=1)
        registration_title.grid_columnconfigure(1,weight=1)

        # Registration Button on Main Page
        register_button = tk.Button(master=self, text ="Register",command = self.registration_page_open)
        register_button.grid(row =5 ,columnspan=2, padx =10, pady =10)

        #Registration Button on Registration Page
        register_button_reg = tk.Button(self.registration_window, text= "Register", command= self.register_function)
        register_button_reg.grid(row= 8, column=1)
        register_button_reg.grid_rowconfigure(1,weight=1)
        register_button_reg.grid_columnconfigure(1,weight=1)

        # First name label and Entry
        firstname_label = tk.Label(self.registration_window, text= "First name:")
        firstname_label.grid(row=1, column=0, sticky=tk.E, padx=10, pady=10)
        self.first_name_reg = tk.StringVar()
        self.first_name_reg = tk.Entry(self.registration_window,textvariable= self.first_name_reg)
        self.first_name_reg.grid(row=1, column=1, sticky =tk.W, padx=10, pady=10 )

        # Last name label and Entry
        lastname_label = tk.Label(self.registration_window, text= "Last Name:")
        lastname_label.grid(row=2, column=0, sticky=tk.E, padx=10, pady=10)
        self.last_name_reg = tk.StringVar()
        self.last_name_reg = tk.Entry(self.registration_window,textvariable= self.last_name_reg)
        self.last_name_reg.grid(row=2, column=1, sticky =tk.W, padx=10, pady=10 )

        # dob_label = tk.Label(self.registration_window, text= "Date of Birth:")
        # dob_label.grid(row=3, column=0, sticky=tk.E, padx=10, pady=10)
        # self.date_of_birth = tk.StringVar()
        # self.date_of_birth = tk.Entry(self.registration_window,textvariable= self.date_of_birth)
        # self.date_of_birth.grid(row=3, column=1, sticky =tk.W, padx=10, pady=10 )


        # Username Label and Entry
        username_label = tk.Label(self.registration_window, text= "Username:")
        username_label.grid(row=4, column=0, sticky=tk.E, padx=10, pady=10)
        self.username_reg = tk.StringVar()
        self.username_reg = tk.Entry(self.registration_window,textvariable= self.username_reg)
        self.username_reg.grid(row=4, column=1, sticky =tk.W, padx=10, pady=10 )

        #Password Label and Entry
        password_label = tk.Label(self.registration_window, text= "Password:")
        password_label.grid(row=5, column=0, sticky=tk.E, padx=10, pady=10)
        self.password_reg = tk.StringVar()
        self.password_reg = tk.Entry(self.registration_window,textvariable= self.password_reg,show="*")
        self.password_reg.grid(row=5, column=1, sticky =tk.W, padx=10, pady=10 )

        # Email Label and Entry
        email_label = tk.Label(self.registration_window, text= "Email:")
        email_label.grid(row=6, padx=10, pady=10)
        self.email_reg = tk.StringVar()
        self.email_reg = tk.Entry(self.registration_window,textvariable= self.email_reg)
        self.email_reg.grid(row=6, column=1, padx=10, pady=10 )

        #Role Label and Entry
        self.role_reg = tk.StringVar()
        self.role_reg.set("")
        role_label = tk.Label(self.registration_window, text= "Role:")
        role_label.grid(row= 7, padx =10, pady=10)
        student_role= tk.Radiobutton(self.registration_window, variable= self.role_reg, text = "Student", value ="Student")
        student_role.grid(row=7, column=1)
        teacher_role = tk.Radiobutton(self.registration_window, variable= self.role_reg, text = "Teacher", value ="Teacher")
        teacher_role.grid(row=7, column=2)

    def registration_page_open(self):
        self.master.withdraw()
        self.registration_window.deiconify()

    def register_function(self):
        self.first_name_reg= self.first_name_reg.get()
        self.last_name_reg= self.last_name_reg.get()
        self.username_reg= self.username_reg.get()
        self.password_reg =self.password_reg.get()
        self.email_reg = self.email_reg.get()
        self.role_reg = self.role_reg.get()

        if not self.username_reg or not self.password_reg or not self.last_name_reg or not self.first_name_reg or not self.role_reg:
            messagebox.showerror("Error", "Please fill in all fields.")
            return
    
        with open("registered_users.txt","a") as file:
            file.write(f"{self.username_reg},{self.password_reg},{self.first_name_reg},{self.last_name_reg},{self.email_reg},{self.role_reg},{'1'}\n")

        messagebox.showinfo(message="Registration Succesfully Saved.")
        self.registration_window.withdraw()
        self.master.deiconify()    


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
