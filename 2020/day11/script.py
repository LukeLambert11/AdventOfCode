import copy 

grid = []

with open('input.txt', 'r') as file: 

	for line in file: 
		line = line.strip()
		grid.append(list(line))

M, N = len(grid), len(grid[0])

def CheckAdj(grid, r, c): 

	numOccupied = 0

	for dr in range(-1, 2): 
		for dc in range(-1, 2): 
			if dr == dc == 0: 
				continue 

			nr, nc = r + dr, c + dc 

			if nr < 0 or nr >= M or nc < 0 or nc >= N: 
				continue 
			if grid[nr][nc] == '#': 
				numOccupied += 1
	return numOccupied

def Check2(grid, r, c): 

	dirs = []

	for dr in range(-1, 2): 
		for dc in range(-1, 2): 
			if dr == dc == 0: 
				continue 
			dirs.append((dr, dc))

	visable = 0

	for dr, dc in dirs: 
		cr, cc = r, c

		while 0 <= cr + dr < M and 0 <= cc + dc < N: 
			cr += dr
			cc += dc 

			if grid[cr][cc] == 'L': 
				break 
			if grid[cr][cc] == '#': 
				visable += 1
				break 

	return visable




def Part1(grid): 

	while True: 

		newGrid = copy.deepcopy(grid)

		for r in range(M): 
			for c in range(N): 
				numAdj = CheckAdj(grid, r, c)
				if grid[r][c] == 'L' and numAdj == 0: 
					newGrid[r][c] = '#'
				elif grid[r][c] == '#' and numAdj >= 4: 
					newGrid[r][c] = 'L'

		if newGrid == grid: 
			break 
		grid = newGrid

	numOccupied = 0 
	for row in grid: 
		numOccupied += row.count('#')

	return numOccupied

def Part2(grid): 

	while True: 

		newGrid = copy.deepcopy(grid)

		for r in range(M): 
			for c in range(N): 
				
				if grid[r][c] == '.': 
					continue 

				numAdj = Check2(grid, r, c)
				
				if grid[r][c] == 'L' and numAdj == 0: 
					newGrid[r][c] = '#'
				elif grid[r][c] == '#' and numAdj >= 5: 
					newGrid[r][c] = 'L'
		print('iter')
		if newGrid == grid: 
			break 
		grid = newGrid

	numOccupied = 0 
	for row in grid: 
		numOccupied += row.count('#')

	return numOccupied



#print(Part1(grid))
print(Part2(grid))




