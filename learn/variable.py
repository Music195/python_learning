num1 = 2+3j
num2 = complex(9, 3)  # Creates a complex number with real part 9 and imaginary part 3
# print(num1, num2)
# print(type(num1), type(num2))
print(num1.real, num1.imag)  # Accessing real and imaginary parts of the complex number
print(num2.real, num2.imag)  # Accessing real and imaginary parts of the complex number
print(num1 + num2)  # Adding two complex numbers
print(abs(-5.5))  # Absolute value of a number
print(round(5.589))  # Rounding a number to the nearest integer
print(round(5.5, 1))  # Rounding a number to one decimal place
print(round(5.590, 2))  # Rounding a number to two decimal places

from enum import Enum
class State ( Enum ):
    START = 1
    STOP = 2
    PAUSE = 3

print(State.START.value)  # Accessing an enum member
print(State.STOP.value)  # Accessing an enum member
print(State.PAUSE.value)  # Accessing an enum member
print(State.START.name)  # Accessing the name of an enum member
print(State(1))  # Accessing an enum member by its value
print(State["STOP"])  # Accessing an enum member by its name
print(list(State))  # Listing all enum members
print(len(State))  # Length of the enum