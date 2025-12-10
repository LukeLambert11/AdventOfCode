lightPatterns = []
buttons = []
joltages = []

with open('input.txt', 'r') as file: 
	for line in file: 
		line = line.strip()
		line = line.split(' ')
		
		light = line[0][1:-1]
		lightIndexs = [i for i, n in enumerate(light) if n == '#']
		lightPatterns.append(lightIndexs)

		currButtons = line[1:-1]
		for i in range(len(currButtons)): 
			b = currButtons[i]
			b = b[1:-1].split(',')
			b = list(map(int, b))
			currButtons[i] = b

		buttons.append(currButtons)

		jol = line[-1][1:-1]
		jol = list(map(int, jol.split(',')))
		joltages.append(jol)




def F(target, curr, index, buttons): 

	if curr == target: 
		return 0 

	if index == len(buttons): 
		return 10 ** 10 

	skip = F(target, curr, index+1, buttons)

	toggled = curr ^ set(buttons[index])
	take = 1 + F(target, toggled, index+1, buttons)

	return min(skip, take)


def Part1(): 

	ans = 0

	for lightPattern, currButtons in zip(lightPatterns, buttons): 
		ans += F(set(lightPattern), set(), 0, currButtons)

	return ans 


def G(joltage, currButtons): 



def Part2(): 
	ans = 0

	for joltage, currButtons in zip(joltages, buttons): 
		G(joltage, currButtons)

	return ans



print(Part1())
