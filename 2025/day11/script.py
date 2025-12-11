from functools import cache
graph = {}

with open('input.txt', 'r') as file: 
	for line in file: 
		line = line.strip()

		line = line.split(' ')
		par = line[0][:-1]
		graph[par] = line[1:]


def Part1(): 

	def dfs(curr): 

		if curr == 'out': 
			return 1

		ans = 0 
		for nei in graph[curr]: 
			ans += dfs(nei)

		return ans 

	return dfs('you')


def Part2():

	@cache
	def dfs(curr, fft, dac): 

		if curr == 'out': 
			return fft and dac

		ans = 0 
		for nei in graph[curr]: 
			ans += dfs(nei, fft or nei == 'fft', dac or nei == 'dac')


		return ans 

	return dfs('svr', False, False)


print(Part1())
print(Part2())