
nav = []

with open('input.txt','r') as file: 

	for line in file: 
		line = line.strip()
		command = line[0]
		unit = int(line[1:])
		nav.append((command, unit))

degreeToDir = {0: (1, 0), 90: (0, 1), 180: (-1, 0), 270: (0, -1)}

def Part1(nav): 

	x, y = 0, 0 

	for command, unit in nav: 
		dx, dy = degreeToDir[currDir]

		if command == 'F': 
			x += unit * dx
			y += unit * dy 
		elif command == 'N': 
			y += unit
		elif command == 'S': 
			y -= unit
		elif command == 'E': 
			x += unit 
		elif command == 'W': 
			x -= unit 
		elif command == 'L': 
			currDir = (currDir + unit) % 360
		elif command == 'R': 
			currDir = (currDir - unit) % 360

	return abs(x) + abs(y)


def rotateRight(x, y, degrees): 

	iters = degrees // 90
	for _ in range(iters): 
		x, y = y, -x

	return [x, y]


def Part2(nav): 

	x, y = 0, 0 
	wayPoint = [10, 1]
	currDir = 0

	for command, unit in nav: 
		dx, dy = degreeToDir[currDir]

		if command == 'F': 
			x += wayPoint[0] * unit
			y += wayPoint[1] * unit 
		elif command == 'N': 
			wayPoint[1] += unit
		elif command == 'S': 
			wayPoint[1] -= unit
		elif command == 'E': 
			wayPoint[0] += unit 
		elif command == 'W': 
			wayPoint[0] -= unit 
		elif command == 'L': 
			wayPoint = rotateRight(wayPoint[0], wayPoint[1], 360 - unit)
		elif command == 'R': 
			wayPoint = rotateRight(wayPoint[0], wayPoint[1], unit)

	return abs(x) + abs(y)

#print(Part1(nav))
print(Part2(nav))
