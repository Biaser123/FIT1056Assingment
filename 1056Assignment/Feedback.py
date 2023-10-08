from datetime import datetime

from main import user1


class Feedback:
    def __init__(self, user, message):
        self.user = user
        self.message = message
        self.timestamp = datetime.now()


# Testing
# user_feedback = Feedback(user1, "The website is great! I love it!")
#
#
# print(f"User: {user_feedback.user.username}")
# print(f"Timestamp: {user_feedback.timestamp}")
# print(f"Feedback: {user_feedback.message}")
