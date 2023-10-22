from Notifications import NotificationSystem

notification = NotificationSystem()

alert = notification.notification_alert()

message = alert.split(":")[1:]

assert message in notification.notifications 
