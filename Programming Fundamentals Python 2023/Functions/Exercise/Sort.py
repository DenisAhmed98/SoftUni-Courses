numbers_as_string = input().split()
numbers_as_digits = []

for number in numbers_as_string:
    numbers_as_digits.append(int(number))

result = list(sorted(numbers_as_digits))
print(result)