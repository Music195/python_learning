import random

def kanji_multiple_choice(sentence, kanji_info):
    """
    Presents a Japanese sentence with a multiple-choice question for a specific kanji.

    Args:
        sentence (str): The Japanese sentence.
        kanji_info (dict): A dictionary containing:
            'target_kanji' (str): The kanji to be quizzed.
            'correct_reading' (str): The correct reading/meaning for the context.
            'choices' (list): A list of strings, where one is the correct_reading
                              and others are distractors.
    """
    print("Sentence:")
    # Replace the target kanji with a placeholder for the quiz
    quiz_sentence = sentence.replace(kanji_info['target_kanji'], f"[{kanji_info['target_kanji']}]")
    print(f"  {quiz_sentence}\n")

    print(f"What is the correct reading/meaning for the kanji in {kanji_info['target_kanji']} in this context?")

    # Shuffle choices to make it random
    random.shuffle(kanji_info['choices'])
    
    for i, choice in enumerate(kanji_info['choices']):
        print(f"{i+1}. {choice}")

    while True:
        try:
            user_answer = int(input("\nEnter your choice (number): "))
            if 1 <= user_answer <= len(kanji_info['choices']):
                break
            else:
                print("Invalid choice. Please enter a number from the list.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    selected_choice = kanji_info['choices'][user_answer - 1]

    if selected_choice == kanji_info['correct_reading']:
        print(f"\nCorrect! 🎉 The kanji is 「{kanji_info['target_kanji']}」 which means/reads '{kanji_info['correct_reading']}'.")
        print(f"Full sentence: {sentence}")
    else:
        print(f"\nIncorrect. 😢 You chose '{selected_choice}'.")
        print(f"The correct answer was '{kanji_info['correct_reading']}' for the kanji 「{kanji_info['target_kanji']}」.")
        print(f"Full sentence: {sentence}")

# --- Example Usage ---
if __name__ == "__main__":
    # Example 1
    sentence1 = "今日は良い天気ですね。"
    kanji_info1 = {
        'target_kanji': '天気',
        'correct_reading': 'てんき',
        'choices': ['てんき', 'あめ ', 'くも ', 'そら ']
    }
    print("--- Quiz 1 ---")
    kanji_multiple_choice(sentence1, kanji_info1)
    print("\n" + "="*20 + "\n")

    # Example 2
    sentence2 = "図書館で本を借りました。"
    kanji_info2 = {
        'target_kanji': '借',
        'correct_reading': 'か',
        'choices': ['か', 'て', 'う', 'と']
    }
    print("--- Quiz 2 ---")
    kanji_multiple_choice(sentence2, kanji_info2)
    print("\n" + "="*20 + "\n")

    # Example 3: Focusing on a different aspect, like a specific compound
    sentence3 = "彼は新しい発見をした。"
    kanji_info3 = {
        'target_kanji': '発見', # Target is a compound word
        'correct_reading': 'はっけん',
        'choices': ['はっけん', 'はつめい', 'けんきゅう', 'ちょうさ']
    }
    print("--- Quiz 3 ---")
    kanji_multiple_choice(sentence3, kanji_info3)
    print("\n" + "="*20 + "\n")
    # For this example, we'll adjust the display slightly since '発見' is two kanji
    # The code above will replace the first occurrence of '発' or '見' if not handled.
    # A more robust solution would identify the exact position.
    # For simplicity, let's assume the quiz sentence is manually prepared for compounds:
    
    #quiz_sentence3_modified = "彼は新しい [ ? ] をした。"
    # We need to pass the original sentence for the final reveal
    
    # Simplified call for this specific compound example (manual placeholder)
    # print("Sentence:")
    # print(f"  {quiz_sentence3_modified}\n")
    # print(f"What is the correct reading/meaning for the word in [ ? ] in this context?")
    
    # random.shuffle(kanji_info3['choices'])
    # for i, choice in enumerate(kanji_info3['choices']):
    #     print(f"{i+1}. {choice}")

    # while True:
    #     try:
    #         user_answer = int(input("\nEnter your choice (number): "))
    #         if 1 <= user_answer <= len(kanji_info3['choices']):
    #             break
    #         else:
    #             print("Invalid choice. Please enter a number from the list.")
    #     except ValueError:
    #         print("Invalid input. Please enter a number.")

    # selected_choice = kanji_info3['choices'][user_answer - 1]

    # if selected_choice == kanji_info3['correct_reading']:
    #     print(f"\nCorrect! 🎉 The word is 「{kanji_info3['target_kanji']}」 which means/reads '{kanji_info3['correct_reading']}'.")
    #     print(f"Full sentence: {sentence3}")
    # else:
    #     print(f"\nIncorrect. 😢 You chose '{selected_choice}'.")
    #     print(f"The correct answer was '{kanji_info3['correct_reading']}' for the word 「{kanji_info3['target_kanji']}」.")
    #     print(f"Full sentence: {sentence3}")