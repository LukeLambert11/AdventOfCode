
import math

buses = []
with open('input.txt', 'r') as file: 
	file = list(file)

	leaveTime = int(file[0])


	for b in file[1].split(','): 
		b = int(b) if b != 'x' else -1
		buses.append(b)

def part1(buses, leaveTime): 
	early = 10 ** 10 
	bNum = -1

	for b in buses: 
		if b == -1: 
			continue 

		times = math.ceil(leaveTime / b)
		if early > times * b: 
			early = times * b
			bNum = b

	return (early - leaveTime) * bNum

def part2(buses): 

	time = 100000000000000
	step = 1 

	for offset, bus in enumerate(buses): 

		if bus == -1: 
			continue 

		while (time + offset) % bus != 0: 
			time += step

		step = math.lcm(step, bus)

	return time
	


#print(part1(buses, leaveTime))

print(part2(buses))


