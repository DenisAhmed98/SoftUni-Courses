#finished in 16min
race = list(map(int, input().split(" ")))
racer_one = 0
racer_two = 0

finish_line = (len(race) - 1)/2
finish_line = int(finish_line)

for x in range(finish_line):
    if race[x] == 0:
        racer_one *= 0.8
    else:
        racer_one += race[x]

race_reversed = race.reverse()

for y in range (finish_line):
    if race[y] == 0:
        racer_two *= 0.8
    else:
        racer_two += race[y]

if racer_one < racer_two:
    print(f"The winner is left with total time: {racer_one:.1f}")
elif racer_one > racer_two:
    print(f"The winner is right with total time: {racer_two:.1f}")
