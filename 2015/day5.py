
def numberVowels(line):
	vowels = "aeiou"
	vowelCount = 0
	for char in line:
		if char in vowels:
			vowelCount += 1
	if vowelCount >= 3:
		return True
	else:
		return False

def isDouble(line):
	curLetter = str("!")
	for char in line:
		if curLetter == char:
			return True
			break
		else:
			curLetter = char
	return False

def badCombos(line):
	bad = ["ab", "cd", "pq", "xy"]
	curLetter = str("!")
	for char in line:
		if curLetter + char in bad:
			return False
			break
		else:
			curLetter = char
	return True




with open('day5-input.txt', 'r') as file:
	goodStrings = 0
	lineCount = 0
	for line in file:
		lineCount += 1
		print("Line Number: ", lineCount)
		print("Number of Vowels: ", numberVowels(line))
		print("Doubles exist: ", isDouble(line))
		print("No bad Combos: ", badCombos(line))
		if badCombos(line) and isDouble(line) and numberVowels(line):
			goodStrings += 1

	print("Total Good Strings: ", goodStrings)