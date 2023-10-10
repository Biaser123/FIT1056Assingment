import tkinter as tk
from tkinter import ttk

from post import Comment, Post


class ForumPage(tk.Frame):
    def __init__(self, master, user):
        super().__init__(master)
        self.post_content_text = None
        self.add_comment_button = None
        self.new_comment_entry = None
        self.comment_listbox = None
        self.comment_label = None
        self.post_content_label = None
        self.post_title_label = None
        self.post_tree = None
        self.master = master
        self.user = user
        self.pack()
        self.create_widgets()
        self.new_post_window = None
        self.load_data_from_file()

    def create_widgets(self):
        # list
        post_list_frame = tk.Frame(self)
        post_list_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        self.post_tree = ttk.Treeview(post_list_frame, columns=("PostID", "Title", "Author"))
        self.post_tree.heading("#1", text="PostID")
        self.post_tree.column("#1", width=0, stretch=tk.NO)
        self.post_tree.heading("#1", text="", anchor=tk.W)
        self.post_tree.heading("#2", text="Title")
        self.post_tree.heading("#3", text="Author")
        self.post_tree.pack(fill=tk.BOTH, expand=True)

        self.update_post_list()

        self.post_tree.bind("<ButtonRelease-1>", self.show_post_details_popup)

        new_post_button = tk.Button(self, text="New Post", command=self.create_new_post)
        new_post_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

    def show_post_details_popup(self, event):
        selected_item = self.post_tree.selection()
        if selected_item:
            post_id = self.post_tree.item(selected_item[0], "values")[0]
            selected_post = Post.posts.get(int(post_id))

            if selected_post:
                post_popup_window = tk.Toplevel(self)
                post_popup_window.title(selected_post.title)

                post_details_frame = tk.Frame(post_popup_window)
                post_details_frame.pack()

                post_content_label = tk.Label(post_details_frame, text=selected_post.content)
                post_content_label.pack()

                comment_label = tk.Label(post_details_frame, text="Comments:")
                comment_label.pack()

                comment_listbox = tk.Listbox(post_details_frame, height=5, selectmode=tk.SINGLE)
                comment_listbox.pack()

                for comment in selected_post.comments:
                    comment_listbox.insert(tk.END, f"{comment.user.username}: {comment.content}")

                new_comment_entry = tk.Entry(post_details_frame, width=30)
                new_comment_entry.pack()

                add_comment_button = tk.Button(post_details_frame, text="Add Comment",
                                               command=lambda: self.add_comment(selected_post, new_comment_entry,
                                                                                comment_listbox))
                add_comment_button.pack()

    def update_post_list(self):
        for item in self.post_tree.get_children():
            self.post_tree.delete(item)

        posts = Post.get_all_posts()
        for post in posts:
            self.post_tree.insert("", "end", values=(post.post_id, post.title, post.user.username))

    def show_post_details(self, event):
        selected_item = self.post_tree.selection()
        if selected_item:
            post_id = selected_item[0]
            selected_post = Post.posts.get(post_id)

            if selected_post:
                self.post_title_label.config(text=selected_post.title)
                self.post_content_text.delete(1.0, tk.END)
                self.post_content_text.insert(tk.END, selected_post.content)
                self.comment_listbox.delete(0, tk.END)
                comments = Comment.get_comments_for_post(selected_post)
                for comment in comments:
                    self.comment_listbox.insert(tk.END, f"{comment.user.username}: {comment.content}")
        else:
            # Clear content when no post is selected
            self.post_title_label.config(text="")
            self.post_content_label.config(text="")
            self.comment_listbox.delete(0, tk.END)

    def add_comment(self, selected_post, new_comment_entry, comment_listbox):
        new_comment_content = new_comment_entry.get()
        new_comment = self.user.create_comment(selected_post, new_comment_content)
        comment_listbox.insert(tk.END, f"{new_comment.user.username}: {new_comment.content}")
        new_comment_entry.delete(0, tk.END)

    def create_new_post(self):
        new_post_window = tk.Toplevel(self)
        new_post_window.title("New Post")
        self.new_post_window = new_post_window

        new_post_frame = tk.Frame(new_post_window)
        new_post_frame.pack()

        title_label = tk.Label(new_post_frame, text="Title:")
        title_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")
        title_entry = tk.Entry(new_post_frame)
        title_entry.grid(row=0, column=1, padx=10, pady=10, sticky="w")

        content_label = tk.Label(new_post_frame, text="Content:")
        content_label.grid(row=1, column=0, padx=10, pady=10, sticky="ne")
        content_text = tk.Text(new_post_frame, width=30, height=10)
        content_text.grid(row=1, column=1, padx=10, pady=10, sticky="nw")

        create_button = tk.Button(new_post_frame, text="Create Post",
                                  command=lambda: self.submit_new_post(title_entry.get(),
                                                                       content_text.get("1.0", tk.END)))
        create_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    def submit_new_post(self, title, content):

        new_post = self.user.create_post(title, content)
        self.update_post_list()
        self.save_data_to_file()

        self.new_post_window.destroy()

    def save_data_to_file(self):
        with open("forum_data.txt", "w") as file:
            for post_id, post in Post.posts.items():

                file.write(f"Post,{post_id},{post.title},{post.content},{post.user.username},\n")

            for comment_id, comment in Comment.comments.items():

                file.write(f"Comment,{comment_id},{comment.user.username},{comment.post.post_id},{comment.content},\n")

    def load_data_from_file(self):
        try:
            with open("forum_data.txt", "r") as file:
                lines = file.readlines()
                for line in lines:
                    parts = line.strip().split(",")
                    if parts[0] == "Post":
                        post_id, title, content, username = parts[1:]
                        self.user.create_post(title, content, username=username)
                    elif parts[0] == "Comment":
                        comment_id, username, post_id, content = parts[1:]
                        post = Post.posts.get(int(post_id))
                        if post:
                            self.user.create_comment(post, content, username=username)

        except FileNotFoundError:
            pass
