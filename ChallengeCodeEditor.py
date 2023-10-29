# third party and local imports
import tkinter as tk
from tkinter import filedialog,font, messagebox
import subprocess
from module_dic import challenges

file_path = '' # globalis the path file to use when click run the code in the created IDE

class ChallengeCodeEditor(tk.Frame):
    """
    Class definition for the ChallengeCodeEditor class
    """
    def __init__(self, master,challenge_selected , user, return_challenge):
        super().__init__(master)
        self.master = master
        self.challenge_selected = challenge_selected
        self.user = user
        self.return_challenge = return_challenge
        
        """
        Constructor for the AdminForumPage class,
        :param master: tkinter frame
        :param user: inherited from User class
        :param challenge_selected: string
        :param return_challeng: frame
        """
        self.scroll_bar = tk.Scrollbar(self)
        self.scroll_bar.pack(side= tk.RIGHT, fill= tk.Y)

        self.hoz_scroll = tk.Scrollbar(self)
        self.hoz_scroll.pack(side= tk.BOTTOM, fill= tk.Y)

        # create the text widget for code editor
        self.code_editor = tk.Text(self, yscrollcommand= self.scroll_bar.set,xscrollcommand= self.hoz_scroll.set)
        self.code_editor.pack()

        # create console for output of the code
        self.code_output =tk.Text(self, height= 10)
        self.code_output.pack()

        # Create the toolbar menu
        my_menu= tk.Menu(self)
        self.master.config(menu= my_menu)

        # The toolbar menu include Save, New, Open, Save As tools
        file_menu = tk.Menu(my_menu, tearoff= False)
        my_menu.add_cascade(label= "File", menu = file_menu)
        file_menu.add_command(label= "New", command= self.new_file)
        file_menu.add_command(label= "Open", command= self.open_file)
        file_menu.add_command(label= "Save", command= self.save_as)
        file_menu.add_command(label= "Save As", command= self.save_as)

        # Create toolbar to run the code
        run_bar = tk.Menu(my_menu, tearoff= False)
        my_menu.add_cascade(label= "Run", menu = run_bar)
        run_bar.add_command(label= 'Run', command=self.run)

        # Display status of the file
        self.status_bar = tk.Label(self, text ="Ready", anchor= tk.E)
        self.status_bar.pack(fill= tk.X, side = tk.BOTTOM, ipady= 5)

        # Create run code button
        run_button=  tk.Button(self,text = 'Run', command= self.run)
        run_button.pack()

        # Create Submit Code Button
        submit_button = tk.Button(self, text ="Submit Code", command =lambda m= f"{challenge_selected}":self.submit_code(m))
        submit_button.pack()

        #Create Return Button 
        return_button = tk.Button(self,text ="Return", command=self.return_to_last_page)
        return_button.pack()

    # This method is used to run the code editor when 'Run' button is clicked on command
    def run(self):
        if file_path == '': #If the there is no file path, prompt user to save the file
            messagebox.showinfo(title= None, message= "Please save your code")
            return
        command = f'python3.10 {file_path}' # the command line to execute the code on the console
        process = subprocess.Popen(command,stdout=subprocess.PIPE,stderr=subprocess.PIPE, shell=True)
        output, error =process.communicate()
        self.code_output.insert('1.0',output)
        self.code_output.insert('1.0',error)

    def new_file(self):
        self.code_editor.delete("1.0",tk.END)
        self.master.title('New File')
        self.status_bar.config(text= "New File")

    def open_file(self):
        path = filedialog.askopenfilename(title= "Open File", filetypes=[("Python Files",'*.py')])
        with open(path,'r') as file:
            code = file.read()
            self.code_editor.delete('1.0',tk.END)
            self.code_editor.insert('1.0', code)
            self.set_file_path(path)
        
    def save_as(self):
        if file_path =='':
            path = filedialog.asksaveasfilename(title= "Save File", filetypes=[("Python Files","*.py")])
        else:
            path = file_path
        with open(path,'w') as file:
            code = self.code_editor.get("1.0", tk.END)
            file.write(code)
            self.set_file_path(path)
    
    def set_file_path(self, path):
        global file_path
        file_path =path

    def return_to_last_page(self):
        self.place_forget()
        self.return_challenge.place(relx=.5, rely=.5, anchor= tk.CENTER)

    def submit_code(self, challenge_selected):
        print(challenge_selected)
        my_code =str(self.code_editor.get(1.0, tk.END))
        for challenge in range(1,len(challenges)+1):
            if challenge_selected == f"Challenge {challenge}":
                with open ("data/code_submission.txt","a") as file:
                    file.write(f"Code Submission from {self.user.get_username()}: Challenge {challenge_selected}: {my_code}\n")
        messagebox.showinfo(title= None, message="Sucessfully submitted")