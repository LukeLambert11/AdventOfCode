
validRanges = []
ids = []
seenSpace = False 

with open('input.txt', 'r') as file: 
	for line in file: 
		line = line.strip()
		if line == '': 
			seenSpace = True
			continue

		if not seenSpace: 
			a, b = map(int, line.split('-'))
			validRanges.append((a, b))
		else: 
			ids.append(int(line))

def Part1(): 

	freshCount = 0 

	for id in ids: 
		for a, b in validRanges: 
			if a <= id <= b: 
				freshCount += 1
				break

	return freshCount

def Part2(): 

	validRanges.sort(key = lambda x: (x[0], -x[1]))

	currStart, currEnd = validRanges[0]
	ans = 0
	
	for start, end in validRanges[1:]: 
		
		if end < currEnd: 
			continue 

		if currEnd < start: 
			ans += currEnd - currStart + 1
			currStart = start
			 

		currEnd = end 

	ans += currEnd - currStart + 1
	return ans


	
print(Part1())
print(Part2())