import tkinter as tk
from tkinter import filedialog, messagebox

class PostFilter(tk.Frame):
    def __init__(self, master, user, return_page):
        super().__init__(master)
        self.master = master
        self.user = user
        self.return_page =return_page
        self.filename = ""
        self.bad_words = []
        

        self.load_button = tk.Button(self, text="Load .txt File", command=self.load_file)
        self.load_button.pack(pady=20)

        self.file_label = tk.Label(self, text="No file loaded.")
        self.file_label.pack(pady=10)

        self.bad_word_label = tk.Label(self, text="Add Bad Word:")
        self.bad_word_label.pack(pady=10)

        self.bad_word_entry = tk.Entry(self)
        self.bad_word_entry.pack(pady=10)

        self.add_button = tk.Button(self, text="Add Bad Word", command=self.add_bad_word)
        self.add_button.pack(pady=10)

        self.filter_button = tk.Button(self, text="Filter Posts", command=self.filter_posts)
        self.filter_button.pack(pady=20)

        self.return_button = tk.Button(self, text= "Return",command= self.return_to_previous )
        self.return_button.pack(pady=20)

    def load_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if file_path:
            self.filename = file_path
            self.file_label.config(text=file_path)

    def add_bad_word(self):
        word = self.bad_word_entry.get()
        if word:
            self.bad_words.append(word)
            self.bad_word_entry.delete(0, tk.END)

    def filter_posts(self):  # Renamed from filter_bad_words
        with open(self.filename, 'r') as file:
            lines = file.readlines()

        filtered_lines = []
        for line in lines:
            elements = line.strip().split('|')
            post_content = elements[3]
            
            if not any(bad_word in post_content for bad_word in self.bad_words):
                filtered_lines.append(line.strip())

        # Overwrite the file with the filtered contents
        with open(self.filename, 'w') as file:
            file.write('\n'.join(filtered_lines))

        messagebox.showinfo("Success", "Posts filtered successfully!")

    def return_to_previous(self):
        self.place_forget()
        self.return_page.place(relx=.5, rely=.5, anchor= tk.CENTER)