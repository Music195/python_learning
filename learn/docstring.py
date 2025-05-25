#Docstrings

# def increment(n): 
#     """Increment a number.""" #Docstring for the class
#     return n + 1 #Increment the number by 1

# print(increment(5)) #Print the result of the increment function #6
# print(increment.__doc__) #Print the docstring of the increment function #A class representing a dog.


"""
Dog module
This module contains a class representing a dog and its behavior.
It includes methods to initialize the dog's attributes and make it bark.
"""

# class Dog: 
#     """A class representing a dog.""" #Docstring for the class
#     def __init__(self, name, age): #Constructor method to initialize the object
#         """Initialize the dog's name and age."""
#         self.name = name #Set the name of the dog to the value passed in the constructor
#         self.age = age #Set the age of the dog to the value passed in the constructor

#     def bark(self): #Method to make the dog bark
#         """Make the dog bark.""" #Docstring for the method
#         print("Woof! Woof!") #Print the sound of the dog barking


# print(help(Dog)) #Print the help information for the Dog class
# print(Dog.__doc__) #Print the docstring of the Dog class

#------------------------------------------

def add_numbers(a, b):
    """
    Adds two numbers and returns the result.

    Parameters:
    a (int or float): The first number.
    b (int or float): The second number.

    Returns:
    int or float: The sum of the two numbers.
    """
    return a + b

help(add_numbers) #Print the help information for the add_numbers function