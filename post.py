# 创建一个帖子类
from datetime import datetime

from main import user1


class Post:
    def __init__(self, author, title, content):
        self.author = author
        self.title = title
        self.content = content
        self.comments = []

    def add_comment(self, comments):
        self.comments.append(comments)


# 创建一个评论类
class Comment:
    def __init__(self, user, text):
        self.user = user
        self.text = text
        self.timestamp = datetime.now()


# create post
post1 = Post(user1, "Introduction", "Welcome to the discussion forum!")

# add comment to the post
comment1 = Comment(user1, "Great forum!")
comment2 = Comment(user1, "I have a question.")
post1.add_comment(comment1)
post1.add_comment(comment2)

# test
print(f"Author: {post1.author.username}")
print(f"Title: {post1.title}")
print(f"Content: {post1.content}")
print("Comments:")
for comment in post1.comments:
    print(f"- User: {comment.user.username}")
    print(f"  Comment: {comment.text}")
    print(f"  Timestamp: {comment.timestamp}")
