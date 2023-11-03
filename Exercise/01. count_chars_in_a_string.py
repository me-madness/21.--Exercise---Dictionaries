# First task from the lecture

symbols = [character for character in input() if character != " "]
letters = {}

for symbol in symbols:
    if symbol not in letters.keys():  # by default is if symbol not in letters
        letters[symbol] = 0
    letters[symbol] += 1
    
for symbol, occurrences in letters.items():
    print(f"{symbol} -> {occurrences}")        

# Second task from me me

