nums = int(input())
left = 0
right = 0
for i in range(nums):
    new = int(input())
    left += new

for i in range(nums):
    new = int(input())
    right += new

if left == right:
    print("Yes, sum =",left)
else:
    print("No, diff =",abs(left-right))
