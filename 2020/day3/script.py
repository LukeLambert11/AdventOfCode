
grid = []

with open('input.txt', 'r') as file: 
	for line in file: 
		grid.append(line.strip())

N = len(grid)
M =	len(grid[0])

def check(dc, dr): 

	counter = 0 
	c = 0

	for r in range(0, N, dr): 

		if grid[r][c] == '#': 
			counter += 1

		c = (c + dc) % M

	return counter

print(check(1, 1) * check(3, 1) * check(5, 1) * check(7, 1) * check(1, 2)) 
	
