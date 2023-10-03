hour_of_exam = int(input())
minutes_of_exam = int(input())
hour_of_arriving = int(input())
minutes_of_arriving = int(input())
time_of_exam = hour_of_exam * 60 + minutes_of_exam
time_of_arriving = hour_of_arriving * 60 + minutes_of_arriving
if time_of_arriving > time_of_exam:
    print("Late")
elif time_of_exam - 30 <= time_of_arriving <= time_of_exam:
    print("On time")
elif time_of_exam - 30 > time_of_arriving:  # else
    print("Early")
difference = abs(time_of_exam - time_of_arriving)
hours = difference // 60
minutes = difference % 60
if time_of_exam - 60 < time_of_arriving < time_of_exam:
    print(f"{minutes} minutes before the start")
elif time_of_arriving <= time_of_exam - 60:
    # if minutes < 10:
    #     print(f"{hours}:0{minutes} hours before the start")
    # else:
    #     print(f"{hours}:{minutes} hours before the start")
    print(f"{hours}:{minutes:02d} hours before the start")
elif time_of_exam < time_of_arriving < time_of_exam + 60:
    print(f"{minutes} minutes after the start")
elif time_of_arriving >= time_of_exam + 60:
    print(f"{hours}:{minutes:02d} hours after the start" )