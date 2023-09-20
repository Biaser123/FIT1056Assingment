def progress_tracker(modules, quizzes):
    '''
    Displays users overall progress in-game. It uses both the number of quizzes and
    modules the user has completed. 

    Inputs
    modules: a list of all instances of the class Module
    quizzes: a list of all instances of the class Quiz
    '''
    # intitalise counts to zero
    module_count = 0
    quiz_count = 0 

    # check which modules user has completed, and add to the count
    for module in modules:
        if module.status == "complete":
            module_count += 1
    
    # check which quizzes user has completed, and add to the count
    for quiz in quizzes:
        if quiz.status == "complete":
            quiz_count += 1
    
    # computes the percentage of total quizzes and modules the user has completed
    completion_status = ((module_count + quiz_count) / (len(modules) + len(quizzes))) * 100
    
    # if user has finished everything, displays congratulatory message instead of stats
    if completion_status == 100:
        congratulations = "Well Done! You have completed all content."
        return congratulations
    
    # prints progress stats of user 
    progress = (f"--- Progress Report ---\nModules: ({module_count}/{len(modules)}) complete"
                f"\nQuizzes: ({quiz_count}/{len(quizzes)} complete\nIn total, you have completed"
                f" {completion_status}% of the game.")
               
    print(progress)
    
