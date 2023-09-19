import time

class SupportTeam:
    def __init__(self):
        self.requests = []

    def request_recieved(self, username, question):
        print(f"The CodeVenture Support Team has received your support request: '{question}' ")
        self.requests.append((username, question))

    def request_respond(self):
        while self.requests:
            username, _ = self.requests.pop(0)
            print(f"The Support Team is currently is responding your request...")
            time.sleep(3)
            print(f"You have recieved a message regarding your support request.")

class User:
    def __init__(self, username):
        self.username = username

    def support_line(self, support):
        print("Would you like to connect to the Code Venture Support Team? (y/n)")
        answer = input()
        if answer.lower() == "y":
            print("Connecting to real-time chat, please wait...")
            time.sleep(2)
            print("You are now connected to the Dan from the Support Team.")
            question = input("\nPlease submit your support request: ")
            support.request_recieved(self.username, question)
            print("Support request sent. Pending response...")
            time.sleep(3)
        elif answer.lower() != "y":
            print("Disconnecting from Support Line...")

if __name__ == "__main__":
    support = SupportTeam()
    user = User("WolfgangMozart")

    #user support request
    user.support_line(support)

    #support team response
    support.request_respond()