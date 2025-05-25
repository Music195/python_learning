# #Exception
# try:
#     #Code that may raise an exception
#     result = 1 / 0 #Division by zero will raise an exception
# except ZeroDivisionError as e:
#     #Handle the exception
#     print("Error:", e)
# finally:    
#     #Code that will always execute
#     print("This block always executes, regardless of exceptions.")
# # #This block always executes, regardless of exceptions.

# try:
#     raise Exception("This is a custom exception message.")
# except Exception as e:
#     #Handle the exception
#     print("Error:", e)
# # #This is a custom exception message.


# class CustomException(Exception):
#     """Custom exception class."""
#     pass


# try:
#     raise CustomException("This is a custom exception message.")
# except CustomException as e:
#     #Handle the exception
#     print("Error:", e)
# # #This is a custom exception message.

# """
# This is a comment
# written in 
# more than just one line.

# """


# try:
#     print (x) #Print the value of x
# except NameError:
#     print ("Variable x is not defined")
# except TypeError:
#     print ("Variable x is not a number")

while True:
    try:
        x = int(input("Please enter a number: ")) #Prompt the user to enter a number
        break #Exit the loop if the input is valid
    except ValueError:
        print("Invalid input. Please enter a valid number.")

print ("You entered:", x) #Print the value of x
