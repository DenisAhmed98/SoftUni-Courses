nums = int(input())
even = 0
odd = 0
for i in range(nums):
    new = int(input())
    if i%2 ==0:
        even += new
    else:
        odd +=new

if even == odd:
    print("Yes")
    print("Sum =",even)
else:
    print("No")
    print("Diff =",abs(even-odd))
