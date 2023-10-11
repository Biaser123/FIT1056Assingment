
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
