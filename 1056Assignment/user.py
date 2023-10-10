""" Constructor: def __init__(self, user_id, first_name, last_name, username, password, email, role):
#         Attributes: self.user_id = user_id
#                     self.first_name = first_name
#                     self.last_name = last_name
#                     self.username = username
#                     self.password = password
#                     self.email = email
#                     self.role = role
#                     self.is_logged_in = False
                      User.users[name] =self
#         Methods: login(self, entered_password)
#                  logout(self)
#                  """


# class User:
#     users = {}
#     next_user_id = 1

#     def __init__(self, user_id, first_name, last_name, username, password, email, role):
#         self.user_id = user_id
#         self.first_name = first_name
#         self.last_name = last_name
#         self.username = username
#         self.password = password
#         self.email = email
#         self.role = role
#         self.is_logged_in = False
#         # profile data (Wei Lu)
#         self.profile_data = {}
#         # post and comments
#         self.posts = []
#         self.comments = []

#         User.users[username] = self

#     @classmethod
#     # This function create user account
#     def create_user(cls, first_name, last_name, username, password, email, role):
#         if username in cls.users:
#             print("Username already exists. Please choose a different username.")
#             return None
#         user_id = cls.next_user_id
#         cls.next_user_id += 1
#         user = cls(user_id, first_name, last_name, username, password, email, role)
#         return user

#     # This function allows user for logging in
#     def login(self, entered_password):
#         if self.password == entered_password:
#             if self.is_logged_in:
#                 print(f"You are already logged in.")
#             else:
#                 self.is_logged_in = True
#                 print(f"Welcome, {self.first_name} {self.last_name} ({self.role})!")
#         else:
#             print("Incorrect password. Please try again.")

#     # This function allows user to log out
#     def logout(self):
#         if self.is_logged_in:
#             self.is_logged_in = False
#             print(f"Goodbye, {self.first_name} {self.last_name}!")
#         else:
#             print(f"You are not currently logged in.")

#     def add_profile_data(self, key, value):
#         self.profile_data[key] = value

#     def create_post(self, post_title, post_content):
#         from post import Post

#         post = Post(len(self.posts) + 1, self, post_title, post_content)
#         self.posts.append(post)
#         return post

#     def create_comment(self, post, comment_content):
#         from post import Comment
#         comment = Comment(len(self.comments) + 1, self, post, comment_content)
#         post.comments.append(comment)
#         self.comments.append(comment)
#         return comment


class User:
    def __init__(self, first_name, last_name, username, password, email, role=None):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.password = password
        self.email = email
        self.role = role