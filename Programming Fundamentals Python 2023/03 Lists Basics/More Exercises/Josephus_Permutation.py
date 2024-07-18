#finished in 1h15min
circle_of_numbers = list(map(int, input().split(" ")))
length_of_circle = len(circle_of_numbers)
executor = int(input())
executed = []
pointer = 1
number_of_kill = 1

while length_of_circle != 0:


    if pointer > length_of_circle:
        pointer = 1
    if pointer == length_of_circle:
        if number_of_kill % executor == 0:
            if pointer - 1 < 0:
                pointer = length_of_circle + 1
            executed.append(circle_of_numbers[pointer - 1])
            circle_of_numbers.pop(pointer - 1)
            number_of_kill = 1
            length_of_circle -= 1
            pointer = 1
    if number_of_kill % executor == 0:
        if pointer-1 < 0:
            pointer = length_of_circle + 1
        executed.append(circle_of_numbers[pointer-1])
        circle_of_numbers.pop(pointer-1)
        number_of_kill = 0
        length_of_circle -= 1
        pointer-=1
    pointer += 1
    number_of_kill += 1

print(f"[{','.join(str(x) for x in executed)}]")
