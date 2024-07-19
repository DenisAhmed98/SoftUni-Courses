import re
sequence = input()
patern = r"(^|(?<=\s))-?([0]|[1-9][0-9]*)(\.\d+)?($|(?=\s))"

matches = re.finditer(patern, sequence)

for match in matches:
    print(match.group(), end=" ")