from math import sqrt

def get_primes(numbers):
    for num in numbers:
        if num <= 1:
            continue

        for div in range(2, int(sqrt(num)+1)):
            if num % div == 0:
                break
        else:
            yield num

print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))
print(list(get_primes([-2, 0, 0, 1, 1, 0])))
