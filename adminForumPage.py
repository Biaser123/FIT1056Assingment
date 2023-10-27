from tkinter import messagebox, ttk

from ForumPage import ForumPage
from post import Post
import tkinter as tk


class AdminForumPage(ForumPage):
    def __init__(self, master, user):
        self.selected_post = None
        self.delete_post_button = None
        super().__init__(master, user)

    def create_widgets(self):
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

        # "Delete Post" button (hidden by default)
        self.delete_post_button = tk.Button(self, text="Delete Post",
                                            command=lambda: self.delete_post(self.selected_post))
        self.delete_post_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
        self.delete_post_button.grid_remove()  # Hide the "Delete Post" button

    def show_post_details_popup(self, event):
        # Call the parent class method to show post details popup
        super().show_post_details_popup(event)

        selected_item = self.post_tree.selection()
        if selected_item:
            post_id = self.post_tree.item(selected_item[0], "values")[0]
            self.selected_post = Post.posts.get(int(post_id))

            if self.selected_post:
                # Show the "Delete Post" button
                self.delete_post_button.grid()

    def delete_post(self, post):

        result = messagebox.askyesno("Confirm Delete", f"Are you sure you want to delete the post '{post.title}'?")
        if result:
            # Delete the post
            post.delete()
            # Update the UI
            self.update_post_list()

            # Save data to file after deletion
            self.save_data_to_file()


