number = int(input())
for current_number in range(1111, 9999 + 1):
    current_number_as_string = str(current_number)
    current_number_is_special = True
    for current_digit in current_number_as_string:
        # current_number  не е специално, когато current_digit = 0 или number се дели на current_digit с остатък
        if int(current_digit) == 0 or number % int(current_digit) != 0:
            current_number_is_special = False
            break
    if current_number_is_special:
        print(current_number_as_string, end=" ")