def hello (name = "World"): #Define a function with a default parameter
    print("Hello, " + name + ".") #Print "Hello, World!" + name
hello() #Print "Hello, World."
hello("Win") #Print "Hello, Win."
hello("Empire") #Print "Hello, Empire."

def hello (name, age):
    print("Hello, " + name + ". You are " + str(age) + " years old.") #Print "Hello, World!" + name + age
hello("Win", 20) #Print "Hello, Win. You are 20 years old."

val = 10 #Create a variable with the value of 10
def change (value):
    value = 5 #Change the value to 5
print(val) #Print the original value #10
change(val) #Call the function to change the value but it will not affect the original value because it is immutable
print(val) #Print the original value #10
lst = [1, 2, 3] #Create a list with the values of 1, 2, and 3
def change (value):
    value[0] = 5 #Change the first element of the list to 5
    # return value #Return the modified list

change(lst) #Call the function to change the list
print(lst) #Print the original list #1, 2, 3

def hello (name):
    if not name:# #Check if the name is empty
        return
    print ("Hello " + name + ".") #Print "Hello, World!" + name
# hello() #Print nothing because the name is empty and the the later part of the code will not be executed.
hello("Win") #Print "Hello, Win."
def hello (name):
    print ("Hello " + name + ".") #Print "Hello, World!" + name
    return name, "Empire" , 8 #Return the name, "Empire", and 8
print(hello("Win")) #Print "Hello, Win." and return the name, "Empire", and 8

age = 20 #Create a variable with the value of 20 in the global scope
def test():
    age = 25 #Create a variable with the value of 25 in the local scope
    print(age) #Print the value of the variable in the local scope #25

print(age) #Print the original value #20

test() #Call the function to test the value and it will print the value in the local scope #25

def talk(phrase):
    def say(word): #Define a nested function
        print(word)
    words = phrase.split() #Split the phrase into words
    for word in words: #Loop through the words
        say(word) #Call the nested function to print each word

talk(" I am going to buy the milk") #Call the function to print the words in the phrase

def count():
    count = 0 #Create a variable with the value of 0
    def increment(): #Define a nested function
        nonlocal count #Use the nonlocal keyword to access the variable in the outer function
        count += 2 #Increment the value of the variable by 2
        print(count) #Print the value of the variable

    increment() #Call the nested function to increment the value of the variable

count() #Call the function to test the value and it will print the value in the local scope #2

print ("--------------------------------------------------") #Print a separator line

# Closures

def make_counter():
    count = 0 #Create a variable with the value of 0
    def counter(): #Define a nested function
        nonlocal count#Use the nonlocal keyword to access the variable in the outer function
        count += 1 #Increment the value of the variable by 1
        return count #Return the value of the variable

    return counter #Return the nested function
counter = make_counter() #Call the outer function to create the counter function
print(counter()) #Call the counter function to print the value of the variable #1
print(counter()) #Call the counter function to print the value of the variable #2
print(counter()) #Call the counter function to print the value of the variable #3
print(counter()) #Call the counter function to print the value of the variable #4