sentence = input()

sequence = sentence.split(", ")
sequence.reverse()
wolf_position = 1
counter = 1
for word in sequence:
    if word == "wolf":
        wolf_position = counter
    counter +=1
if wolf_position == 1:
    print("Please go away and stop eating my sheep")
else:
    print(f"Oi! Sheep number {wolf_position-1}! You are about to be eaten by a wolf!")