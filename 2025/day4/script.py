import copy


grid = []

with open('input.txt', 'r') as file: 
	for line in file: 
		line = line.strip()
		grid.append(list(line))

M = len(grid)
N = len(grid[0])


def CountAdj(row, col, grid): 

	dirs = []
	for r in range(-1, 2): 
		for c in range(-1, 2): 
			if r == c == 0: 
				continue
			dirs.append((r, c))

	count = 0 
	for dr, dc in dirs: 
		nr, nc = row + dr, col + dc
		if nr < 0 or nr >= M or nc < 0 or nc >= N or grid[nr][nc] != '@': 
			continue 
		count += 1

	return count


def Part1(grid): 
	ans = 0 
	
	for r in range(M): 
		for c in range(N): 
			
			if grid[r][c] != '@': 
				continue
			
			if CountAdj(r, c, grid) < 4: 
				ans += 1

	return ans


def Part2(grid): 
	ans = 0 
	oldGrid = None

	while oldGrid != grid: 
		oldGrid = copy.deepcopy(grid)

		for r in range(M): 
			for c in range(N): 
				
				if grid[r][c] != '@': 
					continue
				
				if CountAdj(r, c, grid) < 4: 
					grid[r][c] = '.'
					ans += 1

	return ans


print(Part1(grid))
print(Part2(grid))



