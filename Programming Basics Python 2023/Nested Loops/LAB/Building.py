stories = int(input())
rooms_per_storie = int(input())
top = stories
for floors in reversed(range (1,stories+1)):
    room_type = "A" if floors % 2 else "O"
    if floors == stories:
        room_type = "L"

    for rooms in range (rooms_per_storie):
        room_name = f"{room_type}{floors}{rooms}"
        print(room_name, end=" ")
    print()

