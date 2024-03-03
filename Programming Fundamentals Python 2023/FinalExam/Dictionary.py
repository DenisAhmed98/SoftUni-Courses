dictionary = {}

word_and_definitions = input().split(" | ")
test_words = input().split(" | ")
result = input()

for words in word_and_definitions:
    token = words.split(": ")
    word = token[0]
    definition = token[1]
    if word not in dictionary:
        dictionary[word] = []
    dictionary[word].append(definition)

if result == "Test":
    for test_word in test_words:
        for key, value in dictionary.items():
            if key == test_word:
                print(f"{key}:")
                for i in value:
                    print(f' -{i}')
if result == "Hand Over":
    for key in dictionary:
        print(key, end=" ")