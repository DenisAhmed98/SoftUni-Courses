strings = input().split(" ")
result_string = ""

for w in strings:
    length = len(w)
    result_string += w * length

print(result_string)
