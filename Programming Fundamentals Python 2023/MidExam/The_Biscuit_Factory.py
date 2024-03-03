import math
biscuits_per_worker = int(input())
count_of_workers = int(input())
competitor_per_month = int(input())
produce = 0

daily = biscuits_per_worker * count_of_workers

for day in range(30):
    if day % 3 == 0:
        percent = math.floor(daily*0.75)
        produce += percent
    else:
        produce += daily

print(f"You have produced {produce} biscuits for the past month.")

if competitor_per_month < produce:
    compare = produce - competitor_per_month
    compare = (compare/competitor_per_month) * 100
    print(f"You produce {compare:.2f} percent more biscuits.")
else:
    compare = competitor_per_month - produce
    compare = (compare / competitor_per_month) * 100
    print(f"You produce {compare:.2f} percent less biscuits.")
