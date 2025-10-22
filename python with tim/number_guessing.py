import random
import sys

# top_of_range = input("Enter an number: ")

# if top_of_range.isdigit():
#     top_of_range = int(top_of_range)
#     if top_of_range <= 0:
#         print("You must enter a number larger than 0")
#         quit()
# else :
#     print("Enter only the digit number!")
#     quit()
while True:   
    s = input("Enter a number: ")
    try:
        n = int(s)         # accepts "+3", " 4 ", "-2"
        if n <= 0:
            print("Enter a number greater than 0!")
        else:
            break
    except ValueError:
        input("Not an integer. Press Enter and Enter again!")
    
rand_num = random.randint(0, n)

print(rand_num)

guess_count = 0
while True:
    guess_count += 1
    user_guess = input("Make a guess: ")
    # if user_guess.lower() == "q":
    #     print("Thanks for playing!")
    #     sys.exit()
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please enter only digit!!")
        continue

    if user_guess == rand_num:
        print(f"You got it at {guess_count} time/s!!")
        break
    elif user_guess > rand_num:
        print("You are above the number!")
    else:
        print("You are below the number!")