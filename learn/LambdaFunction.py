#Lambda Function
lambda num : num * 2 #Create a lambda function to multiply the number by 2

multiply = lambda a, b: a * b #Create a lambda function to multiply two numbers
print(multiply(2, 3)) #Print the result of the lambda function #6

#Lambda Function with Map

numbers = [1, 2, 3, 4, 5] #Create a list with the values of 1, 2, 3, 4, and 5

# def double(x): #Define a function to double the number
#     return x * 2 #Return the doubled number

double = lambda x: x * 2 #Create a lambda function to double the number

result = map(double, numbers) #Apply the function to each element in the list using map
            #double can be directly replaced with the lambda function

print(list(result)) #Print the result of the map function #<map object at 0x7f8c8c8c8c10>


#Lambda Function with Filter

numbers = [1, 2, 3, 4, 5] #Create a list with the values of 1, 2, 3, 4, and 5

# def is_even(x): #Define a function to check if the number is even
#         return x % 2 == 0 #Return True if the number is even, False otherwise

result = filter(#is_even = 
    lambda n: n % 2 == 0, numbers) #Apply the function to each element in the list using filter

print(list(result)) #Print and list the result of the filter function # [2, 4]

#Lambda Function with Reduce

from functools import reduce #Import the reduce function from the functools module

expenses = [ ('Dinner', 20), ('Groceries', 50), ('Rent', 100)] 
#Create a list of tuples with the values of Dinner, Groceries, and Rent


#sum = reduce(lambda acc, expense: acc + expense[1], expenses, 0)
sum = reduce(lambda a,b : a + b[1], expenses, 0)
#Apply the function to each element in the list using reduce
#acc is the accumulator that holds the sum of the expenses

print (sum) #Print the result of the reduce function #1070
# sum = 0 

# for expense in expenses: #Loop through the list of tuples
#     sum += expense[1] #Add the value of the second element in the tuple to the sum

# print(sum) #Print the sum of the expenses #1070