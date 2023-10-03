bad_grades = int(input())
avg = 0
counter = 0
last_problem = ""
failed_times = 0
failed = False
problem = input()
while problem !="Enough":
    grade = int(input())
    if grade <= 4:
        failed_times+=1
        if failed_times == bad_grades:
            failed = True
            break
    avg += grade
    counter +=1
    last_problem = problem
    problem = input()

if failed:
    print(f"You need a break, {bad_grades} poor grades.")
else:
    print(f"Average score: {avg/counter:.2f}")
    print(f"Number of problems: {counter}")
    print(f"Last problem: {last_problem}")