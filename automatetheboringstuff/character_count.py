message = 'It was a bright cold day in April, and the clocks were stricking thirteen.'
count = {}

for char in message:
    # setdefault method ensures key's existing > if exist, does nothing
    count.setdefault(char, 0) 
    count[char] += 1
    
print(count)