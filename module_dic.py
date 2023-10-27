module = [{'heading': "Module 1: Introduction to Python",
           "content": """Welcome to CodeVenture! In this module, we will start to get familiar with Python programming language by covering
            basic information about Python.

            Let's get statrted!

            1. What is Python?
            Python is a popular programming language. It was created by Guido van Rossum, and released in 1991.

            It is used for:

                web development (server-side),
                software development,
                mathematics,
                system scripting.

            2. What can Python do?
                Python can be used on a server to create web applications.
                Python can be used alongside software to create workflows.
                Python can connect to database systems. It can also read and modify files.
                Python can be used to handle big data and perform complex mathematics.
                Python can be used for rapid prototyping, or for production-ready software development.

            3. Why Python?
                Python works on different platforms (Windows, Mac, Linux, Raspberry Pi, etc).
                Python has a simple syntax similar to the English language.
                Python has syntax that allows developers to write programs with fewer lines than some other programming languages.
                Python runs on an interpreter system, meaning that code can be executed as soon as it is written. This means that prototyping can be very quick.
                Python can be treated in a procedural way, an object-oriented way or a functional way.

            4. Good to know
                The most recent major version of Python is Python 3, which we shall be using in this tutorial. However, Python 2, although not being updated with anything other than security updates, is still quite popular.
                In this tutorial Python will be written in a text editor. It is possible to write Python in an Integrated Development Environment, such as Thonny, Pycharm, Netbeans or Eclipse which are particularly useful when managing larger collections of Python files.
                Python Syntax compared to other programming languages
                Python was designed for readability, and has some similarities to the English language with influence from mathematics.
                Python uses new lines to complete a command, as opposed to other programming languages which often use semicolons or parentheses.
                Python relies on indentation, using whitespace, to define scope; such as the scope of loops, functions and classes. Other programming languages often use curly-brackets for this purpose.


            5. Example: 
                Instruction to install Python:
                If you find that you do not have Python installed on your computer, then you can download it for free from the following website: https://www.python.org/.

                After installation complete, open Python file and try this line of code:
                print("Hello, World!")
            """},

          {"heading": 'Module 2 :Get to know Python syntax and variables',
           "content": """ Let's get started!
            1. Execute Python Syntax
                As we learned in the previous page, Python syntax can be executed by writing directly in the Command Line:
                >>>print("Hello, World!")
                Hello, World!

                Or by creating a python file on the server, using the .py file extension, and running it in the Command Line:
                

            2. Python Indentation:
                Indentation refers to the spaces at the beginning of a code line.

                Where in other programming languages the indentation in code is for readability only, the indentation in Python is very important.

                Python uses indentation to indicate a block of code.

                Example:

                if 5 > 2:
                    print("Five is greater than two!")

                Python will give you an error if you skip the indentation:

                if 5 > 2:
                print("Five is greater than two!")

            3. Python Variables:
                In Python, variables are created when you assign a value to it:

                Example:
                x = 5
                y = "Hello, World!"
            
            4. Comments:
                Python has commenting capability for the purpose of in-code documentation.

                Comments start with a #, and Python will render the rest of the line as a comment:

                Example:

                #This is a comment.
                print("Hello, World!")
                """},

          {"heading": "Module 3: Python Data Types",
           "content": """
            1. Built-in Data Types:
            In programming, data type is an important concept.

            Variables can store data of different types, and different types can do different things.

            Python has the following data types built-in by default, in these categories:

            Text Type:	str
            Numeric Types:	int, float, complex
            Sequence Types:	list, tuple, range
            Mapping Type:	dict
            Set Types:	set, frozenset
            Boolean Type:	bool
            Binary Types:	bytes, bytearray, memoryview
            None Type:	NoneType

            2. Getting Data Types:
                You can get the data type of any object by using the type() function:

                Example:
                Print the data type of the variable x:

                x = 5
                print(type(x))

            3.Setting Data Types:

            Example	                                            Data Type	
            x = "Hello World"	                                   str	
            x = 20	                                               int	
            x = 20.5	                                          float	
            x = 1j	                                              complex	
            x = ["apple", "banana", "cherry"]	                   list	
            x = ("apple", "banana", "cherry")	                   tuple	
            x = range(6)	                                       range	
            x = {"name" : "John", "age" : 36}	                    dict	
            x = {"apple", "banana", "cherry"}	                    set	
            x = frozenset({"apple", "banana", "cherry"})	      frozenset	
            x = True	                                            bool	
            x = b"Hello"	                                        bytes	
            x = bytearray(5)	                                   bytearray	
            x = memoryview(bytes(5))	                           memoryview	
            x = None	                                            NoneType


            4. Setting Specific Data Type:

            If you want to specify the data type, you can use the following constructor functions:

            Example	Data                                        Type	
            x = str("Hello World")	                            str	
            x = int(20)	                                        int	
            x = float(20.5)	                                   float	
            x = complex(1j)	                                   complex	
            x = list(("apple", "banana", "cherry"))	            list	
            x = tuple(("apple", "banana", "cherry"))	        tuple	
            x = range(6)	                                    range	
            x = dict(name="John", age=36)	                    dict	
            x = set(("apple", "banana", "cherry"))	            set	
            x = frozenset(("apple", "banana", "cherry"))	   frozenset	
            x = bool(5)	                                         bool	
            x = bytes(5)	                                    bytes	
            x = bytearray(5)	                                bytearray	
            x = memoryview(bytes(5))	                        memoryview	

            5. Python Numbers:

            There are three numeric types in Python:

                - int
                - float
                - complex

                Variables of numeric types are created when you assign a value to them:

                Example:
                x = 1    # int  Int Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length.
                y = 2.8  # float  Float, or "floating point number" is a number, positive or negative, containing one or more decimals.
                z = 1j   # complex  Complex numbers are written with a "j" as the imaginary part

            6. Type Conversion:
                Example:

                Convert from one type to another:

                x = 1    # int
                y = 2.8  # float
                z = 1j   # complex

                #convert from int to float:
                a = float(x)

                #convert from float to int:
                b = int(y)

                #convert from int to complex:
                c = complex(x)

                print(a)
                print(b)
                print(c)

                print(type(a))
                print(type(b))
                print(type(c))
            7. Choosing the Right Variable Name
                Programmers generally choose names for their variables that are meaningful to the human readers of the program — they help the programmer document, or remember, what the variable is used for. Beginning programmers sometimes think it is funny to use strange or obscene names for their variables. This is not good practice and will not amuse your professor. Get in the habit of using meaningful names right away.

                Caution:
                Beginners sometimes confuse “meaningful to the human readers” with “meaningful to the computer”. So they'll wrongly think that because they've called some variable average or pi, it will somehow automagically calculate an average, or automagically associate the variable pi with the value 3.14159. No! The computer doesn't attach semantic meaning to your variable names.

                So you'll find some instructors who deliberately don't choose meaningful names when they teach beginners — not because they don't think it is a good habit, but because they're trying to reinforce the message that you, the programmer, have to write some program code to calculate the average, or you must write an assignment statement to give a variable the value you want it to have.
            8. Statements and Expressions
                A statement is an instruction that the Python interpreter can execute. You have only seen the assignment statement so far. Some other kinds of statements that you'll see in future chapters are while statements, for statements, if statements, and import statements. (There are other kinds too!)

                An expression is a combination of literals, variable names, operators, and calls to functions. Expressions need to be evaluated. The result of evaluating an expression is a value or object.       
            9. Operators and Operands
                You can build complex expressions out of simpler ones using operators. Operators are special tokens that represent computations like addition, multiplication and division. The values the operator works on are called operands.

                The following are all legal Python expressions whose meaning is more or less clear:

                20 + 32
                5 ** 2
                (5 + 9) * (15 - 7)

                The tokens +, -, and *, and the use of parentheses for grouping, mean in Python what they mean in mathematics. The asterisk (*) is the token for multiplication, and ** is the token for exponentiation. Addition, subtraction, multiplication, and exponentiation all do what you expect.

                Remember that if we want to see the results of the computation, the program needs to specify that with the word print. The first three computations occur, but their results are not printed out.
                In Python 3, which we will be using, the division operator / produces a floating point result (even if the result is an integer; 4/2 is 2.0). If you want truncated division, which ignores the remainder, you can use the // operator (for example, 5//2 is 2).


                print(9 / 5)
                print(5 / 9)
                print(9 // 5)
                Pay particular attention to the examples above. Note that 9//5 truncates rather than rounding, so it produces the value 1 rather than 2.

                The truncated division operator, //, also works on floating point numbers. It truncates to the nearest integer, but still produces a floating point result. Thus 7.0 // 3.0 is 2.0.


                print(7.0 / 3.0)
                print(7.0 // 3.0)
                The modulus operator, sometimes also called the remainder operator or integer remainder operator works on integers (and integer expressions) and yields the remainder when the first operand is divided by the second. In Python, the modulus operator is a percent sign (%). The syntax is the same as for other operators.

                print(7 // 3)    # This is the integer division operator
                print(7 % 3)     # This is the remainder or modulus operator
                In the above example, 7 divided by 3 is 2 when we use integer division and there is a remainder of 1.

                The modulus operator turns out to be surprisingly useful. For example, you can check whether one number is divisible by another—if x % y is zero, then x is divisible by y. Also, you can extract the right-most digit or digits from a number. For example, x % 10 yields the right-most digit of x (in base 10). Similarly x % 100 yields the last two digits.
            """},
          {'heading': "Module 4: String,List, Dictionary, and Conditionals",
           'content': """
             1. Introduction to Conditionals
                So far, our programs have been a series of statements. Yet programs frequently need to be more subtle with their behavior. For example, a messaging app might only set a message’s title bold if it has not been read by the user. Or a video game needs to update the position of all the characters that are not asleep. This is done with something called a selection or a conditional statement.
                By the end of this section you should be able to:

                - properly evaluate a (compound) boolean expression

                - use parenthesis to properly demonstrate operator precedence

                - use conditional statements to properly branch code

            2. Boolean Values and Boolean Expressions
                The Python type for storing true and false values is called bool, named after the British mathematician, George Boole. George Boole created Boolean Algebra, which is the basis of all modern computer arithmetic.

                There are only two boolean values. They are True and False. Capitalization is important, since true and false are not boolean values (remember Python is case sensitive).

                Example: do this on your console
                    print(True)
                    print(type(True))
                    print(type(False))
                Note:
                Booleans are not strings!
                It is extremely important to realize that True and False are not strings. They are not surrounded by quotes. They are the only two values in the data type bool. Take a close look at the types shown below.

                Example:
                print(type(True))
                print(type("True"))
                A boolean expression is an expression that evaluates to a boolean value. The equality operator, ==, compares two values and produces a boolean value related to whether the two values are equal to one another.

                Example
                print(5 == 5)
                print(5 == 6)
                In the first statement, the two operands are equal, so the expression evaluates to True. In the second statement, 5 is not equal to 6, so we get False.

                The == operator is one of six common comparison operators; the others are:

                x != y               # x is not equal to y
                x > y                # x is greater than y
                x < y                # x is less than y
                x >= y               # x is greater than or equal to y
                x <= y               # x is less than or equal to y
                Although these operations are probably familiar to you, the Python symbols are different from the mathematical symbols. A common error is to use a single equal sign (=) instead of a double equal sign (==). Remember that = is an assignment operator and == is a comparison operator. Also, there is no such thing as =< or =>.

                Note: too that an equality test is symmetric, but assignment is not. For example, if a == 7 then 7 == a. But in Python, the statement a = 7 is legal and 7 = a is not. (Can you explain why?)
            3. Logical Operators
                There are three logical operators: and, or, and not. All three operators take boolean operands and produce boolean values. The semantics (meaning) of these operators is similar to their meaning in English:

                - x and y is True if both x and y are True. Otherwise, and produces False.

                - x or y yields True if x or y or both are True. Only if both operands are False does or yield False.

                - not x yields False if x is True, and vice versa.

                Look at the following example. See if you can predict the output. Then, Run to see if your predictions were correct:

                Example:
                x = True
                y = False
                print(x or y)
                print(x and y)
                print(not x)
                Although you can use boolean operators with simple boolean literals or variables as in the above example, they are often combined with the comparison operators, as in this example. Again, before you run this, see if you can predict the outcome:

                Example:
                x = 5
                print(x > 0 and x < 10)
                n = 25
                print(n % 2 == 0 or n % 3 == 0)
                The expression x > 0 and x < 10 is True only if x is greater than 0 and at the same time, x is less than 10. In other words, this expression is True if x is between 0 and 10, not including the endpoints.

                Common Mistake!
                There is a very common mistake that occurs when programmers try to write boolean expressions. For example, what if we have a variable number and we want to check to see if its value is 5 or 6. In words we might say: “number equal to 5 or 6”. However, if we translate this into Python, number == 5 or 6, it will not yield correct results. The or operator must have a complete equality check on both sides. The correct way to write this is number == 5 or number == 6. Remember that both operands of or must be booleans in order to yield proper results.

            4. Strings,Lists, Dictionaries:
                So far we have used strings to represent words or phrases that we wanted to print out. Our definition was simple: a string is simply some characters inside quotes. However, there are other storage types that exist to allow us to make groupings of things e.g. lists.
                Strings can be defined as sequential collections of characters. This means that the individual characters that make up a string are in a particular order from left to right.
                A string that contains no characters, often referred to as the empty string, is still considered to be a string. It is simply a sequence of zero characters and is represented by ‘’ or “” (two single or two double quotes with nothing in between).
                A list is a sequential collection of Python data values, where each value is identified by an index. The values that make up a list are called its elements. Lists are similar to strings, which are ordered collections of characters, except that the elements of a list can have any type and for any one list, the items can be of different types.

                There are several ways to create a new list. The simplest is to enclose the elements in square brackets ( [ and ]).

                [10, 20, 30, 40]
                ["spam", "bungee", "swallow"]
                The first example is a list of four integers. The second is a list of three strings. As we said above, the elements of a list don’t have to be the same type. The following list contains a string, a float, an integer, and another list.

                ["hello", 2.0, 5, [10, 20]]
                Note
                WP: Don't Mix Types!
                You'll likely see some of the examples in this course to give you odd combinations of data types within a list, but when you create lists you should generally not mix types together. A list of just strings, or just integers or just floats is generally easier to deal with.

                Access Items
                List items are indexed and you can access them by referring to the index number:

                ExampleGet your own Python Server
                Print the second item of the list:

                thislist = ["apple", "banana", "cherry"]
                print(thislist[1])

                To add an item to the end of the list, use the append() method:

                Example
                Get your own Python Server
                Using the append() method to append an item:

                thislist = ["apple", "banana", "cherry"]
                thislist.append("orange")
                print(thislist)

                The remove() method removes the specified item.

                Example
                Get your own Python Server
                Remove "banana":

                thislist = ["apple", "banana", "cherry"]
                thislist.remove("banana")
                print(thislist)

                Dictionaries are used to store data values in key:value pairs.

                A dictionary is a collection which is ordered*, changeable and do not allow duplicates.

                As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.

                Dictionaries are written with curly brackets, and have keys and values:

                Example:
                thisdict = {
                "brand": "Ford",
                "model": "Mustang",
                "year": 1964
                }
                print(thisdict)

                Dictionary Items:

                Dictionary items are ordered, changeable, and does not allow duplicates.

                Dictionary items are presented in key:value pairs, and can be referred to by using the key name.

                Example:
                Print the "brand" value of the dictionary:

                thisdict = {
                "brand": "Ford",
                "model": "Mustang",
                "year": 1964
                }
                print(thisdict["brand"])


                You can access the items of a dictionary by referring to its key name, inside square brackets:

                Example
                Get your own Python Server
                Get the value of the "model" key:

                thisdict = {
                "brand": "Ford",
                "model": "Mustang",
                "year": 1964
                }
                x = thisdict["model"]


                Adding an item to the dictionary is done by using a new index key and assigning a value to it:

                Example
                Get your own Python Server

                thisdict = {
                "brand": "Ford",
                "model": "Mustang",
                "year": 1964
                }
                thisdict["color"] = "red"
                print(thisdict)

                There are several methods to remove items from a dictionary:

                Example
                Get your own Python Server
                The pop() method removes the item with the specified key name:

                thisdict = {
                "brand": "Ford",
                "model": "Mustang",
                "year": 1964
                }
                thisdict.pop("model")
                print(thisdict)


            5. The 'in' and 'not in' operators
                The in operator tests if one string is a substring of another: (run these example in your console)

                Examples:
                print('p' in 'apple')
                print('i' in 'apple')
                print('ap' in 'apple')
                print('pa' in 'apple')
                Note that a string is a substring of itself, and the empty string is a substring of any other string. (Also note that computer scientists like to think about these edge cases quite carefully!)

                Examples:
                print('a' in 'a')
                print('apple' in 'apple')
                print('' in 'a')
                print('' in 'apple')
                The not in operator returns the logical opposite result of in.

                Examples:
                print('x' not in 'apple')
                We can also use the in and not in operators on lists!

                Examples:
                print("a" in ["a", "b", "c", "d"])
                print(9 in [3, 2, 9, 10, 9.0])
                print('wow' not in ['gee wiz', 'gosh golly', 'wow', 'amazing'])
                However, remember how you were able to check to see if an “a” was in “apple”? Let’s try that again to see if there’s an “a” somewhere in the following list.

                Example:
                print("a" in ["apple", "absolutely", "application", "nope"])
                Clearly, we can tell that a is in the word apple, and absolutely, and application. For some reason though, the Python interpreter returns False. Why is that? When we use the in and not in operators on lists, Python checks to see if the item on the left side of the expression is equivalent to an element in the item on the right side of the expression. In this case, Python is checking whether or not an element of the list is the string “a” - nothing more or less than that. 
                6. Conditional Execution
                    In order to write useful programs, we almost always need the ability to check conditions and change the behavior of the program accordingly. Selection statements, sometimes also referred to as conditional statements, give us this ability. The simplest form of selection is the if statement. This is sometimes referred to as binary selection since there are two possible paths of execution.

                    Examples:
                    x = 15

                    if x % 2 == 0:
                        print(x, "is even")
                    else:
                        print(x, "is odd")

                    The syntax for an if statement looks like this:

                    if BOOLEAN EXPRESSION:
                        STATEMENTS_1        # executed if condition evaluates to True
                    else:
                        STATEMENTS_2        # executed if condition evaluates to False

                    The boolean expression after the if statement is called the condition. If it is true, then the indented statements get executed. If not, then the statements indented under the else clause get executed.

                    The if statement consists of a header line and a body. The header line begins with the keyword if followed by a boolean expression and ends with a colon (:).

                    The indented statements that follow are called a block. The first unindented statement marks the end of the block.

                    Each of the statements inside the first block of statements is executed in order if the boolean expression evaluates to True. The entire first block of statements is skipped if the boolean expression evaluates to False, and instead all the statements under the else clause are executed.

                    There is no limit on the number of statements that can appear under the two clauses of an if statement, but there has to be at least one statement in each block.

                    Another form of the if statement is one in which the else clause is omitted entirely. This creates what is sometimes called unary selection. In this case, when the condition evaluates to True, the statements are executed. Otherwise the flow of execution continues to the statement after the body of the if.

                    Example:
                    x = 10
                    if x < 0:
                        print("The negative number ",  x, " is not valid here.")
                    print("This is always printed")
                    
                    One conditional can also be nested within another. For example, assume we have two integer variables, x and y. The following pattern of selection shows how we might decide how they are related to each other.

                    Example: (nested condition)

                    if x < y:
                        print("x is less than y")
                    else:
                        if x > y:
                            print("x is greater than y")
                        else:
                            print("x and y must be equal")

                    The outer conditional contains two branches. The second branch (the else from the outer) contains another if statement, which has two branches of its own. Those two branches could contain conditional statements as well.

                    Python provides an alternative way to write nested selection such as the one shown in the previous section. This is sometimes referred to as a chained conditional.
                    Example: (Chained Conditionals)
                    if x < y:
                        print("x is less than y")
                    elif x > y:
                        print("x is greater than y")
                    else:
                        print("x and y must be equal")
                        
                    elif is an abbreviation of else if. Again, exactly one branch will be executed. There is no limit of the number of elif statements but only a single (and optional) final else statement is allowed and it must be the last branch in the statement.
                    
                    Setting Up Conditionals:

                    Before writing your conditionals, it can be helpful to make your own flowchart that will plot out the flow of each condition. By writing out the flow, you can better determine how complex the set of conditionals will be as well as check to see if any condition is not taken care of before you begin writing it out.

                    To make sure that your code covers all of the conditions that you intend for it to cover, you should add comments for each clause that explains what that clause is meant to do. Then, you should add tests for each possible path that the program could go though. What leads to certain conditional statements being executed? Is that what you intended?

                    Choosing your type of Conditional
                    When adding conditionals to your program, you should also consider the kinds of conditionals that are at your disposal and what would fit best."""

           },
          {'heading': "Module 5:Loops and Functions",
           'content': """
                1. While looop
                
                    The while Loop
                    With the while loop we can execute a set of statements as long as a condition is true.

                    Example
                    Get your own Python Server
                    Print i as long as i is less than 6:

                    i = 1
                    while i < 6:
                    print(i)
                    i += 1
                    Note: remember to increment i, or else the loop will continue forever.

                    The while loop requires relevant variables to be ready, in this example we need to define an indexing variable, i, which we set to 1.
                    
                    The break Statement:

                    With the break statement we can stop the loop even if the while condition is true:

                    Example:
                    Exit the loop when i is 3:

                    i = 1
                    while i < 6:
                    print(i)
                    if i == 3:
                        break
                    i += 1

                    The continue Statement:

                    With the continue statement we can stop the current iteration, and continue with the next:

                    Example
                    Continue to the next iteration if i is 3:

                    i = 0
                    while i < 6:
                    i += 1
                    if i == 3:
                        continue
                    print(i)

                    The else Statement:

                    With the else statement we can run a block of code once when the condition no longer is true:

                    Example
                    Print a message once the condition is false:

                    i = 1
                    while i < 6:
                    print(i)
                    i += 1
                    else:
                    print("i is no longer less than 6")
                    
                2. For loop
                    A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

                    This is less like the for keyword in other programming languages, and works more like an iterator method as found in other object-orientated programming languages.

                    With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.

                    Example:
                    Get your own Python Server
                    Print each fruit in a fruit list:

                    fruits = ["apple", "banana", "cherry"]
                    for x in fruits:
                    print(x)
                    The for loop does not require an indexing variable to set beforehand.

                    Looping Through a String
                    Even strings are iterable objects, they contain a sequence of characters:

                    Example:
                    Loop through the letters in the word "banana":

                    for x in "banana":
                    print(x)
                    The break Statement
                    With the break statement we can stop the loop before it has looped through all the items:

                    Example:
                    Exit the loop when x is "banana":

                    fruits = ["apple", "banana", "cherry"]
                    for x in fruits:
                    print(x)
                    if x == "banana":
                        break
                        
                    Example:
                    Exit the loop when x is "banana", but this time the break comes before the print:

                    fruits = ["apple", "banana", "cherry"]
                    for x in fruits:
                    if x == "banana":
                        break
                    print(x)

                    The continue Statement:

                    With the continue statement we can stop the current iteration of the loop, and continue with the next:

                    Example:
                    Do not print banana:

                    fruits = ["apple", "banana", "cherry"]
                    for x in fruits:
                    if x == "banana":
                        continue
                    print(x)

                    The range() Function:

                    To loop through a set of code a specified number of times, we can use the range() function,
                    The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.

                    Example
                    Using the range() function:

                    for x in range(6):
                    print(x)
                    Note that range(6) is not the values of 0 to 6, but the values 0 to 5.

                    The range() function defaults to 0 as a starting value, however it is possible to specify the starting value by adding a parameter: range(2, 6), which means values from 2 to 6 (but not including 6):

                    Example
                    Using the start parameter:

                    for x in range(2, 6):
                    print(x)
                    The range() function defaults to increment the sequence by 1, however it is possible to specify the increment value by adding a third parameter: range(2, 30, 3):

                    Example
                    Increment the sequence with 3 (default is 1):

                    for x in range(2, 30, 3):
                    print(x)
                    Else in For Loop
                    The else keyword in a for loop specifies a block of code to be executed when the loop is finished:

                    Example
                    Print all numbers from 0 to 5, and print a message when the loop has ended:

                    for x in range(6):
                    print(x)
                    else:
                    print("Finally finished!")
                    Note: The else block will NOT be executed if the loop is stopped by a break statement.

                    Example
                    Break the loop when x is 3, and see what happens with the else block:

                    for x in range(6):
                    if x == 3: break
                    print(x)
                    else:
                    print("Finally finished!")
                    Nested Loops
                    A nested loop is a loop inside a loop.

                    The "inner loop" will be executed one time for each iteration of the "outer loop":

                    Example
                    Print each adjective for every fruit:

                    adj = ["red", "big", "tasty"]
                    fruits = ["apple", "banana", "cherry"]

                    for x in adj:
                    for y in fruits:
                        print(x, y)
                    The pass Statement
                    for loops cannot be empty, but if you for some reason have a for loop with no content, put in the pass statement to avoid getting an error.

                    Example
                    for x in [0, 1, 2]:
                    pass
                    
                3. Function
                    A function is a block of code which only runs when it is called.

                    You can pass data, known as parameters, into a function.

                    A function can return data as a result.

                    Creating a Function
                    In Python a function is defined using the def keyword:

                    Example:
                    Get your own Python Server
                    def my_function():
                    print("Hello from a function")
                    Calling a Function
                    To call a function, use the function name followed by parenthesis:

                    Example:
                    def my_function():
                    print("Hello from a function")

                    my_function()
                    Arguments
                    Information can be passed into functions as arguments.

                    Arguments are specified after the function name, inside the parentheses. You can add as many arguments as you want, just separate them with a comma.

                    The following example has a function with one argument (fname). When the function is called, we pass along a first name, which is used inside the function to print the full name:

                    Example:
                    def my_function(fname):
                    print(fname + " Refsnes")

                    my_function("Emil")
                    my_function("Tobias")
                    my_function("Linus")
                    Arguments are often shortened to args in Python documentations.

                    Parameters or Arguments?
                    The terms parameter and argument can be used for the same thing: information that are passed into a function.

                    From a function's perspective:

                    A parameter is the variable listed inside the parentheses in the function definition.

                    An argument is the value that is sent to the function when it is called.

                    Number of Arguments
                    By default, a function must be called with the correct number of arguments. Meaning that if your function expects 2 arguments, you have to call the function with 2 arguments, not more, and not less.

                    Example
                    This function expects 2 arguments, and gets 2 arguments:

                    def my_function(fname, lname):
                    print(fname + " " + lname)

                    my_function("Emil", "Refsnes")
                    If you try to call the function with 1 or 3 arguments, you will get an error:
                    Example
                    This function expects 2 arguments, but gets only 1:

                    def my_function(fname, lname):
                    print(fname + " " + lname)

                    my_function("Emil")

                    Arbitrary Arguments, *args:

                    If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.

                    This way the function will receive a tuple of arguments, and can access the items accordingly:

                    Example
                    If the number of arguments is unknown, add a * before the parameter name:

                    def my_function(*kids):
                    print("The youngest child is " + kids[2])

                    my_function("Emil", "Tobias", "Linus")
                    Arbitrary Arguments are often shortened to *args in Python documentations.

                    Keyword Arguments:
                    You can also send arguments with the key = value syntax.

                    This way the order of the arguments does not matter.

                    Example
                    def my_function(child3, child2, child1):
                    print("The youngest child is " + child3)

                    my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")
                    The phrase Keyword Arguments are often shortened to kwargs in Python documentations.

                    Arbitrary Keyword Arguments, **kwargs:

                    If you do not know how many keyword arguments that will be passed into your function, add two asterisk: ** before the parameter name in the function definition.

                    This way the function will receive a dictionary of arguments, and can access the items accordingly:

                    Example
                    If the number of keyword arguments is unknown, add a double ** before the parameter name:

                    def my_function(**kid):
                    print("His last name is " + kid["lname"])

                    my_function(fname = "Tobias", lname = "Refsnes")
                    Arbitrary Kword Arguments are often shortened to **kwargs in Python documentations.

                    Default Parameter Value:
                    The following example shows how to use a default parameter value.

                    If we call the function without argument, it uses the default value:

                    Example
                    def my_function(country = "Norway"):
                    print("I am from " + country)

                    my_function("Sweden")
                    my_function("India")
                    my_function()
                    my_function("Brazil")
                    Passing a List as an Argument
                    You can send any data types of argument to a function (string, number, list, dictionary etc.), and it will be treated as the same data type inside the function.

                    E.g. if you send a List as an argument, it will still be a List when it reaches the function:

                    Example
                    def my_function(food):
                    for x in food:
                        print(x)

                    fruits = ["apple", "banana", "cherry"]

                    my_function(fruits)
                    Return Values
                    To let a function return a value, use the return statement:

                    Example
                    def my_function(x):
                    return 5 * x

                    print(my_function(3))
                    print(my_function(5))
                    print(my_function(9))
                    The pass Statement
                    function definitions cannot be empty, but if you for some reason have a function definition with no content, put in the pass statement to avoid getting an error.

                    Example
                    def myfunction():
                    pass"""}
          ]

