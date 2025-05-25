import re

# result = re.search(r"\d+", "There are 243 apples")
# #\d means "any digit" (0-9).
# # + means "one or more times".
# # So, \d+ matches one or more digits in a row (e.g., "24").
# if result:
#     print(f"Match found: {result.group()}") #
# else:
#     print("No match found.")

# import re

# text = "My phone number is 123-456-7890."
# match = re.search(r"\d{3}-\d{3}-\d{4}", text)
# if match:
#     print("Found phone number:", match.group())

def is_kanji(char):
    """Checks if a character is a Kanji."""
    # CJK Unified Ideographs, CJK Unified Ideographs Extension A, CJK Compatibility Ideographs
    return '\u4e00' <= char <= '\u9fff' or \
           '\u3400' <= char <= '\u4dbf' or \
           '\uf900' <= char <= '\ufaff'


print(is_kanji('改善'))  # Should return True for Kanji character '勉'