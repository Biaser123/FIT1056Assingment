from login import CodeVenture
from user import User

user1 = User("Hasbulla", "Magomedov", "lil_manz","RU551@", "no1@gmail.com", is_active=True)

user_1_login = CodeVenture()

assert user_1_login.create_user("Hasbulla", "Magomedov", "lil_manz","RU551@", "no1@gmail.com", "Student") == (1, "Hasbulla", "Magomedov", "lil_manz","RU551@", "no1@gmail.com", "Student") 

user_1_login.is_logged_in = False

assert user_1_login.login("RU551@") == "Welcome, Hasbulla Magomedov (Student)!"
assert user_1_login.login("RU551@") == "You are already logged in."
assert user_1_login.logout() == "Goodbye, Hasbulla Magomedov!"

user_1_login.is_logged_in = False
assert user_1_login.login("hello world") == "Incorrect password. Please try again."
assert user_1_login.logout() == "You are not currently logged in."



