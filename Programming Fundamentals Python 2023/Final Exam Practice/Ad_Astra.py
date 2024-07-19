import re

string = input()
pattern = r"(?i)([#|])([a-z\s]+)(\1)(\d{2}\/\d{2}\/\d{2})(\1)(\d+)(\1)"

matches = re.findall(pattern, string)
total_calories = sum([int(match[5]) for match in matches]) #groups from the pattern
days = total_calories // 2000
print(f"You have food to last you for: {days} days!")

for element in matches:
    item = element[1] #groups from the pattern
    expiration_day = element[3] #groups from the pattern
    nutrition = element[5] #groups from the pattern
    print(f"Item: {item}, Best before: {expiration_day}, Nutrition: {nutrition}")