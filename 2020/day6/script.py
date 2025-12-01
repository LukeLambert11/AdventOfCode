from collections import defaultdict

ans = 0

def check(s, numPeople): 
	count = 0
	for v in s.values(): 
		if v == numPeople: 
			count += 1
	return count 

with open('input.txt', 'r') as file: 

	s = defaultdict(int)
	numPeople = 0 
	for line in file: 
		line = line.strip()
		
		if line == '': 
			ans += check(s, numPeople)
			s.clear()
			numPeople = 0
		else: 
			for c in line: 
				s[c] += 1
			numPeople += 1

ans += check(s, numPeople)

print(ans)

