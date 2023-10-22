from DataStorage import Student, ProgressTracker, Quiz


def test_DataStorage():
    progress_tracker = ProgressTracker()

    student1 = Student(1, "Alice", 12)
    student2 = Student(2, "Bob", 11)

    quiz1 = Quiz(101, "Python Basics")
    quiz2 = Quiz(102, "Variables and Data Types")

    progress_tracker.add_student(student1)
    progress_tracker.add_student(student2)

    assert progress_tracker.students == {1:student1, 2:student2}
                                         
    progress_tracker.add_quiz(quiz1)
    progress_tracker.add_quiz(quiz2)

    assert progress_tracker.quizzes == {101:quiz1, 102:quiz2}

    student1.take_quiz(quiz1, 85)
    student1.take_quiz(quiz2, 92)

    student2.take_quiz(quiz1, 78)
    student2.take_quiz(quiz2, 88)

    assert print(student1) == "Student ID: 1, Name: Alice, Age: 12, Progress: 88.5%"