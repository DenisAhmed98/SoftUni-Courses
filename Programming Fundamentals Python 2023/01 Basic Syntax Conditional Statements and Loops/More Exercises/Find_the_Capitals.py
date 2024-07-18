word = input()
wordlist = []
counter = 0
for i in word:
    if i.isupper():
        wordlist.append(counter)
    counter +=1

print(wordlist)
