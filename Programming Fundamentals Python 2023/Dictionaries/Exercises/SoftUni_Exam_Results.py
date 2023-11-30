language_submissions = {}
participants = {}

while True:
    command = input()
    if command == "exam finished":
        break
    else:
        token = command.split("-")
        username = token[0]
        language = token[1]
        if language == "banned":
            participants.pop(username)
        else:
            points = int(token[2])
            if username not in participants:
                participants[username] = 0
            if participants[username] < points:
                participants[username] = points
            if language not in language_submissions:
                language_submissions[language] = 0
            language_submissions[language] += 1

print("Results:")
for key,value in participants.items():
    print(f"{key} | {value}")
print("Submissions:")
for key,value in language_submissions.items():
    print(f"{key} - {value}")

