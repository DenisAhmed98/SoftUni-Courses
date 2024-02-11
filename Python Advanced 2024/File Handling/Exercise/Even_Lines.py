symbols = ("-", ",", ".", "!", "?")

with open("Files\File01.txt", "r") as file:
    text = file.readlines()

for line in range(0,len(text), 2):
    for symbol in symbols:
        text[line] = text[line].replace(symbol, "@")

    print(*text[line].split()[::-1])

            
