from collections import defaultdict
from functools import reduce
from operator import add, mul

data = defaultdict(list)
grid = []

with open('input.txt', 'r') as file: 

	for line in file: 
		grid.append(line.rstrip('\n'))
		line = line.strip()

		line = line.split()

		if line[0].isnumeric(): 
			lineInt = map(int, line)
			for i, n in enumerate(lineInt): 
				data[i].append(n)
		else: 
			ops = line


def Part1(): 
	ans = 0 

	for i, op in enumerate(ops): 
		
		if op == '*': 
			ans += reduce(mul, data[i])
		else: 
			ans += reduce(add, data[i])

	return ans

def Part2():

	ans = 0
	boundries = [i for i, n in enumerate(grid[-1]) if n != ' ']
	boundries.append(len(grid[-1])+1)

	for start, end in zip(boundries, boundries[1:]): 
		group = []
		for col in reversed(range(start, end-1)): 
			curr = ''
			for row in range(len(grid)-1): 
				curr += grid[row][col]
			group.append(int(curr))

		if grid[-1][start] == '*': 
			ans += reduce(mul, group)
		else: 
			ans += reduce(add, group)


	return ans



print(Part1())
print(Part2())