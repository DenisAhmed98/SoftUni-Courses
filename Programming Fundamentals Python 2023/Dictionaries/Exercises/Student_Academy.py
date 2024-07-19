def average_grade(values):
    grade = 0
    for n in range(len(values)):
        grade += values[n]

    grade /= len(values)
    return grade

number_commands = int(input())
student_register = {}

for num in range(number_commands):
    student = input()
    grade = float(input())

    if student not in student_register.keys():
        student_register[student] = []
    student_register[student].append(grade)

for key, value in student_register.items():
    avg = average_grade(value)
    if avg >= 4.50:
        print(f"{key} -> {avg:.2f}")