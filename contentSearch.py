def content_search(quizzes):
    '''
    Prints out a list of modules available that are related
    to the content type inputted by user

    Inputs
    modules: a list of all instances of class Module
    '''
    # ask user which topic they need
    content_type = input("What kind of content are you looking for?")

    # creates a string, with header, to add relevant modules onto to be printed
    results = f"--- Modules related to {content_type} ---"

    # searches through available modules and if topic of module matches, adds to string
    for quiz in quizzes:
        # create a count to keep track of number of modules for the topic in order
        # to display stats in string
        count = 0
        if quiz.topic == content_type:
            count += 1
            results += f"\n{count}. f{quiz.name}"
            
    # ends string by giving user a look at how many modules match their search
    results += f"\n--- {count}/{len(quizzes)} modules matched search ---"
            
    