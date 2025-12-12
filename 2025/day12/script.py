
presents = {}
regions = []


with open('input.txt', 'r') as file: 

	buildingP = True 
	currPresent = ''
	index = 0

	for line in file: 
		line = line.strip()
		
		if 'x' in line: 
			buildingP = False

		if line == '': 
			presents[index] = currPresent
			currPresent = ''
			index += 1 
			continue 

		if buildingP: 

			if line.startswith(str(index)):
				continue 
			currPresent += line

		else: 

			size, p = line.split(': ')
			size = list(map(int, size.split('x')))
			p = list(map(int, p.split(' ')))
			regions.append((size, p))



def Part1(): 
	ans = 0

	for (N, M), p in regions: 
		area = N * M

		requiredArea = 0
		for i, n in enumerate(p): 
			currP = presents[i]
			requiredArea += (n * currP.count('#'))

		if requiredArea < area: 
			ans += 1

	return ans





print(Part1())




