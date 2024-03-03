students = int(input())
r1 = 0
r2 = 0
r3 = 0
r4 = 0
avg = 0

for i in range (students):
    grade = float(input())
    avg += grade
    if grade >= 5.00:
        r1 +=1

    elif 4.00 <= grade < 5.00:
        r2 += 1

    elif 3.00 <= grade < 4.00:
        r3 += 1

    elif grade < 3.00:
        r4 += 1


print(f"Top students: {(r1/students)*100:.2f}%")
print(f"Between 4.00 and 4.99: {(r2/students)*100:.2f}%")
print(f"Between 3.00 and 3.99: {(r3/students)*100:.2f}%")
print(f"Fail: {(r4/students)*100:.2f}%")
print(f"Average: {avg/students:.2f}")
