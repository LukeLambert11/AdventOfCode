data = []


with open('input.txt', 'r') as file: 
	for line in file: 
		line = line.strip()
		data.append(line)


def Part1(data): 
	
	ans = 0

	for bank in data: 
		first = int(max(bank[:-1]))
		second = int(max(bank[bank.find(str(first))+1:]))
		ans += (first * 10) + second

	return ans





def Part2(data):
	ans = 0 

	for bank in data: 
		stack = []
		for i, n in enumerate(bank): 

			while stack and stack[-1] < n and len(stack) + (len(bank) - i) > 12: 
				stack.pop()

			stack.append(n)
		ans += int(''.join(stack[:12]))

	return ans



print(Part1(data))
print(Part2(data))