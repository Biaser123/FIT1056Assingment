import tkinter as tk
from tkinter import messagebox
from mainPageFrame import MainPageFrame
from module_dic import module
from QuizPage import QuizPage
from moduleFrame import moduleFrame


class LearningModulePage(tk.Frame):
    def __init__(self, master, user, student_page):
        super().__init__(master)
        self.user = user
        self.master = master
        self.student_page = student_page
        self.module_buttons = {}
        self.module_status_dict = self.load_module_states()

        self.canvas = tk.Canvas(self, width=1200, height=540)
        self.canvas.grid()
        self.canvas.grid_rowconfigure(0, weight=1)
        self.scrollable_frame = tk.Frame(self.canvas)
        self.canvas.create_window((600,250),window=self.scrollable_frame)
        self.scrollable_frame.bind("<Configure>", self.on_frame_configure)
        self.canvas.bind("<Configure>", self.on_canvas_configure)

        for module in range(1, 6):
            # Create module buttons
            module_name = f"Module {module}"
            self.create_module_button(module_name)

        return_button = tk.Button(self.scrollable_frame, text="Return", command=self.return_func,width=10,height=2)
        return_button.grid(row=1,column=3,pady=(100,0))

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

    def on_frame_configure(self, event):
        self.scrollable_frame.update_idletasks()
        self.canvas.config(scrollregion=self.canvas.bbox("all"))

    def on_canvas_configure(self, event):
        self.canvas.config(scrollregion=self.canvas.bbox("all"))

    def create_module_button(self, module_name):
        custom_font = ("Helvetica",20, 'bold')
        is_active = self.module_status_dict.get(module_name, True)

        if is_active:
            module_button = tk.Button(self.scrollable_frame, text=module_name,
                                      command=lambda m=module_name: self.module(m),width=12,height=6,bg="lightblue",font=custom_font)
            module_button.grid(row=0, column=len(self.module_buttons) + 1, padx=7)
        else:
            module_button = tk.Button(self.scrollable_frame, text=f"{module_name}\n(Unavailable)" , width=12,height=6, fg="gray",font=custom_font)
            module_button.grid(row=0, column=len(self.module_buttons) + 1,padx=7)

        self.module_buttons[module_name] = module_button

    def module(self, module_selected):
        is_active = self.module_status_dict.get(module_selected, True)

        if is_active:
            print(module_selected)
            self.place_forget()
            module_page = moduleFrame(self.master, self, module_selected, self.user)
            module_page.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        else:
            messagebox.showwarning("Module Not Available",
                                   f"The selected module ({module_selected}) is not currently available.")

    def return_func(self):
        self.place_forget()
        self.student_page.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def load_module_states(self):
        module_states = {}
        try:
            with open('data/module_states.txt', 'r') as file:
                lines = file.readlines()
                for line in lines:
                    module_name, state = line.strip().split(',')
                    module_states[module_name] = (state == 'Active')
                    print(f"Module name: {module_name}, State: {state}")
        except FileNotFoundError:
            pass
        return module_states
