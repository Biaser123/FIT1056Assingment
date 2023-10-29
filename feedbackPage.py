import tkinter as tk
from tkinter import filedialog,font, messagebox
class FeedbackFrame(tk.Frame):
    def __init__(self, master, user, return_page):
        super().__init__(master)
        self.user= user
        self.master = master
        self.return_page= return_page

        self.my_feedback = tk.Text(self, wrap= tk.WORD, font=("Arial", 13), selectbackground= "blue", selectforeground="black", undo= "True")
        self.my_feedback.pack()
        toolbar_frame = tk.Frame(self)
        toolbar_frame.pack(fill=tk.X)

        my_menu= tk.Menu(self)
        self.master.config(menu= my_menu)

        file_menu = tk.Menu(my_menu, tearoff= False)
        my_menu.add_cascade(label= "File", menu = file_menu)
        file_menu.add_command(label= "New", command= self.new_file)
        file_menu.add_command(label= "Open", command= self.open_file)
        file_menu.add_command(label= "Save", command= self.save_file)
        file_menu.add_command(label= "Save As", command= self.save_as)

        edit_menu = tk.Menu(my_menu, tearoff= False)
        my_menu.add_cascade(label= "Edit", menu = edit_menu)
        edit_menu.add_command(label= "Undo", command=self.my_feedback.edit_undo, accelerator = "(Ctrl+z)")
        edit_menu.add_command(label = "Redo",command=self.my_feedback.edit_redo, accelerator= "(Ctrl+y)" ) 

        self.status_bar = tk.Label(self, text ="Ready", anchor= tk.E)
        self.status_bar.pack(fill= tk.X, side = tk.BOTTOM, ipady= 5)

        bold_button = tk.Button(toolbar_frame,text ="Bold", command= self.bold)
        bold_button.grid(row= 0, column=0, sticky= tk.NW)

        italic_button = tk.Button(toolbar_frame,text ="Italic", command= self.italic)
        italic_button.grid(row= 0, column=1, sticky= tk.NW)

        submit_button = tk.Button(self, text="Submit", command = self.submit_feedback)
        submit_button.pack(fill= tk.X)

        self.user_choice =tk.IntVar()
        self.user_choice.set(None)

        quiz_feedback_select = tk.Radiobutton(self,variable=self.user_choice, text = "Quiz Feedback", value= 1, command=self.selected_type)
        quiz_feedback_select.pack(fill=tk.X, side= tk.LEFT)

        system_feedback_select = tk.Radiobutton(self,variable= self.user_choice, text= "System Feedback", value=2, command=self.selected_type)
        system_feedback_select.pack(fill=tk.X, side= tk.LEFT)

        message = tk.Label(self, text = "Please select feedback type and fill in the feedback ", font =("Arial Bold",15))
        message.pack()

        return_button = tk.Button(self,text ="Return", command=self.return_to_last_page)
        return_button.pack()
        self.open_status_name = False

    def new_file(self):
        self.my_feedback.delete("1.0",tk.END)
        self.master.title('New File')
        self.status_bar.config(text= "New File")

    def open_file(self):
        self.my_feedback.delete("1.0",tk.END)
        text_file = filedialog.askopenfilename(title="Open File", filetypes=(("Text Files","*.txt"), ("All Files","*.*")))

        if text_file:
            self.open_status_name = text_file

        name = text_file
        self.status_bar.config(text = f"{name}   ")
        self.master.title(f"{name}")

        text_file = open(text_file,"r")
        content = text_file.read()
        self.my_feedback.insert(tk.END, content)

        text_file.close()

    def save_as(self):
        text_file = filedialog.asksaveasfilename(defaultextension=".*", title= "Save File", filetypes=(("Text Files","*.txt"), ("All Flies","*.*")))
        if text_file:
            name= text_file
            self.status_bar.config(text = f"Saved: {name}")
            self.master.title(f'{name}')

            text_file = open(text_file,"w")
            text_file.write(self.my_feedback.get(1.0, tk.END))

            text_file.close()

    def save_file(self):
        if self.open_status_name:
            text_file =open(text_file,"w")
            text_file.write(self.my_feedback.get(1.0,tk.END))
            text_file.close()

            self.status_bar.config(text = f"Saved: {self.open_status_name}")
        else:
            self.save_as()


    def bold(self):
        bold_font = font.Font(self.my_feedback, self.my_feedback.cget("font"))
        bold_font.configure(weight ="bold")

        self.my_feedback.tag_configure("bold", font= bold_font)
        current_tags =self.my_feedback.tag_names("sel.first")
        if "bold" in current_tags:
            self.my_feedback.tag_remove("bold", "sel.first","sel.last")
        else:
            self.my_feedback.tag_add("bold","sel.first", "sel.last")

    def italic(self):
        italic_font = font.Font(self.my_feedback, self.my_feedback.cget("font"))
        italic_font.configure(slant ="italic")

        self.my_feedback.tag_configure("italic", font= italic_font)
        current_tags =self.my_feedback.tag_names("sel.first")
        if "italic" in current_tags:
            self.my_feedback.tag_remove("italic", "sel.first","sel.last")
        else:
            self.my_feedback.tag_add("italic","sel.first", "sel.last")

    def selected_type(self):
        self.selected_option = self.user_choice.get()
        return self.selected_option
    
    def submit_feedback(self):
        feedback_content =str(self.my_feedback.get(1.0, tk.END))
        print(feedback_content)
        if self.selected_option == 1:
            with open ("data/feedback.txt","a") as file:
                file.write(f"Quiz Feedback from {self.user.get_username()}: {feedback_content}")
        elif self.selected_option ==2:
            with open ("data/feedback.txt","a") as file:
                file.write(f"System Feedback from {self.user.get_username()}: {feedback_content}")
    
        messagebox.showinfo(title=None, message="Feedback Sumitted!")

    def return_to_last_page(self):
        self.place_forget()
        self.return_page.place(relx=.5, rely=.5, anchor= tk.CENTER)




        

        

