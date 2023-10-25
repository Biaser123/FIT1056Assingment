import datetime
import json



class Student:
    def __init__(self, student_id, name, age):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.quiz_attempts = {}  # A dictionary to store quiz attempts by quiz name
        self.progress = 0  # Progress represented as a percentage

    def take_quiz(self, quiz, score):
        timestamp = datetime.datetime.now().isoformat()
        if quiz.name not in self.quiz_attempts:
            self.quiz_attempts[quiz.name] = []
        self.quiz_attempts[quiz.name].append({"timestamp": timestamp, "score": score})
        self.update_progress()

    def update_progress(self):
        total_score = 0
        total_possible_score = 0

        for quiz_name, attempts in self.quiz_attempts.items():
            for attempt in attempts:
                total_score += attempt["score"]
                total_possible_score += 100  # Assuming each quiz is out of 100

        if total_possible_score > 0:
            self.progress = (total_score / total_possible_score) * 100

    def __str__(self):
        return f"Student ID: {self.student_id}, Name: {self.name}, Age: {self.age}, Progress: {self.progress:.2f}%"


class Quiz:
    def __init__(self, quiz_id, name):
        self.quiz_id = quiz_id
        self.name = name

    def __str__(self):
        return f"Quiz ID: {self.quiz_id}, Quiz Name: {self.name}"


class ProgressTracker:
    def __init__(self):
        self.students = {}
        self.quizzes = {}

    def add_student(self, student):
        self.students[student.student_id] = student

    def add_quiz(self, quiz):
        self.quizzes[quiz.quiz_id] = quiz

    def get_student_by_id(self, student_id):
        return self.students.get(student_id)

    def get_quiz_by_id(self, quiz_id):
        return self.quizzes.get(quiz_id)

    def backup_data_to_file(self):
        backup_data = {
            "students": [student.__dict__ for student in self.students.values()],
            "quizzes": [quiz.__dict__ for quiz in self.quizzes.values()],
        }
        with open("backup.json", "w") as backup_file:
            json.dump(backup_data, backup_file)
        print("Data backed up to a file.")

    def restore_data_from_file(self):
        try:
            with open("backup.json", "r") as backup_file:
                backup_data = json.load(backup_file)

            for student_data in backup_data["students"]:
                student = Student(student_data["student_id"], student_data["name"], student_data["age"])
                student.quiz_attempts = student_data["quiz_attempts"]
                student.progress = student_data["progress"]
                self.add_student(student)

            for quiz_data in backup_data["quizzes"]:
                quiz = Quiz(quiz_data["quiz_id"], quiz_data["name"])
                self.add_quiz(quiz)

            print("Data restored from a file.")
        except FileNotFoundError:
            print("No backup data file found.")
    
    def print_results(self):
        # check which quizzes user has completed, and add to the count
        for quiz in self.quizzes:
            if quiz.status == "complete":
                quiz_count += 1

        # computes the percentage of total quizzes and modules the user has completed
        completion_status = ((quiz_count) / (len(self.quizzes))) * 100
        
        # if user has finished everything, displays congratulatory message instead of stats
        if completion_status == 100:
            congratulations = "Well Done! You have completed all content."
            return congratulations
        
        # prints progress stats of user 
        progress = (f"--- Progress Report ---"
                    f"\nQuizzes: ({quiz_count}/{len(quizzes)} complete\nIn total, you have completed"
                    f" {completion_status}% of the game.")
                
        print(progress)
        



if __name__ == "__main__":
    # Example usage:
    progress_tracker = ProgressTracker()

    student1 = Student(1, "Alice", 12)
    student2 = Student(2, "Bob", 11)

    quiz1 = Quiz(101, "Python Basics")
    quiz2 = Quiz(102, "Variables and Data Types")

    progress_tracker.add_student(student1)
    progress_tracker.add_student(student2)
    progress_tracker.add_quiz(quiz1)
    progress_tracker.add_quiz(quiz2)

    student1.take_quiz(quiz1, 85)
    student1.take_quiz(quiz2, 92)

    student2.take_quiz(quiz1, 78)
    student2.take_quiz(quiz2, 88)

    print(quiz1)
    print(student1)
    print(student2)

    # Backup and restore data to/from a file
    progress_tracker.backup_data_to_file()
    progress_tracker.restore_data_from_file()
