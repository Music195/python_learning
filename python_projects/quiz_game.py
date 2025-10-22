print("Welcome to the Quiz Game!")

playing = input("Do you want to play? (yes/no) ").lower()
if playing != "yes":
    print("Exiting the game. Goodbye!")
    quit()  
else:
    print("Great! Let's start the game.")
    
score = 0
    
answer = input("What does CPU stand for? ").lower()
if answer == "central processing unit":
    print("Correct! Well done.")
    score += 1
else:
    print("Incorrect. The correct answer is 'Central Processing Unit'.")

answer = input("What does GPU stand for? ").lower()
if answer == "graphics processing unit":
    print("Correct! Well done.")
    score += 1
else:
    print("Incorrect. The correct answer is 'Graphics Processing Unit'.")

print(f"You correct {score} question/s.")