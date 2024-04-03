from itertools import permutations

def possible_permutations(elements):
    for n in permutations(elements):
        yield list(n)

[print(n) for n in possible_permutations([1, 2, 3])]
[print(n) for n in possible_permutations([1])]
