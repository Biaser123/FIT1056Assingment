import time
import random


class NotificationSystem:
    def __init__(self):
        self.notifications = [
            "You have received a message from your teacher",
            "Your assignment is due in 10 minutes",
            "There are 3 unread messages in your inbox",
            "You have been idle for 2 minutes, the system will shut down if there is no response",
            "Reminder notice: coding class starts in 30 minutes"
        ]

    def notification_alert(self):
        notification = random.choice(self.notifications)
        print(f"Notification: {notification}")

    def run(self):
        while True:
            self.notification_alert()
            time.sleep(2)


if __name__ == "__main__":
    notification_system = NotificationSystem()
    notification_system.run()
