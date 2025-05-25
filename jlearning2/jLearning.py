import random
from sudachipy import Dictionary, SplitMode
import re # For checking if a string contains Kanji

# --- Initialize SudachiPy Tokenizer ---pip install sudachipy sudachidict_core
try:
    tokenizer_obj = Dictionary().create()
except Exception as e:
    print(f"Error initializing SudachiPy tokenizer: {e}")
    print("Please make sure you have installed sudachipy and sudachidict_core.")
    print("Run: pip install sudachipy sudachidict_core")
    tokenizer_obj = None

def is_kanji(char):
    """Checks if a character is a Kanji."""
    # CJK Unified Ideographs, CJK Unified Ideographs Extension A, CJK Compatibility Ideographs
    return '\u4e00' <= char <= '\u9fff' or \
           '\u3400' <= char <= '\u4dbf' or \
           '\uf900' <= char <= '\ufaff'

def contains_kanji(word_surface):
    """Checks if a word string contains any Kanji."""
    return any(is_kanji(char) for char in word_surface)

def get_kanji_words_from_sentence(sentence):
    """
    Uses SudachiPy to tokenize a sentence and extract words containing Kanji
    along with their readings.

    Args:
        sentence (str): The Japanese sentence.

    Returns:
        list: A list of dictionaries, where each dictionary contains:
              'surface' (str): The word as it appears in the sentence (e.g., "勉強").
              'reading' (str): The reading of the word in Katakana (e.g., "ベンキョウ").
                               SudachiPy often gives Katakana; we can convert if needed.
              'pos' (tuple): Part-of-speech tags.
    """
    if not tokenizer_obj:
        return []

    kanji_words_info = []
    # Tokenize in 'C' mode for longer word units, often better for quizzes on whole words
    morphemes = tokenizer_obj.tokenize(sentence, SplitMode.C) 
    
    for m in morphemes:
        if contains_kanji(m.surface()):
            kanji_words_info.append({
                'surface': m.surface(),
                'reading': m.reading_form(), # This is usually Katakana
                'pos': m.part_of_speech() 
            })
    return kanji_words_info

def katakana_to_hiragana(katakana_string):
    """Converts a Katakana string to Hiragana."""
    return "".join(chr(ord(char) - 96) if 'ァ' <= char <= 'ヶ' else char for char in katakana_string)


def advanced_kanji_multiple_choice(sentence):
    """
    Presents a multiple-choice question for a randomly selected Kanji word
    from the sentence using SudachiPy for analysis.
    """
    if not tokenizer_obj:
        print("SudachiPy tokenizer not available. Cannot create quiz.")
        return

    print(f"\nSentence: {sentence}\n")
    
    kanji_words = get_kanji_words_from_sentence(sentence)

    if not kanji_words:
        print("No Kanji words found in this sentence to quiz on.")
        return

    # Randomly select one kanji word to quiz
    target_word_info = random.choice(kanji_words)
    target_surface = target_word_info['surface']
    correct_reading_kata = target_word_info['reading']
    correct_reading_hira = katakana_to_hiragana(correct_reading_kata) # Convert to Hiragana for choices

    # --- Generate Choices (Simple Approach) ---
    # For a more robust system, distractors should be contextually relevant or common misreadings.
    # Here, we'll use the correct reading and some generic/randomly altered ones.
    
    choices = [correct_reading_hira]
    
    # Simple distractor generation (can be significantly improved)
    # 1. A slightly modified version of the correct reading (if long enough)
    if len(correct_reading_hira) > 2:
        temp_distractor = list(correct_reading_hira)
        idx_to_change = random.randrange(len(temp_distractor))
        # Simplistic: change a hiragana character to 'あ' or 'い' if it's not already
        original_char = temp_distractor[idx_to_change]
        if original_char != 'あ':
            temp_distractor[idx_to_change] = 'あ'
        else:
            temp_distractor[idx_to_change] = 'い'
        distractor1 = "".join(temp_distractor)
        if distractor1 != correct_reading_hira and distractor1 not in choices:
             choices.append(distractor1)


    # 2. Readings from other Kanji words in the sentence (if available and different)
    other_readings = [katakana_to_hiragana(kw['reading']) for kw in kanji_words if kw['surface'] != target_surface]
    random.shuffle(other_readings)
    for r in other_readings:
        if r != correct_reading_hira and r not in choices and len(choices) < 4:
            choices.append(r)
            
    # 3. Add some generic incorrect options if we don't have enough choices
    generic_distractors = ["がくせい", "せんせい", "にほん", "かいしゃ", "くるま"] # Example generic words
    random.shuffle(generic_distractors)
    
    idx = 0
    while len(choices) < 4 and idx < len(generic_distractors):
        if generic_distractors[idx] != correct_reading_hira and generic_distractors[idx] not in choices:
            choices.append(generic_distractors[idx])
        idx += 1
    
    # Ensure we have at least 2 choices, if not, it's hard to make a quiz
    if len(choices) < 2:
        choices.append("？？？") # Placeholder if not enough distractors
        if correct_reading_hira not in choices: # Should not happen if logic is correct
             choices.insert(0, correct_reading_hira)


    random.shuffle(choices) # Shuffle the final list of choices

    # --- Present Quiz ---
    quiz_sentence = sentence.replace(target_surface, f"[ {target_surface} ]", 1) # Replace only the first instance for simplicity
    
    print(f"What is the reading (in hiragana) for the word 「{target_surface}」 in this context?")
    print(f"  {quiz_sentence}\n")

    for i, choice in enumerate(choices):
        print(f"{i+1}. {choice}")

    while True:
        try:
            user_answer_idx = int(input("\nEnter your choice (number): ")) - 1
            if 0 <= user_answer_idx < len(choices):
                break
            else:
                print(f"Invalid choice. Please enter a number between 1 and {len(choices)}.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    selected_choice = choices[user_answer_idx]

    if selected_choice == correct_reading_hira:
        print(f"\nCorrect! 🎉 The reading of 「{target_surface}」 is 「{correct_reading_hira}」.")
    else:
        print(f"\nIncorrect. 😢 You chose 「{selected_choice}」.")
        print(f"The correct reading for 「{target_surface}」 is 「{correct_reading_hira}」.")
    
    print(f"Full sentence: {sentence}")
    print(f"POS tags for '{target_surface}': {target_word_info['pos']}")


# --- Example Usage ---
if __name__ == "__main__":
    if tokenizer_obj: # Only run examples if tokenizer initialized successfully
        sentence1 = "今日は良い天気ですね。"
        advanced_kanji_multiple_choice(sentence1)
        print("\n" + "="*30 + "\n")

        sentence2 = "図書館で本を借りました。"
        advanced_kanji_multiple_choice(sentence2)
        print("\n" + "="*30 + "\n")

        sentence3 = "彼は新しい発見をした。"
        advanced_kanji_multiple_choice(sentence3)
        print("\n" + "="*30 + "\n")
        
        sentence4 = "猫が窓から外を見ています。"
        advanced_kanji_multiple_choice(sentence4)
    else:
        print("Examples cannot be run as SudachiPy tokenizer failed to initialize.")