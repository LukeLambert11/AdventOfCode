from functools import cache
grid = []


with open('input.txt', 'r') as file: 
	for line in file: 
		line = line.strip()
		grid.append(line)

M, N = len(grid), len(grid[0])
def Part1(): 
	beams = set()
	startIndex = grid[0].find('S')
	beams.add(startIndex)
	splits = 0

	for row in grid[1:]: 
		nBeams = beams.copy()
		splitters = [i for i, n in enumerate(row) if n == '^']

		for index in splitters: 
			if index in beams: 
				splits += 1
				nBeams.remove(index)
				nBeams.add(index-1)
				nBeams.add(index+1)
		beams = nBeams

	return splits

def Part2(): 

	@cache
	def recur(r, c): 

		if r == M-1: 
			return 1

		if grid[r+1][c] != '^': 
			return recur(r+1, c)
		
		return recur(r+1, c-1) + recur(r+1, c+1)

	startCol = grid[0].find('S')
	return recur(0, startCol)





print(Part1())
print(Part2())