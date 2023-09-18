# from user import User
# from student import Student

class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

class File:
    def __init__(self, filename, content):
        self.filename = filename
        self.content = content

class CloudStorage():
    def __init__(self):
        self.users = []
        self.files = []

    def create_user(self, username, email):
        user = User(username, email)
        self.users.append(user)
        return user

    def upload_file(self, user, filename, content):
        file = File(filename, content)
        self.files.append(file)
        print(f"File '{filename}' uploaded to the cloud storage for '{user.username}'.")

    def list_files(self, user):
        user_files = [file for file in self.files if user.username == file.filename]
        return user_files




if __name__ == "__main__":
    cloud_storage = CloudStorage()
    user1 = cloud_storage.create_user("Alice", "alice@example.com")
    user2 = cloud_storage.create_user("Bob", "bob@example.com")

    cloud_storage.upload_file(user1, "PythonBasics.py", "print('Hello, World!')")
    cloud_storage.upload_file(user2, "MyGame.py", "print('Welcome to My Game!')")

    user1_files = cloud_storage.list_files(user1)
    for file in user1_files:
        print(f"File '{file.filename}' contents: {file.content}")