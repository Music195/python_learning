#Accepting Arguments

# import sys 
# # Check if the script is being run directly

# name = sys.argv[1] #Get the first argument from the command line
# print("Hello, " + name + ".") #Print "Hello," + name
# print("Hello World")

import argparse #Import the argparse module to handle command line arguments

parser = argparse.ArgumentParser(
    description="A simple program that accepts command line arguments." #Description of the program
    #Create a parser object to handle command line arguments
)

parser .add_argument(
    '-c', '--color', metavar='color',
    required=True, choices= {'red', 'yellow'},help='the color to search for') #Add an argument for color

args = parser.parse_args() #Parse the command line arguments
print(args.color) #Print the value of the color argument