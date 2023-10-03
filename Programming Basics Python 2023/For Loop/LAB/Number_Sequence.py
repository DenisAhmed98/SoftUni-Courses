from sys import maxsize
nums = int(input())
minimum = maxsize
maximum = -maxsize
for i in range(nums):
    new = int(input())
    if minimum>new:
        minimum = new
    if maximum<new:
        maximum = new

print("Max number:",maximum)
print("Min number:",minimum)
