import tkinter as tk
from tkinter import ttk
from module_dic import *

custom_font = ("Helvetica", 16) 
red_color = "red"

class updateProgressFrame(tk.Frame):
    def __init__(self, master, user, return_page):
        super().__init__(master)
        self.master = master
        self.user = user
        self.return_page =return_page
        self.number_of_tasks = len(module)+len(quiz)
        self.progress_bar = ttk.Progressbar(self, maximum=100)
        self.progress_bar.pack(side="top",pady=10)

    
        self.progress_var ={}
        for index in range(self.number_of_tasks):
            if 0<= index <=4:
                self.progress_var[f"Module {index+1}"]=0
            elif 5<= index <=9:
                self.progress_var[f"Quiz {10-index}"]=0

        self.stored_progress = {task_name:0 for task_name in self.progress_var}
        

        self.checkboxes = {}
        
        for task_name in enumerate(self.progress_var):
            self.checkboxes[task_name] = tk.BooleanVar()
            checkbox =tk.Checkbutton(self, text = task_name, variable= self.checkboxes[task_name],  command=lambda tn=task_name: self.on_checkbox_toggle(tn))
            checkbox.pack(side="top", padx=10)

        return_button = tk.Button(self, text = "Return", command=self.return_to_page, width=15)
        return_button.pack(side="top", ipady =5)

    
    def update_progress_bar(self):
        total_progress = sum(self.progress_var.values())
        self.progress_bar["value"] = total_progress
        if hasattr(self, "username_label") and total_progress != 100:
            self.username_label.pack_forget()
        elif total_progress == 100:
            self.username_label = tk.Label(self, text="Well Done! You completed all Modules and Quizzes!",font=custom_font, fg=red_color,anchor='n')
            self.username_label.pack(side="bottom")

    def on_checkbox_toggle(self,task_name):
        if self.checkboxes[task_name].get():
            self.progress_var[task_name] = 100 / self.number_of_tasks
        else:
            self.progress_var[task_name] = 0
        self.update_progress_bar()

    def store_progress(self):
        global progress 
        for task_name in self.progress_var:
            self.stored_progress[task_name] = self.progress_var[task_name]
            progress = self.stored_progress[task_name]
            return(progress)

    def restore_progress(self):
        for task_name in self.stored_progress:
            self.progress_var[task_name] = self.stored_progress[task_name]
        self.update_progress_bar()

    def return_to_page(self):
        self.store_progress()
        print(self.store_progress())
        self.pack_forget()
        self.return_page.place(relx=.5, rely=.5, anchor = tk.CENTER)
