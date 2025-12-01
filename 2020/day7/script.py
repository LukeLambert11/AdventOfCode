from collections import defaultdict

parents = defaultdict(list)
children = defaultdict(list)



with open('input.txt', 'r') as file: 
	for line in file: 

		s = line.split('contain')
		parentBag = ' '.join(s[0].split(' ')[:2])

		for child in s[1].split(','): 
			child = child.strip()
			child = child.split(' ')
			
			if child[0] == 'no':
				continue 

			childCount = int(child[0])
			childName = ' '.join(child[1:3])

			parents[childName].append(parentBag)
			children[parentBag].append((childName, childCount))



def part1(parents): 

	s = set()

	def dfs(curr): 
		for par in parents[curr]: 
			if par not in s: 
				s.add(par)
				dfs(par)

	dfs('shiny gold')
	return len(s)

def part2(children): 

	def dfs(curr): 

		count = 0
		for childName, childCount in children[curr]: 
			count += childCount * dfs(childName)

		return 1 + count

	return dfs('shiny gold') - 1

print('part1', part1(parents))
print('part2', part2(children))