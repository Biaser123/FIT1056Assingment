# third party import
import tkinter as tk
from tkinter import messagebox

from module_dic import *

class LearningModulePage(tk.Frame):
    def __init__(self,master, user):
        super().__init__(master)
        self.user = user
        self.master = master
        
        # Create module buttons
        module1_button = tk.Button(self.master, text = "Module 1", command= self.module_1)
        module1_button.grid(row =0, column = 0 , padx =10, pady=10)

        module2_button = tk.Button(self.master, text = "Module 2", command= self.module_2)
        module2_button.grid(row =1, column = 0 , padx =10, pady=10)

        module3_button = tk.Button(self.master, text = "Module 3",command= self.module_3)
        module3_button.grid(row =2, column = 0 , padx =10, pady=10)

        # module4_button = tk.Button(self.master, text = "Module 4")
        # module4_button.grid(row =3, column = 0 , padx =10, pady=10)

    def module_1(self): 
        # This function allow access to module 1
        self.place_forget()
        module1_frame = tk.Toplevel(self.master)
        module1_frame.title("Module 1")

        module1_heading = tk.Label(module1_frame, text= module_1['heading'], font = ("Arial Bold",25))
        module1_heading.grid(row=0)
        module1_heading.rowconfigure(1, weight=1)
        module1_heading.columnconfigure(1,weight=1)

        module1_content = tk.Label(module1_frame,text = module_1['content'], font = ("Arial",12))
        module1_content.grid(row = 1)
        

        module1_quiz = tk.Button(module1_frame, text= "Quiz 1")
        module1_quiz.grid (row =2)

    def module_2(self):
        # This function allow access to module 2
        self.place_forget()
        module2_frame = tk.Toplevel(self.master)
        module2_frame.title("Module 2")

        module2_heading = tk.Label(module2_frame, text= module_2['heading'], font = ("Arial Bold",25))
        module2_heading.grid(row=0)
        

        module2_content = tk.Label(module2_frame,text = module_2['content'], font = ("Arial",12))
        module2_content.grid(row = 1)

        module2_quiz = tk.Button(module2_frame, text= "Quiz 2")
        module2_quiz.grid (row =2)

    def module_3(self):
        # This function allow access to module 3
        self.place_forget()
        module3_frame = tk.Toplevel(self.master)
        module3_frame.title("Module 3")

        module3_heading = tk.Label(module3_frame, text= module_3['heading'], font = ("Arial Bold",25))
        module3_heading.grid(row=0)
        

        module3_content = tk.Label(module3_frame,text = module_3['content'], font = ("Arial",12))
        module3_content.grid(row = 1)

        module3_quiz = tk.Button(module3_frame, text= "Quiz 3")
        module3_quiz.grid (row =2)

    # def module_4(self):
    #     self.place_forget()
    #     module4_frame = tk.Toplevel(self.master)
    #     module4_frame.title("Module 4")

    #     module4_heading = tk.Label(module4_frame, text= module_4['heading'], font = ("Arial Bold",25))
    #     module4_heading.grid(row=0)
        

    #     module4_content = tk.Label(module4_frame,text = module_4['content'], font = ("Arial",12))
    #     module4_content.grid(row = 1)

    #     module4_quiz = tk.Button(module4_frame, text= "Quiz 4")
    #     module4_quiz.grid (row =2)
      
    
    






        

        



