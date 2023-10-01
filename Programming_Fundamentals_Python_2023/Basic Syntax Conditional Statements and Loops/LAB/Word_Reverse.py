word = input()
reveresed =""

for i in range (len(word) - 1, -1, -1):
    reveresed += word[i]

print(reveresed)