characters = input().split(", ")
ascii_dictionary = {}

for char in characters:
    key = char
    value = ord(char)

    ascii_dictionary[key] = int(value)

print(ascii_dictionary)