line_one = list(map(int, input().split(" ")))
line_two = list(map(int, input().split(" ")))
line_three = list(map(int, input().split(" ")))

if line_one[0] == 1 and line_two[0] == 1 and line_three[0] == 1:
    print("First player won")
elif line_one[1] == 1 and line_two[1] == 1 and line_three[1] == 1:
    print("First player won")
elif line_one[2] == 1 and line_two[2] == 1 and line_three[2] == 1:
    print("First player won")
elif line_one[0] == 1 and line_two[1] == 1 and line_three[2] == 1:
    print("First player won")
elif line_one[2] == 1 and line_two[1] == 1 and line_three[0] == 1:
    print("First player won")
elif line_one[0] == 1 and line_one[1] == 1 and line_one[2] == 1:
    print("First player won")
elif line_two[0] == 1 and line_two[1] == 1 and line_two[2] == 1:
    print("First player won")
elif line_three[0] == 1 and line_three[1] == 1 and line_three[2] == 1:
    print("First player won")

elif line_one[0] == 2 and line_two[0] == 2 and line_three[0] == 2:
    print("Second player won")
elif line_one[1] == 2 and line_two[1] == 2 and line_three[1] == 2:
    print("Second player won")
elif line_one[2] == 2 and line_two[2] == 2 and line_three[2] == 2:
    print("Second player won")
elif line_one[0] == 2 and line_two[1] == 2 and line_three[2] == 2:
    print("Second player won")
elif line_one[2] == 2 and line_two[1] == 2 and line_three[0] == 2:
    print("Second player won")
elif line_one[0] == 2 and line_one[1] == 2 and line_one[2] == 2:
    print("Second player won")
elif line_two[0] == 2 and line_two[1] == 2 and line_two[2] == 2:
    print("Second player won")
elif line_three[0] == 2 and line_three[1] == 2 and line_three[2] == 2:
    print("Second player won")

else:
    print("Draw!")