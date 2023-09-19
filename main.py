# from login import CodeVenture
# from teacher import Teacher
# from student import Student
# from Admin import Admin
# from user import User

# codeventure = CodeVenture()
# # Usage


# # User registration
# teacher1 = Teacher.create_user("John", "Smith", "MrSmith", "teacherpass", "mrsmith@example.com", "Teacher")
# teacher2 = codeventure.create_user("Alice", "Johnson", "MsJohnson", "secureteacherpass", "msjohnson@example.com", "Teacher")
# student1 = codeventure.create_user("Bob", "Doe", "Alice", "password123", "alice@example.com", "Student")
# student2 = codeventure.create_user("Eve", "Smith", "Bob", "securepass", "bob@example.com", "Student")
# admin = codeventure.create_user("Admin", "User", "AdminUser", "adminpass", "admin@example.com", "Admin")

# # User login
# logged_in_teacher = codeventure.login("MrSmith", "teacherpass")
# logged_in_student = codeventure.login("Alice", "password123")
# logged_in_admin = codeventure.login("AdminUser", "adminpass")

# if logged_in_teacher:
#     # Perform actions for the logged-in teacher here

#     # Logout
#     codeventure.logout(logged_in_teacher)

# if logged_in_student:
#     # Perform actions for the logged-in student here

#     # Logout
#     codeventure.logout(logged_in_student)

# if logged_in_admin:
#     # Perform actions for the logged-in admin here

#     # Logout
#     codeventure.logout(logged_in_admin)


from teacher import Teacher
from student import Student
from Admin import Admin
from user import User
from teacher import Teacher
from student import Student
from Admin import Admin
from backup import CloudStorage


# def main():
#     while True:
#         print("\nWelcome to CodeVenture:")
#         print("1. Register")
#         print("2. Login")
#         print("3. Logout")
#         print("4. Exit")

#         choice = input("Select an option (1/2/3/4): ")

#         if choice == "1":
#             register()
#         elif choice == "2":
#             login()

#         elif choice == "3":
#             logout()
#         elif choice == "4":
#             print("Goodbye!")
#             break
#         else:
#             print("Invalid option. Please choose a valid option.")

# def register():
#     print("\nRegistration:")
#     role = input("Enter your role (Teacher/Student/Admin): ").capitalize()
#     first_name = input("Enter First Name: ")
#     last_name = input("Enter Last Name: ")
#     username = input("Enter Username: ")
#     password = input("Enter Password: ")
#     email = input("Enter Email: ")

#     if role == "Teacher":
#         user = Teacher.create_user(first_name, last_name, username, password, email, "Teacher")
#     elif role == "Student":
#         user = Student.create_user(first_name, last_name, username, password, email, "Student")
#     elif role == "Admin":
#         user = Admin.create_user(first_name, last_name, username, password, email, "Admin")
#     else:
#         print("Invalid role. Please choose Teacher, Student, or Admin.")
#         return

#     if user:
#         print(f"{role} registration successful!")

# def login():
#     username = input("Enter Username: ")
#     password = input("Enter Password: ")

#     if username in User.users:
#         user = User.users[username]
#         user.login(password)
#     else:
#         print("User not found.")

# def logout():
#     username = input("Enter Username: ")

#     if username in User.users:
#         user = User.users[username]
#         user.logout()
#     else:
#         print("User not found.")

# if __name__ == "__main__":
#     main()


# User registration
teacher1 = Teacher.create_user("John", "Smith", "MrSmith", "teacherpass", "mrsmith@example.com", "Teacher")
student1 = Student.create_user("Alice", "Doe", "Alice", "password123", "alice@example.com", "Student")
student2 = Student.create_user("Bob", "Farrell", "Bob", "pass5555", "bob@example.com", "Student")
print(student1.username)
# Attempt to log out when not logged in
teacher1.logout()  # Should print: "You are not currently logged in."
student1.logout()  # Should print: "You are not currently logged in."

# User login
teacher1.login("teacherpass")
student1.login("password123")

# Attempt to log out when logged in
teacher1.logout()  # Should print: "Goodbye, John Smith!"
student1.logout()  # Should print: "Goodbye, Bob Doe!"

# Cloud backup
# Create list that requires for data back
cloud_storage = CloudStorage()
user1 = cloud_storage.create_user("Alice", "alice@example.com")
user2 = cloud_storage.create_user("Bob", "bob@example.com")

cloud_storage.upload_file(user1, "PythonBasics.py", "print('Hello, World!')")
cloud_storage.upload_file(user2, "MyGame.py", "print('Welcome to My Game!')")

user1_files = cloud_storage.list_files(user1)
for file in user1_files:
    print(f"File '{file.filename}' contents: {file.content}")



