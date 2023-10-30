import tkinter as tk
from tkinter.colorchooser import askcolor
class settingFrame(tk.Frame):
    def __init__(self, master, user, page_return):
        super().__init__(master)
        self.master= master
        self.user = user
        self.page_return = page_return

        self.font_label = tk.Label(self,text = "Select Font")
        self.font_label.pack()

        self.font_choices = ["Arial", "Times New Roman", "Verdana", "Helvetica"]
        self.font_var = tk.StringVar()
        self.font_var.set("Arial") 

        self.font_menu = tk.OptionMenu(self, self.font_var, *self.font_choices)
        self.font_menu.pack()

        self.background_color_label = tk.Label(self, text="Background Color:")
        self.background_color_label.pack()

        self.background_color_var = tk.StringVar()
        self.background_color_var.set("white")  # Default background color

        self.background_color_button = tk.Button(self, text="Pick Color", command=lambda: self.pick_color(self.background_color_var))
        self.background_color_button.pack()

        self.button_color_label = tk.Label(self, text="Button Color:")
        self.button_color_label.pack()

        self.button_color_var = tk.StringVar()
        self.button_color_var.set("lightblue")  # Default button color

        self.button_color_button = tk.Button(self, text="Pick Color", command=lambda: self.pick_color(self.button_color_var))
        self.button_color_button.pack()

        self.apply_button = tk.Button(self, text="Apply Theme", command=self.apply_theme)
        self.apply_button.pack()

        self.custom_button = tk.Button(self, text="Custom Button", font=("Arial", 12), bg="lightblue")
        self.custom_button.pack()

        self.return_button = tk.Button(self, text ="Return", command=self.return_to_previous)
        self.return_button.pack()
                
    def apply_theme(self):
        # Get user preferences
        selected_font = self.font_var.get()
        background_color = self.background_color_var.get()
        button_color = self.button_color_var.get()

        # Configure the root window
        self.master.configure(bg=background_color)

        # Configure the button with user-selected font and color
        self.custom_button.configure(font=(selected_font, 12), bg=button_color)

    def pick_color(sel,var):
        color = askcolor()[1]  # Open a color dialog and get the selected color
        var.set(color)

    def return_to_previous(self):
        self.place_forget()
        self.page_return.place(relx=.5, rely=.5, anchor =tk.CENTER)