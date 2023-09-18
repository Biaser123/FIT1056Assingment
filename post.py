
from datetime import datetime
from user import User


class Post:
    posts = {}
    next_post_id = 1

    def __init__(self, post_id, user, title, content):
        self.post_id = post_id
        self.user = user
        self.title = title
        self.content = content
        self.comments = []

        Post.posts[post_id] = self


class Comment:
    comments = {}
    next_comment_id = 1

    def __init__(self, comment_id, user, post, content):
        self.comment_id = comment_id
        self.user = user
        self.post = post
        self.content = content

        Comment.comments[comment_id] = self


user_test = User(1, "Alice", "Doe", "alice_user", "password123", "alice@example.com", "Student")

# create post
post1 = user_test.create_post("Introduction", "Welcome to the discussion forum!")

# add comment to post
comment1 = user_test.create_comment(post1, "Great forum!")
comment2 = user_test.create_comment(post1, "I have a question!")

# test
print(f"Author: {post1.user.username}")
print(f"Title: {post1.title}")
print(f"Content: {post1.content}")
print("Comments:")
for comment in post1.comments:
    print(f"- User: {comment.user.username}")
    print(f"  Comment: {comment.content}")

