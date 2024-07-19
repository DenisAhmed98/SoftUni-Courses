import re

input_string = input()

regex = r'(\d{2})([-./])([A-Z][a-z]{2})\2(\d{4})'

matches = re.finditer(regex, input_string)

for match in matches:
    day = match.group(1)
    month = match.group(3)
    year = match.group(4)
    print(f'Day: {day}, Month: {month}, Year: {year}')