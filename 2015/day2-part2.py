totalRibbon = 0
with open('day2-input.txt', 'r') as file:
	for line in file:
		l, w, h = map(int, line.strip().split('x'))
		twoSmallest = sorted([l, w, h])[:2]
		totalRibbon += l * w * h + twoSmallest[0] + twoSmallest[0] + twoSmallest[1] + twoSmallest[1]
print(totalRibbon)