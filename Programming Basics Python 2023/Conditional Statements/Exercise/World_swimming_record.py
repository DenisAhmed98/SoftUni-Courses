import math
record_seconds = float(input())
length = float(input())
meter_per_second = float(input())

swim = length * meter_per_second
addition = length // 15 * 12.5

total_time = swim + addition

if record_seconds>total_time:
    print(f"Yes, he succeeded! The new world record is {'%.2f'%total_time} seconds.")
else:
    print(f"No, he failed! He was {'%.2f'%(total_time - record_seconds)} seconds slower.")