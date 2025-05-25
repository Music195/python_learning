#object
age = 20 #Create a variable with the value of 20 in the global scope
print(age.real) #Print the real value of the variable in the global scope #20
print(age.imag) #Print the imaginary value of the variable in the global scope #0
print(age.bit_length()) #Print the number of bits required to represent the variable in the global scope #5

items = [1, 2, 3] #Create a list with the values of 1, 2, and 3
print(items) #Print the original list #1, 2, 3

items.append(4) #Append the value of 4 to the list
print(items) #Print the modified list #1, 2, 3, 4

items.pop() #Remove the last element of the list
print(items) #Print the modified list #1, 2, 3

age = 8 #Create a variable with the value of 8 in the global scope

age = age + 1 # create a new age value by adding 1 to the original value
