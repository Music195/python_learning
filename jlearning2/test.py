import re

result = re.search(r"\d+", "There are 243 apples")
#\d means "any digit" (0-9).
# + means "one or more times".
# So, \d+ matches one or more digits in a row (e.g., "24").
if result:
    print(f"Match found: {result.group()}") #
else:
    print("No match found.")