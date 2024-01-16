count = int(input())
students = {}
for _ in range(count):
    student, grade = tuple(input().split())
    grade = float(grade)
    if student not in students:
        students[student] = []
    students[student].append(grade)

for key, value in students.items():
    avg = sum(value) / len(value)
    fromated_grades = f"{' '.join([f'{g:.2f}' for g in value])}"
    print(f"{key} -> {fromated_grades} (avg: {avg:.2f})")

