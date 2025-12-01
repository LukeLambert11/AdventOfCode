dirs = []

with open('input.txt', 'r') as file: 
	for line in file: 
		line = line.strip()
		d = line[0]
		val = int(line[1:])
		if d == 'L': 
			val = -val
		dirs.append(val)


def Part1(dirs): 
	zeroLand = 0 
	dial = 50

	for d in dirs: 
		dial = (dial + d) % 100

		if dial == 0: 
			zeroLand += 1

	return zeroLand

def Part2(dirs): 
	zeroPass = 0 
	dial = 50 

	for d in dirs: 

		rawDial = dial + d 
		# if 0 is reached or passed need to count
		if rawDial <= 0 and dial != 0: 
			zeroPass += 1
		
		zeroPass += abs(rawDial) // 100
		dial = (dial + d) % 100

	return zeroPass

print(Part1(dirs))
print(Part2(dirs))

		

