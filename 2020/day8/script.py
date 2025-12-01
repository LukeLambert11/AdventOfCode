
instructions = []

with open('input.txt', 'r') as file: 
	for line in file: 
		instruction, val = line.split(' ')
		instructions.append((instruction, int(val)))


def part1(instructions): 
	visited = set()
	i = 0 
	accumulator = 0

	while i not in visited: 
		instruction, val = instructions[i]
		visited.add(i)


		if instruction == 'jmp': 
			i += val
		elif instruction == 'acc': 
			accumulator += val
			i += 1
		else: 
			i += 1

	return accumulator

def check(instructions): 
	visited = set()
	i = 0 
	accumulator = 0

	while i not in visited: 


		if i == len(instructions): 
			return accumulator

		instruction, val = instructions[i]
		visited.add(i)

		if instruction == 'jmp': 
			i += val
		elif instruction == 'acc': 
			accumulator += val
			i += 1
		else: 
			i += 1

	return None


def part2(instructions): 

	for i, (instruction, val) in enumerate(instructions): 
		if instruction == 'acc': 
			continue 

		updated = instructions.copy()
		updated[i] = ('jmp', val) if instruction == 'nop' else ('nop', val)
		isValid = check(updated)
		if isValid: 
			return isValid

	return -1


print(part1(instructions))
print(part2(instructions))

