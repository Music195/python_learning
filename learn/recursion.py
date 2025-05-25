#Recursion

def factorial(n):
    if n == 0:return 1 #Base case: if n is 0, return 1
        # print("Base case reached with n =", n) #Debugging statement
        
    return n * factorial(n - 1)



print(factorial(0)) #Print the result of the factorial function #1
print(factorial(1)) #Print the result of the factorial function #1
print(factorial(2)) #Print the result of the factorial function #2
print(factorial(3)) #Print the result of the factorial function #6  
print(factorial(4)) #Print the result of the factorial function #24
print(factorial(5)) #Print the result of the factorial function #120
print(factorial(6)) #Print the result of the factorial function #720
print(factorial(7)) #Print the result of the factorial function #5040
print(factorial(8)) #Print the result of the factorial function #40320
print(factorial(9)) #Print the result of the factorial function #362880
print(factorial(10)) #Print the result of the factorial function #3628800
print(factorial(11)) #Print the result of the factorial function #39916800
