from math import ceil

Name_of_Serial = input()
episode_length = int(input())
break_length = int(input())

lunch_time = break_length / 8
relax_time = break_length / 4
time_left = break_length - lunch_time - relax_time
difference = ceil(abs(time_left - episode_length))

if time_left>=episode_length:
    print(f"You have enough time to watch {Name_of_Serial} and left with {difference} minutes free time.")
else:
    print(f"You don't have enough time to watch {Name_of_Serial}, you need {difference} more minutes.")