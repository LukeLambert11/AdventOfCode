from collections import defaultdict
tiles = []

with open('input.txt', 'r') as file: 
	for line in file: 
		line = line.strip()
		point = list(map(int, line.split(',')))
		tiles.append(point)

N = len(tiles)

def Part1(): 

	ans = 0 

	for i in range(N): 
		x1, y1 = tiles[i]
		for j in range(i+1, N): 
			x2, y2 = tiles[j]

			dx = (x1 - x2 + 1)
			dy = (y1 - y2 + 1)

			ans = max(ans, abs(dx * dy))

	return ans 


def CheckCoord(x, y, xToY, yToX): 
	# run through in 2's to check left, right and top, bottom 



def Part2(): 

	xToY = defaultdict(list)
	yToX = defaultdict(list)

	for y, x in tiles: 
		xToY[x].append(y)
		yToX[y].append(x)

	for l in xToY.values(): l.sort()
	for l in yToX.values(): l.sort()

	ans = 0 

	for i in range(N): 
		x1, y1 = tiles[i]
		for j in range(i+1, N): 
			x2, y2 = tiles[j]

			dx = abs(x1 - x2 + 1)
			dy = abs(y1 - y2 + 1)
			area = dx * dy

			if area <= ans: 
				continue 

			# check the two other coords 
			if CheckCoord(x1, y2, xToY, yToX) and CheckCoord(x2, y1, xToY, yToX): 
				ans = area 

	return ans


print(Part2())