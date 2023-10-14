employees = input().split(" ")
happiness = int(input())

employees = list(map(lambda x: int(x)*happiness,employees))
filter_employees = list(filter(lambda x: x>=sum(employees) / len(employees),employees))

if len(filter_employees)>=len(employees)/2:
    print(f"Score: {len(filter_employees)}/{len(employees)}. Employees are happy!")
else:
    print(f"Score: {len(filter_employees)}/{len(employees)}. Employees are not happy!")