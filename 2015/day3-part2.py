
def move(direction,location):
	x, y = map(int, location.split(','))
	y += 1 if direction == "^" else 0
	y += -1 if direction == "v" else 0
	x += 1 if direction == ">" else 0
	x += -1 if direction == "<" else 0
	return f"{x},{y}"

with open('day3-input.txt', 'r') as file:
	grid = ["0,0"]
	currentLocationSanta = "0,0"
	currentLocationRobo = "0,0"
	for line in file:
		lineLength = len(line)
		for char in line:
			if lineLength % 2 == 0:
				newLocation = move(char,currentLocationSanta)
				print("Location Santa: ", newLocation)
				currentLocationSanta = newLocation
			else:
				newLocation = move(char,currentLocationRobo)
				print("Location Robo: ", newLocation)
				currentLocationRobo = newLocation
			lineLength -= 1
			grid.append(newLocation)

print(len(set(grid)))
