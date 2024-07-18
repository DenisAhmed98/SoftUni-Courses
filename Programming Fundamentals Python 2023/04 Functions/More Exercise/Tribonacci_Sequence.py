def tribonachi(sequence):
    tempA = 1
    tempB = 0
    tempC = 0
    for x in range(0,sequence):
        result = tempA+tempB+tempC
        tempA = tempB
        tempB = tempC
        tempC = result
        print(result, end=" ")

sequence = int(input())
tribonachi(sequence)