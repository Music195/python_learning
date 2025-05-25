import json
import os

class Dictionary:
    def __init__(self, filename='dictionary.json'):
        self.filename = filename
        self.words = {}
        self.load() # 

    def add_word(self, word, definition):
        self.words[word.lower()] = definition

    def search_word(self, word):
        return self.words.get(word.lower())

    def list_words(self):
        for word in sorted(self.words):
            print(f"{word}: {self.words[word]}")

    def save(self):
        with open(self.filename, 'w') as f:
            json.dump(self.words, f, indent=2)

    def load(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as f:
                self.words = json.load(f)

def main():
    dictionary = Dictionary()

    while True:
        print("\nDictionary App")
        print("1. Add Word")
        print("2. Search Word")
        print("3. List All Words")
        print("4. Save and Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            word = input("Enter word: ")
            definition = input("Enter definition: ")
            dictionary.add_word(word, definition)
            print("Word added.")

        elif choice == "2":
            word = input("Enter word to search: ")
            result = dictionary.search_word(word)
            if result:
                print(f"Definition: {result}")
            else:
                print("Word not found.")

        elif choice == "3":
            print("All words:")
            dictionary.list_words()

        elif choice == "4":
            dictionary.save()
            print("Dictionary saved. Goodbye!")
            break

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
