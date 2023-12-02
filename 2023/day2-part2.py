

def getGameData():
	data = []
	with open('day2-input.txt', 'r') as file:
	    for line in file:
	        line = line.strip().split(': ')
	        gameID = line[0]
	        items = line[1].split('; ')
	        
	        gameResults = {gameID: []}
	        for item in items:
	            itemDict = {}
	            pairs = item.split(', ')
	            for pair in pairs:
	                value, key = pair.split()
	                itemDict[key] = int(value)
	            gameResults[gameID].append(itemDict)
	        
	        data.append(gameResults)
	return data

games = getGameData()
allTheTotals = 0

for gameEntry in games:
	for gameKey, gameOutcome in gameEntry.items():
		reds, greens, blues = [],[],[]
		for gameResult in gameOutcome:
			for colorCube, colorCount in gameResult.items():
				if colorCube == 'red':
					reds.append(colorCount)
				if colorCube == 'green':
					greens.append(colorCount)
				if colorCube == 'blue':
					blues.append(colorCount)
		maxReds = max(reds)
		maxGreens = max(greens)
		maxBlues = max(blues)
		colorMultiplier = maxReds * maxGreens * maxBlues
		allTheTotals += colorMultiplier
		print(f"Highest number of Reds {maxReds} for {gameKey}")
		print(f"Highest number of Greens {maxGreens} for {gameKey}")
		print(f"Highest number of Blues {maxBlues} for {gameKey}")
		print(f"Highest color count multiplied together for {gameKey} is {colorMultiplier}")
		print(f"Running sum of multiplied colors {allTheTotals}")


print(f"Final total of all whatevers {allTheTotals}")



				# for count in colorCube['green']:
				# 	print(f"Result {count} for {gameKey}")





# 				colorMax = colorMaxes.get(colorCube)
# 				if colorCount > colorMax:
# 					gameSuccess = False
# 					print(f"High number detected for {colorCube} in {gameKey}: {colorCount}")

# 		if gameSuccess:
# 			print(f"{gameKey} is considered a win")
# 			gameSuccesses += 1
# 			gameIDsTotal += int(gameKey.split(" ")[1])
# 			print(f"Current total Game IDs added up: ", gameIDsTotal)
# 		else:
# 			gameFails += 1
# 			print(f"{gameKey} is considered a fail")



# print("Game Successes:", gameSuccesses)
# print("Game Fails:", gameFails)
# print("Sum of Game ID Successes:", gameIDsTotal)
# # print(games)