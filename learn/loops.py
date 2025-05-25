#loop

# condition = True
# while condition == True: #Start of the while loop
#     print("This is a while loop")
#     condition = False #Change the condition to False to exit the loop
#     print("This is the end of the while loop") #Print the end of the while loop


# count = 0 #Create a variable with the value of 0
# while count < 5: #Start of the while loop
#     print(count) #Print the value of the variable
#     count += 1 #Increment the value of the variable by 1

#     print("This is the end of the while loop") #Print the end of the while loop after the loop

# print("\nThis is the end of the whole while loop") #Print the end of the while loop after the whole while loop


# items = [1, 2, 3] #Create a list with the values of 1, 2, and 3
# for item in items: #Start of the for loop
#     print(item) #Print the value of the item in the list
#     print("This is the end of the for loop") #Print the end of the for loop after the loop

# for item in range(15): #Start of the for loop
#     print(item) #Print the value of the item in the list
# print("\nThis is the end of the for loop") #Print the end of the for loop after the loop

# items = ["John", "Jack", "Jim"] #Create a list with the values of Jonh, Jack, and Jim
# for index, item in enumerate(items): #Start of the for loop
#     print(index,"th -->", item) #Print the value of the item in the list
# print("This is the end of the for loop") #Print the end of the for loop after the loop

# items = ["John", "Jack", "Jim"] #Create a list with the values of Jonh, Jack, and Jim
# for i in range(len(items)): #Start of the for loop
#     print(i,"th -->", items[i]) #Print the value of the item in the list
# print("\nThis is the end of the for loop") #Print the end of the for loop after the loop

# items = ["John", "Jack", "Jim"] #Create a list with the values of Jonh, Jack, and Jim
# for item in items: #Start of the for loop
#     if item == "Jack":
#         continue
#     print(item) #Print the value of the item in the list
# print("\nThis is the end of the for loop") #Print the end of the for loop after the loop

#Break and Continue

# items = [1, 2, 3] #Create a list with the values of 1, 2, and 3
# for item in items: #Start of the for loop
#     if item == 2:
#         continue #Skip the value of 2 and continue to the next iteration
#     print(item) #Print the value of the item in the list

# for item in items: #Start of the for loop
#     if item == 2:
#         break #Break the loop when the value is 2
#     print(item) #Print the value of the item in the list

# #Classes

class animal: #Define a class named animal
    def walk(self):
        print("I can walk")
class Dog(animal): #Define a class named Dog that inherits from the animal class
    def __init__(self, name, age): ##Constructor method to initialize the object
        self.name = name #Set the name of the dog to the value passed in the constructor
        self.age = age #Set the age of the dog to the value passed in the constructor
    def bark(self):
        print("Woof! Woof!") #Print "Woof! Woof!" when the bark method is called

roger = Dog("Roger", 8) #Create an instance of the Dog class  

print(roger.name) #Print the name of the dog #Roger
print(roger.age) #Print the age of the dog #8
roger.bark() #Call the bark method of the dog instance #Woof! Woof!
roger.walk() #Call the walk method of the dog instance #I can walk