from user import User

class Teacher(User):
    def __init__(self, user_id, first_name, last_name, username, password, email,role):
        super().__init__(user_id, first_name, last_name, username, password,email, role)