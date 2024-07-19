words = input().split(" ")
dictionary = {}

for w in words:
    w_ins = w.lower()
    if w_ins not in dictionary:
        dictionary[w_ins] = 1
    else:
        dictionary[w_ins] += 1

for key, value in dictionary.items():
    if value % 2 != 0:
        print(key, end=" ")