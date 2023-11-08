number = int(input())
synonyms = {}

for i in range (number):
    word = input()
    synonym = input()

    if word not in synonyms:
        synonyms[word] = []
    synonyms[word].append(synonym)

for key in synonyms:
    print(f"{key} - {', '.join(synonyms[key])}")