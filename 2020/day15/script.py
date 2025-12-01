from collections import defaultdict

data = [0,12,6,13,20,1,17]

prev = defaultdict(int)

for i, n in enumerate(data[:-1], start=1): 
	prev[n] = i 


curr = data[-1]

for turn in range(len(data), 30000000): 
	if curr in prev: 
		nxt = turn - prev[curr]
	else: 
		nxt = 0
	prev[curr] = turn
	curr = nxt


print(curr)