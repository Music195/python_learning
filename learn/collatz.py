import time
def collatz(number):
    if  number % 2 == 0:
        print(f"{number} // 2")
        return number // 2
    else:
        print(f"{number} * 3 + 1")
        return number * 3 + 1
    
while True:
    try:
        input_number = int(input("Enter a positive integer: "))
        if input_number > 0:
            break
    except ValueError:
        print("Please enter a valid integer.")
print(f"Starting with: {input_number}")
# The Collatz conjecture is a sequence defined as follows:
# - Start with any positive integer n.
# - If n is even, divide it by 2.
# - If n is odd, multiply it by 3 and add 1.
# - Repeat the process with the resulting number.
# The conjecture states that no matter what positive integer you start with, the sequence will eventually
# reach 1. This code implements the Collatz conjecture in Python.
# It prompts the user to enter a positive integer and then generates the sequence until it reaches 1.
# The code includes error handling to ensure the input is a valid positive integer.
# The sequence is printed step by step, showing how the number changes at each step.
# The code uses a while loop to continue the process until the number reaches 1.
# The `collatz` function performs the necessary calculations based on whether the number is even or odd.
# The output is printed with a delay for better readability, allowing the user to see each
# step of the sequence as it unfolds.
# The code is a simple demonstration of the Collatz conjecture, which remains an unsolved
# problem in mathematics, despite being verified for many numbers.
# The conjecture is a fascinating topic in number theory and has intrigued mathematicians for decades.
# The code is structured to handle invalid inputs gracefully, ensuring that the user is prompted
# to enter a valid positive integer before proceeding with the sequence generation.
# The sequence will continue until it reaches 1, at which point the program will end.
# The code is a practical implementation of the Collatz conjecture, showcasing how it works
# through a simple Python program. It serves as an educational tool for understanding the conjecture
# and provides a hands-on experience for users to see the sequence in action.
# The code is designed to be user-friendly, with clear prompts and error messages to guide the
# user through the process. It demonstrates the basic principles of the Collatz conjecture
# and provides a visual representation of the sequence as it progresses.
print("Generating Collatz sequence:")

while input_number != 1:
    input_number = collatz(input_number)
    print(f"Next number: {input_number}")
    time.sleep(0.1)  # Adding a delay for better readability of the output
print("Reached 1, ending the sequence.")
# This code implements the Collatz conjecture, where the next number is determined based on whether
# the current number is even or odd. If even, it is divided by 2;
# if odd, it is multiplied by 3 and incremented by 1. The process
# continues until the number reaches 1, at which point the sequence ends.
# The code prints each step of the sequence, showing how the number changes.
# The user is prompted to enter a starting number, and the sequence is generated from there.
# The output shows the operations performed at each step and the resulting number.
# This is a simple implementation of the Collatz conjecture, which states that no matter what
# positive integer you start with, the sequence will eventually reach 1.
# The conjecture remains unproven for all integers, but it has been verified for many
# numbers. The code provides a practical demonstration of the conjecture in action. 