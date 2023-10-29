import tkinter as tk
from module_dic import module
from QuizPage import QuizPage


class moduleFrame(tk.Frame):
    def __init__(self, master, module_page, module_selected, user):
        super().__init__(master)
        self.master = master
        self.module_page = module_page
        self.module_selected = module_selected
        self.user = user

        canvas = tk.Canvas(self, width=1200, height=500)
        canvas.grid(row=0, column=0)
        scroll_bar_y = tk.Scrollbar(self, orient='vertical', command=canvas.yview)
        scroll_bar_y.grid(row=0, column=1, sticky='ns')
        scroll_bar_x = tk.Scrollbar(self, orient='horizontal', command=canvas.xview)
        scroll_bar_x.grid(row=1, column=0, sticky='ew')
        canvas.config(yscrollcommand=scroll_bar_y.set, xscrollcommand=scroll_bar_x.set)

        second_frame = tk.Frame(canvas)

        canvas.create_window((0, 0), window=second_frame, anchor='nw')
        for i in range(0, 15):
            if module_selected == f"Module {i}":
                module3_heading = tk.Label(second_frame, text=module[i - 1]['heading'], font=("Arial Bold", 25))
                module3_heading.grid(row=0)
                module3_content = tk.Label(second_frame, text=module[i - 1]['content'], font=("Arial", 12))
                module3_content.grid(row=1)

        module_quiz = tk.Button(second_frame, text="Take Quiz", command=self.quiz)
        module_quiz.grid(row=2)
        return_button = tk.Button(second_frame, text="Return", command=self.module_return)
        return_button.grid(row=3)

        second_frame.update_idletasks()
        canvas.config(scrollregion=canvas.bbox("all"))

    def module_return(self):
        self.place_forget()
        self.module_page.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def quiz(self):
        self.place_forget()
        quiz_page = QuizPage(self.master, self.user, self)
        quiz_page.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
