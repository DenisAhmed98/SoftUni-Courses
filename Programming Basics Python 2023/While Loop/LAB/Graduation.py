student = input()
years = 1
avg = 0
fail = 0
while years<=12:
    grade = float(input())
    if grade >= 4.00:
        avg += grade
        years += 1
    else:
        fail +=1
        if fail == 2:
            break

if fail == 2:
    print(f"{student} has been excluded at {years} grade")
else:
    print(f"{student} graduated. Average grade: {avg/12:.2f}")



