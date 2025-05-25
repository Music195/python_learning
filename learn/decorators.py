#Decorators are a powerful and useful tool in Python 
# since they allow you to modify the behavior of a function or class.
#  They are often used in web frameworks, logging, access control, memoization, and more.


def logtime(func):
    def wrapper(): #Define a wrapper function to modify the behavior of the original function
        print("Start time") #Print the start time
        val = func()
        print("End time")
        return val
    return wrapper #Return the wrapper function
#The decorator is applied to the hello function using the @ symbol

@logtime #Apply the logtime decorator to the function
def hello():
    print("Hello") #Print "Hello"

hello() #Call the function to test the decorator

#--------------------------------------------------------------
# Decorate the function with the parameter that is the same as the function parameter


def log_execution(func):
    """
    A decorator that logs the execution of a function.
    """
    def wrapper(name):  # Accept any arguments the original function might take
        print(f"Executing '{func.__name__}'...")  # Log the function name
        result = func(name)  # Call the original function
        print(f"Finished executing '{func.__name__}'")  # Log after execution
        return result  # Return the result of the original function
    return wrapper  # Return the wrapper function

# Apply the decorator to a function
@log_execution
def greet(name):
    print(f"Hello, {name}!")

# Call the decorated function
greet("Alice")

#--------------------------------------------------------------

#Decorate the function with two parameters

#Example 1

def log_execution(func):
    """
    A decorator that logs the execution of a function.
    """
    def wrapper(name, greeting="Hello", punctuation="!"):  # Use the same parameter names as the original function
        print(f"Executing '{func.__name__}'...")  # Log the function name
        result = func(name, greeting, punctuation)  # Call the original function with the same parameters
        print(f"Finished executing '{func.__name__}'")  # Log after execution
        return result  # Return the result of the original function
    return wrapper  # Return the wrapper function

# Apply the decorator to a function
@log_execution
def greet(name, greeting="Hello", punctuation="!"):
    print(f"{greeting}, {name}{punctuation}")

# Call the decorated function
greet("Alice", greeting="Hi", punctuation="!!!")
greet("Bob", punctuation=".")

#Example 2

def log_execution(func):
    """
    A decorator that logs the execution of a function.
    """
    def wrapper(*args, **kwargs):  # Accept any arguments the original function might take
        print(f"Executing '{func.__name__}'...")  # Log the function name
        result = func(*args, **kwargs)  # Call the original function with all arguments
        print(f"Finished executing '{func.__name__}'")  # Log after execution
        return result  # Return the result of the original function
    return wrapper  # Return the wrapper function

# Apply the decorator to a function
@log_execution
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

# Call the decorated function with positional and keyword arguments
greet("Alice")
greet("Bob", greeting="Hi")

#--------------------------------------------------------------------

# Decorate the function with multiple parameters
# This example shows how to use a decorator with a function that has multiple parameters.


def log_execution(func):
    """
    A decorator that logs the execution of a function.
    """
    def wrapper(*args, **kwargs):  # Accept any arguments the original function might take
        print(f"Executing '{func.__name__}'...")  # Log the function name
        result = func(*args, **kwargs)  # Call the original function with all arguments
        print(f"Finished executing '{func.__name__}'")  # Log after execution
        return result  # Return the result of the original function
    return wrapper  # Return the wrapper function

# Apply the decorator to a function
@log_execution
def greet(name, greeting="Hello", punctuation="!"):
    print(f"{greeting}, {name}{punctuation}")

# Call the decorated function with three parameters
greet("Alice", greeting="Hi", punctuation="!!!")
greet("Bob", punctuation=".")

#-----------------------------------------------------------------------

# Decorate the function without using the @ symbol

def log_execution(func):
    """
    A decorator that logs the execution of a function.
    """
    def wrapper(*args, **kwargs):  # Accept any arguments the original function might take
        print(f"Executing '{func.__name__}'...")  # Log the function name
        result = func(*args, **kwargs)  # Call the original function with all arguments
        print(f"Finished executing '{func.__name__}'")  # Log after execution
        return result  # Return the result of the original function
    return wrapper  # Return the wrapper function

# Define the function
def greet(name, greeting="Hello", punctuation="!"):
    print(f"{greeting}, {name}{punctuation}")

# Manually apply the decorator
greet = log_execution(greet)

# Call the decorated function
greet("Alice", greeting="Hi", punctuation="!!!")
greet("Bob", punctuation=".")