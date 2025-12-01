from functools import cache

rules = []
otherTickets = []

with open('input.txt', 'r') as file: 

	emptyLines = 0
	for line in file: 
		line = line.strip()
		if line == '': 
			emptyLines += 1 
			continue 
		if line == 'your ticket:' or line == 'nearby tickets:': 
			continue
		
		if emptyLines == 0: 
			line = line.split(':')
			ruleName = line[0]
			line = line[1].split(' ')
			a = line[1].split('-')
			b = line[3].split('-')
			rules.append((ruleName, list(map(int, a)), list(map(int, b))))
		
		if emptyLines == 1: 
			myTicket = list(map(int, line.split(',')))

		if emptyLines == 2: 
			otherTickets.append(list(map(int, line.split(','))))

#print(rules)
#print(myTicket)
#print(otherTickets)

def Part1(rules, otherTickets): 
	validNums = set()
	ans = 0

	for _, a, b in rules: 
		for i in range(a[0], a[1]+1): 
			validNums.add(i)
		for i in range(b[0], b[1]+1): 
			validNums.add(i)

	validTickets = []


	for ticket in otherTickets: 
		isValid = True
		for val in ticket: 
			if val not in validNums: 
				ans += val 
				isValid = False
		if isValid: 
			validTickets.append(ticket)

	return ans, validTickets

def Part2(rules, myTicket, validTickets): 

	ticketToRuleIndex = {}
	full_mask = (1 << len(rules)) - 1

	# this index is the index in ticket
	@cache
	def F(index, mask):

		if index == len(rules): 
			return mask == 0			


		m = mask 
		j = 0 
		# indexes in rules that are open
		while m: 

			lb = m & -m
			j = (lb.bit_length() - 1) 	
			m ^= lb

			_, a, b = rules[j]
			isValid = True 
			for ticket in validTickets: 
				ticketRule = ticket[index]
				if not (ticketRule in range(a[0], a[1]+1) or ticketRule in range(b[0], b[1] + 1)): 
					isValid = False 
					break 
			if isValid: 
				if F(index + 1, mask & ~(1 << j)):
					ticketToRuleIndex[index] = j
					return True 

		return False 

	print(F(0, full_mask))
	print(ticketToRuleIndex)




p1Ans, validTickets = Part1(rules, otherTickets)
print(p1Ans)
Part2(rules, myTicket, validTickets)