quiz = [[{'question': "What is Python primarily used for?",
          'options': ['Data Analysis', 'Web Development', 'All the above', 'None of the above'],
          'correct option': 2},
         {'question': "Which of the following is a characteristic of Python?",
          'options': ['A compiled language', 'A dynamically typed language',
                      'A language with strict data type declarations',
                      'A language primarily used for game development'],
          'correct option': 1},
         {'question': "What is the Python interpreter?",
          'options': ['A tool for writing Python code', 'A text editor',
                      'A program that executes Python code line by line', 'A code repository'],
          'correct option': 2},
         {'question': "How do you print 'Hello, World!' in Python?",
          'options': ['console.log("Hello, World!")', 'print("Hello, World!")', 'System.out.println("Hello, World!")',
                      'print "Hello, World!"'],
          'correct option': 1},
         {'question': "What is a variable in Python?",
          'options': ['A value that never changes', 'A reference to a memory location containing data',
                      'A type of loop', 'A function'],
          'correct option': 1},
         {'question': "Which keyword is used to take user input in Python?",
          'options': ['input()', ' user_input()', 'get_input()', 'userInput()'],
          'correct option': 0},
         ],
        [{'question': "Which symbol is used to assign a value to a variable in Python?",
          'options': [':=', '=>', '=', '=='],
          'correct option': 2},
         {'question': "What is the correct way to declare a variable in Python?",
          'options': ['variable name = value', 'var_name: value', 'variable_name = value', '1_variable = value'],
          'correct option': 2},
         {'question': "Which of the following variable names is not allowed in Python?",
          'options': ['my_variable', '123variable', '_variable', 'variable123'],
          'correct option': 1},
         {'question': "Which operator is used for exponentiation in Python?",
          'options': ['^', '**', '//', '&'],
          'correct option': 1},
         {'question': "What is the purpose of the == operator in Python?",
          'options': ['Assignment', 'Equality comparison', ' Inequality comparison', 'Concatenation'],
          'correct option': 1}
         ],
        [{'question': "What is the data type of the variable age if it is assigned the value 25?",
          'options': ['String', 'Integer', 'Float', 'Boolean'],
          'correct option': 1},
         {'question': "Which of the following is a floating-point number in Python?",
          'options': [' 42', '3.14', "'Hello'", 'True'],
          'correct option': 1},
         {'question': "Which data type is used to store a sequence of elements in Python?",
          'options': [' String', 'Integer', 'List', 'Boolean'],
          'correct option': 2},
         {'question': "What is the data type of the variable is_raining if it is assigned the value True?",
          'options': [' String', 'Integer', 'List', 'Boolean'],
          'correct option': 3}
         ],
        [{'question': "Which of the following best describes a Python list?",
          'options': ['A collection of key-value pairs', 'An ordered, mutable sequence of elements',
                      'A dictionary with unique keys', 'A data type used for storing characters'],
          'correct option': 1},
         {'question': "How do you access an element in a Python list by its index?",
          'options': ['Using a key', 'Using a loop', 'Using square brackets with the index',
                      'Using parentheses with the index'],
          'correct option': 2},
         {'question': "How do you add an element to the end of a list in Python?",
          'options': ['Using the append() method', 'Using the insert() method', 'Using the add() function',
                      'You cannot add elements to the end of a list'],
          'correct option': 0},
         {'question': "How do you access a value in a dictionary using its key?",
          'options': ['Using square brackets with the value', 'Using parentheses with the key', 'Using a loopn',
                      'You cannot access values in a dictionary'],
          'correct option': 0},
         {'question': "What is a Python dictionary?",
          'options': ['A collection of ordered elements', 'A mutable sequence of key-value pairs',
                      ' An unordered collection of key-value pairs', 'A list with numeric indices'],
          'correct option': 2},
         {'question': "What is the result of the following code: my_dict = {'apple': 3, 'banana': 2, 'cherry': 5}?",
          'options': [' A list of fruit names', 'A dictionary with key-value pairs', ' An error', 'The number 5'],
          'correction option': 0},
         {'question': "What is the primary purpose of the if statement in Python?",
          'options': ['To declare variables', 'To create loops', ' To make decisions based on conditions',
                      'To print text'],
          'correction option': 2},
         {
             'question': "In Python, which statement allows you to specify alternative conditions to be executed if the initial condition is not met?",
             'options': ['then', 'elif', 'else', 'unless'],
             'correction option': 1},
         {'question': "What is the result of the expression 5 > 3 in Python?",
          'options': ['True', 'False', '5', '3'],
          'correction option': 0}],
        [{'question': "What is the main purpose of a while loop in Python?",
          'options': ['To execute a block of code a specified number of times.',
                      'To create an infinite loop that never ends.',
                      'To execute a block of code as long as a condition is true.',
                      'To iterate through a list or tuple.'],
          'correction option': 2},
         {'question': "Which keyword is used to exit a while loop prematurely?",
          'options': ['exit', 'break', 'continue', 'finish'],
          'correction option': 1},
         {'question': "What is the purpose of the 'continue' statement in a while loop?",
          'options': ['To restart the loop from the beginning.',
                      'To skip the rest of the current iteration and continue with the next one.', 'To exit the loop.',
                      ' To print a message to the console.'],
          'correction option': 1},
         {'question': "When would you use a for loop in Python?",
          'options': [' To create an infinite loop.', 'To execute a block of code a specific number of times.',
                      'To exit the program.', 'To execute code as long as a condition is true.'],
          'correction option': 1},
         {'question': "What is the purpose of the 'range' function in a for loop?",
          'options': ['To specify the range of numbers to be looped through.', 'To generate random numbers.',
                      'To count the number of loop iterations.', 'To exit the loop.'],
          'correction option': 0},
         {'question': """What is the output of the following code: 
            for i in range(1, 6):
                if i == 3:
                    continue
                print(i)""",
          'options': ['1 2 3 4 5', '1 2 4 5', '1 2', '3'],
          'correction option': 1}]
        ]
