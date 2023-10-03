budget = float(input())
season = input()
destination = ""
rest_type = ""
spent_sum = 0
if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        spent_sum = budget * 0.3
    elif season == "winter":
        spent_sum = budget * 0.7
elif budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        spent_sum = budget * 0.4
    elif season == "winter": 
        spent_sum = budget * 0.8
else:
    destination = "Europe"
    spent_sum = budget * 0.9
if season == "summer" and destination != "Europe":
    rest_type = "Camp"
else: 
    rest_type = "Hotel"
print(f"Somewhere in {destination}")
print(f"{rest_type} - {spent_sum:.2f}")