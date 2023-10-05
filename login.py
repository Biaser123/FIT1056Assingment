from user import User


class CodeVenture(User):
    def __init__(self):
        self.users = {}
        self.next_user_id = 1

    def create_user(cls, first_name, last_name, username, password, email, role):
        if username in cls.users:
            print("Username already exists. Please choose a different username.")
            return None
        user_id = cls.next_user_id
        cls.next_user_id += 1
        user = cls(user_id, first_name, last_name, username, password, email, role)
        return user

    # This function allows user for logging in
    def login(self, entered_password):
        if self.password == entered_password:
            if self.is_logged_in:
                print(f"You are already logged in.")
            else:
                self.is_logged_in = True
                print(f"Welcome, {self.first_name} {self.last_name} ({self.role})!")
        else:
            print("Incorrect password. Please try again.")

    # This function allows user to log out
    def logout(self):
        if self.is_logged_in:
            self.is_logged_in = False
            print(f"Goodbye, {self.first_name} {self.last_name}!")
        else:
            print(f"You are not currently logged in.")
