import re

result = re.search(r"\d+", "There are 243 apples")
if result:
    print(f"Match found: {result.group()}")
else:
    print("No match found.")