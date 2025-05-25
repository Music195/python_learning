#Modules

import learn.Dog as Dog #Import the Dog module

Dog.bark() #Call the bark function from the Dog module

#to use the module, need to create a file named __init__.py in the same directory as the module. 
# This file can be empty, but it tells Python that this directory should be treated as a package.

from lib import cat #Import the cat module
cat.walk() #Call the walk function from the cat module

from lib.cat import walk #Import the walk function from the cat module
walk() #Call the walk function from the cat module


# Python common libraries
# math for math utilities
# re for regular expressions
#json to work with JSON data
# datetime to work with dates and times
#sqlite3 to work with SQLite databases
# os to work with the operating system
#random to generate random numbers
#statistics to work with statistics
#requests to make HTTP network requests
#http to create HTTP servers and clients
#urllib to work with URLs

import math #Import the math module

print(math.sqrt(16)) #Calculate the square root of 16 and print the result #4.0

from math import sqrt #Import the sqrt function from the math module
print(sqrt(16)) #Calculate the square root of 16 and print the result #4.0