# words = {}
# def add_word(word, definition):
#     words[word.lower()] = definition

# add_word("Go", "to go")
# add_word("eat", "to eat")

# def list_words():
#     for word in sorted(words):
#         print (f"{word}: {words[word]}")

# sorted_dict = {  key: words[key] for key in sorted(words)}
# print(sorted_dict)

# list_words()

# import json

# # Python dictionary
# python_data = {
#     "name": "John Doe",
#     "age": 30,
#     "isStudent": False,
#     "courses": [
#         {"title": "History", "credits": 3},
#         {"title": "Math", "credits": 4}
#     ]
# }
# print(f"This is python dictionary\n{python_data}")
# # Convert Python dictionary to JSON string
# json_string = json.dumps(python_data, indent=4) # indent for pretty printing
# print("\nJSON String:")
# print(json_string)

# # Convert JSON string back to Python dictionary
# python_object_from_string = json.loads(json_string)
# print("\nPython object from JSON string:")
# print(python_object_from_string)

# # Writing JSON to a file
# with open("data.json", "w") as outfile:
#     json.dump(python_data, outfile, indent=4)

# # Reading JSON from a file
# with open("data.json", "r") as infile:
#     data_from_file = json.load(infile)
# print("\nData read from file:")
# print(data_from_file)

from dicApp import Dictionary

# Using the Dictionary class
my_dict = Dictionary()
my_dict.add_word("test", "a procedure for evaluation")
my_dict.list_words()

