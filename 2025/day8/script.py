import heapq
from collections import defaultdict
from functools import reduce
from operator import mul

data = []

with open('input.txt', 'r') as file: 
	for line in file: 
		line = line.strip()
		nums = line.split(',')
		nums = list(map(int, nums))
		data.append(nums)

N = len(data)


def Distance(a, b): 
	return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2 + (a[2] - b[2]) ** 2


def BuildEdges(): 

	edges = []

	for i in range(N): 
		a = data[i]
		for j in range(i+1, N): 
			b = data[j]
			d = Distance(a, b)
			edges.append((d, i, j))

	
	return sorted(edges)


def Part1(): 

	par = [i for i in range(N)]
	rank = [1] * N

	def Find(n): 
		while n != par[n]: 
			par[n] = par[par[n]]
			n = par[n]
		return n 

	def Union(n1, n2): 
		p1, p2 = Find(n1), Find(n2)

		if p1 == p2: 
			return 

		if rank[p1] < rank[p2]: 
			p1, p2 = p2, p1

		rank[p1] += rank[p2]
		par[p2] = p1
	

	edges = BuildEdges()

	for _, a, b in edges[:1000]: #add back 1000
		Union(a, b)

	groups = {}

	for i in range(N): 
		p = Find(i)
		r = rank[p]
		groups[p] = r

	return reduce(mul, heapq.nlargest(3, groups.values()))


def Part2(): 
	par = [i for i in range(N)]
	rank = [1] * N
	last = ()

	def Find(n): 
		while n != par[n]: 
			par[n] = par[par[n]]
			n = par[n]
		return n 

	def Union(n1, n2): 
		p1, p2 = Find(n1), Find(n2)

		if p1 == p2: 
			return 

		nonlocal last
		last = (n1, n2)
		if rank[p1] < rank[p2]: 
			p1, p2 = p2, p1


		rank[p1] += rank[p2]
		par[p2] = p1
	

	edges = BuildEdges()

	for _, a, b in edges: #add back 1000
		Union(a, b)

	a, b = last
	
	return data[a][0] * data[b][0]


print(Part1())
print(Part2())



















