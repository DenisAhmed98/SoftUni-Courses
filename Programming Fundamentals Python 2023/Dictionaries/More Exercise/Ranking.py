contests = {}
participants = {}

while True:
    contest_input = input()
    if contest_input == "end of contests":
        break
    else:
        contest, password = contest_input.split(":")
        contests[contest] = password

while True:
    command = input()
    if command == "end of submissions":
        best_user = ""
        best_points = 0
        for key, value in participants.items():
            points_temp = 0
            for language, points in value.items():
                points_temp += points
            if best_points < points_temp:
                best_user = key
                best_points = points_temp
        print(f"Best candidate is {best_user} with total {best_points} points.")
        print("Ranking:")
        sorted_dict = dict(sorted(participants.items()))
        for key, value in sorted_dict.items():
            print(key)
            sorted_values = dict(sorted(value.items(), key=lambda x: x[1],reverse=True))
            for language, points in sorted_values.items():
                print(f'#  {language} -> {points}')
        break

    contest, password, username, points = command.split("=>")
    if contest in contests and password == contests[contest]:
        if username not in participants:
            participants[username] = {}
            participants[username][contest] = int(points)
        elif contest not in participants[username]:
            participants[username][contest] = int(points)
        elif participants[username][contest] < int(points):
            participants[username][contest] = int(points)
