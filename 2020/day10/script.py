from collections import defaultdict

adapters = []

with open('input.txt', 'r') as file: 
	for line in file: 
		adapters.append(int(line))

adapters.append(0)
adapters.sort()
adapters.append(adapters[-1] + 3)

def part1(adapters): 
	F = defaultdict(int)

	for a, b in zip(adapters, adapters[1:]): 
		F[b-a] += 1

	return F[1] * F[3]

def part2(adapters): 

	dp = [0] * len(adapters)
	dp[0] = 1

	for i in range(1, len(adapters)): 

		for j in range(i-1, -1, -1): 
			if adapters[i] - adapters[j] > 3: 
				continue 

			dp[i] += dp[j]

	return dp[-1]

print(part1(adapters))
print(part2(adapters))

