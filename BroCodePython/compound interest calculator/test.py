# # print(help(str))
# def contains(text, substring):
#     """
#     Checks if a substring is present within a text.

#     Args:
#         text (str): The main string to search within.
#         substring (str): The substring to search for.

#     Returns:
#         bool: True if the substring is found in the text, False otherwise.
#     """
#     return substring in text
# name = "Bro Code"
# # name = add(name, "Python")
# # print(name)
# result = conatins(name, "Code")  # Using the contains function defined above
# result = name.__contains__("Code")  # Using __contains__ method directly
# print(result)  # Should print True if "Code" is in "Bro Code"
name = "Win Ei"
print(name.find("t"))  # Should print -1 since "t" is not in "Win Ei"

# CPython stands for "C Python", which is the reference implementation of the Python programming language written in the C programming language.
# CPython source code for str.find():
# In CPython, str.find() is implemented in C. The relevant code is in 'Objects/unicodeobject.c'.
# The function is called unicode_find(). Here is a simplified excerpt:

# static Py_ssize_t
# unicode_find(PyObject *self, PyObject *sub, Py_ssize_t start, Py_ssize_t end, int direction)
# {
#     // ... (argument checks and setup)
#     // Search for the substring
#     if (direction > 0) {
#         // Forward search
#         for (i = start; i <= end - sub_len; i++) {
#             if (memcmp(main_str + i, sub_str, sub_len) == 0)
#                 return i;
#         }
#     } else {
#         // Backward search
#         for (i = end - sub_len; i >= start; i--) {
#             if (memcmp(main_str + i, sub_str, sub_len) == 0)
#                 return i;
#         }
#     }
#     return -1; // Not found
# }

# So, str.find() returns -1 if the substring is not found.

name = "Alice"
age = 30

# Using f-strings
print(f"Name: {name:s}, Age: {age}") # :s is optional for strings here
print(f"Name: {name}, Age: {age}")   # Same as above

# Using str.format()
print("Name: {0:s}, Age: {1}".format(name, age))
print("Name: {}, Age: {}".format(name, age))