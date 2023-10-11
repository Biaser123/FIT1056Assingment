module_1 = {"heading": "Introduction to Python",
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
            """,
            "challenge": """Create a greeting on a console that display:
             "Hi, my name is Python, nice to meet you" 
             """}

module_2 = {"heading": "Get to know Python syntax and variables",
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
                """}

module_3 = {"heading": "Python Data Types",
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

            """}

module_4 = {"heading": ""}