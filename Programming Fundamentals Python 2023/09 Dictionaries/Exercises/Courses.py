courses = {}

while True:
    command = input().split(" : ")
    if command[0] == "end":
        break
    else:
        course, student = command[0], command[1]

    if course not in courses:
        courses[course] = []
    courses[course].append(student)

for key, value in courses.items():
    print(f"{key}: {len(value)}")
    for i in range(len(value)):
        print(f"-- {value[i]}")