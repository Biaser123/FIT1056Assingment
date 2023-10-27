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

        self.canvas = tk.Canvas(self, width=100, height=540)
        self.canvas.grid(row=0, column=0, sticky="nsew")
        scroll_bar = tk.Scrollbar(self, orient='vertical', command=self.canvas.yview)
        scroll_bar.grid(row=0, column=1, sticky='ns')
        self.canvas.config(yscrollcommand=scroll_bar.set)
        self.scrollable_frame = tk.Frame(self.canvas)
        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor='nw')
        self.scrollable_frame.bind("<Configure>", self.on_frame_configure)
        self.canvas.bind("<Configure>", self.on_canvas_configure)

        for module in range(1, 6):
            # Create module buttons
            module_name = f"Module {module}"
            self.create_module_button(module_name)

        return_button = tk.Button(self.scrollable_frame, text="Return", command=self.return_func)
        return_button.grid(row=module + 1)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

    def on_frame_configure(self, event):
        self.scrollable_frame.update_idletasks()
        self.canvas.config(scrollregion=self.canvas.bbox("all"))

    def on_canvas_configure(self, event):
        self.canvas.config(scrollregion=self.canvas.bbox("all"))

    def create_module_button(self, module_name):
        is_active = self.module_status_dict.get(module_name, True)

        if is_active:
            module_button = tk.Button(self.scrollable_frame, text=module_name,
                                      command=lambda m=module_name: self.module(m))
            module_button.grid(row=len(self.module_buttons) + 1, column=0)
        else:
            module_button = tk.Label(self.scrollable_frame, text=module_name, fg="gray")
            module_button.grid(row=len(self.module_buttons) + 1, column=0)

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
