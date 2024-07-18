text = input().split(" ")
user_palindrome = input()
palindromes = []
counter = 0
for word in text:
    if word == "".join(reversed(word)):
        palindromes.append(word)
    if word == user_palindrome:
        counter +=1

print(f"{palindromes}")
print(f"Found palindrome {counter} times")