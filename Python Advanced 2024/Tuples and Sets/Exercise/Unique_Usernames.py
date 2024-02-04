count = int(input())
unique = set()

for c in range(count):
    name = input()
    unique.add(name)

for n in unique:
    print(n)