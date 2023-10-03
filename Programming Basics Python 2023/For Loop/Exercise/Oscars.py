actor = input()
academy_points = float(input())
jury = int(input())


for i in range (jury):
	jury_name = input()
	jury_points = float(input())
	
	academy_points = academy_points + ((len(jury_name)*jury_points)/2)
	
	if academy_points >=1250.5:
		break

if academy_points <1250.5:
	print(f"Sorry, {actor} you need {1250.5-academy_points} more!")
else:
	print(f"Congratulations, {actor} got a nominee for leading role with {academy_points:.1f}!")