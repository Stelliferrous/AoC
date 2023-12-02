
def move(direction,location):
	x, y = map(int, location.split(','))
	y += 1 if direction == "^" else 0
	y += -1 if direction == "v" else 0
	x += 1 if direction == ">" else 0
	x += -1 if direction == "<" else 0
	return f"{x},{y}"

with open('day3-input.txt', 'r') as file:
	grid = ["0,0"]
	currentLocation = "0,0"
	for line in file:
		for char in line:
			newLocation = move(char,currentLocation)
			grid.append(newLocation)
			currentLocation = newLocation

print(len(set(grid)))
