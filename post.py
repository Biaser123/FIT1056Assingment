
from datetime import datetime
from user import User


class Post:
    posts = {}
    next_post_id = 1

    def __init__(self, user, title, content):
        self.post_id = Post.next_post_id
        Post.next_post_id += 1
        self.user = user
        self.title = title
        self.content = content
        self.comments = []
        Post.posts[self.post_id] = self

    @staticmethod
    def get_all_posts():
        return list(Post.posts.values())

    def get_comments(self):
        return self.comments

    @staticmethod
    def delete_post(post_id):
        if post_id in Post.posts:
            del Post.posts[post_id]


class Comment:
    comments = {}
    next_comment_id = 1

    def __init__(self, user, post, content):
        self.comment_id = Comment.next_comment_id
        Comment.next_comment_id += 1
        self.user = user
        self.post = post
        self.content = content
        Comment.comments[self.comment_id] = self

    @staticmethod
    def get_comments_for_post(post):
        comments = [comment_get for comment_get in Comment.comments.values() if comment_get.post == post]
        return comments


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

