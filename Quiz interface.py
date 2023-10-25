class Question:
    def __init__(self, question, options, answer):
        self.question = question
        self.options = options
        self.answer = answer

    def check_answer(self, user_answer):
        return user_answer == self.answer

class Quiz:

    quizzes = []

    def __init__(self, topic):
        self.questionList = []
        self.question_index = 0
        self.results = 0
        self.startup = 0
        self.topic = topic
        self.status = "incomplete"

        self.quizzes.append(self)


    def add_question(self, question):
        self.questionList.append(question)

    def get_current_question(self):
        if 0 <= self.question_index < len(self.questionList):
            return self.questionList[self.question_index]
        else:
            return None

    def next_question(self):
        self.question_index += 1

    def is_quiz_finished(self):
        return self.question_index >= len(self.questionList)

    def update_quiz_status(self):
        if self.is_quiz_finished():
            self.status = 'complete'
            return self.status


    def start_quiz(self):
        if self.startup != 0:
            while not self.is_quiz_finished():
                current_question = self.get_current_question()
                if current_question:
                    print(current_question.question)
                    for i, option in enumerate(current_question.options):
                        print(f"{i + 1}. {option}")
                    
                    user_answer = input("Enter answer option: ")
                    if user_answer.isdigit():
                        user_answer = int(user_answer) - 1
                        if 0 <= user_answer < len(current_question.options):
                            if current_question.check_answer(user_answer):
                                print("\nCorrect!\n")
                                self.results += 1
                            else:
                                print("\nIncorrect!\n")
                        else:
                            print("Invalid input. Please enter a valid option.\n")
                            continue
                    else:
                        print("Invalid input. Please enter a number.\n")
                        continue

                    self.next_question()

            print(f"You have completed the quiz. \nYour results are: {self.results}/{len(self.questionList)}")

        while True:
            if self.startup == 0:
                entry = input("Do you want to start the Quiz? (y or n): ")
                self.startup +=1
            elif self.startup !=0:
                entry = input("\nWould you like to retry? (y or n): ")

            if entry == "y":
                user_answer = ""
                self.questionList = []
                self.question_index = 0
                self.results = 0

            #ADD QUESTIONS HERE!!!!!!!!!!!!
                q1 = Question("What is 2 + 2?", ["3", "4", "5"], 1)
                q2 = Question("What state are we in?", ["Brisbane", "Sydeny", "Victoria"], 2)
                quiz.add_question(q1)
                quiz.add_question(q2)
            ################################

                quiz.start_quiz()
                break
            elif entry == "n":
                print("Quitting Quiz...")
                break
            elif entry != "y" or entry != "n":
                print("Please input y or n")
                entry = ""
                continue

quiz = Quiz()
quiz.start_quiz()