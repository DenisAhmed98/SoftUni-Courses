number_of_guests = int(input())
invitations = set()

for _ in range(number_of_guests):
    guests = input()
    invitations.add(guests)

guests_came = input()
while guests_came != "END":
    invitations.remove(guests_came)
    guests_came = input()

print(len(invitations))
for g in sorted(invitations):
    print(g)