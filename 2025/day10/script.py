lightPatterns = []
buttons = []

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



def Part1(): 

	ans = 0

	for lightPattern, button in zip(lightPattern, button): 


		# count number of button presses needed


	return ans 



def Part2(): 
	pass


print(Part1())
