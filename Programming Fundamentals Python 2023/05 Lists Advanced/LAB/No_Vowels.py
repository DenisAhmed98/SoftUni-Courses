text = input()
vowels = ['a', 'o', 'u', 'e', 'i', 'A', 'O', 'U', 'E', 'I']

result = ''.join(([x for x in text if x not in vowels]))

print(result)
