class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        # Default string representation
        return f"{self.first_name} {self.last_name}"

    def __format__(self, format_spec):
        print(f"Format specifier received: '{format_spec}'")
        if format_spec == "full":
            return f"Full Name: {self.first_name} {self.last_name}"
        elif format_spec == "short":
            return f"{self.first_name[0]}. {self.last_name}"
        elif format_spec == "last_first":
            return f"{self.last_name}, {self.first_name}"
        elif not format_spec: # Handles empty format spec like format(person) or f"{person}"
            return str(self) # Use the __str__ representation
        else:
            # For any other format_spec, raise an error or return a default
            raise ValueError(f"Unsupported format string '{format_spec}' for Person")

# Create an instance of Person
person = Person("John", "Doe")

# Using the __format__ method directly (less common)
print(person.__format__("full"))
print(person.__format__("short"))

# Using the format() built-in function (more common)
print(format(person, "last_first"))
print(format(person, "full"))
print(format(person)) # Uses empty format_spec, falls back to __str__ via __format__

# Using f-strings (most common and readable)
print(f"{person:short}")
print(f"{person:last_first}")
print(f"{person}") # Uses empty format_spec

# Example of an unsupported format specifier
try:
    print(f"{person:unknown_spec}")
except ValueError as e:
    print(e)

# --- Regarding your code snippet ---
# filepath: c:\Users\minth\OneDrive\Desktop\Programming\Python_learning\BroCodePython\compound interest calculator\main.py
# ...existing code...
name = 1.237
# name = name.__format__("s") # This would cause a TypeError for a float.
                              # Floats have their own format specifiers (e.g., ".2f", "e")
                              # "s" is for string formatting, which float.__format__ doesn't directly support.
                              # If you want to convert it to a string first:
name_str = str(name)
formatted_name_str = name_str.__format__("s") # This will just return the string "1.237"
print(formatted_name_str)

# Or, more commonly for floats:
formatted_float = format(name, ".2f") # Formats to two decimal places: "1.24"
print(formatted_float)

another_formatted_float = f"{name:.1f}" # Formats to one decimal place: "1.2"
print(another_formatted_float)
# ...existing code...