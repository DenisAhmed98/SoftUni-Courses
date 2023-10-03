student_tickets = 0
standard_tickets = 0
kid_tickets = 0
movie_name = input()
while movie_name != "Finish":
    free_seats = int(input())
    sold_seats = 0
    for free_ticket in range(free_seats):
        current_ticket = input()
        if current_ticket == "End":
            break
        elif current_ticket == "student":
            student_tickets += 1
        elif current_ticket == "standard":
            standard_tickets += 1
        elif current_ticket == "kid": # else
            kid_tickets += 1
        sold_seats += 1
    percent_full_hall = sold_seats / free_seats * 100
    print(f"{movie_name} - {percent_full_hall:.2f}% full.")
    movie_name = input()
total_sold_tickets = student_tickets + standard_tickets + kid_tickets
percent_student_tickets = student_tickets / total_sold_tickets * 100
percent_standard_tickets = standard_tickets / total_sold_tickets * 100
percent_kid_tickets = kid_tickets / total_sold_tickets * 100
print(f"Total tickets: {total_sold_tickets}")
print(f"{percent_student_tickets:.2f}% student tickets.")
print(f"{percent_standard_tickets:.2f}% standard tickets.")
print(f"{percent_kid_tickets:.2f}% kids tickets.")