names = input()

while names != "Welcome!":
    if names == "Voldemort":
        print("You must not speak of that name!")
        break
    elif len(names) < 5:
        print(f"{names} goes to Gryffindor.")
    elif len(names) == 5:
        print(f"{names} goes to Slytherin.")
    elif len(names) == 6:
        print(f"{names} goes to Ravenclaw.")
    else:
        print(f"{names} goes to Hufflepuff.")

    names = input()
else:
    print("Welcome to Hogwarts.")

