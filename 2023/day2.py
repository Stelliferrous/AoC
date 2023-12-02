
colorMaxes = {
	'red': 12,
	'green': 13,
	'blue': 14,
}

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
gameSuccesses, gameFails,gameIDsTotal = 0, 0, 0
for gameEntry in games:
	for gameKey, gameOutcome in gameEntry.items():
		gameSuccess = True
		for gameResult in gameOutcome:
			for colorCube, colorCount in gameResult.items():
				colorMax = colorMaxes.get(colorCube)
				if colorCount > colorMax:
					gameSuccess = False
					print(f"High number detected for {colorCube} in {gameKey}: {colorCount}")

		if gameSuccess:
			print(f"{gameKey} is considered a win")
			gameSuccesses += 1
			gameIDsTotal += int(gameKey.split(" ")[1])
			print(f"Current total Game IDs added up: ", gameIDsTotal)
		else:
			gameFails += 1
			print(f"{gameKey} is considered a fail")



print("Game Successes:", gameSuccesses)
print("Game Fails:", gameFails)
print("Sum of Game ID Successes:", gameIDsTotal)
# print(games)