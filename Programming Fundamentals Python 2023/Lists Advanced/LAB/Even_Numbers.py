numbers = list(map(int, input().split(", ")))

found = map(lambda x: x if numbers[x]%2 ==0 else "no",range(len(numbers)))
evens = list(filter(lambda y: y != "no",found))

print(evens)