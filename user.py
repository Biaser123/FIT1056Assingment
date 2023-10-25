from post import Post, Comment


class User:
    next_post_id = 1
    next_comment_id = 1

    def __init__(self, first_name, last_name, username, password, email, role=None, is_active=True):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.password = password
        self.email = email
        self.role = role
        self.posts = []  # Initialize the user's posts list
        self.comments = []  # Initialize the user's comments list
        self.is_active = is_active

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def get_username(self):
        return self.username

    def get_password(self):
        return self.password

    def get_email(self):
        return self.email

    def get_role(self):
        return self.role

    def get_is_active(self):
        return self.is_active

    def create_post(self, post_title, post_content, username=None, post_id=None):
        post = Post(self, post_title, post_content)
        self.posts.append(post)
        return post

    def create_comment(self, post, comment_content, username=None, comment_id = None):
        comment = Comment(self, post, comment_content)
        post.comments.append(comment)
        self.comments.append(comment)
        return comment

    # def get_date_of_birth(self):
    #     return self.date_of_birth


if __name__ == "__main__":
    pass

    # user1 = User('Dat','Le', 'Eddie',"12345",'dakvjnwv', 'Sutdent')
    # print(user1.get_first_name())
