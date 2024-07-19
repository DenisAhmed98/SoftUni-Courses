company_users = {}

def checker(dict, value, company):
    for key, ids in company_users.items():
        if key == company:
            for i in range(len(ids)):
                if value == ids[i]:
                    return True
    return False


while True:
    command = input().split(" -> ")
    if command[0] == "End":
        break
    else:
        company, userid = command[0], command[1]

    if company not in company_users:
        company_users[company] = []

    company_values = company_users.values()
    if checker(company_users, userid, company) == False:
        company_users[company].append(userid)

for key, value in company_users.items():
    print(f"{key}")
    for i in range(len(value)):
        print(f"-- {value[i]}")