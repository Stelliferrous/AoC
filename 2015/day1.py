floor, levelChange, searchBasement = 0, 0, False
with open('day1-input.txt', 'r') as file:
	for string in file:
		char = 0
		for character in string:
			if character == "(":
				levelChange = 1
				print("Up")
			elif character == ")":
				levelChange = -1
				print("Down")
			else:
				print("Invalid Character")
			floor += levelChange
			char += 1
			if floor == -1 and searchBasement:
				print("First basement at Floor: ", char)
				exit()
print("Final Floor: ", floor)