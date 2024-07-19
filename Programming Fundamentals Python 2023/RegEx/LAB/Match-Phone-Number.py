import re
numbers = input()
patern = r"\+359-2-\d{3}-\d{4}\b|\+359 2 \d{3} \d{4}\b"

matches = re.findall(patern, numbers)
print(", ".join(matches))