questions = ("What is the capital of France?",
             "What is 2 + 2?",
             "What is the largest planet in our solar system?",
             "What is the boiling point of water in Celsius?")

options = (("A) Paris", "B) London","C) Berlin", "D) Madrid"),
           ("A) 3", "B) 4", "C) 5", "D) 6"),
           ("A) Earth", "B) Mars", "C) Jupiter", "D) Saturn"),
           ("A) 90", "B) 100", "C) 110", "D) 120"))


answers = ("A", "B", "C", "B")
guesses = []
score = 0
question_num = 0
# Display the questions and options
for question in questions:
    print(question)
    for option in options[question_num]: # Display each option for the current question
        print(option)
    print("-" * 50)
    while True: # Loop until a valid input is received
        guess = input("Enter your answer (A/B/C/D): ").upper() # Get user's guess
        if guess not in ["A", "B", "C", "D"]: # Validate the input
            print("Invalid input. Please enter A, B, C, or D.")
            continue
        else:
            break
    guesses.append(guess) # Store the user's guess
    if guess == answers[question_num]: # Check if the guess is correct
        print("Correct!")
        score += 1 # Increment score for a correct answer
    else:
        print(f"Wrong! The correct answer was {answers[question_num]}.")
    print("-" * 50)
    question_num += 1 # Increment the question number for the next iteration

print(f"You hit the answer {score} out of {len(questions)}") # Display the final score

print("Your guesses were:") # Display the user's guesses
for i in range(len(guesses)):
    print(f"Question {i + 1}: {guesses[i]}") # Print each guess with the corresponding question number
 
print("Your score is: ", score/len(guesses) * 100) # Print the final score

# def ask_question(question, options, answer):
#     print(question)
#     for option in options:
#         print(option)
#     guess = input("Enter your answer (A/B/C/D): ").upper()
#     guesses.append(guess)
#     return guess == answer

