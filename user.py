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


class User:
    users = {}
    next_user_id = 1

    def __init__(self, username, password, role=None, is_active=True):
        """
        Constructor for the User class
        :param username: str
        :param password: str
        :param role: str
        :param is_active: bool
        """
        self.__username = username
        self.__password = password
        self.__role = role
        self.__is_active = is_active

    def get_username(self):
        """
        Getter for the username attribute.
        :return: str
        """
        return self.__username

    def get_password(self):
        """
        Getter for the password attribute.
        :return: str
        """
        return self.__password

    def get_role(self):
        """
        Getter for the role attribute.
        :return: str
        """
        return self.__role

    def get_is_active(self):
        """
        Getter for the is_active attribute.
        :return: bool
        """
        return self.__is_active
    # def __init__(self, user_id, first_name, last_name, username, password, email, role):
    #     self.user_id = user_id
    #     self.first_name = first_name
    #     self.last_name = last_name
    #     self.username = username
    #     self.password = password
    #     self.email = email
    #     self.role = role
    #     self.is_logged_in = False
    #     # profile data (Wei Lu)
    #     self.profile_data = {}
    #     # post and comments
    #     self.posts = []
    #     self.comments = []
    #
    #     User.users[username] = self

    # @classmethod
    # # This function create user account
    # def create_user(cls, first_name, last_name, username, password, email, role):
    #     if username in cls.users:
    #         print("Username already exists. Please choose a different username.")
    #         return None
    #     user_id = cls.next_user_id
    #     cls.next_user_id += 1
    #     user = cls(user_id, first_name, last_name, username, password, email, role)
    #     return user

    # This function allows user for logging in
    # def login(self, entered_password):
    #     if self.password == entered_password:
    #         if self.is_logged_in:
    #             print(f"You are already logged in.")
    #         else:
    #             self.is_logged_in = True
    #             print(f"Welcome, {self.first_name} {self.last_name} ({self.role})!")
    #     else:
    #         print("Incorrect password. Please try again.")
    #
    # # This function allows user to log out
    # def logout(self):
    #     if self.is_logged_in:
    #         self.is_logged_in = False
    #         print(f"Goodbye, {self.first_name} {self.last_name}!")
    #     else:
    #         print(f"You are not currently logged in.")

    # def add_profile_data(self, key, value):
    #     self.profile_data[key] = value
    #
    # def create_post(self, post_title, post_content):
    #     from post import Post
    #
    #     post = Post(self, post_title, post_content)
    #     self.posts.append(post)
    #     return post
    #
    # def create_comment(self, post, comment_content):
    #     from post import Comment
    #     comment = Comment(self, post, comment_content)
    #     post.comments.append(comment)
    #     self.comments.append(comment)
    #     return comment
