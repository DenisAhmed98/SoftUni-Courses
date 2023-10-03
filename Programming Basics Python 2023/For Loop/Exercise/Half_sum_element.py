from sys import maxsize
nums = int(input())
maximum = -maxsize
sum = 0
for i in range(nums):
    new = int(input())
    if maximum<new:
        maximum = new
    sum +=new

if maximum == sum - maximum:
    print("Yes")
    print("Sum =",maximum)
else:
    print("No")
    sum = sum - maximum
    print("Diff =",abs(maximum-sum))