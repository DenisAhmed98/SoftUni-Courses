month = input()
stays = int(input())
studio = 0
apartment = 0


if month == "May" or month == "October":
    if 7 < stays < 15:
        studio = 50-(50*0.05)
        apartment = 65
    elif stays > 14:
        studio = 50-(50*0.3)
        apartment = 65-(65*0.1)
    else:
        studio = 50
        apartment = 65
elif month == "June" or month == "September":
    if stays > 14:
        studio = 75.20 - (75.20 * 0.2)
        apartment = 68.70 - (68.70 * 0.1)
    else:
        studio = 75.20
        apartment = 68.70
elif month == "July" or month == "August":
    if stays > 14:
        studio = 76
        apartment = 77 - (77 * 0.1)
    else:
        studio = 76
        apartment = 77

print(f"Apartment: {stays*apartment:.2f} lv.")
print(f"Studio: {stays*studio:.2f} lv.")