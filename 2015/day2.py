totalPaper = 0
with open('day2-input.txt', 'r') as file:
	for line in file:
		l, w, h = map(int, line.strip().split('x'))
		lw = l * w
		hl = h * l
		wh = w * h
		lowest = min(lw, hl, wh)
		totalPaper += 2 * lw + 2 * hl + 2 * wh + lowest
print(totalPaper)